#!/usr/bin/env python3
"""
Task 4 — Goal Alignment Analysis
Maps enriched conversation data against stated goals.
Produces a ruthless but constructive report.
"""
import json, re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

VAULT = Path("/vault")
m = json.loads((VAULT / "_meta" / "enrichment_mapping.json").read_text(encoding="utf-8"))

# ── Date constants ──
LAST_DATE = datetime(2026, 4, 9)
D30 = datetime(2026, 3, 10)
D60 = datetime(2026, 2, 8)
D90 = datetime(2026, 1, 9)

def parse_date(d):
    try:
        return datetime.strptime(d, "%Y-%m-%d")
    except:
        return None

# ── Goal hierarchy definition ──
GOALS = {
    "near_term": {
        "Privatized AI Solutions": {
            "projects": ["private-ai-consulting", "second-brain-vault"],
            "keywords": ["local llm", "custom ai", "ai consulting", "business ai", "rag", "agentic", "pipeline", "client", "sell ai", "ai service", "private ai"],
            "topics": ["ai-tools", "coding"],
        },
        "Deep Tooling Mastery": {
            "projects": ["homelab-stack"],
            "keywords": ["ollama", "llama.cpp", "gguf", "quantized", "mcp", "rag", "agent", "local model", "agent framework", "hermes agent", "claude code", "cursor", "oobabooga"],
            "topics": ["ai-tools", "homelab", "coding"],
        },
        "IT Bridge (Credibility + Income)": {
            "projects": ["it-certification"],
            "keywords": ["resume", "linkedin", "job application", "help desk", "helpdesk", "comptia", "a+", "network+", "tiffin", "certification", "interview", "cover letter"],
            "topics": ["career", "homelab"],
        },
    },
    "medium_term": {
        "Operation Immortal Agent": {
            "projects": ["operation-immortal-agent"],
            "keywords": ["solana", "meteora", "dlmm", "liquidity", "yield", "trading bot", "autonomous fund", "jupiter", "dex", "token", "phantom mcp", "defi", "perp", "farm"],
            "topics": ["crypto-web3", "coding"],
        },
        "Content / Streaming Infrastructure": {
            "projects": ["streaming-rig"],
            "keywords": ["obs", "stream", "twitch", "youtube", "multistream", "overlay", "voicemeeter", "capture card", "content creation", "recording", "broadcast"],
            "topics": ["streaming", "coding"],
        },
        "AI + Security Convergence": {
            "projects": [],
            "keywords": ["security+", "secai", "ai security", "security ai", "cybersecurity", "penetration test", "threat detection", "vulnerability", "siem", "soc", "ethical hacking"],
            "topics": ["ai-tools", "career", "coding"],
        },
    },
    "long_term": {
        "Blockchain Data Analysis at Scale": {
            "projects": [],
            "keywords": ["blockchain analysis", "exchange", "institution", "data science", "on-chain", "onchain", " whale ", "market maker", "quantitative", "quant"],
            "topics": ["crypto-web3", "ai-tools", "coding"],
        },
    },
}

TOP_PROJECTS = [
    "homelab-stack", "operation-immortal-agent", "private-ai-consulting",
    "it-certification", "second-brain-vault", "streaming-rig", "flappy-meme-bird",
]

# ── Helper: match item to goal ──
def score_item_for_goal(item, goal_def):
    score = 0
    title = item["title"].lower()
    body = item.get("body", "").lower()
    combined = title + " " + body
    fm = item["enriched_frontmatter"]
    cat = fm.get("category", "")
    tags = [t.lower() for t in fm.get("tags", [])]
    projs = [p.lower() for p in fm.get("linked_projects", [])]

    # Project match
    for p in goal_def["projects"]:
        if p.lower() in projs:
            score += 20

    # Topic match
    for t in goal_def["topics"]:
        if t.lower() == cat.lower():
            score += 5
        if t.lower() in tags:
            score += 3

    # Keyword match
    for kw in goal_def["keywords"]:
        if kw in combined:
            score += 2
        if kw in title:
            score += 3

    return score

# ── Build analysis ──
project_conversations = defaultdict(list)
for item in m:
    for p in item["enriched_frontmatter"].get("linked_projects", []):
        project_conversations[p].append(item)

