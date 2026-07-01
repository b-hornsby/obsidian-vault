#!/usr/bin/env python3
"""
Task 1 — Initial Vault Sweep
Parses all processed/ .md files, adds enriched frontmatter, rebuilds node pages.
Never modifies originals in processed/.
"""
import os, re, json, glob
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

VAULT = Path("/vault")
PROCESSED = VAULT / "processed"
NODES = VAULT / "nodes"
INSIGHTS = VAULT / "insights"

SOURCES = ["CLAUDE", "GEMINI", "GPT", "GROK"]
USER_MARKERS = {
    "CLAUDE": ["### HUMAN"],
    "GEMINI": ["### USER"],
    "GPT": ["### USER", "### HUMAN"],
    "GROK": ["### USER", "### HUMAN"],
}
AI_MARKERS = {
    "CLAUDE": ["### ASSISTANT"],
    "GEMINI": ["### GEMINI"],
    "GPT": ["### ASSISTANT", "### GPT"],
    "GROK": ["### ASSISTANT", "### GROK"],
}

CATEGORIES = ["ai-tools", "crypto-web3", "coding", "career", "homelab", "streaming", "general"]
SENTIMENTS = ["curious", "frustrated", "exploratory", "building", "stuck", "executing"]
RESOLUTIONS = ["resolved", "unresolved", "partial", "abandoned"]

PROJECT_NAMES = [
    "flappy-meme-bird", "homelab-stack", "it-certification",
    "operation-immortal-agent", "private-ai-consulting",
    "second-brain-vault", "streaming-rig"
]

TOPIC_KEYWORDS = {
    "ai-tools": ["llm", "ai", "agent", "claude", "gpt", "gemini", "grok", "model", "ollama", "oobabooga", "cursor", "copilot", "rag", "mcp", "openai", "anthropic", "llama.cpp", "gguf", "quantized", "inference", "embedding", "fine-tune", "lora", "hermes", "oobabooga", "text-generation", "local llm", "local model", "ai assistant", "helpdesk ai"],
    "crypto-web3": ["solana", "bitcoin", "ethereum", "crypto", "defi", "meteora", "dlmm", "jupiter", "dex", "token", "wallet", "phantom", "blockchain", "web3", "nft", "trading", "perp", "perpetual", "yield", "liquidity", "amm", "swap", "usdc", "icp", "internet computer", "memecoin", "pump.fun", "axiom", "leverage", "margin", "farm", "staking"],
    "coding": ["python", "javascript", "typescript", "rust", "go", "bash", "shell", "code", "script", "debug", "error", "syntax", "import", "module", "package", "pip", "npm", "git", "github", "vs code", "cursor", "ide", "function", "class", "api", "json", "csv", "database", "sql", "html", "css", "react", "node", "docker", "dockerfile", "compose", "kubernetes", "fastapi", "flask", "django"],
    "career": ["resume", "job", "interview", "certification", "cert", "comptia", "a+", "network+", "it job", "help desk", "helpdesk", "linkedin", "cover letter", "hire", "salary", "career", "entry level", "junior", "tiffin", "secai", "security+", "learning", "course", "study", "exam", "prep"],
    "homelab": ["homelab", "server", "linux", "cachyos", "arch", "ubuntu", "debian", "wsl", "wsl2", "windows", "hardware", "nvidia", "gpu", "cpu", "ram", "ssd", "hdd", "storage", "nas", "raid", "network", "router", "firewall", "vm", "virtual machine", "proxmox", "docker", "portainer", "nginx", "proxy", "ssh", "systemd", "pacman", "paru", "aur", "limine", "sbctl", "secure boot", "uefi", "bios", "dual boot", "dualboot", "distro"],
    "streaming": ["stream", "obs", "twitch", "youtube", "content", "video", "audio", "microphone", "mic", "voicemeeter", "overlay", "scene", "encoder", "nvenc", "recording", "broadcast", "multistream", "chatbot", "alert", "studio", "camera", "webcam", "elgato", "capture card"],
    "general": [],  # default
}

SENTIMENT_KEYWORDS = {
    "curious": ["how", "what is", "why", "explain", "understand", "learn", "curious", "wonder", "tell me about"],
    "frustrated": ["stuck", "error", "broken", "not working", "failed", "fail", "problem", "issue", "bug", "annoying", "hell", "damn", "wtf", "ugh", "can\'t get", "won\'t work", "doesn\'t work"],
    "exploratory": ["try", "test", "experiment", "explore", "option", "alternatives", "compare", "versus", "vs", "maybe", "consider", "brainstorm", "idea", "possibility"],
    "building": ["build", "create", "setup", "set up", "install", "deploy", "develop", "project", "implement", "configure", "make a", "making", "working on"],
    "stuck": ["stuck", "blocked", "can\'t", "unable", "confused", "lost", "don\'t know", "unsure", "help", "how do i", "troubleshoot"],
    "executing": ["run", "execute", "launch", "start", "automate", "script", "cron", "schedule", "pipeline", "workflow", "do this", "go ahead", "proceed"],
}

