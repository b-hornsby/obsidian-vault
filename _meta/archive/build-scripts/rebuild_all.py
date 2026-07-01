#!/usr/bin/env python3
"""
Comprehensive vault rebuild — Phase 1: Parse all 3,400 files with body content
Phase 2: Strict phrase-aware project and goal detection
Phase 3: Regenerate enrichment_mapping.json and Goal Alignment Report
"""
import json, re, yaml
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

VAULT = Path("/vault")
PROCESSED = VAULT / "processed"
META = VAULT / "_meta"
SOURCES = ["CLAUDE", "GEMINI", "GPT", "GROK"]

def parse_file(filepath):
    """Extract frontmatter, title, body from a processed conversation file."""
    text = filepath.read_text(encoding="utf-8")
    
    # Extract YAML frontmatter
    fm = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                text = parts[2]
            except:
                text = text
    
    # Extract title from first heading
    lines = text.split("\n")
    title = ""
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            body_start = i + 1
            break
    
    body = "\n".join(lines[body_start:]).strip()
    
    return {
        "filepath": str(filepath.relative_to(VAULT)).replace("\\", "/"),
        "source": filepath.parent.name,
        "filename": filepath.name,
        "title": title,
        "body": body,
        "date": fm.get("date", "") if isinstance(fm, dict) else "",
        "original_id": fm.get("id", "") if isinstance(fm, dict) else "",
    }

