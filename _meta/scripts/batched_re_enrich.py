#!/usr/bin/env python3
"""
batched_re_enrich.py -- Batched re-enrichment to avoid rate limits.
Processes files in batches of 5-10 per LLM call to reduce API calls.
"""

import os
import re
import json
import time
import glob
import yaml

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
PROCESSED_DIR = os.path.join(VAULT_PATH, "processed")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "batched-re-enrichment.log")
CHECKPOINT_PATH = os.path.join(VAULT_PATH, "_meta", "batched-re-enrichment-checkpoint.txt")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "openrouter/owl-alpha"
BATCH_SIZE = 8


def _load_api_key():
    import json as _json
    with open(os.path.expanduser("~/.hermes/auth.json")) as f:
        auth = _json.load(f)
    for cred in auth.get("credential_pool", {}).get("openrouter", []):
        if cred.get("auth_type") == "api_key":
            return cred["access_token"]
    raise RuntimeError("No OpenRouter API key found")


def read_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)), content
        except yaml.YAMLError:
            return None, content
    return None, content


def write_frontmatter(filepath, fm, content):
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.dump(fm, default_flow_style=False, allow_unicode=True))
        f.write("---\n")
        f.write(body)


def get_body(content):
    match = re.match(r"^---\s*\n.*?\n---\s*\n", content, re.DOTALL)
    if match:
        return content[match.end():]
    return content


def get_user_turns(body):
    turns = re.findall(r"###\s*(?:USER|HUMAN)\s*\n(.*?)(?=###\s*(?:ASSISTANT|GEMINI|GPT|GROK)|$)", body, re.DOTALL)
    return " ".join(t[:300] for t in turns[:3])


def create_batch_prompt(batch_items):
    """batch_items: list of (filename, user_text)"""
    prompt = """Analyze each conversation below and return a JSON array with one object per conversation.
Each object must have these fields:
- category: one of [ai-tools, crypto-web3, coding, career, homelab, streaming, general]
- tags: 3-5 meaningful topic tags (not just keywords)
- sentiment: one of [curious, frustrated, exploratory, building, stuck, executing]
- resolution: one of [resolved, partial, unresolved, abandoned]
- linked_projects: list of projects mentioned (operation-immortal-agent, homelab-stack, private-ai-consulting, second-brain-vault, streaming-rig, it-certification, flappy-meme-bird)
- summary: 1-2 sentence summary of what the user was trying to accomplish

Return ONLY a JSON array, no other text.

Conversations:
"""
    for i, (filename, user_text) in enumerate(batch_items):
        prompt += f"\n{i+1}. Filename: {filename}\n"
        prompt += f"   Excerpt: {user_text[:500]}\n"
    prompt += "\n\nReturn JSON array like: [{\"category\": \"...\", \"tags\": [...], \"sentiment\": \"...\", \"resolution\": \"...\", \"linked_projects\": [...], \"summary\": \"...\"}, ...]\n"
    return prompt


def call_llm_batch(api_key, prompt, max_retries=5):
    import urllib.request
    import urllib.error
    
    for attempt in range(max_retries):
        try:
            data = json.dumps({
                "model": OPENROUTER_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 4000,
                "temperature": 0.3,
            }).encode()

            req = urllib.request.Request(
                f"{OPENROUTER_BASE_URL}/chat/completions",
                data=data,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read())
                return result["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = min(60 * (2 ** attempt), 120)  # Much longer backoff
                print(f"    Rate limited (429), waiting {wait}s...")
                time.sleep(wait)
            elif e.code == 402:
                raise RuntimeError("Insufficient credits")
            else:
                raise
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2)
    raise RuntimeError("Max retries exceeded")


def parse_batch_response(response, batch_size):
    try:
        json_match = re.search(r"\[.*\]", response, re.DOTALL)
        if not json_match:
            return None
        data = json.loads(json_match.group())
        if not isinstance(data, list):
            return None
        while len(data) < batch_size:
            data.append({
                "category": "general",
                "tags": [],
                "sentiment": "curious",
                "resolution": "partial",
                "linked_projects": [],
                "summary": ""
            })
        if len(data) > batch_size:
            data = data[:batch_size]
        return data
    except Exception as e:
        print(f"    Failed to parse response: {e}")
        print(f"    Response preview: {response[:200]}")
        return None