RESOLUTION_KEYWORDS = {
    "resolved": ["worked", "success", "fixed", "solved", "done", "complete", "thanks", "appreciate", "perfect", "great", "awesome", "working now"],
    "unresolved": ["still", "not working", "doesn\'t work", "won\'t", "failed", "error persists", "same issue", "problem remains"],
    "partial": ["partial", "kind of", "sort of", "almost", "mostly", "workaround", "temporary", "semi", "mostly works", "some issues"],
    "abandoned": ["never mind", "forget", "give up", "abandon", "stop", "quit", "not worth", "too hard", "later", "maybe later", "moved on"],
}

PROJECT_KEYWORDS = {p: p.replace("-", " ").split() for p in PROJECT_NAMES}

PEOPLE = ["bryan", "dad", "girlfriend"]

def extract_frontmatter(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not m:
        return {}, text
    fm_lines = m.group(1).splitlines()
    fm = {}
    for line in fm_lines:
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    body = text[m.end():]
    return fm, body

def classify(text, title, source):
    combined = (title + " " + text).lower()
    # Category
    cat_scores = {}
    for cat, kws in TOPIC_KEYWORDS.items():
        if cat == "general":
            continue
        score = sum(3 for kw in kws if kw in title.lower()) + sum(1 for kw in kws if kw in text.lower())
        cat_scores[cat] = score
    best_cat = max(cat_scores, key=cat_scores.get) if cat_scores and max(cat_scores.values()) > 0 else "general"

    # Tags (up to 8, deduped)
    tag_scores = defaultdict(int)
    for cat, kws in TOPIC_KEYWORDS.items():
        for kw in kws:
            if kw in combined:
                tag_scores[kw] += 1
    # Promote category + top keywords
    tags = [best_cat]
    for t, _ in Counter(tag_scores).most_common(10):
        if t not in tags and len(tags) < 8:
            tags.append(t)

    # Sentiment
    sent_scores = defaultdict(int)
    for sent, kws in SENTIMENT_KEYWORDS.items():
        for kw in kws:
            if kw in combined:
                sent_scores[sent] += 1
    sentiment = max(sent_scores, key=sent_scores.get) if sent_scores and max(sent_scores.values()) > 0 else "curious"

    # Resolution
    res_scores = defaultdict(int)
    for res, kws in RESOLUTION_KEYWORDS.items():
        for kw in kws:
            if kw in combined:
                res_scores[res] += 1
    # Default heuristic: if chat is short -> partial, if has success words -> resolved, if has errors/frustration -> unresolved
    resolution = max(res_scores, key=res_scores.get) if res_scores and max(res_scores.values()) > 0 else "partial"
    # Override: if text is very short, likely partial
    if len(text.split()) < 80:
        resolution = "partial"

    # Projects
    linked_projects = []
    for p, kws in PROJECT_KEYWORDS.items():
        if any(kw in combined for kw in kws) or p.replace("-", " ") in combined:
            linked_projects.append(p)

    # Nodes/entities
    linked_nodes = []
    for person in PEOPLE:
        if person in combined:
            linked_nodes.append(person)

    return {
        "tags": tags,
        "category": best_cat,
        "sentiment": sentiment,
        "resolution": resolution,
        "linked_projects": linked_projects,
        "linked_nodes": linked_nodes,
    }

def process_all():
    stats = defaultdict(int)
    all_files = []
    for src in SOURCES:
        src_dir = PROCESSED / src
        if not src_dir.exists():
            continue
        files = sorted(src_dir.glob("*.md"))
        print(f"[{src}] {len(files)} files")
        for f in files:
            fm, body = extract_frontmatter(f)
            title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else f.stem
            classification = classify(body, title, src)
            enriched_fm = {**fm, **classification}
            all_files.append({
                "src": src,
                "path": f,
                "title": title,
                "fm": enriched_fm,
                "body": body,
                "stem": f.stem,
            })
            stats[f"{src}_count"] += 1
            stats[f"cat_{classification['category']}"] += 1

    print(f"\nTotal parsed: {len(all_files)}")
    print("Categories:", {k:v for k,v in stats.items() if k.startswith("cat_")})

    # Write enrichment mapping JSON (do NOT overwrite originals)
    mapping_path = VAULT / "_meta" / "enrichment_mapping.json"
    serializable = []
    for item in all_files:
        serializable.append({
            "source": item["src"],
            "file": str(item["path"].relative_to(VAULT)),
            "title": item["title"],
            "enriched_frontmatter": item["fm"],
        })
    mapping_path.write_text(json.dumps(serializable, indent=2), encoding="utf-8")
    print(f"\nWrote enrichment mapping -> {mapping_path}")

    # Build topic aggregations
    topic_data = defaultdict(lambda: {"conversations": [], "tags": Counter(), "projects": set(), "people": set()})
    project_data = defaultdict(lambda: {"conversations": [], "first": None, "last": None})
    person_data = defaultdict(lambda: {"conversations": [], "mentions": 0, "quotes": []})

    for item in all_files:
        fm = item["fm"]
        cat = fm["category"]
        rel_path = str(item["path"].relative_to(VAULT))
        date = fm.get("date", "")

        topic_data[cat]["conversations"].append({"path": rel_path, "title": item["title"], "date": date})
        for t in fm["tags"]:
            topic_data[cat]["tags"][t] += 1
        for p in fm["linked_projects"]:
            topic_data[cat]["projects"].add(p)
            project_data[p]["conversations"].append({"path": rel_path, "title": item["title"], "date": date})
            if date:
                if project_data[p]["first"] is None or date < project_data[p]["first"]:
                    project_data[p]["first"] = date
                if project_data[p]["last"] is None or date > project_data[p]["last"]:
                    project_data[p]["last"] = date
        for person in fm["linked_nodes"]:
            topic_data[cat]["people"].add(person)
            person_data[person]["conversations"].append({"path": rel_path, "title": item["title"], "date": date})
            person_data[person]["mentions"] += 1
            # Add a quote snippet
            user_lines = extract_user_turns(item["body"], item["src"])
            if user_lines:
                person_data[person]["quotes"].append((item["src"], user_lines[0][:200]))

    # ─── Write Topic Pages ───
    topics_dir = NODES / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)
    for cat, data in topic_data.items():
        fname = f"{cat}.md"
        fpath = topics_dir / fname
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        top_tags = data["tags"].most_common(10)
        projects_list = sorted(data["projects"])
        people_list = sorted(data["people"])

        md = f"""---
type: topic
tags: [topic, moc]
aliases: [{cat.replace('-', ' ')}]
---

# {cat.replace('-', ' ').title()}

> 🧠 Topic hub for **{cat.replace('-', ' ').title()}**.

## Stats
- **Total conversations**: {len(convs)}
- **Top tags**: {', '.join([t for t,_ in top_tags[:5]])}
- **Linked projects**: {', '.join([f"[[nodes/projects/{p}|{p.replace('-',' ').title()}]]" for p in projects_list]) if projects_list else 'None'}
- **Linked people**: {', '.join([f"[[nodes/people/{p}|{p.title()}]]" for p in people_list]) if people_list else 'None'}

## Conversations
"""
        for c in convs[:100]:  # cap to keep file size sane
            md += f"- [[{c['path']}|{c['title'][:60]}]] — {c['date']}\n"
        if len(convs) > 100:
            md += f"\n_... and {len(convs)-100} more. See enrichment mapping for full list._\n"

        md += "\n## Connected Topics\n"
        for other_cat in sorted(topic_data.keys()):
            if other_cat != cat:
                md += f"- [[nodes/topics/{other_cat}.md|{other_cat.replace('-',' ').title()}]]\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Wrote topic: {fpath}")

    # ─── Write Project Pages ───
    projects_dir = NODES / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)
    for p, data in project_data.items():
        fpath = projects_dir / f"{p}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        md = f"""---
