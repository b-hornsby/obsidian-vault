#!/usr/bin/env python3
"""
Complete rebuild with original enrichment + strict project detection.
1. Re-parse all 3,400 files
2. Re-run ORIGINAL classification (tags, category, sentiment, resolution)
3. Run STRICT phrase-aware project detection (tightened OIA)
4. Merge and save enrichment_mapping.json
5. Regenerate Goal Alignment Report
"""
import json, re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

VAULT = Path("/vault")
PROCESSED = VAULT / "processed"
META = VAULT / "_meta"
INSIGHTS = VAULT / "insights"
SOURCES = ["CLAUDE", "GEMINI", "GPT", "GROK"]

# ── Original enrichment constants from enrich_and_build.py ──
CATEGORIES = ["ai-tools", "crypto-web3", "coding", "career", "homelab", "streaming", "general"]
SENTIMENTS = ["curious", "frustrated", "exploratory", "building", "stuck", "executing"]
RESOLUTIONS = ["resolved", "unresolved", "partial", "abandoned"]

TOPIC_KEYWORDS = {
    "ai-tools": ["llm", "ai", "agent", "claude", "gpt", "gemini", "grok", "model", "ollama", "oobabooga", "cursor", "copilot", "rag", "mcp", "openai", "anthropic", "llama.cpp", "gguf", "quantized", "inference", "embedding", "fine-tune", "lora", "hermes", "text-generation", "local llm", "local model", "ai assistant", "helpdesk ai"],
    "crypto-web3": ["solana", "bitcoin", "ethereum", "crypto", "defi", "meteora", "dlmm", "jupiter", "dex", "token", "wallet", "phantom", "blockchain", "web3", "nft", "trading", "perp", "perpetual", "yield", "liquidity", "amm", "swap", "usdc", "icp", "internet computer", "memecoin", "pump.fun", "axiom", "leverage", "margin", "farm", "staking"],
    "coding": ["python", "javascript", "typescript", "rust", "go", "bash", "shell", "code", "script", "debug", "error", "syntax", "import", "module", "package", "pip", "npm", "git", "github", "vs code", "cursor", "ide", "function", "class", "api", "json", "csv", "database", "sql", "html", "css", "react", "node", "docker", "dockerfile", "compose", "kubernetes", "fastapi", "flask", "django"],
    "career": ["resume", "job", "interview", "certification", "cert", "comptia", "a+", "network+", "it job", "help desk", "helpdesk", "linkedin", "cover letter", "hire", "salary", "career", "entry level", "junior", "tiffin", "secai", "security+", "learning", "course", "study", "exam", "prep"],
    "homelab": ["homelab", "server", "linux", "cachyos", "arch", "ubuntu", "debian", "wsl", "wsl2", "windows", "hardware", "nvidia", "gpu", "cpu", "ram", "ssd", "hdd", "storage", "nas", "raid", "network", "router", "firewall", "vm", "virtual machine", "proxmox", "docker", "portainer", "nginx", "proxy", "ssh", "systemd", "pacman", "paru", "aur", "limine", "sbctl", "secure boot", "uefi", "bios", "dual boot", "dualboot", "distro"],
    "streaming": ["stream", "obs", "twitch", "youtube", "content", "video", "audio", "microphone", "mic", "voicemeeter", "overlay", "scene", "encoder", "nvenc", "recording", "broadcast", "multistream", "chatbot", "alert", "studio", "camera", "webcam", "elgato", "capture card"],
    "general": [],
}

SENTIMENT_KEYWORDS = {
    "curious": ["how", "what is", "why", "explain", "understand", "learn", "curious", "wonder", "tell me about"],
    "frustrated": ["stuck", "error", "broken", "not working", "failed", "fail", "problem", "issue", "bug", "annoying", "hell", "damn", "wtf", "ugh", "can't get", "won't work", "doesn't work"],
    "exploratory": ["try", "test", "experiment", "explore", "option", "alternatives", "compare", "versus", "vs", "maybe", "consider", "brainstorm", "idea", "possibility"],
    "building": ["build", "create", "setup", "set up", "install", "deploy", "develop", "project", "implement", "configure", "make a", "making", "working on"],
    "stuck": ["stuck", "blocked", "can't", "unable", "confused", "lost", "don't know", "unsure", "help", "how do i", "troubleshoot"],
    "executing": ["run", "execute", "launch", "start", "automate", "script", "cron", "schedule", "pipeline", "workflow", "do this", "go ahead", "proceed"],
}

