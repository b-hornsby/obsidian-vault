#!/usr/bin/env python3
"""
Task 1 — Vault Enrichment & Tag Writer
Parses all processed/ .md files, adds enriched frontmatter tags,
writes tags BACK to the source files (not just JSON),
and rebuilds all node pages.
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
    "ai-tools": ["llm", "ai", "agent", "claude", "gpt", "gemini", "grok", "model", "ollama",
                 "oobabooga", "cursor", "copilot", "rag", "mcp", "openai", "anthropic",
                 "llama.cpp", "gguf", "quantized", "inference", "embedding", "fine-tune",
                 "lora", "hermes", "text-generation", "local llm", "local model",
                 "ai assistant", "helpdesk ai", "autogen", "crewai", "dspy", "langchain",
                 "langgraph", "n8n", "vector db", "chroma", "pinecone", "weaviate"],
    "crypto-web3": ["solana", "bitcoin", "ethereum", "crypto", "defi", "meteora", "dlmm",
                    "jupiter", "dex", "token", "wallet", "phantom", "blockchain", "web3", "nft",
                    "trading", "perp", "perpetual", "yield", "liquidity", "amm", "swap",
                    "usdc", "icp", "internet computer", "memecoin", "pump.fun", "axiom",
                    "hyperliquid", "leverage", "margin", "farm", "staking", "near", "zec",
                    "hype", "wb tc", "long", "short", "funding rate", "liquidation"],
    "coding": ["python", "javascript", "typescript", "rust", "go", "golang", "bash", "shell",
               "code", "script", "debug", "error", "syntax", "import", "module", "package",
               "pip", "npm", "git", "github", "vs code", "ide", "function", "class", "api",
               "json", "csv", "database", "sql", "html", "css", "react", "node", "docker",
               "dockerfile", "compose", "kubernetes", "fastapi", "flask", "django", "golang",
               "cli", "terminal", "compile", "runtime", "module", "sdk"],
    "career": ["resume", "job", "interview", "certification", "cert", "comptia", "a+", "network+",
               "security+", "it job", "help desk", "helpdesk", "linkedin", "cover letter",
               "hire", "salary", "career", "entry level", "junior", "tiffin", "secai",
               "learning", "course", "study", "exam", "prep", "at", "job application",
               "warehouse", "income", "loan", "garnishment", "financial"],
    "homelab": ["homelab", "server", "linux", "cachyos", "arch", "ubuntu", "debian", "wsl",
                "wsl2", "windows", "hardware", "nvidia", "gpu", "cpu", "ram", "ssd", "hdd",
                "storage", "nas", "raid", "network", "router", "firewall", "vm",
                "virtual machine", "proxmox", "docker", "portainer", "nginx", "proxy", "ssh",
                "systemd", "pacman", "paru", "aur", "limine", "sbctl", "secure boot", "uefi",
                "bios", "dual boot", "dualboot", "distro", "pop!os", "nixos", "fedora",
                "rtx 5080", "rtx 5090", "mac mini", "m4", "ollama"],
    "streaming": ["stream", "obs", "twitch", "youtube", "content", "video", "audio",
                  "microphone", "mic", "voicemeeter", "overlay", "scene", "encoder", "nvenc",
                  "recording", "broadcast", "multistream", "chatbot", "alert", "studio",
                  "camera", "webcam", "elgato", "capture card", "discord", "restream",
                  "itum", "streamlabs", "vdo.ninja"],
    "general": [],
}

SENTIMENT_KEYWORDS = {
    "curious": ["how", "what is", "why", "explain", "understand", "learn", "curious",
                "wonder", "tell me about"],
    "frustrated": ["stuck", "error", "broken", "not working", "failed", "fail", "problem",
                   "issue", "bug", "annoying", "hell", "damn", "wtf", "ugh",
                   "can\\'t get", "won\\'t work", "doesn\\'t work", "doesnt work"],
    "exploratory": ["try", "test", "experiment", "explore", "option", "alternatives",
                    "compare", "versus", "vs", "maybe", "consider", "brainstorm", "idea",
                    "possibility", "worth it", "should i"],
    "building": ["build", "create", "setup", "set up", "install", "deploy", "develop",
                 "project", "implement", "configure", "make a", "making", "working on",
                 "building a"],
    "stuck": ["stuck", "blocked", "can\\'t", "unable", "confused", "lost", "don\\'t know",
              "unsure", "help", "how do i", "troubleshoot", "cant figure out"],
    "executing": ["run", "execute", "launch", "start", "automate", "script", "cron",
                  "schedule", "pipeline", "workflow", "do this", "go ahead", "proceed",
                  "done", "finished", "shipped", "live"],
}

RESOLUTION_KEYWORDS = {
    "resolved": ["worked", "success", "fixed", "solved", "done", "complete", "thanks",
                 "appreciate", "perfect", "great", "awesome", "working now", "nice",
                 "exactly what i needed", "that works"],
    "unresolved": ["still", "not working", "doesn\\'t work", "won\\'t", "failed",
                   "error persists", "same issue", "problem remains", "doesnt work",
                   "still stuck", "still broken"],
    "partial": ["partial", "kind of", "sort of", "almost", "mostly", "workaround",
                "temporary", "semi", "mostly works", "some issues", "close enough"],
    "abandoned": ["never mind", "forget", "give up", "abandon", "stop", "quit",
                  "not worth", "too hard", "later", "maybe later", "moved on"],
}

PROJECT_PHRASES = {
    "flappy-meme-bird": [
        "flappy bird", "flappy meme", "dank flappy", "flappy-meme",
        "flappy bird clone", "flappy bird-style", "flappy bird game",
        "flappy bird dank", "flappy meme bird", "flappy bird meme",
        "flappy bird with meme", "flappy bird assets", "flappy bird character",
        "flappy bird shop", "flappy bird coin", "flappy bird logo",
        "flappy bird phaser", "flappy bird canvas", "flappy bird html5",
        "flappy bird vibe", "flappy bird windsurf", "flappy bird prd",
        "dank flappy bird", "flappy bird project", "flappy bird code",
        "flappy bird javascript", "flappy bird typescript",
    ],
    "homelab-stack": [
        "homelab", "home lab", "self-hosted", "self hosted",
        "cachyos", "cachy os", "proxmox", "portainer",
        "tailscale", "cloudflare tunnel", "cloudflare tunnels",
        "local llm server", "local ai server", "home server",
        "homelab stack", "homelab-stack", "home lab stack",
        "homelab sprint", "homelab demo", "homelab mvp",
        "homelab project", "homelab setup", "homelab build",
        "homelab infrastructure", "homelab hardware", "homelab os",
        "homelab docker", "homelab vm", "homelab network",
        "homelab config", "homelab configuration",
    ],
    "it-certification": [
        "comptia", "a+ cert", "network+ cert", "security+ cert",
        "it certification", "it cert", "certification exam",
        "comptia a+", "comptia network+", "comptia security+",
        "tiffin cert", "secai cert", "secai certification",
        "it exam", "cert exam", "certification study",
        "book the exam", "book your exam", "exam booked",
        "study system", "anki deck", "practice test score",
        "help desk cert", "helpdesk cert", "it help desk cert",
        "certification prep", "exam prep", "exam preparation",
        "study schedule", "study session", "study log",
        "practice test", "practice exam", "mock exam",
        "certification goal", "cert goal", "get certified",
        "become certified", "certification path", "cert path",
        "career bridge", "it bridge", "bridge cert",
    ],
    "operation-immortal-agent": [
        "immortal agent", "operation immortal", "operation-immortal",
        "oia project", "oia code", "oia codebase",
        "solana trading agent", "solana fund manager",
        "meteora dlmm", "phantom mcp", "jupiter api trading",
        "trading agent", "defi trading agent", "autonomous trading",
        "solana defi trading", "dlmm trading", "perpetual trading agent",
        "immortal agent project", "immortal agent code",
        "immortal agent trade", "immortal agent test",
        "immortal agent live", "immortal agent archive",
        "immortal agent ship", "immortal agent kill",
        "immortal agent stalled", "immortal agent blocked",
        "immortal agent uptime", "immortal agent monitor",
        "immortal agent real trade", "immortal agent devnet",
        "immortal agent testnet", "immortal agent mainnet",
        "immortal agent phantom", "immortal agent jupiter",
        "immortal agent meteora", "immortal agent dlmm",
    ],
    "private-ai-consulting": [
        "private ai consulting", "private-ai-consulting",
        "private ai stack", "private-ai-stack",
        "ai consulting", "consulting package", "consulting business",
        "client-facing demo", "client facing demo",
        "sell ai", "sell local ai", "sell private ai",
        "clinic ai", "office ai setup", "small business ai",
        "ai setup for", "ai package", "$500 package", "500 package",
        "first paid engagement", "first client",
        "prospect outreach", "reach out to 3", "reach out to three",
        "private ai revenue", "consulting revenue", "ai consulting revenue",
        "private ai business", "ai consulting business",
        "private ai service", "ai consulting service",
        "private ai deliverable", "consulting deliverable",
        "private ai scope", "consulting scope",
        "private ai pricing", "consulting pricing",
        "private ai prospect", "consulting prospect",
        "private ai pitch", "consulting pitch",
        "private ai offer", "consulting offer",
    ],
    "second-brain-vault": [
        "second brain", "second-brain", "second brain vault",
        "obsidian vault", "vault setup", "vault structure",
        "knowledge graph", "knowledge base", "personal knowledge",
        "vault audit", "vault health", "vault optimization",
        "enrichment mapping", "enrichment algorithm", "enrich_and_tag",
        "processed files", "processed/ files", "conversation vault",
        "ai conversation vault", "conversation archive",
        "hermes briefing", "weekly briefing", "vault briefing",
        "node pages", "topic pages", "project pages",
        "dataview query", "dataview queries", "live dataview",
        "wikilink", "obsidian note", "obsidian-based",
        "vault integration", "vault meta", "vault system",
        "vault handoff", "vault cron", "vault weekly",
        "vault sweep", "vault check", "vault status",
        "vault second brain", "vault as second brain",
        "second brain setup", "second brain system",
        "second brain operational", "second brain status",
    ],
    "streaming-rig": [
        "streaming rig", "streaming-rig", "stream rig",
        "obs streaming", "obs setup", "obs scene",
        "voicemeeter", "voice meeter", "ndi stream",
        "multistream", "multi-stream", "restream",
        "stream to tiktok", "tiktok studio", "tiktok stream",
        "stream to twitch", "twitch stream", "youtube stream",
        "streaming setup", "streaming infrastructure",
        "content plan", "video topics", "streaming content",
        "audio routing", "audio mix", "microphone setup",
        "streaming audio", "capture card", "elgato stream",
        "streamlabs", "vdo.ninja", "stream alert",
        "stream overlay", "overlay scene", "stream scene",
        "streaming equipment", "streaming gear",
        "streaming pc", "streaming computer",
        "streaming config", "streaming configuration",
        "obs audio", "obs video", "obs capture",
        "obs encoder", "obs nvenc", "obs bitrate",
    ],
}

PROJECT_NAMES = list(PROJECT_PHRASES.keys())
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


def write_frontmatter_to_file(path, enriched_fm, body):
    """Rewrite the file with enriched frontmatter, preserving the body."""
    fm_lines = []
    for k, v in enriched_fm.items():
        if isinstance(v, list):
            fm_lines.append(f"{k}: [{', '.join(repr(str(x)) for x in v)}]")
        else:
            fm_lines.append(f"{k}: {v}")
    fm_block = "---\n" + "\n".join(fm_lines) + "\n---\n"
    path.write_text(fm_block + body, encoding="utf-8")


def classify(text, title, source):
    combined = (title + " " + text).lower()
    # Category
    cat_scores = {}
    for cat, kws in TOPIC_KEYWORDS.items():
        if cat == "general":
            continue
        score = sum(3 for kw in kws if f" {kw} " in f" {combined} ") + \
                sum(3 for kw in kws if kw in title.lower()) + \
                sum(1 for kw in kws if kw in combined)
        cat_scores[cat] = score
    best_cat = max(cat_scores, key=cat_scores.get) if cat_scores and max(cat_scores.values()) > 0 else "general"

    # Tags (up to 8, deduped)
    tag_scores = defaultdict(int)
    for cat, kws in TOPIC_KEYWORDS.items():
        for kw in kws:
            if kw in combined:
                tag_scores[kw] += 1
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
    resolution = max(res_scores, key=res_scores.get) if res_scores and max(res_scores.values()) > 0 else "partial"
    if len(text.split()) < 80:
        resolution = "partial"

    # Projects — precise phrase matching using PROJECT_PHRASES
    linked_projects = []
    for project, phrases in PROJECT_PHRASES.items():
        for phrase in phrases:
            if phrase in combined:
                linked_projects.append(project)
                break  # one match is enough per project

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
    tagged_count = 0
    skipped_count = 0

    print("=== Phase 1: Enrich and tag processed/ files ===\n")
    for src in SOURCES:
        src_dir = PROCESSED / src
        if not src_dir.exists():
            continue
        files = sorted(src_dir.glob("*.md"))
        src_tagged = 0
        print(f"[{src}] {len(files)} files")
        for f in files:
            fm, body = extract_frontmatter(f)
            title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else f.stem
            classification = classify(body, title, src)
            enriched_fm = {**fm, **classification}

            # Write tags back to the source file
            write_frontmatter_to_file(f, enriched_fm, body)
            tagged_count += 1
            src_tagged += 1

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

        print(f"  -> Tagged {src_tagged} files")

    print(f"\nTotal tagged: {tagged_count}")
    print(f"Categories: {dict({k:v for k,v in stats.items() if k.startswith('cat_')})}")

    # Write enrichment mapping JSON
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
    print(f"Wrote enrichment mapping -> {mapping_path}")

    # ─── Phase 2: Build Topic Aggregations ───
    print("\n=== Phase 2: Build node pages ===\n")
    topic_data = defaultdict(lambda: {"conversations": [], "tags": Counter(),
                                      "projects": set(), "people": set(),
                                      "sentiments": Counter(), "resolutions": Counter()})
    project_data = defaultdict(lambda: {"conversations": [], "first": None, "last": None})
    person_data = defaultdict(lambda: {"conversations": [], "mentions": 0, "quotes": []})

    for item in all_files:
        fm = item["fm"]
        cat = fm["category"]
        rel_path = str(item["path"].relative_to(VAULT))
        date = fm.get("date", "")

        topic_data[cat]["conversations"].append({
            "path": rel_path, "title": item["title"],
            "date": date, "source": item["src"]
        })
        for t in fm["tags"]:
            topic_data[cat]["tags"][t] += 1
        topic_data[cat]["sentiments"][fm["sentiment"]] += 1
        topic_data[cat]["resolutions"][fm["resolution"]] += 1

        for p in fm["linked_projects"]:
            topic_data[cat]["projects"].add(p)
            project_data[p]["conversations"].append({
                "path": rel_path, "title": item["title"], "date": date
            })
            if date:
                if project_data[p]["first"] is None or date < project_data[p]["first"]:
                    project_data[p]["first"] = date
                if project_data[p]["last"] is None or date > project_data[p]["last"]:
                    project_data[p]["last"] = date

        for person in fm["linked_nodes"]:
            topic_data[cat]["people"].add(person)
            person_data[person]["conversations"].append({
                "path": rel_path, "title": item["title"], "date": date
            })
            person_data[person]["mentions"] += 1
            user_lines = extract_user_turns(item["body"], item["src"])
            if user_lines:
                person_data[person]["quotes"].append((item["src"], user_lines[0][:200]))

    # Source breakdown per topic
    source_counts = defaultdict(lambda: defaultdict(int))
    for item in all_files:
        source_counts[item["fm"]["category"]][item["src"]] += 1

    # ─── Write Topic Pages ───
    topics_dir = NODES / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)

    # Top tags per category (computed globally for sourcing)
    for cat, data in topic_data.items():
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        top_tags = data["tags"].most_common(8)
        projects_list = sorted(data["projects"])
        people_list = sorted(data["people"])
        sc = source_counts.get(cat, {})
        src_str = ", ".join([f"{k}={v}" for k, v in sorted(sc.items())])
        sentiments = data["sentiments"]
        resolutions = data["resolutions"]
        total_convs = len(convs)
        resolved = resolutions.get("resolved", 0)
        resolution_rate = f"{int(resolved/total_convs*100)}%" if total_convs > 0 else "0%"

        md = f"""---
