#!/usr/bin/env python3
"""
re_enrich_missing.py -- Re-enrich files that lost their new enrichment.
Uses local llama.cpp server (completion endpoint).
Skips files with broken frontmatter.
"""

import os
import re
import json
import time
import urllib.request
import urllib.error
import yaml
from pathlib import Path

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "re-enrichment.log")
CHECKPOINT_PATH = os.path.join(VAULT_PATH, "_meta", "re-enrichment-checkpoint.txt")

# Use local llama.cpp completion endpoint
BASE_URL = "http://localhost:8080"
MODEL = "Qwen3.6-35B-A3B-UD-IQ3_XXS.gguf"


def read_frontmatter(filepath):
    """Read frontmatter from a file. Returns (fm, content) or (None, None) on error."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not match:
            return None, None
        try:
            fm = yaml.safe_load(match.group(1))
            if not isinstance(fm, dict):
                return None, None
            return fm, content
        except yaml.YAMLError:
            return None, None
    except Exception:
        return None, None


def write_frontmatter(filepath, fm, content):
    """Rewrite frontmatter, keeping the body intact."""
    try:
        body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(fm, default_flow_style=False, allow_unicode=True))
            f.write("---\n")
            f.write(body)
        return True
    except Exception:
        return False


def get_user_turns(content):
    """Extract USER/HUMAN turns from conversation body."""
    if not content:
        return ""
    body_match = re.match(r"^---\s*\n.*?\n---\s*\n", content, re.DOTALL)
    body = content[body_match.end():] if body_match else content
    turns = re.findall(
        r"###\s*(?:USER|HUMAN)\s*\n(.*?)(?=###\s*(?:ASSISTANT|GEMINI|GPT|GROK)|$)",
        body,
        re.DOTALL,
    )
    return " ".join(t[:500] for t in turns[:5])


def call_llm(prompt):
    """Call local llama.cpp completion endpoint with retries."""
    for attempt in range(3):
        try:
            data = json.dumps({
                "prompt": prompt,
                "n_predict": 512,
                "temperature": 0.3,
                "mirostat": 0,
            }).encode()
            req = urllib.request.Request(
                f"{BASE_URL}/v1/completions",
                data=data,
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode())
                return result["choices"][0]["text"]
        except Exception as e:
            if attempt < 2:
                time.sleep(2 * (2 ** attempt))
            else:
                raise
    raise RuntimeError("Max retries exceeded")


def extract_json(text):
    """Extract JSON from LLM output, stripping any thinking tags."""
    text = re.sub(r"<thinking>.*?</thinking>", "", text, flags=re.DOTALL)
    match = re.search(r"\{[^{}]*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return None


def enrich_file(filepath):
    """Enrich a single file with summary, tags, sentiment, resolution, linked_projects."""
    fm, content = read_frontmatter(filepath)
    if not fm:
        return False, "No valid frontmatter"
    if not content:
        return False, "No content"

    user_text = get_user_turns(content)
    if len(user_text) < 20:
        return False, "Not enough user content"

    orig_id = fm.get("id")
    orig_date = fm.get("date")
    orig_source = fm.get("source")

    prompt = f"""Extract structured data from this conversation. Return ONLY valid JSON with these fields:
{{
  "category": "one of: ai-tools, crypto-web3, coding, career, homelab, streaming, general",
  "tags": ["tag1", "tag2", "tag3"],
  "sentiment": "one of: curious, frustrated, exploratory, building, stuck, executing",
  "resolution": "one of: resolved, partial, unresolved, abandoned",
  "linked_projects": ["project1", "project2"],
  "summary": "1-2 sentence summary of what was accomplished"
}}

Rules:
- Use the exact values shown (no new values)
- linked_projects can include: homelab-stack, second-brain-vault, streaming-rig, it-certification, private-ai-consulting, flappy-meme-bird, operation-immortal-agent
- Keep summary to 1-2 sentences maximum
- Return ONLY the JSON object, nothing else

Conversation:
{user_text[:2000]}"""

    response = call_llm(prompt)
    data = extract_json(response)

    if data is None:
        return False, f"Could not parse JSON from response ({len(response)} chars)"

    fm["category"] = data.get("category", "general")
    fm["tags"] = data.get("tags", [])
    fm["sentiment"] = data.get("sentiment", "curious")
    fm["resolution"] = data.get("resolution", "partial")
    fm["linked_projects"] = data.get("linked_projects", [])
    fm["summary"] = data.get("summary", "")

    if orig_id:
        fm["id"] = orig_id
    if orig_date:
        fm["date"] = orig_date
    if orig_source:
        fm["source"] = orig_source

    if not write_frontmatter(filepath, fm, content):
        return False, "Failed to write frontmatter"
    return True, "OK"


def find_files_needing_enrichment():
    """Find files with category but no summary, skipping broken files."""
    files = []
    skip_count = 0
    for root, dirs, filenames in os.walk(PROCESSED_DIR):
        for f in filenames:
            if f.endswith(".md") and "CONVERSATION-HUB" not in f:
                filepath = os.path.join(root, f)
                fm, content = read_frontmatter(filepath)
                if fm and "category" in fm and "summary" not in fm:
                    files.append(filepath)
                else:
                    skip_count += 1
    return files, skip_count


def load_checkpoint():
    done = set()
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH) as f:
            for line in f:
                done.add(line.strip())
    return done


def save_checkpoint(filename):
    with open(CHECKPOINT_PATH, "a") as f:
        f.write(filename + "\n")


def main():
    log_lines = []
    done = load_checkpoint()
    files, skipped = find_files_needing_enrichment()
    remaining = [f for f in files if os.path.basename(f) not in done]

    log_lines.append(f"Total files needing re-enrichment: {len(remaining)}")
    log_lines.append(f"Skipped (no category or already has summary or broken): {skipped}")
    log_lines.append(f"Already done (from checkpoint): {len(done)}")
    print(f"Found {len(remaining)} files to re-enrich")
    print(f"Skipped {skipped} (broken/no summary), checkpoint has {len(done)}")

    processed = 0
    errors = 0
    bad_frontmatter = 0

    for i, filepath in enumerate(remaining):
        filename = os.path.basename(filepath)
        try:
            ok, msg = enrich_file(filepath)
            if ok:
                save_checkpoint(filename)
                processed += 1
                log_lines.append(f"[{i+1}/{len(remaining)}] OK: {filename}")
                if i % 5 == 0:
                    print(f"  Progress: {i+1}/{len(remaining)} processed, {processed} succeeded")
            else:
                errors += 1
                log_lines.append(f"[{i+1}/{len(remaining)}] FAIL: {filename}: {msg}")
                if "frontmatter" in msg.lower():
                    bad_frontmatter += 1
        except Exception as e:
            errors += 1
            log_lines.append(f"[{i+1}/{len(remaining)}] ERROR: {filename}: {e}")

    log_lines.append(f"\nDone! Processed: {processed}, Errors: {errors}, Bad frontmatter: {bad_frontmatter}")

    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log_lines))

    print(f"\n{processed} enriched, {errors} errors")
    print(f"Log: {LOG_PATH}")


if __name__ == "__main__":
    main()