RESOLUTION_KEYWORDS = {
    "resolved": ["worked", "success", "fixed", "solved", "done", "complete", "thanks", "appreciate", "perfect", "great", "awesome", "working now"],
    "unresolved": ["still", "not working", "doesn't work", "won't", "failed", "error persists", "same issue", "problem remains"],
    "partial": ["partial", "kind of", "sort of", "almost", "mostly", "workaround", "temporary", "semi", "mostly works", "some issues"],
    "abandoned": ["never mind", "forget", "give up", "abandon", "stop", "quit", "not worth", "too hard", "later", "maybe later", "moved on"],
}

PROJECT_NAMES = [
    "flappy-meme-bird", "homelab-stack", "it-certification",
    "operation-immortal-agent", "private-ai-consulting",
    "second-brain-vault", "streaming-rig"
]

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


def classify_original(body, title):
    """Original classification logic from enrich_and_build.py"""
    combined = (title + " " + body).lower()
    title_lower = title.lower()
    
    # Category
    cat_scores = {}
    for cat, kws in TOPIC_KEYWORDS.items():
        if cat == "general":
            continue
        score = sum(3 for kw in kws if kw in title_lower) + sum(1 for kw in kws if kw in body.lower())
        cat_scores[cat] = score
    best_cat = max(cat_scores, key=cat_scores.get) if cat_scores and max(cat_scores.values()) > 0 else "general"
    
    # Tags
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
    if len(body.split()) < 80:
        resolution = "partial"
    
    # Original project detection (keyword-based)
    linked_projects = []
    for p in PROJECT_NAMES:
        kws = p.replace("-", " ").split()
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


