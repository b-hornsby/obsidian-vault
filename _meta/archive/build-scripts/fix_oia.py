#!/usr/bin/env python3
"""
Focused fix: Tighten OIA detection and regenerate report.
Preserves all other enrichment fields.
"""
import json, re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

VAULT = Path("/vault")
META = VAULT / "_meta"
INSIGHTS = VAULT / "insights"

m = json.loads((META / "enrichment_mapping.json").read_text())

def strict_oia_detect(title, body):
    """Very strict OIA detection. Only direct trading bot / autonomous fund work."""
    t = title.lower()
    b = body.lower()
    combined = t + "\n" + b
    
    # EXCLUSIONS: If title contains these, it's NOT OIA unless very strong signal
    exclusion_title = ["linkedin", "profile", "resume", "cover letter", "job application", 
                       "obsidian", "skill", "pivot", "not for my immortal", "isn't for my immortal"]
    if any(exc in t for exc in exclusion_title):
        return False
    
    # REQUIRED: Must have at least one CORE OIA phrase
    core_phrases = [
        "operation immortal agent",
        "operation-immortal-agent", 
        "immortal-agent",
        "meteora dlmm",
        "meteora-ag/dlmm",
        "autonomous fund",
        "autonomous trading",
        "solana trading bot",
        "trading bot solana",
        "dex bot solana",
        "defi bot solana",
        "phantom mcp",
        "phantom mcp server",
        "~/vc projects/immortal agent",
        "immortal agent main",
        "immortal agent latest_branch",
        "immortal agent temporary_baseline",
        "liquidity position solana",
        "yield farming solana",
        "jupiter perp",
        "concentrated liquidity solana",
    ]
    
    core_score = sum(10 if phrase in t else (3 if phrase in b else 0) 
                     for phrase in core_phrases)
    
    # Title must contain a strong signal OR body must have multiple signals
    has_title_signal = any(phrase in t for phrase in core_phrases)
    has_body_signals = sum(1 for phrase in core_phrases if phrase in b) >= 2
    
    if has_title_signal:
        return True
    if core_score >= 6:
        return True
    
    return False

# Fix OIA for all items
fixed_count = 0
for item in m:
    fm = item["enriched_frontmatter"]
    projects = fm.get("linked_projects", [])
    
    # Remove OIA if it fails strict check
    if "operation-immortal-agent" in projects:
        if not strict_oia_detect(item["title"], item.get("body_preview", "")):
            projects.remove("operation-immortal-agent")
            fixed_count += 1

print(f"Removed OIA from {fixed_count} conversations")

# Save updated mapping
(META / "enrichment_mapping.json").write_text(
    json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8"
)

# Verify new counts
proj_counts = Counter()
for item in m:
    for p in item["enriched_frontmatter"].get("linked_projects", []):
        proj_counts[p] += 1

print("\nCorrected project distribution:")
for p, c in proj_counts.most_common():
    print(f"  {p}: {c}")

# Show remaining OIA titles
oia_items = [item for item in m if "operation-immortal-agent" in item["enriched_frontmatter"].get("linked_projects", [])]
print(f"\n=== Remaining OIA conversations ({len(oia_items)}) ===")
for item in oia_items:
    print(f"  - {item['title']}")

# Check for any remaining false positives
suspicious = [item for item in oia_items if any(word in item["title"].lower() for word in ["linkedin", "profile", "resume", "wallet setup", "obsidian", "skill"])]
print(f"\nRemaining suspicious: {len(suspicious)}")

# Regenerate Goal Alignment Report
print("\n=== Regenerating Goal Alignment Report ===")

LAST_DATE = datetime(2026, 4, 9)
D30 = datetime(2026, 3, 10)
D60 = datetime(2026, 2, 8)
D90 = datetime(2026, 1, 9)

def parse_date(d):
    try:
        return datetime.strptime(d, "%Y-%m-%d")
    except:
        return None