goal_conversations = defaultdict(lambda: defaultdict(list))
for item in m:
    for tier_name, tier in GOALS.items():
        for goal_name, goal_def in tier.items():
            score = score_item_for_goal(item, goal_def)
            if score >= 5:
                goal_conversations[tier_name][goal_name].append((item, score))

# ── Progress metrics per project ──
def project_metrics(proj_name, convs):
    if not convs:
        return {}
    dates = [parse_date(c["enriched_frontmatter"].get("date", "")) for c in convs]
    dates = [d for d in dates if d]
    sentiments = Counter(c["enriched_frontmatter"].get("sentiment", "unknown") for c in convs)
    resolutions = Counter(c["enriched_frontmatter"].get("resolution", "unknown") for c in convs)
    sources = Counter(c["source"] for c in convs)
    recent30 = sum(1 for d in dates if d >= D30)
    recent60 = sum(1 for d in dates if d >= D60)
    recent90 = sum(1 for d in dates if d >= D90)
    return {
        "count": len(convs),
        "first": min(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "last": max(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "sentiments": sentiments,
        "resolutions": resolutions,
        "sources": sources,
        "recent30": recent30,
        "recent60": recent60,
        "recent90": recent90,
        "stalled": (LAST_DATE - max(dates)).days > 60 if dates else True,
    }

# ── Goal coverage metrics ──
def goal_metrics(goal_name, scored_convs):
    if not scored_convs:
        return {}
    convs = [c for c, s in scored_convs]
    dates = [parse_date(c["enriched_frontmatter"].get("date", "")) for c in convs]
    dates = [d for d in dates if d]
    sentiments = Counter(c["enriched_frontmatter"].get("sentiment", "unknown") for c in convs)
    resolutions = Counter(c["enriched_frontmatter"].get("resolution", "unknown") for c in convs)
    recent30 = sum(1 for d in dates if d >= D30)
    recent60 = sum(1 for d in dates if d >= D60)
    recent90 = sum(1 for d in dates if d >= D90)
    # Unique conversations (dedupe)
    unique = len(set(c["file"] for c in convs))
    return {
        "count": unique,
        "first": min(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "last": max(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "sentiments": sentiments,
        "resolutions": resolutions,
        "recent30": recent30,
        "recent60": recent60,
        "recent90": recent90,
        "stalled": (LAST_DATE - max(dates)).days > 60 if dates else True,
    }

# ── Generate report ──
report_lines = []

def line(s=""): report_lines.append(s)

def header(title, level=1):
    line(f"{'#' * level} {title}")
    line()

header("Goal Alignment Report", 1)
line(f"> Generated: {LAST_DATE.strftime('%Y-%m-%d')}")
line(f"> Total conversations analyzed: {len(m)}")
line(f"> Date range: 2023-11-05 to 2026-04-09")
line()

# ── Section 1: Goal Hierarchy ──
header("Current Goal Hierarchy", 2)
line("```")
line("Primary → Privatized AI Solutions + Deep Tooling Mastery")
line("        → IT Bridge (Credibility + Income)")
line("Medium  → Operation Immortal Agent")
line("        → Content / Streaming Infrastructure")
line("        → AI + Security Convergence")
line("Long    → Blockchain Data Analysis at Scale")
line("```")
line()

# ── Section 2: Project Progress Signals ──
header("Progress Signals by Project", 2)
line("| Project | Convos | First → Last | 30d | 60d | 90d | Status |")
line("|---------|--------|-------------|-----|-----|-----|--------|")
for proj in TOP_PROJECTS:
    convs = project_conversations.get(proj, [])
    pm = project_metrics(proj, convs)
    if not pm:
        line(f"| {proj.replace('-', ' ').title()} | 0 | N/A | — | — | — | 🔴 No data |")
        continue
    status = "🔴 STALLED" if pm["stalled"] else "🟢 ACTIVE"
    line(f"| {proj.replace('-', ' ').title()} | {pm['count']} | {pm['first']} → {pm['last']} | {pm['recent30']} | {pm['recent60']} | {pm['recent90']} | {status} |")
line()

# Sentiment + resolution detail for top projects
header("Sentiment & Resolution Breakdown", 3)
for proj in TOP_PROJECTS:
    convs = project_conversations.get(proj, [])
    if not convs:
        continue
    pm = project_metrics(proj, convs)
    line(f"**{proj.replace('-', ' ').title()}** ({pm['count']} convos)")
    sent_str = ", ".join([f"{k}={v}" for k, v in pm["sentiments"].most_common()])
    res_str = ", ".join([f"{k}={v}" for k, v in pm["resolutions"].most_common()])
    line(f"- Sentiment: {sent_str}")
    line(f"- Resolution: {res_str}")
    line()

# ── Section 3: Goal Coverage ──
header("Goal Coverage Analysis", 2)
for tier_name, tier in GOALS.items():
    tier_label = tier_name.replace("_", " ").title()
    header(tier_label, 3)
    for goal_name, goal_def in tier.items():
        scored = goal_conversations[tier_name][goal_name]
        gm = goal_metrics(goal_name, scored)
        if not gm:
            line(f"**{goal_name}**: 🔴 Zero signal. Not discussed.")
            line()
            continue
        status = "🔴 STALLED" if gm["stalled"] else "🟢 ACTIVE"
        line(f"**{goal_name}** — {gm['count']} unique conversations, last: {gm['last']} {status}")
        line(f"- 30d/60d/90d activity: {gm['recent30']}/{gm['recent60']}/{gm['recent90']}")
        sent_str = ", ".join([f"{k}={v}" for k, v in gm["sentiments"].most_common(3)])
        res_str = ", ".join([f"{k}={v}" for k, v in gm["resolutions"].most_common(3)])
        line(f"- Sentiment: {sent_str}")
        line(f"- Resolution: {res_str}")
        line()

# ── Section 4: Misalignments & Conflicts ──
header("Misalignments & Conflicts", 2)

# Find biggest goal gaps
line("### ⚠️ Where the Energy Is NOT Going")
line()

# AI + Security
sec_convs = goal_conversations["medium_term"]["AI + Security Convergence"]
if not sec_convs:
    line("🔴 **AI + Security Convergence**: **ZERO conversations.**")
    line("Bryan says this is the right direction. The vault says he hasn't touched it. Not a single mention of SecAI, security+, threat detection, or SIEM in 3,400 conversations.")
    line()

# Private AI Consulting
consult_convs = project_conversations.get("private-ai-consulting", [])
if len(consult_convs) < 20:
    line("🟡 **Privatized AI Solutions**: Only **10 conversations** explicitly about consulting/business.")
    line("Most 'AI' energy goes into *using* tools (Ollama, Cursor, local models) rather than *selling* or *packaging* them. There's a big gap between 'I want to do this for clients' and actually discussing business models, pricing, or client acquisition.")
    line()

# IT Certification
it_convs = project_conversations.get("it-certification", [])
it_gm = project_metrics("it-certification", it_convs)
if it_gm.get("recent90", 0) < 3:
    recent90_it = it_gm.get('recent90', 0)
    line(f"🟡 **IT Bridge**: Only **{recent90_it} conversations in the last 90 days.**")
    line("The IT cert is supposed to be 'credibility and income while the bigger thing develops.' But the conversation volume is minimal. Either the cert is on track and doesn't need discussion, or it's getting deprioritized.")
    line()

# Homelab vs actual building
homelab_convs = project_conversations.get("homelab-stack", [])
if len(homelab_convs) > 300:
    line("🟠 **Homelab Stack**: **{} conversations** — massive volume.".format(len(homelab_convs)))
    line("This is the dominant project by conversation count, but much of it is *setup/debugging* (WSL2 errors, CUDA installs, model loading failures) rather than *building*. The homelab is the lab, yes — but labs exist to run experiments, not just to be maintained.")
    line()

# Operation Immortal Agent
oia_convs = project_conversations.get("operation-immortal-agent", [])
oia_gm = project_metrics("operation-immortal-agent", oia_convs)
if oia_gm.get("recent30", 0) < 2:
    recent30_oia = oia_gm.get('recent30', 0)
    line(f"🟡 **Operation Immortal Agent**: Only **{recent30_oia} conversations in last 30 days.**")
    line("This is described as 'the most serious thing I've built.' The conversation count (24 total) and recent activity suggest it's not getting daily attention. It may be in maintenance mode or blocked.")
    line()

# Streaming
stream_convs = project_conversations.get("streaming-rig", [])
if len(stream_convs) < 20:
    line("🟡 **Content/Streaming**: Only **{} conversations.**".format(len(stream_convs)))
    line("The streaming rig exists in the vault but the content strategy doesn't. No discussions about audience building, content calendar, or streaming schedule.")
    line()

# Long term goal
block_convs = goal_conversations["long_term"]["Blockchain Data Analysis at Scale"]
if not block_convs:
    line("🔴 **Long Term (Blockchain Data Analysis at Scale)**: **Zero signal.**")
    line("No conversations about data science at exchanges, quantitative analysis, or institutional blockchain roles. This remains a vision statement with no supporting exploration.")
    line()

# Source analysis: where does Bryan ask what?
line("### 🔍 Cross-LLM Pattern")
line()
sources_by_project = defaultdict(Counter)
for proj in TOP_PROJECTS:
    for c in project_conversations.get(proj, []):
        sources_by_project[proj][c["source"]] += 1
for proj in ["operation-immortal-agent", "private-ai-consulting", "it-certification"]:
    sc = sources_by_project[proj]
    if sc:
        line(f"- **{proj.replace('-', ' ').title()}**: {dict(sc)}")
line()

# ── Section 5: Recommended Actions ──
header("Recommended Next Actions / Quarterly Focus", 2)
line()
line("### Q2 2026 Priority Matrix")
line()
line("| Priority | Action | Rationale |")
line("|----------|--------|-----------|")
line("| **P0** | **Ship something for Operation Immortal Agent** | 24 conversations is enough research. Time to make it trade live or document why not. |")
line("| **P0** | **Start SecAI / Security+ conversations** | Zero signal = zero progress. Add 1 conversation per week minimum. |")
line("| **P1** | **Turn homelab energy into client-facing demos** | 344 convos of tooling depth → package ONE working demo (helpdesk bot, local RAG, etc.) |")
line("| **P1** | **Schedule IT cert exam or deprioritize** | Either commit to a test date or admit it's not the bridge and adjust the narrative. |")
line("| **P2** | **Write content plan for streaming** | 16 convos on setup. 0 on content. Decide: is this marketing or hobby? |")
line("| **P2** | **Explore exchange data APIs** | Long-term goal needs at least *some* signal. Try one exchange API (Binance, Coinbase). |")
line()

line("### Immediate Conversation Prompts (Ask Next)")
line()
line("1. **For Immortal Agent**: 'What's the single blocker preventing this from running live? Is it technical, capital, or fear?'")
line("2. **For Security+AI**: 'What specific security certification or course should I start this week, and what's the first module?'")
line("3. **For AI Consulting**: 'What would a $500 local-AI package look like? Who would buy it and how would I deliver it?'")
line("4. **For Career Bridge**: 'If I don't get the IT cert, what's the alternative credibility path?'")
line("5. **For Homelab**: 'Which of these 344 conversations produced a reusable asset? List the top 5.'")
line()

# ── Section 6: Entity Links ──
header("Relevant Entity Pages", 2)
line("- [[nodes/projects/operation-immortal-agent]]")
line("- [[nodes/projects/private-ai-consulting]]")
line("- [[nodes/projects/homelab-stack]]")
line("- [[nodes/projects/it-certification]]")
line("- [[nodes/projects/second-brain-vault]]")
line("- [[nodes/projects/streaming-rig]]")
line("- [[nodes/topics/ai-tools]]")
line("- [[nodes/topics/crypto-web3]]")
line("- [[nodes/topics/coding]]")
line("- [[nodes/topics/career]]")
line("- [[goals/goals]]")
line()

# ── Write report ──
report_text = "\n".join(report_lines)
out_path = VAULT / "insights" / "goal-alignment-2026-Q2.md"
out_path.write_text(report_text, encoding="utf-8")
print(f"Report written to: {out_path}")
print(f"Size: {len(report_text)} chars, {len(report_lines)} lines")
