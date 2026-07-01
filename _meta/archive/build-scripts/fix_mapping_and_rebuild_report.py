#!/usr/bin/env python3
"""
1. Update enrichment_mapping.json with restored projects
2. Regenerate goal alignment report with STRICT goal scoring
"""
import json, re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

VAULT = Path("/vault")
m = json.loads((VAULT / "_meta" / "enrichment_mapping.json").read_text(encoding="utf-8"))

# ── Part 1: Update mapping with restored projects ──

def detect_restored_projects(item):
    """Balanced detection for homelab-stack and private-ai-consulting."""
    title = item["title"].lower()
    body = item.get("body", "").lower()
    combined = title + " " + body
    found = []

    # Homelab: hardware + setup/build context
    hw_terms = ["4090", "rtx", "7700", "ryzen", "nvidia-smi", "cachyos install", "cachyos setup",
                "dual boot", "dualboot", "pfsense", "opnsense", "unraid", "truenas", "proxmox",
                "server rack", "home server", "nas setup", "gpu cooling", "hardware", "desktop-n",
                "steam deck", "limine", "sbctl", "secure boot"]
    hw_count = sum(1 for t in hw_terms if t in combined)
    if hw_count >= 2:
        found.append("homelab-stack")
    # Also: category=homelab + strong hardware signals
    if item["enriched_frontmatter"].get("category") == "homelab" and hw_count >= 1:
        if "homelab-stack" not in found:
            found.append("homelab-stack")

    # Consulting: business direction for AI
    biz_terms = ["private ai", "ai consulting", "ai business", "ai for business", "client ai",
                 "custom ai", "sell ai", "ai service", "ai solution", "business ai",
                 "freelance ai", "ai product", "tech service business", "tech support business",
                 "pc repair", "custom build shop", "business name", "linkedin job", "linkedin profile"]
    biz_count = sum(1 for t in biz_terms if t in combined)
    if biz_count >= 1:
        found.append("private-ai-consulting")

    return found

# Update each item
updated_count = 0
for item in m:
    existing = set(item["enriched_frontmatter"].get("linked_projects", []))
    new = set(detect_restored_projects(item))
    merged = sorted(existing | new)
    if merged != sorted(existing):
        item["enriched_frontmatter"]["linked_projects"] = merged
        updated_count += 1

# Save updated mapping
(VAULT / "_meta" / "enrichment_mapping.json").write_text(
    json.dumps(m, indent=2), encoding="utf-8"
)
print(f"Updated {updated_count} records with restored projects.")

# Verify project distribution
proj_counts = Counter()
for item in m:
    for p in item["enriched_frontmatter"].get("linked_projects", []):
        proj_counts[p] += 1
print("Project distribution after fix:")
for p, c in proj_counts.most_common():
    print(f"  {p}: {c}")

# ── Part 2: STRICT Goal Alignment Report ──

LAST_DATE = datetime(2026, 4, 9)
D30 = datetime(2026, 3, 10)
D60 = datetime(2026, 2, 8)
D90 = datetime(2026, 1, 9)

def parse_date(d):
    try:
        return datetime.strptime(d, "%Y-%m-%d")
    except:
        return None

# STRICT goal definitions: only strong signals
GOALS = {
    "near_term": {
        "Privatized AI Solutions": {
            "projects": ["private-ai-consulting"],
            "min_score": 15,  # Must have project link OR strong biz keywords
            "keywords": ["private ai", "ai consulting", "ai business", "client ai", "sell ai", "ai service", "business ai", "freelance ai", "custom ai solution", "ai product", "ai for business"],
        },
        "Deep Tooling Mastery": {
            "projects": ["homelab-stack", "second-brain-vault"],
            "min_score": 12,
            "keywords": ["ollama", "llama.cpp", "gguf", "quantized", "mcp server", "rag system", "agent framework", "claude code", "cursor ide", "oobabooga", "text-generation-webui", "local llm setup", "hermes agent", "model quantization"],
        },
        "IT Bridge (Credibility + Income)": {
            "projects": ["it-certification"],
            "min_score": 10,
            "keywords": ["resume", "linkedin profile", "job application", "help desk job", "helpdesk job", "comptia a+", "comptia network+", "security+", "tiffin university", "tiffin cert", "secai cert", "certification exam", "interview prep", "cover letter", "entry level it"],
        },
    },
    "medium_term": {
        "Operation Immortal Agent": {
            "projects": ["operation-immortal-agent"],
            "min_score": 15,
            "keywords": ["meteora", "dlmm", "solana bot", "autonomous fund", "phantom mcp", "jupiter perp", "liquidity position", "yield farming", "trading bot solana", "defi bot", "dex bot"],
        },
        "Content / Streaming Infrastructure": {
            "projects": ["streaming-rig"],
            "min_score": 10,
            "keywords": ["obs studio", "obs setup", "twitch stream", "youtube stream", "multistream", "stream overlay", "voicemeeter", "capture card", "elgato", "stream deck", "recording setup", "broadcast setup"],
        },
        "AI + Security Convergence": {
            "projects": [],
            "min_score": 8,
            "keywords": ["security+", "secai", "ai security", "security ai", "cybersecurity", "penetration testing", "threat detection", "vulnerability scan", "siem", "soc analyst", "ethical hacking", "security certification"],
        },
    },
    "long_term": {
        "Blockchain Data Analysis at Scale": {
            "projects": [],
            "min_score": 8,
            "keywords": ["blockchain data analysis", "exchange data", "on-chain analysis", "onchain data", "quantitative crypto", "crypto quant", "market maker data", "institutional blockchain", "binance api", "coinbase api"],
        },
    },
}