type: topic
tags: [topic, moc, q2-2026]
aliases: [{cat.replace('-', ' ')}]
---

# {cat.replace('-', ' ').title()}

> Topic tracked across **{total_convs} conversations**.

## Summary

- **By source:** {src_str}
- **Top tags:** {', '.join([t for t,_ in top_tags[:6]])}
- **Resolution rate:** {resolution_rate} resolved ({resolved}/{total_convs})
- **Sentiment breakdown:** {', '.join([f'{k}={v}' for k,v in sentiments.most_common(3)])}

## Activity Timeline

"""

        # Build monthly activity
        monthly = defaultdict(int)
        for c in convs:
            if c['date']:
                ym = c['date'][0:7]  # YYYY-MM
                monthly[ym] += 1
        for ym in sorted(monthly.keys()):
            md += f"| {ym} | {monthly[ym]} |\n"

        md += f"""
## Recent Conversations

"""
        for c in convs[-15:]:
            md += f"- [[{c['path']}|{c['title'][:60]}]] — {c['date']}\n"

        md += f"""
## All Conversations

```dataview
TABLE title AS "Title", date AS "Date", source AS "Source"
FROM "processed"
WHERE contains(tags, "{cat}")
SORT date DESC
LIMIT 50
```

## Related Topics

"""
        for other_cat in sorted(topic_data.keys()):
            if other_cat != cat:
                md += f"- [[nodes/topics/{other_cat}.md|{other_cat.replace('-',' ').title()}]]\n"

        fpath = topics_dir / f"{cat}.md"
        fpath.write_text(md, encoding="utf-8")
        print(f"  Wrote topic: {fpath.name}")

    # ─── Write Project Pages ───
    projects_dir = NODES / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)
    for p, data in project_data.items():
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        md = f"""---
type: project
status: active
first_seen: {data['first'] or 'unknown'}
last_seen: {data['last'] or 'unknown'}
tags: [project, synthesis]
---

