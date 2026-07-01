#!/usr/bin/env python3
"""
enrich_semantic.py — Re-enrich all processed conversation files with proper semantic analysis.

Reads files in batches of 50 per provider subfolder, sends USER turns to LLM,
and writes enriched frontmatter back to each file.

Usage: python3 enrich_semantic.py
"""

import os
import re
import json
import time
import glob
import urllib.request
import urllib.error
from pathlib import Path
from collections import defaultdict

# ── Configuration ──────────────────────────────────────────────────────────────
VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
SCRIPTS_DIR = os.path.join(VAULT_PATH, "_meta", "scripts")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-log-v2.md")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openrouter/owl-alpha"
# Use a model name that OpenRouter understands directly
OPENROUTER_MODEL = "openrouter/owl-alpha"  # fast, cheap, good for batch classification

# Read OpenRouter API key from auth.json
def _load_api_key():
    import json as _json
    try:
        with open('/home/toastedmel0n/.hermes/auth.json') as f:
            auth = _json.load(f)
        for cred in auth.get('credential_pool', {}).get('openrouter', []):
            if cred.get('auth_type') == 'api_key':
                return cred['access_token']
    except Exception:
        pass
    return os.environ.get('OPENROUTER_API_KEY', '')

OPENROUTER_API_KEY = _load_api_key()

BATCH_SIZE = 50
REQUEST_DELAY = 1.0  # seconds between API calls to avoid rate limits
MAX_RETRIES = 3
RETRY_DELAY = 5

PROVIDERS = ["CLAUDE", "GEMINI", "GPT", "GROK"]

# Role label mapping per provider
USER_LABELS = {
    "CLAUDE": "### HUMAN",
    "GEMINI": "### USER",
    "GPT": "### USER",      # also check ### HUMAN
    "GROK": "### USER",     # also check ### HUMAN
}

ALT_USER_LABELS = {
    "GPT": ["### HUMAN"],
    "GROK": ["### HUMAN"],
}

CATEGORIES = ["ai-tools", "crypto-web3", "coding", "career", "homelab", "streaming", "general"]
SENTIMENTS = ["curious", "frustrated", "exploratory", "building", "stuck", "executing"]
RESOLUTIONS = ["resolved", "unresolved", "partial", "abandoned"]

PROJECTS = [
    "operation-immortal-agent",
    "homelab-stack",
    "private-ai-consulting",
    "second-brain-vault",
    "streaming-rig",
    "it-certification",
    "flappy-meme-bird",
]

# ── Helpers ────────────────────────────────────────────────────────────────────

def extract_frontmatter(content):
    """Extract YAML frontmatter dict from file content. Returns (fm_dict, body_start_idx)."""
    if not content.startswith("---"):
        return {}, 0
    end = content.find("---", 3)
    if end == -1:
        return {}, 0
    fm_text = content[3:end].strip()
    fm = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        # Parse list values like ['a', 'b'] or [a, b]
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = re.findall(r"'([^']*)'|\"([^\"]*)\"|([^,]+)", inner)
                fm[key] = [a or b or c.strip() for a, b, c in items if (a or b or c.strip())]
        else:
            fm[key] = val
    return fm, end + 3


def build_frontmatter(fm):
    """Build YAML frontmatter string from dict."""
    lines = ["---"]
    # Preserve order: id, source, date, then enriched fields
    for key in ["id", "source", "date"]:
        if key in fm:
            lines.append(f"{key}: {fm[key]}")
    for key in ["tags", "category", "sentiment", "resolution", "linked_projects", "linked_nodes", "summary"]:
        if key in fm:
            val = fm[key]
            if isinstance(val, list):
                if val:
                    items = ", ".join(f"'{v}'" for v in val)
                    lines.append(f"{key}: [{items}]")
                else:
                    lines.append(f"{key}: []")
            else:
                lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def extract_user_turns(content, provider):
    """Extract USER turns from conversation body."""
    user_label = USER_LABELS.get(provider, "### USER")
    alt_labels = ALT_USER_LABELS.get(provider, [])

    body_start = content.find("---", 3)
    if body_start == -1:
        return ""
    body = content[body_start + 3:]

    turns = []
    lines = body.split("\n")
    in_user = False
    current_turn = []

    for line in lines:
        stripped = line.strip()
        is_user_header = stripped == user_label
        is_alt_header = stripped in alt_labels
        is_any_header = stripped.startswith("### ")

        if is_user_header or is_alt_header:
            if current_turn:
                turns.append("\n".join(current_turn).strip())
            in_user = True
            current_turn = []
        elif is_any_header and in_user:
            if current_turn:
                turns.append("\n".join(current_turn).strip())
            in_user = False
            current_turn = []
        elif in_user:
            current_turn.append(line)

    if current_turn and in_user:
        turns.append("\n".join(current_turn).strip())

    return "\n\n".join(turns)