def strict_project_detection(item):
    """
    Strict phrase-aware project detection.
    Returns list of project slugs with confidence scoring.
    """
    title = item["title"].lower()
    body = item["body"].lower()
    combined = title + "\n" + body
    body_lower = body
    
    found = {}
    
    # ── HOMELAB-STACK ──
    # Must have hardware context. Not generic "computer" or "laptop" talk.
    hw_phrases = [
        "rtx 4090", "rtx4090", "rtx-4090", "nvidia 40", "geforce rtx",
        "cachyos", "cachy os", "limine", "sbctl", "secure boot",
        "7700x", "ryzen 7", "ryzen 9", "zen 4", "am5 socket", "am5 platform",
        "pfsense", "opnsense", "router", "firewall", "network card", "nic card",
        "unraid", "truenas", "proxmox", "esxi", "hypervisor", "vm host",
        "home server", "server rack", "nas server", "storage server",
        "gpu passthrough", "pci passthrough", "vfio", "iommu", "kvm",
        "nvidia-smi", "nvidia driver", "nvidia-smi", "cuda driver",
        "steam deck", "steam os", "handheld", "legion go", "ally", "rog ally",
        "dual boot", "dualboot", "grub", "systemd-boot", "refind",
        "laptop stand", "monitor arm", "desk setup", "peripherals",
        "ddr5", "ddr4", "ram upgrade", "nvme", "ssd", "m.2", "pcie",
        "power supply", "psu", "cpu cooler", "liquid cooling", "aio",
        "motherboard", "bios", "uefi", "overclock", "undervolt",
        "raspberry pi", "rpi", "orange pi", "sbc", "single board",
        "pihole", "adguard", "dns server", "reverse proxy", "traefik",
        "docker", "kubernetes", "k3s", "container", "self-hosted", "self hosted",
        "homelab", "home lab", "lab setup", "test bench", "dev machine",
        "hardware acceleration", "vaapi", "vdpau", "nvenc",
        "fan curve", "thermal paste", "temps", "temperature", "monitoring",
        "cable management", "build", "pc build", "rig", "desktop build",
    ]
    hw_score = sum(5 if phrase in title else 2 if phrase in body_lower else 0 
                   for phrase in hw_phrases)
    if hw_score >= 4:
        found["homelab-stack"] = hw_score
    
    # Also: category=homelab + any hardware signal
    if item.get("category") == "homelab" and hw_score > 0:
        found["homelab-stack"] = found.get("homelab-stack", 0) + 5
    
    # ── OPERATION IMMORTAL AGENT ──
    oia_phrases = [
        "meteora", "dlmm", "liquidity pool", "liquidity position",
        "solana bot", "trading bot solana", "dex bot solana", "defi bot",
        "autonomous fund", "autonomous trading", "auto trade", "auto trader",
        "jupiter perp", "jupiter exchange", "jupiter aggregator", "jupiter swap",
        "phantom mcp", "phantom mcp server", "phantom wallet",
        "yield farming", "yield farm", "farm solana", "lp position",
        "raydium", "orca solana", "orca finance", "whirlpool", "concentrated liquidity",
        "token price oracle", "price feed solana", "pyth network", "switchboard",
        "wallet tracking", "copy trade", "copy trading", "copytrade",
        "momentum strategy", "arbitrage solana", "sandwich attack", "mev bot",
        "backtest trading", "backtest solana", "strategy backtest",
        "live trading", "paper trading", "mainnet beta", "devnet",
        "immortal agent", "operation immortal",
    ]
    oia_score = sum(5 if phrase in title else 2 if phrase in body_lower else 0 
                     for phrase in oia_phrases)
    if oia_score >= 4:
        found["operation-immortal-agent"] = oia_score
    
    # ── PRIVATE-AI-CONSULTING ──
    consult_phrases = [
        "ai consulting", "ai consultant", "consulting business", "tech consulting",
        "private ai", "private ai service", "custom ai solution", "custom ai pipeline",
        "ai for business", "ai for client", "ai for customer", "ai for smb",
        "ai service", "ai offering", "ai package", "ai deliverable",
        "freelance ai", "ai freelancer", "contract ai", "ai contractor",
        "business name", "company name", "llc", "inc.", "d/b/a", "dba",
        "pricing", "hourly rate", "project rate", "retainer", "invoice",
        "linkedin job", "linkedin profile", "upwork", "fiverr", "toptal",
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
        "side hustle", "side income", "extra income", " Earn ", "money from ai",
        "marketing ai", "ai marketing", "content service",
    ]
    consult_score = sum(5 if phrase in title else 2 if phrase in body_lower else 0 
                        for phrase in consult_phrases)
    if consult_score >= 6:
        found["private-ai-consulting"] = consult_score
    
    # Boost: explicit consulting context
    if "business" in title and ("ai" in title or "tech" in title):
        found["private-ai-consulting"] = found.get("private-ai-consulting", 0) + 8
    if "consulting" in title:
        found["private-ai-consulting"] = found.get("private-ai-consulting", 0) + 15
    if "ai service" in title or "ai business" in title:
        found["private-ai-consulting"] = found.get("private-ai-consulting", 0) + 10
    
    # ── IT-CERTIFICATION ──
    cert_phrases = [
        "comptia a+", "comptia network+", "comptia security+", "comptia project+",
        "security+", "network+", "a+ cert", "it cert", "it certification",
        "tiffin university", "tiffin cert", "tiffin program",
        "resume", "cover letter", "job application", "job search", "applying for",
        "help desk", "helpdesk", "desktop support", "it support", "technical support",
        "entry level it", "entry-level it", "junior it", "it intern", "it apprenticeship",
        "interview prep", "interview practice", "interview question",
        "linkedin profile", "linkedin optimization", "linkedin headline",
        "certification exam", "exam prep", "study plan", "test date",
        "secai", "security ai", "ai security cert", "cybersecurity cert",
        "comptia", "cisco cert", "cisco ccna", "ccna", "azure cert", "aws cert",
        "it job", "it career", "tech career", "career change", "career transition",
    ]
    cert_score = sum(5 if phrase in title else 2 if phrase in body_lower else 0 
                      for phrase in cert_phrases)
    if cert_score >= 6:
        found["it-certification"] = cert_score
    
    # ── STREAMING-RIG ──
    stream_phrases = [
        "obs studio", "obs setup", "obs configuration", "obs scene", "obs transition",
        "twitch stream", "twitch setup", "twitch affiliate", "twitch partner",
        "youtube live", "youtube stream", "live stream", "streaming platform",
        "multistream", "multi stream", "simulcast", "restream",
        "capture card", "elgato", "stream deck", "go xlr", "audio mixer",
        "voicemeeter", "virtual cable", "nvidia broadcast", "noise suppression",
        "stream overlay", "overlay design", "alert box", "follow alert",
        "green screen", "chroma key", "virtual background", "vtuber",
        "recording setup", "recording studio", "broadcast setup", "broadcasting",
        "camera setup", "webcam", "dslr", "mirrorless", "camlink",
        "lighting setup", "key light", "softbox", "ring light",
        "microphone", "mic setup", "audio interface", "xlr mic", "usb mic",
        "content creation", "content strategy", "content calendar",
        "video editing", "post production", "thumbnail design",
        "streaming rig", "stream pc", "encoding pc", "capture pc",
    ]
    stream_score = sum(5 if phrase in title else 2 if phrase in body_lower else 0 
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
    brain_score = sum(5 if phrase in title else 2 if phrase in body_lower else 0 
                      for phrase in brain_phrases)
    if brain_score >= 6:
        found["second-brain-vault"] = brain_score
    
    # ── FLAPPY-MEME-BIRD (keep existing if already matched) ──
    # Only detected if title or body explicitly mentions the game
    if "flappy" in combined or "meme bird" in combined:
        found["flappy-meme-bird"] = 20
    
    # Return projects with sufficient score
    threshold = {"homelab-stack": 4, "operation-immortal-agent": 4, 
                 "private-ai-consulting": 6, "it-certification": 6,
                 "streaming-rig": 6, "second-brain-vault": 6, 
                 "flappy-meme-bird": 10}
    
    result = []
    for proj, score in found.items():
        if score >= threshold.get(proj, 6):
            result.append(proj)
    
    return sorted(set(result))

# ── Phase 1: Parse ALL files ──
print("Phase 1: Parsing all 3,400 conversation files...")
all_items = []
for source in SOURCES:
    folder = PROCESSED / source
    files = sorted(folder.glob("*.md"))
    print(f"  {source}: {len(files)} files...")
    for f in files:
        item = parse_file(f)
        item["source"] = source
        all_items.append(item)
    print(f"    ✓ Parsed {len(files)}")

print(f"\nTotal parsed: {len(all_items)}")

def json_serialize(obj):
    if isinstance(obj, (datetime, )):
        return obj.isoformat()
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# Save raw parsed data (with body) for reference
META.mkdir(exist_ok=True)
raw_dump = [{k: v for k, v in item.items() if k != "body"} for item in all_items]
(META / "parsed_files_index.json").write_text(json.dumps(raw_dump, indent=2, default=json_serialize), encoding="utf-8")
print("Parsed file index saved.")

# ── Phase 2: Rebuild enrichment mapping with strict detection ──
print("\nPhase 2: Rebuilding enrichment mapping with strict detection...")

# Build mapping mirroring enrichment_mapping.json structure
new_mapping = []
for item in all_items:
    fm = item.get("original_frontmatter", {})
    if not isinstance(fm, dict):
        fm = {}
    
    entry = {
        "source": item["source"],
        "file": item["filepath"],
        "title": item["title"],
        "body_preview": item["body"][:500] if item["body"] else "",
        "enriched_frontmatter": {
            "id": str(item.get("original_id", "")),
            "source": item["source"],
            "date": str(item.get("date", "")),
            "tags": [],
            "category": "",
            "sentiment": "",
            "resolution": "",
            "linked_projects": [],
            "linked_nodes": [],
        }
    }
    new_mapping.append(entry)

print(f"Built skeleton for {len(new_mapping)} entries")
