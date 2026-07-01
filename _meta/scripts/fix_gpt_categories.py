#!/usr/bin/env python3
"""
fix_gpt_categories.py - Fix GPT enrichment quality issues.

Problems to fix:
1. Business/consulting conversations tagged as 'coding'
2. Generic AI-tool keywords instead of actual topic tags
3. linked_projects includes projects not actually mentioned

Usage: python3 fix_gpt_categories.py
"""

import os
import re
import yaml

VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
GPT_DIR = os.path.join(VAULT_PATH, "processed", "GPT")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-gpt-fix.log")

# Project name patterns to search for in text
PROJECT_PATTERNS = {
    "operation-immortal-agent": [r"operation\s*immortal\s*agent", r"\bOIA\b", r"immortal\s*agent"],
    "homelab-stack": [r"homelab", r"home\s*lab", r"self.?hosted", r"local\s*llm", r"ollama", r"docker"],
    "private-ai-consulting": [r"consulting", r"consult", r"client", r"business\s*package", r"\$\s*500"],
    "second-brain-vault": [r"second\s*brain", r"vault", r"obsidian.*memory", r"knowledge\s*graph"],
    "streaming-rig": [r"streaming", r"obs\s*studio", r"twitch", r"content\s*creation", r"multistream"],
    "it-certification": [r"certification", r"cert\b", r"comptia", r"security\+", r"network\+", r"exam\s*date"],
    "flappy-meme-bird": [r"flappy", r"meme\s*game", r"flappy\s*bird"],
}

# Category detection patterns
CATEGORY_RULES = [
    ("career", [r"career", r"job", r"linkedin", r"resume", r"interview", r"hiring", r"warehouse", r"workplace", r"promotion", r"salary", r"employment"]),
    ("crypto-web3", [r"crypto", r"bitcoin", r"ethereum", r"solana", r"trading", r"defi", r"blockchain", r"wallet", r"token", r"coin", r"perp", r"jupiter", r"meteora", r"liquidity"]),
    ("streaming", [r"stream", r"obs\b", r"twitch", r"youtube", r"content", r"video", r"broadcast", r"overlay", r"webcam", r"microphone", r"audio\s*routing"]),
    ("ai-tools", [r"llm", r"language\s*model", r"gpt", r"claude", r"gemini", r"ollama", r"hugging\s*face", r"prompt", r"fine.?tun", r"rag", r"agent", r"ai\s*model", r"local\s*ai"]),
    ("homelab", [r"homelab", r"home\s*lab", r"server", r"proxmox", r"vm\b", r"virtual\s*machine", r"linux", r"debian", r"ubuntu", r"arch", r"cachyos", r"docker", r"kubernetes", r"nas", r"raid"]),
    ("coding", [r"python", r"javascript", r"code\b", r"programming", r"debug", r"error\b", r"syntax", r"function", r"variable", r"api\b", r"script", r"git\b", r"repo"]),
]


def read_frontmatter(filepath):
    """Read YAML frontmatter from a markdown file."""
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
    """Write YAML frontmatter back to a markdown file."""
    # Remove old frontmatter
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
    # Write new frontmatter
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.dump(fm, default_flow_style=False, allow_unicode=True))
        f.write("---\n")
        f.write(body)


def detect_category(text):
    """Detect the correct category based on conversation content."""
    text_lower = text.lower()
    scores = {}
    for category, patterns in CATEGORY_RULES:
        score = 0
        for pattern in patterns:
            matches = len(re.findall(pattern, text_lower))
            score += matches
        if score > 0:
            scores[category] = score
    if not scores:
        return "general"
    return max(scores, key=scores.get)


def find_linked_projects(text):
    """Find which projects are actually mentioned in the conversation."""
    text_lower = text.lower()
    found = []
    for project, patterns in PROJECT_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower):
                found.append(project)
                break
    return found


def fix_tags(fm, category):
    """Fix tags to be more relevant to the actual category."""
    # Keep existing tags that are actually relevant
    existing_tags = fm.get("tags", [])
    # Remove generic AI-tool tags if category is not ai-tools
    if category not in ("ai-tools", "coding", "homelab"):
        generic_ai_tags = {"ai", "ai-tools", "model", "llm", "gpt", "claude", "gemini", "cursor", "copilot", "rag", "fine-tune", "ai assistant"}
        existing_tags = [t for t in existing_tags if t.lower().strip("'\"") not in generic_ai_tags]
    return existing_tags


def main():
    log = []
    fixed = 0
    skipped = 0
    errors = 0

    files = sorted(glob.glob(os.path.join(GPT_DIR, "*.md")))
    log.append(f"Processing {len(files)} GPT files...")

    for filepath in files:
        filename = os.path.basename(filepath)
        try:
            fm, content = read_frontmatter(filepath)
            if not fm:
                skipped += 1
                continue

            # Get the conversation text (after frontmatter)
            body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
            # Focus on USER turns
            user_turns = re.findall(r"###\s*(?:USER|HUMAN)\s*\n(.*?)(?=###\s*(?:ASSISTANT|GEMINI|GPT|GROK)|$)", body, re.DOTALL)
            user_text = " ".join(user_turns) if user_turns else body

            old_category = fm.get("category", "")
            old_tags = fm.get("tags", [])
            old_projects = fm.get("linked_projects", [])

            # Detect correct category
            new_category = detect_category(user_text)

            # Find actual linked projects
            new_projects = find_linked_projects(user_text)

            # Fix tags
            new_tags = fix_tags(fm, new_category)

            # Check if anything changed
            changed = False
            if new_category != old_category:
                log.append(f"  CATEGORY: {filename}: '{old_category}' -> '{new_category}'")
                fm["category"] = new_category
                changed = True

            if set(new_tags) != set(old_tags):
                log.append(f"  TAGS: {filename}: {old_tags} -> {new_tags}")
                fm["tags"] = new_tags
                changed = True

            if set(new_projects) != set(old_projects):
                log.append(f"  PROJECTS: {filename}: {old_projects} -> {new_projects}")
                fm["linked_projects"] = new_projects
                changed = True

            if changed:
                write_frontmatter(filepath, fm, content)
                fixed += 1
            else:
                skipped += 1

        except Exception as e:
            log.append(f"  ERROR: {filename}: {e}")
            errors += 1

    log.append(f"\nDone! {fixed} files fixed, {skipped} unchanged, {errors} errors")

    # Write log
    with open(LOG_PATH, "w") as f:
        f.write("\n".join(log))

    # Print summary
    for line in log[-10:]:
        print(line)
    print(f"\nFull log: {LOG_PATH}")


if __name__ == "__main__":
    import glob
    main()