def extract_title(content):
    """Extract the # Title from the body."""
    body_start = content.find("---", 3)
    if body_start == -1:
        return ""
    body = content[body_start + 3:]
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return ""


def call_llm(prompt, retries=MAX_RETRIES):
    """Call OpenRouter API and return the response text."""
    payload = json.dumps({
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": 2000,
    }).encode()

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                f"{OPENROUTER_BASE_URL}/chat/completions",
                data=payload,
                headers=headers,
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode())
                return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else ""
            print(f"  HTTP {e.code}: {body[:200]}")
            if e.code == 429:
                wait = RETRY_DELAY * (attempt + 1) * 2
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif e.code == 402:
                # Insufficient credits — reduce max_tokens and retry
                print(f"  Insufficient credits, reducing max_tokens...")
                try:
                    payload_obj = json.loads(payload)
                    payload_obj["max_tokens"] = max(500, payload_obj.get("max_tokens", 2000) // 2)
                    payload = json.dumps(payload_obj).encode()
                    print(f"  Retrying with max_tokens={payload_obj['max_tokens']}")
                except Exception:
                    pass
                time.sleep(RETRY_DELAY * (attempt + 1))
            elif e.code >= 500:
                time.sleep(RETRY_DELAY * (attempt + 1))
            else:
                return None
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < retries - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))
    return None


def parse_llm_response(response_text, expected_count):
    """Parse JSON array from LLM response."""
    if not response_text:
        return None

    # Try to find JSON array in the response
    match = re.search(r'\[.*\]', response_text, re.DOTALL)
    if not match:
        # Try to find JSON object
        match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if not match:
            return None
        try:
            return [json.loads(match.group())]
        except json.JSONDecodeError:
            return None

    try:
        results = json.loads(match.group())
        if isinstance(results, list):
            return results
        return [results]
    except json.JSONDecodeError:
        # Try line-by-line JSON objects
        results = []
        for m in re.finditer(r'\{[^{}]*\}', response_text, re.DOTALL):
            try:
                results.append(json.loads(m.group()))
            except json.JSONDecodeError:
                pass
        return results if results else None


def build_batch_prompt(batch_files, provider):
    """Build the LLM prompt for a batch of files."""
    user_label = USER_LABELS.get(provider, "### USER")

    prompt = f"""You are analyzing {len(batch_files)} conversation files from Bryan's second-brain vault. Bryan is building toward: private AI consulting, web3/Solana development, local LLM expertise, streaming infrastructure, and IT career transition.

For EACH conversation, analyze ONLY the USER turns (labeled "{user_label}"). Understand what Bryan was REALLY trying to accomplish — his questions, goals, and emotional state matter more than the AI responses.

Return a JSON array with one object per file, in the same order as listed. Each object must have these exact fields:

{{
  "filename": "the exact filename from the list",
  "tags": ["3-8 MEANINGFUL topic tags — be specific, e.g. 'local-llm-deployment' not just 'llm', 'solana-trading-bot' not just 'crypto'"],
  "category": "one of: ai-tools, crypto-web3, coding, career, homelab, streaming, general",
  "sentiment": "one of: curious, frustrated, exploratory, building, stuck, executing",
  "resolution": "one of: resolved, unresolved, partial, abandoned",
  "linked_projects": ["project names actually discussed: operation-immortal-agent, homelab-stack, private-ai-consulting, second-brain-vault, streaming-rig, it-certification, flappy-meme-bird"],
  "linked_nodes": ["people/entities mentioned: bryan, dad, girlfriend, or project names as nodes"],
  "summary": "1-2 sentences summarizing what Bryan was actually trying to accomplish in this conversation"
}}

RULES:
- tags must be SPECIFIC and MEANINGFUL, not generic keywords
- category must reflect the ACTUAL topic, not a tangential mention
- linked_projects should ONLY include projects actually discussed in the USER turns
- linked_nodes should include people/entities Bryan mentions (dad, girlfriend, etc.) or project names as nodes
- If a conversation is very short or unclear, use category: general and resolution: partial
- Return ONLY the JSON array, no other text

Here are the conversations:
"""

    for i, f in enumerate(batch_files):
        title = f.get("title", "")
        user_turns = f.get("user_turns", "")
        # Truncate very long user turns to fit in context
        if len(user_turns) > 3000:
            user_turns = user_turns[:3000] + "\n... [truncated]"

        prompt += f"""
--- FILE {i+1}/{len(batch_files)}: {f['filename']} ---
Title: {title}
{user_turns}
"""

    return prompt