# {p.replace('-', ' ').title()}

> Project tracked across **{len(convs)} conversations**.

## Conversation Timeline

"""
        for c in convs:
            md += f"- [[{c['path']}|{c['title'][:60]}]] — {c['date']}\n"

        md += "\n## Related Topics\n"
        for cat, tdata in topic_data.items():
            if p in tdata["projects"]:
                md += f"- [[nodes/topics/{cat}.md|{cat.replace('-',' ').title()}]]\n"

        fpath = projects_dir / f"{p}.md"
        fpath.write_text(md, encoding="utf-8")
        print(f"  Wrote project: {fpath.name}")

    # ─── Write People Pages ───
    people_dir = NODES / "people"
    people_dir.mkdir(parents=True, exist_ok=True)
    for person, data in person_data.items():
        convs = sorted(data["conversations"], key=lambda x: x["date"] or "")
        md = f"""---
type: person
tags: [people]
---

# {person.title()}

Mentioned in **{len(convs)} conversations**.

## Conversations

"""
        for c in convs[:60]:
            md += f"- [[{c['path']}|{c['title'][:60]}]] — {c['date']}\n"

        md += "\n## What They Say\n"
        for src, quote in data["quotes"][:10]:
            md += f"> [{src}] {quote}...\n\n"

        fpath = people_dir / f"{person}.md"
        fpath.write_text(md, encoding="utf-8")
        print(f"  Wrote person: {fpath.name}")

    print(f"\n=== Done ===")
    print(f"Files tagged: {tagged_count}")
    print(f"Topics: {len(topic_data)}, Projects: {len(project_data)}, People: {len(person_data)}")

    # Print summary stats for briefing
    print("\n=== Stats for Briefing ===")
    for cat, data in sorted(topic_data.items()):
        total = len(data["conversations"])
        resolved = data["resolutions"].get("resolved", 0)
        rate = int(resolved/total*100) if total > 0 else 0
        sc = source_counts.get(cat, {})
        top_src = max(sc, key=sc.get) if sc else "?"
        top_src_count = sc.get(top_src, 0)
        print(f"  {cat}: {total} convs, {rate}% resolved, top={top_src}({top_src_count}), sentiment={data['sentiments'].most_common(1)}")


def extract_user_turns(body, source):
    markers = USER_MARKERS.get(source, ["### HUMAN", "### USER"])
    ai_markers = AI_MARKERS.get(source, ["### ASSISTANT"])
    lines = []
    in_user = False
    for line in body.splitlines():
        stripped = line.strip()
        if any(stripped.startswith(m) for m in markers):
            in_user = True
            continue
        if any(stripped.startswith(m) for m in ai_markers):
            in_user = False
            continue
        if in_user and stripped:
            lines.append(stripped)
    return lines


if __name__ == "__main__":
    process_all()