type: project
status: active
first_seen: {data['first'] or 'unknown'}
last_seen: {data['last'] or 'unknown'}
tags: [project, synthesis]
---

# {p.replace('-', ' ').title()}

> Evergreen notes on {p.replace('-', ' ')}.

## What It Is
Project identified across {len(convs)} conversation(s).

## Conversation Timeline
"""
        for c in convs[:80]:
            md += f"- [[{c['path']}|{c['title'][:60]}]] — {c['date']}\n"
        if len(convs) > 80:
            md += f"\n_... and {len(convs)-80} more._\n"

        md += "\n## Related Topics\n"
        # Find topics that link to this project
        for cat, tdata in topic_data.items():
            if p in tdata["projects"]:
                md += f"- [[nodes/topics/{cat}.md|{cat.replace('-',' ').title()}]]\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Wrote project: {fpath}")

    # ─── Write People Pages ───
    people_dir = NODES / "people"
    people_dir.mkdir(parents=True, exist_ok=True)
    for person, data in person_data.items():
        fpath = people_dir / f"{person}.md"
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        md = f"""---
type: person
tags: [people]
---

# {person.title()}

## Mentioned In
{len(convs)} conversation(s).

## Conversations
"""
        for c in convs[:60]:
            md += f"- [[{c['path']}|{c['title'][:60]}]] — {c['date']}\n"
        if len(convs) > 60:
            md += f"\n_... and {len(convs)-60} more._\n"

        md += "\n## What They Say\n"
        for src, quote in data["quotes"][:10]:
            md += f"> [{src}] {quote}...\n\n"

        fpath.write_text(md, encoding="utf-8")
        print(f"  Wrote person: {fpath}")

    print("\n=== Done ===")
    print(f"Total files processed: {len(all_files)}")
    print(f"Topics: {len(topic_data)}")
    print(f"Projects: {len(project_data)}")
    print(f"People: {len(person_data)}")

def extract_user_turns(body, source):
    markers = USER_MARKERS.get(source, ["### HUMAN", "### USER"])
    lines = []
    in_user = False
    for line in body.splitlines():
        stripped = line.strip()
        if any(stripped.startswith(m) for m in markers):
            in_user = True
            continue
        if any(stripped.startswith(m) for m in AI_MARKERS.get(source, ["### ASSISTANT"])):
            in_user = False
            continue
        if in_user and stripped:
            lines.append(stripped)
    return lines

if __name__ == "__main__":
    process_all()