def strict_project_detection(title, body, category):
    """Strict phrase-aware project detection. OVERRIDES original project links."""
    title_lower = title.lower()
    body_lower = body.lower()
    combined = title_lower + "\n" + body_lower
    found = {}
    
    # ── HOMELAB-STACK ──
    hw_phrases = [
        "rtx 4090", "rtx4090", "rtx-4090", "geforce rtx", "nvidia 40",
        "cachyos", "cachy os", "limine", "sbctl", "secure boot",
        "7700x", "ryzen 7", "ryzen 9", "zen 4", "am5",
        "pfsense", "opnsense", "firewall", "network card", "nic card",
        "unraid", "truenas", "proxmox", "esxi", "hypervisor", "vm host",
        "home server", "server rack", "nas server", "storage server",
        "gpu passthrough", "pci passthrough", "vfio", "iommu", "kvm",
        "nvidia-smi", "nvidia driver",
        "steam deck", "steam os", "handheld", "legion go", "ally", "rog ally",
        "dual boot", "dualboot", "grub", "systemd-boot", "refind",
        " ddr5 ", " ddr4 ", " ram upgrade", "nvme", "m.2", "pcie",
        "power supply", "psu", "cpu cooler", "liquid cooling", "aio",
        "bios", "uefi", "overclock", "undervolt",
        "raspberry pi", "rpi", "orange pi", "sbc", "single board",
        "pihole", "adguard", "dns server", "reverse proxy",
        "docker", "kubernetes", "k3s", "self-hosted", "self hosted",
        "home lab", "lab setup", "test bench", "dev machine",
        "hardware acceleration", "vaapi", "nvenc",
        "fan curve", "thermal paste", "temperature", "monitoring",
        "cable management", "pc build", "desktop build",
        "wsl2", "wsl install", "wsl setup",
        "cuda install", "cuda driver", "cuda toolkit",
        "nvidia gpu", "amd gpu", "intel arc",
        "distro hop", "distro hopping", "linux install", "arch install",
        "pacman", "paru", "yay", "aur", "sbctl", "limine",
    ]
    hw_score = sum(5 if phrase in title_lower else (2 if phrase in body_lower else 0) 
                   for phrase in hw_phrases)
    if category == "homelab" and hw_score > 0:
        hw_score += 5
    if hw_score >= 4:
        found["homelab-stack"] = hw_score
    
    # ── OPERATION IMMORTAL AGENT (TIGHTENED) ──
    # ONLY match explicit trading bot / autonomous fund language
    # EXCLUDE: general phantom wallet, solana talk, crypto curiosity
    oia_phrases = [
        "meteora", "dlmm", "liquidity pool", "liquidity position",
        "autonomous fund", "autonomous trading", "auto trade",
        "jupiter perp", "jupiter exchange", "jupiter aggregator", "jupiter swap",
        "phantom mcp", "phantom mcp server",
        "yield farming", "yield farm", "lp position",
        "raydium", "orca solana", "whirlpool", "concentrated liquidity",
        "pyth network", "switchboard",
        "copy trade", "copy trading", "copytrade",
        "arbitrage solana", "mev bot",
        "backtest trading", "backtest solana", "strategy backtest",
        "paper trading", "mainnet beta", "devnet",
        "immortal agent", "operation immortal",
        "solana trading bot", "solana bot", "trading bot solana", 
        "dex bot solana", "defi bot", "solana defi bot",
        "liquidity mining", "yield optimization", "pool strategy",
    ]
    oia_score = sum(5 if phrase in title_lower else (2 if phrase in body_lower else 0) 
                     for phrase in oia_phrases)
    
    # Strong contextual boost ONLY with explicit trading language
    if "trading" in title_lower and ("bot" in title_lower or "agent" in title_lower or "fund" in title_lower):
        oia_score += 10
    if "autonomous" in title_lower and ("fund" in title_lower or "trade" in title_lower or "agent" in title_lower):
        oia_score += 15
    if "immortal" in title_lower:
        oia_score += 20
    if "meteora" in title_lower or "dlmm" in title_lower:
        oia_score += 15
    
    # EXCLUSIONS: If it's just general wallet talk, crypto curiosity, or price discussion
    wallet_only = ("phantom wallet" in combined or "phantom" in combined) and oia_score < 10
    if wallet_only:
        oia_score = 0  # Exclude general phantom wallet discussions
    
    # Must have strong signal to qualify
    if oia_score >= 8:
        found["operation-immortal-agent"] = oia_score
    
    # ── PRIVATE-AI-CONSULTING ──
    consult_phrases = [
        "ai consulting", "ai consultant", "consulting business", "tech consulting",
        "private ai", "private ai service", "custom ai solution", "custom ai pipeline",
        "ai for business", "ai for client", "ai for customer",
        "ai service", "ai offering", "ai package", "ai deliverable",
        "freelance ai", "ai freelancer", "contract ai", "ai contractor",
        "business name", "company name", "llc", "inc.", "d/b/a", "dba",
        "pricing", "hourly rate", "project rate", "retainer", "invoice",
        "upwork", "fiverr", "toptal",
        "client acquisition", "finding clients", "getting clients",
        "lead generation", "sales funnel", "cold outreach", "cold email",
        "value proposition", "unique selling", "usp", "competitive advantage",
        "pc repair", "computer repair", "custom build shop", "pc build service",
        "tech support business", "tech service business", "it support business",
        "managed service", "msp", "managed it", "break/fix",
        "white label", "resell ai", "ai agency", "ai automation agency",
        "local llm service", "local ai service", "on-premise ai", "on premise ai",
        "rag pipeline", "rag system", "knowledge base", "document processing",
        "ai assistant", "ai agent", "virtual assistant", "ai chatbot",
        "small business ai", "smb ai", "local business ai",
        "building a business", "start a business", "business model",
        "side hustle", "side income", "extra income",
        "marketing ai", "ai marketing", "content service",
    ]
    consult_score = sum(5 if phrase in title_lower else (2 if phrase in body_lower else 0) 
                        for phrase in consult_phrases)
    
    # Contextual boosts
    if "consulting" in title_lower:
        consult_score += 15
    if ("ai" in title_lower or "tech" in title_lower) and ("business" in title_lower or "client" in title_lower):
        consult_score += 10
    if "ai service" in title_lower or "ai business" in title_lower:
        consult_score += 10
    if "private ai" in title_lower:
        consult_score += 15
    if "side hustle" in title_lower or "side income" in title_lower:
        consult_score += 8
    if "upwork" in body_lower or "fiverr" in body_lower or "freelance" in body_lower:
        consult_score += 5
        
    if consult_score >= 6:
        found["private-ai-consulting"] = consult_score
    
    # ── IT-CERTIFICATION ──
    cert_phrases = [
        "comptia a+", "comptia network+", "comptia security+",
        "security+", "network+", "it cert", "it certification",
        "tiffin university", "tiffin cert", "tiffin program",
        "help desk", "helpdesk", "desktop support", "it support", "technical support",
        "entry level it", "entry-level it", "junior it", "it intern", "it apprenticeship",
        "interview prep", "interview practice", "interview question",
        "certification exam", "exam prep", "study plan", "test date",
        "secai", "security ai", "ai security cert", "cybersecurity cert",
        "comptia", "cisco cert", "cisco ccna", "ccna", "azure cert", "aws cert",
        "it job", "it career", "tech career", "career change", "career transition",
    ]
    cert_score = sum(5 if phrase in title_lower else (2 if phrase in body_lower else 0) 
                      for phrase in cert_phrases)
    if "linkedin" in title_lower and ("job" in title_lower or "profile" in title_lower or "career" in title_lower):
        cert_score += 8
    if "resume" in title_lower and ("it" in title_lower or "tech" in title_lower):
        cert_score += 8
    if cert_score >= 6:
        found["it-certification"] = cert_score
    
    # ── STREAMING-RIG ──
    stream_phrases = [
        "obs studio", "obs setup", "obs configuration", "obs scene",
        "twitch stream", "twitch setup", "twitch affiliate", "twitch partner",
        "youtube live", "youtube stream", "live stream", "streaming platform",
        "multistream", "multi stream", "simulcast", "restream",
        "capture card", "elgato", "stream deck", "go xlr", "audio mixer",
        "voicemeeter", "virtual cable", "nvidia broadcast",
        "stream overlay", "overlay design", "alert box", "follow alert",
        "green screen", "chroma key", "virtual background", "vtuber",
        "recording setup", "recording studio", "broadcast setup", "broadcasting",
        "camera setup", "dslr", "mirrorless", "camlink",
        "lighting setup", "key light", "softbox", "ring light",
        "microphone", "mic setup", "audio interface", "xlr mic", "usb mic",
        "content creation", "content strategy", "content calendar",
        "video editing", "post production", "thumbnail design",
        "streaming rig", "stream pc", "encoding pc", "capture pc",
    ]
    stream_score = sum(5 if phrase in title_lower else (2 if phrase in body_lower else 0) 
                       for phrase in stream_phrases)
    if stream_score >= 6:
        found["streaming-rig"] = stream_score
    
    # ── SECOND-BRAIN-VAULT ──
    brain_phrases = [
        "second brain", "knowledge base", "zettelkasten", "note system",
        "obsidian", "obsidian vault", "obsidian plugin", "obsidian setup",
        "dataview", "templater", "quickadd", "canvas", "obsidian graph",
        "notion alternative", "notion vs", "roam research", "logseq",
        "pkm", "personal knowledge management", "knowledge management",
        "information capture", "capture system", "read later",
        "tag system", "folder structure", "vault organization",
        "linking notes", "note link", "backlink", "bidirectional link",
    ]
    brain_score = sum(5 if phrase in title_lower else (2 if phrase in body_lower else 0) 
                      for phrase in brain_phrases)
    if brain_score >= 6:
        found["second-brain-vault"] = brain_score
    
    # ── FLAPPY-MEME-BIRD ──
    if "flappy" in title_lower or "flappy" in body_lower:
        found["flappy-meme-bird"] = 20
    if "meme bird" in title_lower or "meme bird" in body_lower:
        found["flappy-meme-bird"] = found.get("flappy-meme-bird", 0) + 20
    
    # Thresholds
    threshold = {"homelab-stack": 4, "operation-immortal-agent": 8, 
                 "private-ai-consulting": 6, "it-certification": 6,
                 "streaming-rig": 6, "second-brain-vault": 6, 
                 "flappy-meme-bird": 10}
    
    result = []
    for proj, score in found.items():
        if score >= threshold.get(proj, 6):
            result.append(proj)
    
    return sorted(set(result))


