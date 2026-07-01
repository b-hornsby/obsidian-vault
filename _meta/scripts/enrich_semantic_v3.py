#!/usr/bin/env python3
"""
enrich_semantic_v3.py — Second pass semantic enrichment for files that errored/skipped in v2.

Improvements over v2:
- Progress tracking: writes done files to a checkpoint so retries skip them
- Simpler prompt: no linked_nodes (saves tokens), reduced max_tokens to 1500
- Exponential backoff on 429 rate limits (up to 60s)
- Per-file write retry
- Logs to enrichment-log-v3.md

Usage: python3 enrich_semantic_v3.py
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

# -- Configuration ---------------------------------------------------------------
VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
SCRIPTS_DIR = os.path.join(VAULT_PATH, "_meta", "scripts")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-log-v3.md")
CHECKPOINT_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-v3-checkpoint.txt")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "openrouter/owl-alpha"

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
REQUEST_DELAY = 2.0       # seconds between API calls
MAX_RETRIES = 5            # increased from 3
RETRY_DELAY = 3            # base delay for backoff
MAX_BACKOFF = 60           # max backoff seconds

PROVIDERS = ["CLAUDE", "GEMINI", "GPT", "GROK"]

USER_LABELS = {
    "CLAUDE": "### HUMAN",
    "GEMINI": "### USER",
    "GPT": "### USER",
    "GROK": "### USER",
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

# -- Helpers ---------------------------------------------------------------------

def load_checkpoint():
    """Load set of already-processed filenames from checkpoint file."""
    done = set()
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    done.add(line)
    return done

def save_checkpoint(filename):
    """Append a completed filename to checkpoint."""
    with open(CHECKPOINT_PATH, "a") as f:
        f.write(filename + "\n")

def extract_frontmatter(content):
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
    lines = ["---"]
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

def call_llm(prompt, max_tokens=1500):
    """Call OpenRouter API with exponential backoff on rate limits."""
    payload = json.dumps({
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": max_tokens,
    }).encode()

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(
                f"{OPENROUTER_BASE_URL}/chat/completions",
                data=payload, headers=headers, method="POST",
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode())
                return data["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else ""
            print(f"\n  HTTP {e.code}: {body[:200]}")
            if e.code == 429:
                wait = min(RETRY_DELAY * (2 ** attempt) * 2, MAX_BACKOFF)
                print(f"  Rate limited, waiting {wait:.0f}s (attempt {attempt+1}/{MAX_RETRIES})...")
                time.sleep(wait)
            elif e.code == 402:
                # Insufficient credits — reduce max_tokens and retry
                print(f"  Insufficient credits, reducing max_tokens...")
                try:
                    payload_obj = json.loads(payload)
                    new_max = max(500, payload_obj.get("max_tokens", 1500) // 2)
                    payload_obj["max_tokens"] = new_max
                    payload = json.dumps(payload_obj).encode()
                    print(f"  Retrying with max_tokens={new_max}")
                except Exception:
                    pass
                wait = min(RETRY_DELAY * (2 ** attempt), MAX_BACKOFF)
                time.sleep(wait)
            elif e.code >= 500:
                wait = min(RETRY_DELAY * (2 ** attempt), MAX_BACKOFF)
                print(f"  Server error, waiting {wait:.0f}s...")
                time.sleep(wait)
            else:
                print(f"  Non-retryable error {e.code}, skipping.")
                return None
        except Exception as e:
            print(f"\n  Error: {e}")
            if attempt < MAX_RETRIES - 1:
                wait = min(RETRY_DELAY * (2 ** attempt), MAX_BACKOFF)
                time.sleep(wait)
            else:
                return None
    return None

def parse_llm_response(response_text, expected_count):
    if not response_text:
        return None
    # Try JSON array
    match = re.search(r'\[.*\]', response_text, re.DOTALL)
    if not match:
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
        results = []
        for m in re.finditer(r'\{[^{}]*\}', response_text, re.DOTALL):
            try:
                results.append(json.loads(m.group()))
            except json.JSONDecodeError:
                pass
        return results if results else None

def build_batch_prompt(batch_files, provider):
    """Simpler prompt — no linked_nodes, shorter output requested."""
    user_label = USER_LABELS.get(provider, "### USER")

    prompt = f"""You are analyzing {len(batch_files)} conversation files from Bryan's second-brain vault.

For EACH conversation, analyze ONLY the USER turns (labeled "{user_label}"). Understand what Bryan was REALLY trying to accomplish.

Return a JSON array with one object per file, in the same order. Each object must have these exact fields:

{{
  "filename": "the exact filename from the list",
  "tags": ["3-5 specific topic tags, e.g. 'local-llm-deployment' not just 'llm'"],
  "category": "one of: ai-tools, crypto-web3, coding, career, homelab, streaming, general",
  "sentiment": "one of: curious, frustrated, exploratory, building, stuck, executing",
  "resolution": "one of: resolved, unresolved, partial, abandoned",
  "linked_projects": ["project names actually discussed: operation-immortal-agent, homelab-stack, private-ai-consulting, second-brain-vault, streaming-rig, it-certification, flappy-meme-bird"],
  "summary": "1 sentence summarizing what Bryan was trying to accomplish"
}}