def find_files_needing_enrichment():
    files = []
    for root, dirs, filenames in os.walk(PROCESSED_DIR):
        for f in filenames:
            if f.endswith(".md") and "CONVERSATION-HUB" not in f:
                filepath = os.path.join(root, f)
                try:
                    fm, content = read_frontmatter(filepath)
                    if fm and "category" in fm and "summary" not in fm:
                        files.append((filepath, os.path.basename(filepath)))
                except:
                    pass
    return files


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
    log = []
    api_key = _load_api_key()

    done = load_checkpoint()
    all_files = find_files_needing_enrichment()
    remaining = [(fp, fn) for fp, fn in all_files if fn not in done]

    log.append(f"Files needing re-enrichment: {len(remaining)} (already done: {len(done)})")
    print(f"Files needing re-enrichment: {len(remaining)} (already done: {len(done)})")

    processed = 0
    errors = 0
    batch_num = 0

    for i in range(0, len(remaining), BATCH_SIZE):
        batch = remaining[i:i+BATCH_SIZE]
        batch_num += 1
        
        if not batch:
            break
        
        print(f"\n--- Batch {batch_num}/{(len(remaining)+BATCH_SIZE-1)//BATCH_SIZE} ({len(batch)} files) ---")
        log.append(f"--- Batch {batch_num} ({len(batch)} files) ---")
        
        # Prepare batch: extract (filename, user_text) for prompt, keep full data for writing
        batch_items = []  # for prompt: (filename, user_text)
        batch_full = []  # for writing: (filename, filepath, orig_fm, orig_content)
        
        for filepath, filename in batch:
            try:
                fm, content = read_frontmatter(filepath)
                if not fm:
                    continue
                body = get_body(content)
                user_text = get_user_turns(body)
                batch_items.append((filename, user_text))
                batch_full.append((filename, filepath, fm, content))
            except Exception as e:
                log.append(f"    SKIP {filename}: {e}")
                errors += 1
                save_checkpoint(filename)
        
        if not batch_items:
            continue
        
        # Create and call LLM
        prompt = create_batch_prompt(batch_items)
        try:
            response = call_llm_batch(api_key, prompt)
            enrichments = parse_batch_response(response, len(batch_items))
            
            if enrichments is None:
                log.append(f"    FAILED TO PARSE RESPONSE for batch {batch_num}")
                errors += len(batch_items)
                time.sleep(5)
                continue
            
            # Apply enrichments
            for (filename, filepath, orig_fm, orig_content), enrichment in zip(batch_full, enrichments):
                try:
                    if "id" in orig_fm:
                        enrichment["id"] = orig_fm["id"]
                    if "date" in orig_fm:
                        enrichment["date"] = orig_fm["date"]
                    if "source" in orig_fm:
                        enrichment["source"] = orig_fm["source"]
                    
                    write_frontmatter(filepath, enrichment, orig_content)
                    save_checkpoint(filename)
                    processed += 1
                    log.append(f"    OK: {filename}")
                except Exception as e:
                    log.append(f"    ERROR writing {filename}: {e}")
                    errors += 1
                    
        except Exception as e:
            log.append(f"    BATCH {batch_num} FAILED: {e}")
            errors += len(batch_items)
            time.sleep(10)
            continue
       # Delay between batches to be gentle on rate limits
        if i + BATCH_SIZE < len(remaining):
            time.sleep(30)  # 30s between batches
    
    log.append(f"\nDone! {processed} enriched, {errors} errors")
    print(f"\nDone! {processed} enriched, {errors} errors")

    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log))

    for line in log[-10:]:
        print(line)
    print(f"\nFull log: {LOG_PATH}")


if __name__ == "__main__":
    main()