def score_item_strict(item, goal_def):
    score = 0
    title = item["title"].lower()
    body = item.get("body", "").lower()
    combined = title + " " + body
    fm = item["enriched_frontmatter"]

    # Project match = strong signal
    for p in goal_def["projects"]:
        if p.lower() in [x.lower() for x in fm.get("linked_projects", [])]:
            score += 20

    # Keyword match: phrase-only, weighted higher in title
    for kw in goal_def["keywords"]:
        if kw in title:
            score += 5
        elif kw in body:
            score += 2

    return score

# Build strict goal matches
goal_conversations = defaultdict(lambda: defaultdict(list))
for item in m:
    for tier_name, tier in GOALS.items():
        for goal_name, goal_def in tier.items():
            score = score_item_strict(item, goal_def)
            if score >= goal_def["min_score"]:
                goal_conversations[tier_name][goal_name].append(item)

# Project metrics
project_conversations = defaultdict(list)
for item in m:
    for p in item["enriched_frontmatter"].get("linked_projects", []):
        project_conversations[p].append(item)

def pm(proj):
    convs = project_conversations.get(proj, [])
    if not convs:
        return None
    dates = [parse_date(c["enriched_frontmatter"].get("date", "")) for c in convs]
    dates = [d for d in dates if d]
    sentiments = Counter(c["enriched_frontmatter"].get("sentiment", "?") for c in convs)
    resolutions = Counter(c["enriched_frontmatter"].get("resolution", "?") for c in convs)
    recent = [sum(1 for d in dates if d >= D30), sum(1 for d in dates if d >= D60), sum(1 for d in dates if d >= D90)]
    return {
        "count": len(convs),
        "first": min(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "last": max(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "sentiments": sentiments,
        "resolutions": resolutions,
        "recent30": recent[0], "recent60": recent[1], "recent90": recent[2],
        "stalled": (LAST_DATE - max(dates)).days > 60 if dates else True,
    }

def gm(goal_name, convs):
    if not convs:
        return None
    dates = [parse_date(c["enriched_frontmatter"].get("date", "")) for c in convs]
    dates = [d for d in dates if d]
    unique = len(set(c["file"] for c in convs))
    sentiments = Counter(c["enriched_frontmatter"].get("sentiment", "?") for c in convs)
    resolutions = Counter(c["enriched_frontmatter"].get("resolution", "?") for c in convs)
    recent = [sum(1 for d in dates if d >= D30), sum(1 for d in dates if d >= D60), sum(1 for d in dates if d >= D90)]
    return {
        "count": unique,
        "first": min(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "last": max(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "sentiments": sentiments,
        "resolutions": resolutions,
        "recent30": recent[0], "recent60": recent[1], "recent90": recent[2],
        "stalled": (LAST_DATE - max(dates)).days > 60 if dates else True,
    }

# ── Build report ──
lines = []
def L(s=""): lines.append(s)

L("# Goal Alignment Report")
L()
L(f"> Generated: {LAST_DATE.strftime('%Y-%m-%d')}")
L(f"> Total conversations analyzed: {len(m)}")
L(f"> Date range: 2023-11-05 to 2026-04-09")
L()

L("## Current Goal Hierarchy")
L("```")
L("Primary → Privatized AI Solutions + Deep Tooling Mastery")
L("        → IT Bridge (Credibility + Income)")
L("Medium  → Operation Immortal Agent")
L("        → Content / Streaming Infrastructure")
L("        → AI + Security Convergence")
L("Long    → Blockchain Data Analysis at Scale")
L("```")
L()

L("## Progress Signals by Project")
L("| Project | Convos | First → Last | 30d | 60d | 90d | Status |")
L("|---------|--------|-------------|-----|-----|-----|--------|")
TOP_PROJECTS = ["homelab-stack", "operation-immortal-agent", "private-ai-consulting",
                "it-certification", "second-brain-vault", "streaming-rig", "flappy-meme-bird"]
for proj in TOP_PROJECTS:
    p = pm(proj)
    if not p:
        L(f"| {proj.replace('-', ' ').title()} | 0 | N/A | — | — | — | 🔴 No data |")
        continue
    status = "🔴 STALLED" if p["stalled"] else "🟢 ACTIVE"
    L(f"| {proj.replace('-', ' ').title()} | {p['count']} | {p['first']} → {p['last']} | {p['recent30']} | {p['recent60']} | {p['recent90']} | {status} |")
L()

L("### Sentiment & Resolution Breakdown")
L()
for proj in TOP_PROJECTS:
    p = pm(proj)
    if not p:
        continue
    L(f"**{proj.replace('-', ' ').title()}** ({p['count']} convos)")
    L(f"- Sentiment: {', '.join([f'{k}={v}' for k,v in p['sentiments'].most_common()])}")
    L(f"- Resolution: {', '.join([f'{k}={v}' for k,v in p['resolutions'].most_common()])}")
    L()

L("## Goal Coverage Analysis")
for tier_name, tier in GOALS.items():
    L(f"### {tier_name.replace('_', ' ').title()}")
    L()
    for goal_name, goal_def in tier.items():
        convs = goal_conversations[tier_name][goal_name]
        g = gm(goal_name, convs)
        if not g:
            L(f"**🔴 {goal_name}**: Zero signal. Not discussed.")
            L()
            continue
        status = "🔴 STALLED" if g["stalled"] else "🟢 ACTIVE"
        L(f"**{goal_name}** — {g['count']} unique conversations, last: {g['last']} {status}")
        L(f"- 30d/60d/90d activity: {g['recent30']}/{g['recent60']}/{g['recent90']}")
        L(f"- Sentiment: {', '.join([f'{k}={v}' for k,v in g['sentiments'].most_common(3)])}")
        L(f"- Resolution: {', '.join([f'{k}={v}' for k,v in g['resolutions'].most_common(3)])}")
        L()

L("## Misalignments & Conflicts")
L()
L("### ⚠️ Where the Energy Is NOT Going")
L()

# Privatized AI
consult_convs = project_conversations.get("private-ai-consulting", [])
if len(consult_convs) < 20:
    L(f"🟡 **Privatized AI Solutions**: Only **{len(consult_convs)} conversations** explicitly about consulting/business.")
    L("Most 'AI' energy goes into *using* tools rather than *selling* or *packaging* them. Big gap between wanting to do this for clients and actually discussing business models, pricing, or client acquisition.")
    L()

# IT Bridge
it_p = pm("it-certification")
if it_p and it_p["recent90"] < 3:
    L(f"🟡 **IT Bridge**: Only **{it_p['recent90']} conversations in the last 90 days.**")
    L("The IT cert is supposed to be 'credibility and income while the bigger thing develops.' But the volume is minimal. Either it's on track and doesn't need discussion, or it's getting deprioritized.")
    L()

# Homelab volume
homelab_p = pm("homelab-stack")
if homelab_p and homelab_p["count"] > 200:
    L(f"🟠 **Homelab Stack**: **{homelab_p['count']} conversations** — massive volume.")
    L("This is the dominant project by count, but much of it is *setup/debugging* (WSL2 errors, CUDA installs, model loading) rather than *building*. The lab exists to run experiments, not just to be maintained.")
    L()

# OIA
oia_p = pm("operation-immortal-agent")
if oia_p and oia_p["recent30"] < 5:
    L(f"🟡 **Operation Immortal Agent**: Only **{oia_p['recent30']} conversations in last 30 days.**")
    L("Described as 'the most serious thing I've built.' 24 total conversations. Either it's in maintenance mode or blocked. Needs a go/no-go decision.")
    L()

# Streaming
stream_p = pm("streaming-rig")
if stream_p and stream_p["count"] < 20:
    L(f"🟡 **Content/Streaming**: Only **{stream_p['count']} conversations.**")
    L("The rig exists but the content strategy doesn't. No discussions about audience building, content calendar, or streaming schedule.")
    L()

# AI + Security
sec_convs = goal_conversations["medium_term"]["AI + Security Convergence"]
if not sec_convs:
    L("🔴 **AI + Security Convergence**: **ZERO conversations.**")
    L("Bryan says this is the right direction. The vault says he hasn't touched it. Not a single mention of SecAI, threat detection, or SIEM in 3,400 conversations.")
    L()

# Long term
block_convs = goal_conversations["long_term"]["Blockchain Data Analysis at Scale"]
if not block_convs:
    L("🔴 **Long Term (Blockchain Data Analysis at Scale)**: **Zero signal.**")
    L("No conversations about exchange data APIs, quantitative analysis, or institutional blockchain roles. This remains a vision statement with no supporting exploration.")
    L()

L("### 🔍 Cross-LLM Pattern")
L()
sources_by_project = defaultdict(Counter)
for proj in ["operation-immortal-agent", "private-ai-consulting", "it-certification", "homelab-stack"]:
    for c in project_conversations.get(proj, []):
        sources_by_project[proj][c["source"]] += 1
for proj in ["operation-immortal-agent", "private-ai-consulting", "it-certification", "homelab-stack"]:
    sc = sources_by_project[proj]
    if sc:
        L(f"- **{proj.replace('-', ' ').title()}**: {dict(sc)}")
L()

L("## Recommended Next Actions / Quarterly Focus")
L()
L("### Q2 2026 Priority Matrix")
L()
L("| Priority | Action | Rationale |")
L("|----------|--------|-----------|")
L("| **P0** | **Ship Operation Immortal Agent or kill it** | 24 conversations is enough research. Make it trade live, or document why not and free the mental space. |")
L("| **P0** | **Start SecAI / Security+ conversations NOW** | Zero signal = zero progress. Add 1 conversation per week minimum or drop the goal. |")
L("| **P1** | **Turn homelab energy into ONE client-facing demo** | 344 convos of tooling depth → package a working demo (helpdesk bot, local RAG pipeline). Something you can show, not just talk about. |")
L("| **P1** | **Schedule IT cert exam or explicitly deprioritize** | Either commit to a test date or rewrite goals.md to remove IT as a bridge. Ambiguity is expensive. |")
L("| **P2** | **Write content plan for streaming** | 16 convos on setup. 0 on content. Decide: is this marketing or hobby? If marketing, what's the first 10 videos about? |")
L("| **P2** | **Explore ONE exchange data API** | Long-term goal needs at least *some* signal. Try Binance or Coinbase API for 1 hour. Document what you learn. |")
L()

L("### Immediate Conversation Prompts (Ask Next)")
L()
L("1. **Immortal Agent**: 'What is the single blocker preventing this from trading live? Technical, capital, or fear?'")
L("2. **Security+AI**: 'What specific cert or course starts this week? What's module 1?'")
L("3. **AI Consulting**: 'What would a $500 local-AI package look like? Who buys it? How do I deliver it?'")
L("4. **Career Bridge**: 'If I don't get the IT cert, what's the alternative credibility path? Portfolio? Github?'")
L("5. **Homelab**: 'Which of these 344 conversations produced a reusable asset? Name the top 5.'")
L()

L("## Relevant Entity Pages")
L("- [[nodes/projects/operation-immortal-agent]]")
L("- [[nodes/projects/private-ai-consulting]]")
L("- [[nodes/projects/homelab-stack]]")
L("- [[nodes/projects/it-certification]]")
L("- [[nodes/projects/second-brain-vault]]")
L("- [[nodes/projects/streaming-rig]]")
L("- [[nodes/topics/ai-tools]]")
L("- [[nodes/topics/crypto-web3]]")
L("- [[nodes/topics/coding]]")
L("- [[nodes/topics/career]]")
L("- [[goals/goals]]")

report_text = "\n".join(lines)
out_path = VAULT / "insights" / "goal-alignment-2026-Q2.md"
out_path.write_text(report_text, encoding="utf-8")
print(f"\nReport written to: {out_path}")
print(f"Size: {len(report_text)} chars, {len(lines)} lines")