RULES:
- tags must be SPECIFIC and MEANINGFUL
- linked_projects should ONLY include projects actually discussed
- If conversation is short/unclear, use category: general and resolution: partial
- Return ONLY the JSON array, no other text

Here are the conversations:
"""

    for i, f in enumerate(batch_files):
        title = f.get("title", "")
        user_turns = f.get("user_turns", "")
        # Truncate to save tokens
        if len(user_turns) > 2000:
            user_turns = user_turns[:2000] + "\n... [truncated]"

        prompt += f"""
--- FILE {i+1}/{len(batch_files)}: {f['filename']} ---
Title: {title}
{user_turns}
"""

    return prompt

def process_batch(batch_files, provider):
    prompt = build_batch_prompt(batch_files, provider)
    response = call_llm(prompt, max_tokens=1500)
    if not response:
        print(f"  LLM call failed for batch, skipping {len(batch_files)} files")
        return {}

    results = parse_llm_response(response, len(batch_files))
    if not results:
        print(f"  Could not parse LLM response, skipping batch")
        print(f"  Response preview: {response[:300]}")
        return {}

    enrichments = {}
    for r in results:
        fn = r.get("filename", "")
        if fn:
            enrichments[fn] = r
    return enrichments

def enrich_file(filepath, enrichment):
    """Write enriched frontmatter to a file with retry."""
    for attempt in range(3):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            fm, body_start = extract_frontmatter(content)
            if not fm:
                return False

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
            # Skip linked_nodes for this pass (save tokens)
            if enrichment.get("summary"):
                fm["summary"] = enrichment["summary"]

            new_fm = build_frontmatter(fm)
            body = content[body_start:] if body_start > 0 else content
            if body.startswith("\n"):
                body = body[1:]

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_fm + body)
            return True
        except Exception as e:
            print(f"  Error writing {filepath} (attempt {attempt+1}): {e}")
            if attempt < 2:
                time.sleep(1)
    return False

def main():
    print("=" * 60)
    print("Semantic Enrichment v3 — Second Pass")
    print("=" * 60)

    # Load checkpoint of already-done files
    done_files = load_checkpoint()
    print(f"Checkpoint: {len(done_files)} files already processed in previous runs")

    # Collect all files needing enrichment
    all_files = []
    for provider in PROVIDERS:
        provider_dir = os.path.join(PROCESSED_DIR, provider)
        if not os.path.isdir(provider_dir):
            print(f"  Skipping {provider}: directory not found")
            continue

        files = sorted(glob.glob(os.path.join(provider_dir, "*.md")))
        files = [f for f in files if not f.endswith("CONVERSATION-HUB.md")]
        print(f"\n{provider}: {len(files)} files")

        provider_needed = 0
        for filepath in files:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                fm, body_start = extract_frontmatter(content)
                if not fm:
                    continue

                # Skip files that already have semantic enrichment (summary field)
                if fm.get("summary"):
                    continue

                # Skip files already done in this checkpoint
                fname = os.path.basename(filepath)
                if fname in done_files:
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
                user_turns = extract_user_turns(content, provider)

                all_files.append({
                    "filepath": filepath,
                    "filename": fname,
                    "provider": provider,
                    "title": title,
                    "user_turns": user_turns,
                    "fm": fm,
                })
                provider_needed += 1
            except Exception as e:
                print(f"  Error reading {filepath}: {e}")

        print(f"  -> {provider_needed} need enrichment")

    print(f"\nTotal files to process this run: {len(all_files)}")

    if not all_files:
        print("No files to process. All done!")
        return

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
                # Still delay to avoid hammering
                time.sleep(REQUEST_DELAY)
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
                        # Write checkpoint immediately
                        save_checkpoint(fn)
                    else:
                        total_errors += 1
                else:
                    print(f"\n    Missing result for {fn}")
                    total_errors += 1

            total_processed += batch_processed
            print(f"OK ({batch_processed}/{len(batch)} enriched)")

            # Rate limit delay
            time.sleep(REQUEST_DELAY)

    # -- Write log ----------------------------------------------------------------
    print(f"\n{'='*60}")
    print("Writing enrichment log...")

    log_lines = [
        "# Enrichment Log v3 — Second Pass Semantic Batch Analysis",
        "",
        f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Total files processed this run:** {total_processed}",
        f"**Total errors:** {total_errors}",
        f"**Total skipped (LLM failures):** {total_skipped}",
        f"**Total batches:** {batch_num}",
        "",
        "## Category Distribution (this run)",
        "",
    ]

    for cat in sorted(category_counts.keys()):
        count = category_counts[cat]
        pct = count / max(total_processed, 1) * 100
        log_lines.append(f"- **{cat}**: {count} ({pct:.1f}%)")

    log_lines.extend([
        "",
        "## Cumulative Progress",
        f"- Previously done (checkpoint): {len(done_files)}",
        f"- This run: {total_processed}",
        f"- Total enriched: {len(done_files) + total_processed}",
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
    print(f"\nDone! {total_processed} files enriched this run, {total_errors} errors, {total_skipped} skipped")
    print(f"Cumulative: {len(done_files) + total_processed} total files now have semantic enrichment")


if __name__ == "__main__":
    main()