# ── Phase 1: Parse ALL files ──
print("=== PHASE 1: Parsing all 3,400 files ===")
all_items = []
for source in SOURCES:
    folder = PROCESSED / source
    files = sorted(folder.glob("*.md"))
    for f in files:
        fm, body = extract_frontmatter(f)
        title_match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else f.stem
        
        # Original classification
        orig = classify_original(body, title)
        
        # Strict project detection (overrides linked_projects)
        strict_projects = strict_project_detection(title, body, orig["category"])
        
        all_items.append({
            "source": source,
            "filepath": str(f.relative_to(VAULT)).replace("\\", "/"),
            "title": title,
            "body": body,
            "date": fm.get("date", ""),
            "original_id": str(fm.get("id", "")),
            "tags": orig["tags"],
            "category": orig["category"],
            "sentiment": orig["sentiment"],
            "resolution": orig["resolution"],
            "linked_projects": strict_projects,
            "linked_nodes": orig["linked_nodes"],
        })
    print(f"  {source}: parsed {len(files)}")

print(f"Total: {len(all_items)} items")

# ── Phase 2: Build and save enrichment mapping ──
print("\n=== PHASE 2: Saving enrichment mapping ===")
mapping = []
for item in all_items:
    mapping.append({
        "source": item["source"],
        "file": item["filepath"],
        "title": item["title"],
        "body_preview": item["body"][:500],
        "enriched_frontmatter": {
            "id": item["original_id"],
            "source": item["source"],
            "date": item["date"],
            "tags": item["tags"],
            "category": item["category"],
            "sentiment": item["sentiment"],
            "resolution": item["resolution"],
            "linked_projects": item["linked_projects"],
            "linked_nodes": item["linked_nodes"],
        }
    })