def process_batch(batch_files, provider):
    """Process a batch of files through the LLM and return enrichment data."""
    prompt = build_batch_prompt(batch_files, provider)
    response = call_llm(prompt)
    if not response:
        print(f"  LLM call failed for batch, skipping {len(batch_files)} files")
        return {}

    results = parse_llm_response(response, len(batch_files))
    if not results:
        print(f"  Could not parse LLM response, skipping batch")
        print(f"  Response preview: {response[:300]}")
        return {}

    # Index by filename
    enrichments = {}
    for r in results:
        fn = r.get("filename", "")
        if fn:
            enrichments[fn] = r

    return enrichments


def enrich_file(filepath, enrichment):
    """Write enriched frontmatter to a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        fm, body_start = extract_frontmatter(content)
        if not fm:
            return False

        # Update enriched fields
        if enrichment.get("tags"):
            fm["tags"] = enrichment["tags"]
        if enrichment.get("category"):
            cat = enrichment["category"]
            if cat in CATEGORIES:
                fm["category"] = cat
        if enrichment.get("sentiment"):
            sent = enrichment["sentiment"]
            if sent in SENTIMENTS:
                fm["sentiment"] = sent
        if enrichment.get("resolution"):
            res = enrichment["resolution"]
            if res in RESOLUTIONS:
                fm["resolution"] = res
        if enrichment.get("linked_projects"):
            fm["linked_projects"] = enrichment["linked_projects"]
        if enrichment.get("linked_nodes"):
            fm["linked_nodes"] = enrichment["linked_nodes"]
        if enrichment.get("summary"):
            fm["summary"] = enrichment["summary"]

        # Rebuild file
        new_fm = build_frontmatter(fm)
        body = content[body_start:] if body_start > 0 else content
        # Remove leading newline from body if present
        if body.startswith("\n"):
            body = body[1:]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_fm + body)

        return True
    except Exception as e:
        print(f"  Error writing {filepath}: {e}")
        return False


def get_user_label_for_provider(provider):
    """Get the primary user label for a provider."""
    return USER_LABELS.get(provider, "### USER")


def extract_user_turns_from_body(body, provider):
    """Extract user turns from body text based on provider."""
    user_label = USER_LABELS.get(provider, "### USER")
    alt_labels = ALT_USER_LABELS.get(provider, [])

    turns = []
    lines = body.split("\n")
    in_user = False
    current_turn = []

    for line in lines:
        stripped = line.strip()
        is_user_header = stripped == user_label
        is_alt_header = stripped in alt_labels
        is_any_header = stripped.startswith("### ")

        if is_user_header or is_alt_header:
            if current_turn:
                turns.append("\n".join(current_turn).strip())
            in_user = True
            current_turn = []
        elif is_any_header and in_user:
            if current_turn:
                turns.append("\n".join(current_turn).strip())
            in_user = False
            current_turn = []
        elif in_user:
            current_turn.append(line)

    if current_turn and in_user:
        turns.append("\n".join(current_turn).strip())

    return "\n\n".join(turns)


def main():
    print("=" * 60)
    print("Semantic Enrichment v2 — Batch Analysis")
    print("=" * 60)

    # Collect all files
    all_files = []
    for provider in PROVIDERS:
        provider_dir = os.path.join(PROCESSED_DIR, provider)
        if not os.path.isdir(provider_dir):
            print(f"  Skipping {provider}: directory not found")
            continue

        files = sorted(glob.glob(os.path.join(provider_dir, "*.md")))
        # Skip CONVERSATION-HUB.md
        files = [f for f in files if not f.endswith("CONVERSATION-HUB.md")]

        print(f"\n{provider}: {len(files)} files")

        for filepath in files:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                fm, body_start = extract_frontmatter(content)
                if not fm:
                    continue

                # Skip already-enriched files (v2 enrichment has 'summary' field)
                if fm.get("summary"):
                    continue

                # Extract title
                body = content[body_start:] if body_start > 0 else content
                title = ""
                for line in body.split("\n"):
                    ls = line.strip()
                    if ls.startswith("# ") and not ls.startswith("## "):
                        title = ls[2:].strip()
                        break

                # Extract user turns
                user_turns = extract_user_turns_from_body(body, provider)

                all_files.append({
                    "filepath": filepath,
                    "filename": os.path.basename(filepath),
                    "provider": provider,
                    "title": title,
                    "user_turns": user_turns,
                    "fm": fm,
                })
            except Exception as e:
                print(f"  Error reading {filepath}: {e}")

    print(f"\nTotal files to process: {len(all_files)}")

    # Group by provider for batching
    by_provider = defaultdict(list)
    for f in all_files:
        by_provider[f["provider"]].append(f)

    # Process in batches
    total_processed = 0
    total_errors = 0
    total_skipped = 0
    category_counts = defaultdict(int)
    batch_num = 0

    for provider in PROVIDERS:
        files = by_provider.get(provider, [])
        if not files:
            continue

        print(f"\n{'='*40}")
        print(f"Processing {provider} ({len(files)} files)")
        print(f"{'='*40}")

        # Split into batches
        for i in range(0, len(files), BATCH_SIZE):
            batch = files[i:i + BATCH_SIZE]
            batch_num += 1
            batch_start = i + 1
            batch_end = min(i + BATCH_SIZE, len(files))

            print(f"\n  Batch {batch_num} [{batch_start}-{batch_end}/{len(files)}]...", end=" ", flush=True)

            enrichments = process_batch(batch, provider)

            if not enrichments:
                print("FAILED (LLM error)")
                total_skipped += len(batch)
                continue

            batch_processed = 0
            for f in batch:
                fn = f["filename"]
                if fn in enrichments:
                    success = enrich_file(f["filepath"], enrichments[fn])
                    if success:
                        batch_processed += 1
                        cat = enrichments[fn].get("category", "unknown")
                        category_counts[cat] += 1
                    else:
                        total_errors += 1
                else:
                    print(f"\n    Missing result for {fn}")
                    total_errors += 1

            total_processed += batch_processed
            print(f"OK ({batch_processed}/{len(batch)} enriched)")

            # Rate limit delay
            time.sleep(REQUEST_DELAY)

    # ── Write log ──────────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print("Writing enrichment log...")

    log_lines = [
        "# Enrichment Log v2 — Semantic Batch Analysis",
        "",
        f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Total files processed:** {total_processed}",
        f"**Total errors:** {total_errors}",
        f"**Total skipped (LLM failures):** {total_skipped}",
        "",
        "## Category Distribution",
        "",
    ]

    for cat in sorted(category_counts.keys()):
        count = category_counts[cat]
        pct = count / max(total_processed, 1) * 100
        log_lines.append(f"- **{cat}**: {count} ({pct:.1f}%)")

    log_lines.extend([
        "",
        "## Sample Enriched Files",
        "",
        "Random sample of 10 enriched files for quality check:",
        "",
    ])

    # Pick a random sample of enriched files
    import random
    sample_size = min(10, len(all_files))
    sample_files = random.sample(all_files, sample_size)

    for f in sample_files:
        try:
            with open(f["filepath"], "r", encoding="utf-8") as fh:
                content = fh.read()
            fm, _ = extract_frontmatter(content)
            log_lines.append(f"### {f['filename']} ({f['provider']})")
            log_lines.append(f"- **Title:** {f['title']}")
            log_lines.append(f"- **Category:** {fm.get('category', 'N/A')}")
            log_lines.append(f"- **Tags:** {fm.get('tags', [])}")
            log_lines.append(f"- **Sentiment:** {fm.get('sentiment', 'N/A')}")
            log_lines.append(f"- **Resolution:** {fm.get('resolution', 'N/A')}")
            log_lines.append(f"- **Linked Projects:** {fm.get('linked_projects', [])}")
            log_lines.append(f"- **Linked Nodes:** {fm.get('linked_nodes', [])}")
            log_lines.append(f"- **Summary:** {fm.get('summary', 'N/A')}")
            log_lines.append("")
        except Exception as e:
            log_lines.append(f"### {f['filename']} — Error reading: {e}")
            log_lines.append("")

    log_lines.extend([
        "",
        "## Errors",
        "",
    ])

    if total_errors == 0 and total_skipped == 0:
        log_lines.append("No errors encountered.")
    else:
        log_lines.append(f"- {total_errors} write errors")
        log_lines.append(f"- {total_skipped} files skipped due to LLM failures")

    log_lines.append("")

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

    print(f"Log written to: {LOG_PATH}")
    print(f"\nDone! {total_processed} files enriched, {total_errors} errors, {total_skipped} skipped")


if __name__ == "__main__":
    main()