GOALS = {
    "near_term": {
        "Privatized AI Solutions": {
            "projects": ["private-ai-consulting"],
            "keywords": ["private ai", "ai consulting", "ai business", "client ai", "sell ai", "ai service", "business ai", "freelance ai", "custom ai solution", "ai product", "ai for business", "ai agency"],
        },
        "Deep Tooling Mastery": {
            "projects": ["homelab-stack", "second-brain-vault"],
            "keywords": ["ollama", "llama.cpp", "gguf", "quantized", "mcp server", "rag system", "agent framework", "claude code", "cursor ide", "local llm setup", "model quantization", "self-hosted ai", "local model deployment"],
        },
        "IT Bridge (Credibility + Income)": {
            "projects": ["it-certification"],
            "keywords": ["comptia a+", "comptia network+", "comptia security+", "security+", "help desk job", "helpdesk job", "tiffin university", "tiffin cert", "secai cert", "certification exam", "entry level it", "interview prep", "it support role"],
        },
    },
    "medium_term": {
        "Operation Immortal Agent": {
            "projects": ["operation-immortal-agent"],
            "keywords": ["meteora", "dlmm", "solana bot", "autonomous fund", "phantom mcp", "jupiter perp", "liquidity position", "yield farming", "trading bot solana", "defi bot", "dex bot"],
        },
        "Content / Streaming Infrastructure": {
            "projects": ["streaming-rig"],
            "keywords": ["obs studio", "obs setup", "twitch stream", "youtube stream", "multistream", "stream overlay", "voicemeeter", "capture card", "elgato", "stream deck", "recording setup", "broadcast setup"],
        },
        "AI + Security Convergence": {
            "projects": [],
            "keywords": ["security+", "secai", "ai security", "security ai", "cybersecurity", "penetration testing", "threat detection", "vulnerability scan", "siem", "soc analyst", "ethical hacking", "security certification"],
        },
    },
    "long_term": {
        "Blockchain Data Analysis at Scale": {
            "projects": [],
            "keywords": ["blockchain data analysis", "exchange data", "on-chain analysis", "onchain data", "quantitative crypto", "crypto quant", "market maker data", "institutional blockchain", "binance api", "coinbase api"],
        },
    },
}

def score_item_strict(item, goal_def):
    score = 0
    title = item["title"].lower()
    body = item.get("body_preview", "").lower()
    combined = title + "\n" + body
    fm = item["enriched_frontmatter"]
    
    for p in goal_def["projects"]:
        if p.lower() in [x.lower() for x in fm.get("linked_projects", [])]:
            score += 20
    
    for kw in goal_def["keywords"]:
        if kw in combined:
            score += 3
    
    return score

project_conversations = defaultdict(list)
for item in m:
    for p in item["enriched_frontmatter"].get("linked_projects", []):
        project_conversations[p].append(item)