(META / "enrichment_mapping.json").write_text(
    json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("Saved enrichment_mapping.json")

# Verify
proj_counts = Counter()
for item in mapping:
    for p in item["enriched_frontmatter"]["linked_projects"]:
        proj_counts[p] += 1

print("\nProject distribution (corrected):")
for p, c in proj_counts.most_common():
    print(f"  {p}: {c}")

# Spot-check OIA
oia_items = [item for item in all_items if "operation-immortal-agent" in item["linked_projects"]]
print(f"\nOIA spot-check (sample titles):")
for item in oia_items[:15]:
    print(f"  - {item['title']}")

# ── Phase 3: Regenerate Goal Alignment Report ──
print("\n=== PHASE 3: Regenerating Goal Alignment Report ===")

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
    body = item["body"].lower()
    combined = title + "\n" + body
    
    for p in goal_def["projects"]:
        if p.lower() in [x.lower() for x in item["linked_projects"]]:
            score += 20
    
    for kw in goal_def["keywords"]:
        if kw in combined:
            score += 3
    
    return score

project_conversations = defaultdict(list)
for item in all_items:
    for p in item["linked_projects"]:
        project_conversations[p].append(item)

goal_conversations = defaultdict(lambda: defaultdict(list))
for item in all_items:
    for tier_name, tier in GOALS.items():
        for goal_name, goal_def in tier.items():
            score = score_item_strict(item, goal_def)
            if score >= 8:
                goal_conversations[tier_name][goal_name].append(item)

def pm(proj):
    convs = project_conversations.get(proj, [])
    if not convs:
        return None
    dates = [parse_date(c["date"]) for c in convs]
    dates = [d for d in dates if d]
    sentiments = Counter(c["sentiment"] for c in convs)
    resolutions = Counter(c["resolution"] for c in convs)
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
    dates = [parse_date(c["date"]) for c in convs]
    dates = [d for d in dates if d]
    unique = len(set(c["filepath"] for c in convs))
    sentiments = Counter(c["sentiment"] for c in convs)
    resolutions = Counter(c["resolution"] for c in convs)
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
L(f"> Total conversations analyzed: {len(all_items)}")
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