goal_conversations = defaultdict(lambda: defaultdict(list))
for item in m:
    for tier_name, tier in GOALS.items():
        for goal_name, goal_def in tier.items():
            score = score_item_strict(item, goal_def)
            if score >= 8:
                goal_conversations[tier_name][goal_name].append(item)

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
        "count": len(convs), "first": min(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "last": max(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "sentiments": sentiments, "resolutions": resolutions,
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
        "count": unique, "first": min(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "last": max(dates).strftime("%Y-%m-%d") if dates else "N/A",
        "sentiments": sentiments, "resolutions": resolutions,
        "recent30": recent[0], "recent60": recent[1], "recent90": recent[2],
        "stalled": (LAST_DATE - max(dates)).days > 60 if dates else True,
    }

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
L("Primary -> Privatized AI Solutions + Deep Tooling Mastery")
L("        -> IT Bridge (Credibility + Income)")
L("Medium  -> Operation Immortal Agent")
L("        -> Content / Streaming Infrastructure")
L("        -> AI + Security Convergence")
L("Long    -> Blockchain Data Analysis at Scale")
L("```")
L()

L("## Progress Signals by Project")
L("| Project | Convos | First -> Last | 30d | 60d | 90d | Status |")
L("|---------|--------|-------------|-----|-----|-----|--------|")
TOP_PROJECTS = ["homelab-stack", "operation-immortal-agent", "private-ai-consulting",
                "it-certification", "second-brain-vault", "streaming-rig", "flappy-meme-bird"]
for proj in TOP_PROJECTS:
    p = pm(proj)
    if not p:
        L(f"| {proj.replace('-', ' ').title()} | 0 | N/A | - | - | - | No data |")
        continue
    status = "STALLED" if p["stalled"] else "ACTIVE"
    L(f"| {proj.replace('-', ' ').title()} | {p['count']} | {p['first']} -> {p['last']} | {p['recent30']} | {p['recent60']} | {p['recent90']} | {status} |")
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
            L(f"**{goal_name}**: Zero signal. Not discussed.")
            L()
            continue
        status = "STALLED" if g["stalled"] else "ACTIVE"
        L(f"**{goal_name}** - {g['count']} unique conversations, last: {g['last']} {status}")
        L(f"- 30d/60d/90d activity: {g['recent30']}/{g['recent60']}/{g['recent90']}")
        L(f"- Sentiment: {', '.join([f'{k}={v}' for k,v in g['sentiments'].most_common(3)])}")
        L(f"- Resolution: {', '.join([f'{k}={v}' for k,v in g['resolutions'].most_common(3)])}")
        L()

L("## Misalignments & Conflicts")
L()
L("### Where the Energy Is NOT Going")
L()

it_p = pm("it-certification")
if it_p and it_p["recent90"] < 3:
    L(f"**IT Bridge**: Only **{it_p['recent90']} conversations in the last 90 days.**")
    L("The IT cert is supposed to be 'credibility and income while the bigger thing develops.' But the volume is minimal. Either it's on track and doesn't need discussion, or it's getting deprioritized.")
    L()

homelab_p = pm("homelab-stack")
if homelab_p and homelab_p["count"] > 200:
    L(f"**Homelab Stack**: **{homelab_p['count']} conversations** - massive volume.")
    L("This is the dominant project by count, but much of it is *setup/debugging* (WSL2 errors, CUDA installs, model loading) rather than *building*. The lab exists to run experiments, not just to be maintained.")
    L()

consult_convs = project_conversations.get("private-ai-consulting", [])
if len(consult_convs) < 50:
    L(f"**Privatized AI Solutions**: Only **{len(consult_convs)} conversations** explicitly about consulting/business.")
    L("Most 'AI' energy goes into *using* tools rather than *selling* or *packaging* them. Big gap between wanting to do this for clients and actually discussing business models, pricing, or client acquisition.")
    L()

oia_p = pm("operation-immortal-agent")
if oia_p and oia_p["recent30"] < 5:
    L(f"**Operation Immortal Agent**: Only **{oia_p['recent30']} conversations in last 30 days.**")
    L("Described as 'the most serious thing I've built.' The conversation count and recent activity suggest it's not getting daily attention. Needs a go/no-go decision.")
    L()

stream_p = pm("streaming-rig")
if stream_p and stream_p["count"] < 20:
    L(f"**Content/Streaming**: Only **{stream_p['count']} conversations.**")
    L("The rig exists but the content strategy doesn't. No discussions about audience building, content calendar, or streaming schedule.")
    L()

sec_convs = goal_conversations["medium_term"]["AI + Security Convergence"]
if not sec_convs:
    L("**AI + Security Convergence**: **ZERO conversations.**")
    L("Bryan says this is the right direction. The vault says he hasn't touched it. Not a single mention of SecAI, threat detection, or SIEM in 3,400 conversations.")
    L()

block_convs = goal_conversations["long_term"]["Blockchain Data Analysis at Scale"]
if not block_convs:
    L("**Long Term (Blockchain Data Analysis at Scale)**: **Zero signal.**")
    L("No conversations about exchange data APIs, quantitative analysis, or institutional blockchain roles. This remains a vision statement with no supporting exploration.")
    L()

L("### Cross-LLM Pattern")
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
homelab_count = homelab_p["count"] if homelab_p else 0
L(f"| **P0** | **Ship Operation Immortal Agent or kill it** | {oia_p['count'] if oia_p else 0} conversations is enough research. Make it trade live, or document why not and free the mental space. |")
L(f"| **P0** | **Start SecAI / Security+ conversations NOW** | Zero signal = zero progress. Add 1 conversation per week minimum or drop the goal. |")
L(f"| **P1** | **Turn homelab energy into ONE client-facing demo** | {homelab_count} convos of tooling depth -> package a working demo (helpdesk bot, local RAG pipeline). Something you can show, not just talk about. |")
L(f"| **P1** | **Schedule IT cert exam or explicitly deprioritize** | Either commit to a test date or rewrite goals.md to remove IT as a bridge. Ambiguity is expensive. |")
L(f"| **P2** | **Write content plan for streaming** | {stream_p['count'] if stream_p else 0} convos on setup. 0 on content. Decide: is this marketing or hobby? If marketing, what's the first 10 videos about? |")
L(f"| **P2** | **Explore ONE exchange data API** | Long-term goal needs at least *some* signal. Try Binance or Coinbase API for 1 hour. Document what you learn. |")
L()

L("### Immediate Conversation Prompts (Ask Next)")
L()
L("1. **Immortal Agent**: 'What is the single blocker preventing this from trading live? Technical, capital, or fear?'")
L("2. **Security+AI**: 'What specific cert or course starts this week? What's module 1?'")
L("3. **AI Consulting**: 'What would a $500 local-AI package look like? Who buys it? How do I deliver it?'")
L("4. **Career Bridge**: 'If I don't get the IT cert, what's the alternative credibility path? Portfolio? Github?'")
L(f"5. **Homelab**: 'Which of these {homelab_count} conversations produced a reusable asset? Name the top 5.'")
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
out_path = INSIGHTS / "goal-alignment-2026-Q2.md"
out_path.write_text(report_text, encoding="utf-8")
print(f"\nReport written to: {out_path}")
print(f"   Size: {len(report_text)} chars, {len(lines)} lines")
print("\n=== DONE ===")
