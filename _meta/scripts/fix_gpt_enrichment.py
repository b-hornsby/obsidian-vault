#!/usr/bin/env python3
"""
fix_gpt_enrichment.py — Fix miscategorized GPT conversation files (rule-based).

PROBLEM: First-pass enrichment systematically misclassified conversations:
  - Business/consulting/career conversations tagged as 'coding'
  - Tags are generic AI-tool keywords instead of actual topics
  - linked_projects includes projects not discussed

APPROACH: Pure rule-based classification using keyword matching on user turns.
  No LLM calls needed — the misclassification pattern is systematic enough
  that rules handle it well.

Usage: python3 fix_gpt_enrichment.py [--dry-run] [--verbose]
"""

import os
import re
import sys
import json
import time
import glob
from collections import defaultdict

# ── Configuration ──────────────────────────────────────────────────────────────
VAULT_PATH = "/mnt/c/Users/toastedmel0n/Obsidian/Tw1n"
GPT_DIR = os.path.join(VAULT_PATH, "processed", "GPT")
LOG_PATH = os.path.join(VAULT_PATH, "_meta", "enrichment-gpt-fix.log")

VALID_CATEGORIES = ["ai-tools", "crypto-web3", "coding", "career", "homelab", "streaming", "general"]
VALID_SENTIMENTS = ["curious", "frustrated", "exploratory", "building", "stuck", "executing"]
VALID_RESOLUTIONS = ["resolved", "unresolved", "partial", "abandoned"]

PROJECTS = [
    "operation-immortal-agent",
    "homelab-stack",
    "private-ai-consulting",
    "second-brain-vault",
    "streaming-rig",
    "it-certification",
    "flappy-meme-bird",
]

# ── Category keywords ─────────────────────────────────────────────────────────
# Each category has a list of (keyword, weight) tuples.
# Higher weight = stronger signal.
# "coding" has intentionally high-bar keywords.

CAREER_KEYWORDS = [
    ("resume", 3), ("job application", 3), ("interview", 3), ("career change", 3),
    ("cover letter", 3), ("salary", 2), ("warehouse", 2), ("logistics", 2),
    ("supply chain", 3), ("inventory", 2), ("forklift", 2), ("order fulfillment", 2),
    ("shipping", 1), ("receiving", 1), ("quality control", 2), ("help desk", 3),
    ("it certification", 3), ("comptia", 3), ("a+ exam", 3), ("network+ exam", 3),
    ("job description", 2), ("position", 1), ("candidate", 2), ("recruiter", 2),
    ("linkedin", 2), ("performance review", 3), ("promotion", 2), ("raise", 2),
    ("quit", 2), ("fired", 2), ("laid off", 3), ("401k", 3), ("retirement", 2),
    ("benefits", 2), ("payroll", 2), ("timesheet", 2), ("schedule", 1),
    ("entry level", 2), ("work experience", 2), ("employment", 2),
    ("background check", 2), ("drug test", 2), ("onboarding", 2),
    ("hr department", 3), ("human resources", 3), ("job search", 3),
    ("hiring", 2), ("applicant", 2), ("job posting", 3), ("job offer", 3),
    ("warehouse job", 3), ("help desk job", 3), ("it job", 3),
    ("career advice", 3), ("career transition", 3), ("career path", 3),
    ("professional", 1), ("workplace", 2), ("coworker", 2), ("manager", 1),
    ("supervisor", 2), ("team lead", 2), ("internship", 3), ("apprenticeship", 3),
    ("job title", 3), ("what job", 2), ("what would you call", 2),
    ("other jobs", 2), ("paid training", 3), ("no experience", 2),
    ("entry-level", 3), ("entry level", 3), ("job field", 2),
    ("career field", 3), ("job type", 2), ("work in", 1),
    ("job opportunity", 3), ("job opportunities", 3),
    ("find a job", 3), ("looking for work", 3), ("seeking employment", 3),
    ("job board", 2), ("indeed", 2), ("glassdoor", 2),
    ("job market", 2), ("labor market", 2), ("blue collar", 3),
    ("white collar", 3), ("trade school", 3), ("trade job", 3),
    ("skilled trade", 3), ("manual labor", 3), ("hourly", 1),
    ("wage", 2), ("paycheck", 2), ("direct deposit", 1),
    ("workplace safety", 2), ("osha", 3), ("union", 1),
    ("contractor", 1), ("freelance", 1), ("self-employed", 2),
    ("side hustle", 2), ("gig work", 2), ("gig economy", 2),
]

CRYPTO_KEYWORDS = [
    ("crypto", 2), ("cryptocurrency", 3), ("bitcoin", 3), ("ethereum", 3),
    ("solana", 3), ("token", 2), ("defi", 3), ("dex", 3), ("liquidity", 2),
    ("staking", 2), ("yield farming", 3), ("airdrop", 3), ("nft", 3),
    ("wallet", 1), ("metamask", 3), ("phantom wallet", 3), ("blockchain", 2),
    ("smart contract", 3), ("memecoin", 3), ("meme coin", 3), ("trading", 2),
    ("bull market", 2), ("bear market", 2), ("leverage", 1), ("short position", 2),
    ("long position", 2), ("portfolio", 2), ("rug pull", 3), ("pump and dump", 3),
    ("altcoin", 3), ("gas fee", 2), ("mainnet", 2), ("testnet", 1),
    ("serum", 3), ("raydium", 3), ("jupiter aggregator", 3), ("orca", 3),
    ("operation immortal", 3), ("immortal agent", 3), ("fund manager", 2),
    ("solana fund", 3), ("decentralized finance", 3), ("yield", 1),
    ("tokenomics", 3), ("market cap", 2), ("coinmarketcap", 3),
    ("dexscreener", 3), ("birdeye", 3), ("step finance", 3),
    ("xrp", 3), ("ripple", 3), ("hot wallet", 3), ("cold wallet", 3),
    ("cold storage", 3), ("hardware wallet", 3), ("ledger", 2),
    ("trezor", 3), ("wallet support", 2), ("store xrp", 3),
    ("sol to usd", 3), ("solana price", 3), ("crypto price", 2),
    ("tokenize", 3), ("token swap", 2), ("swap", 1),
    ("bridge", 1), ("cross-chain", 3), ("multichain", 2),
    ("solscan", 3), ("explorer", 1), ("block explorer", 2),
    ("validator", 1), ("node operator", 2), ("rpc", 1),
    ("gas", 1), ("transaction fee", 2), ("tx fee", 2),
    ("coinbase", 2), ("binance", 2), ("kraken", 2),
    ("phantom", 3), ("solflare", 3), ("backpack", 3),
]

HOMELAB_KEYWORDS = [
    ("homelab", 3), ("home server", 3), ("proxmox", 3), ("docker", 2),
    ("kubernetes", 3), ("k8s", 3), ("virtual machine", 2), ("nas", 3),
    ("storage", 1), ("raid", 2), ("networking", 2), ("router", 2),
    ("switch", 2), ("firewall", 2), ("vpn", 2), ("wireguard", 3),
    ("pihole", 3), ("raspberry pi", 3), ("linux", 1), ("ubuntu", 1),
    ("debian", 1), ("self-hosted", 3), ("selfhosted", 3), ("home lab", 3),
    ("server rack", 3), ("ups", 2), ("ipmi", 3), ("bios", 1),
    ("gpu", 1), ("graphics card", 2), ("nvidia", 1), ("amd", 1),
    ("overclock", 2), ("thermal", 1), ("cooling", 1), ("pve", 3),
    ("esxi", 3), ("vmware", 2), ("virtualization", 2), ("container", 1),
    ("lxc", 3), ("zfs", 3), ("truenas", 3), ("unraid", 3),
    ("ps/2", 3), ("ps2", 3), ("vga", 2), ("hdmi", 1), ("displayport", 2),
    ("thunderbolt", 3), ("docking station", 3), ("cpu cache", 3),
    ("motherboard", 3), ("mobo", 3), ("ram", 1), ("ddr4", 3), ("ddr5", 3),
    ("ssd", 2), ("hdd", 2), ("nvme", 3), ("sata", 2),
    ("wan", 2), ("lan", 2), ("ethernet", 2), ("wifi", 1),
    ("display", 1), ("tn display", 3), ("ips display", 3), ("oled", 2),
    ("form factor", 2), ("mini itx", 3), ("atx", 2),
    ("power supply", 2), ("psu", 3), ("cable management", 2),
    ("it technician", 3), ("it support", 3), ("tech support", 2),
    ("computer hardware", 3), ("pc build", 3), ("build a pc", 3),
    ("upgrade", 1), ("troubleshoot", 2), ("diagnostic", 1),
]

STREAMING_KEYWORDS = [
    ("stream", 1), ("streaming", 2), ("twitch", 3), ("obs", 3),
    ("obs studio", 3), ("overlay", 2), ("webcam", 2), ("microphone", 2),
    ("audio", 1), ("video", 1), ("bitrate", 2), ("encoder", 2),
    ("nvenc", 3), ("x264", 3), ("resolution", 1), ("fps", 1),
    ("donation", 2), ("subscriber", 2), ("follower", 1), ("chat", 1),
    ("emote", 2), ("badge", 1), ("stream deck", 3), ("elgato", 2),
    ("capture card", 3), ("green screen", 3), ("lighting", 1),
    ("ring light", 3), ("camera", 1), ("dslr", 2), ("streaming rig", 3),
    ("broadcast", 2), ("live stream", 3), ("vod", 2), ("clip", 1),
    ("content creation", 2), ("content creator", 2), ("twitch channel", 3),
]

AI_TOOLS_KEYWORDS = [
    ("chatgpt", 3), ("gpt-4", 2), ("gpt-4o", 2), ("claude", 2), ("gemini", 2),
    ("llama", 2), ("large language model", 3), ("llm", 2), ("ai model", 2),
    ("machine learning", 2), ("deep learning", 2), ("neural network", 2),
    ("transformer", 2), ("fine-tuning", 3), ("fine tuning", 3), ("lora", 3),
    ("qlora", 3), ("rag", 3), ("retrieval augmented", 3), ("prompt engineering", 3),
    ("system prompt", 2), ("ai agent", 2), ("autonomous agent", 3),
    ("copilot", 2), ("openai", 2), ("anthropic", 2), ("hugging face", 3),
    ("huggingface", 3), ("model hub", 2), ("inference", 1),
    ("quantization", 3), ("gguf", 3), ("gptq", 3), ("awq", 3),
    ("vllm", 3), ("ollama", 3), ("lm studio", 3), ("text generation", 2),
    ("image generation", 2), ("dall-e", 3), ("stable diffusion", 3),
    ("midjourney", 3), ("sora", 3), ("text to speech", 3),
    ("speech to text", 2), ("whisper", 2), ("embedding", 2),
    ("vector database", 3), ("pinecone", 3), ("weaviate", 3),
    ("chromadb", 3), ("qdrant", 3), ("ai consulting", 3),
    ("ai business", 2), ("ai startup", 2), ("prompt", 1),
    ("ai workflow", 2), ("ai tool", 2), ("generative ai", 3),
]

# Coding requires ACTUAL code writing/debugging — high bar
CODING_KEYWORDS = [
    ("write a script", 3), ("write code", 3), ("debug this", 3),
    ("error message", 2), ("traceback", 3), ("syntax error", 3),
    ("runtime error", 3), ("compile error", 3), ("compilation failed", 3),
    ("import error", 3), ("module not found", 3), ("package not installed", 3),
    ("my code", 2), ("this code", 2), ("code isn't working", 3),
    ("code doesn't work", 3), ("not working", 1), ("doesn't work", 1),
    ("fix this", 1), ("help me fix", 2), ("programming", 2),
    ("software development", 3), ("web development", 3),
    ("frontend", 2), ("backend", 2), ("fullstack", 3), ("full stack", 3),
    ("api endpoint", 2), ("rest api", 2), ("graphql", 2),
    ("database query", 2), ("sql", 1), ("migration", 1),
    ("git ", 1), ("pull request", 2), ("code review", 2),
    ("refactor", 2), ("unit test", 2), ("integration test", 2),
    ("deploy", 1), ("deployment", 1), ("ci/cd", 3),
    ("dockerfile", 2), ("docker compose", 2), ("makefile", 2),
    ("pip install", 1), ("npm install", 1), ("cargo build", 2),
    ("regex", 2), ("regular expression", 2),
    ("function definition", 2), ("class definition", 2),
    ("variable", 1), ("loop", 1), ("iteration", 1),
    ("python script", 2), ("bash script", 2), ("shell script", 2),
    ("powershell", 2), ("javascript", 1), ("typescript", 1),
    ("react", 1), ("vue", 1), ("angular", 1),
    ("html", 1), ("css", 1), ("json", 1), ("yaml", 1),
    ("xml", 1), ("api call", 2), ("fetch", 1), ("axios", 2),
    ("error handling", 2), ("exception", 2), ("try catch", 2),
    ("null pointer", 3), ("segmentation fault", 3), ("memory leak", 3),
    ("stack overflow", 2), ("infinite loop", 3), ("recursion", 2),
    ("algorithm", 1), ("data structure", 2), ("sorting", 1),
    ("binary search", 2), ("linked list", 2), ("hash map", 2),
    ("binary tree", 2), ("graph", 1), ("dynamic programming", 3),
]

ALL_CATEGORY_KEYWORDS = {
    "career": CAREER_KEYWORDS,
    "crypto-web3": CRYPTO_KEYWORDS,
    "homelab": HOMELAB_KEYWORDS,
    "streaming": STREAMING_KEYWORDS,
    "ai-tools": AI_TOOLS_KEYWORDS,
    "coding": CODING_KEYWORDS,
}


def _keyword_matches(keyword, text):
    """Check if keyword matches in text, using word boundaries for short keywords."""
    # For multi-word keywords or keywords > 4 chars, simple substring is fine
    if ' ' in keyword or len(keyword) > 4:
        return keyword in text
    # For short single-word keywords, use word boundary matching
    return bool(re.search(r'\b' + re.escape(keyword) + r'\b', text))


def classify_category(title, user_turns):
    """
    Rule-based category classification using weighted keyword matching.
    Returns (category, confidence).
    """
    text = (title + " " + user_turns).lower()
    scores = defaultdict(int)

    for category, keywords in ALL_CATEGORY_KEYWORDS.items():
        for keyword, weight in keywords:
            if _keyword_matches(keyword, text):
                scores[category] += weight

    if not scores:
        return "general", "high"

    # Get top 2 categories
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_cat, best_score = sorted_scores[0]
    second_score = sorted_scores[1][1] if len(sorted_scores) > 1 else 0

    # High confidence: clear winner with margin >= 2
    if best_score >= 3 and (best_score - second_score) >= 2:
        return best_cat, "high"
    # Medium confidence: some signal
    elif best_score >= 2:
        return best_cat, "medium"
    else:
        return "general", "low"


def detect_projects(user_turns):
    """Detect which projects are actually mentioned in user turns."""
    text = user_turns.lower()
    found = []

    project_mentions = {
        "operation-immortal-agent": ["operation immortal", "immortal agent", "solana fund", "oia", "fund manager solana"],
        "homelab-stack": ["homelab", "home server", "proxmox", "self-hosted", "selfhosted", "home lab"],
        "private-ai-consulting": ["ai consulting", "consulting business", "consulting practice", "private ai consulting"],
        "second-brain-vault": ["second brain", "obsidian vault", "knowledge base", "zettelkasten"],
        "streaming-rig": ["streaming rig", "stream setup", "streaming setup", "twitch setup"],
        "it-certification": ["it certification", "comptia", "a+ exam", "network+ exam", "security+ exam", "certification exam"],
        "flappy-meme-bird": ["flappy", "flappy bird", "meme bird"],
    }

    for project, keywords in project_mentions.items():
        for kw in keywords:
            if kw in text:
                found.append(project)
                break

    return found


def generate_tags(title, user_turns, category):
    """Generate meaningful tags based on actual conversation content."""
    text = (title + " " + user_turns).lower()
    tags = []

    # Category-specific tag mappings: keyword -> tag
    tag_maps = {
        "career": [
            ("resume", "resume-writing"), ("interview", "interview-prep"),
            ("job application", "job-application"), ("warehouse", "warehouse-work"),
            ("logistics", "logistics"), ("supply chain", "supply-chain"),
            ("401k", "401k"), ("hr", "hr-communication"),
            ("cover letter", "cover-letter"), ("career change", "career-change"),
            ("it certification", "it-certification"), ("help desk", "help-desk"),
            ("comptia", "comptia"), ("a+ exam", "comptia-a-plus"),
            ("job search", "job-search"), ("hiring", "hiring"),
            ("salary", "salary"), ("promotion", "promotion"),
            ("fired", "job-loss"), ("laid off", "job-loss"),
            ("internship", "internship"), ("apprenticeship", "apprenticeship"),
        ],
        "crypto-web3": [
            ("memecoin", "memecoin"), ("solana", "solana"), ("defi", "defi"),
            ("trading", "trading"), ("token", "token"), ("nft", "nft"),
            ("airdrop", "airdrop"), ("staking", "staking"),
            ("liquidity", "liquidity"), ("wallet", "wallet"),
            ("market", "market-analysis"), ("leverage", "leverage-trading"),
            ("bitcoin", "bitcoin"), ("ethereum", "ethereum"),
            ("rug pull", "rug-pull"), ("tokenomics", "tokenomics"),
            ("dex", "dex"), ("yield farming", "yield-farming"),
        ],
        "coding": [
            ("python", "python"), ("javascript", "javascript"),
            ("typescript", "typescript"), ("react", "react"),
            ("docker", "docker"), ("api", "api"), ("debug", "debugging"),
            ("error", "error-fixing"), ("script", "scripting"),
            ("database", "database"), ("git", "git"), ("deploy", "deployment"),
            ("web development", "web-dev"), ("frontend", "frontend"),
            ("backend", "backend"), ("fullstack", "fullstack"),
        ],
        "homelab": [
            ("proxmox", "proxmox"), ("docker", "docker"), ("server", "server"),
            ("nas", "nas"), ("networking", "networking"), ("vpn", "vpn"),
            ("linux", "linux"), ("raspberry pi", "raspberry-pi"),
            ("storage", "storage"), ("gpu", "gpu"), ("virtualization", "virtualization"),
            ("self-hosted", "self-hosted"), ("container", "container"),
        ],
        "streaming": [
            ("twitch", "twitch"), ("obs", "obs"), ("overlay", "overlay"),
            ("audio", "audio"), ("microphone", "microphone"),
            ("webcam", "webcam"), ("lighting", "lighting"),
            ("stream deck", "stream-deck"), ("capture card", "capture-card"),
            ("content creation", "content-creation"), ("encoder", "encoder"),
        ],
        "ai-tools": [
            ("chatgpt", "chatgpt"), ("claude", "claude"), ("llm", "llm"),
            ("prompt", "prompt-engineering"), ("fine-tuning", "fine-tuning"),
            ("rag", "rag"), ("agent", "ai-agent"), ("inference", "inference"),
            ("quantization", "quantization"), ("local", "local-llm"),
            ("generative ai", "generative-ai"), ("ai workflow", "ai-workflow"),
            ("stable diffusion", "stable-diffusion"), ("image generation", "image-gen"),
        ],
        "general": [],
    }

    cat_map = tag_maps.get(category, [])
    for keyword, tag in cat_map:
        if keyword in text and tag not in tags:
            tags.append(tag)

    # Extract meaningful words from title as additional tags
    stop_words = {"the", "a", "an", "is", "are", "was", "were", "be", "been",
                  "being", "have", "has", "had", "do", "does", "did", "will",
                  "would", "could", "should", "may", "might", "shall", "can",
                  "to", "of", "in", "for", "on", "with", "at", "by", "from",
                  "as", "into", "through", "during", "before", "after", "above",
                  "below", "between", "out", "off", "over", "under", "again",
                  "further", "then", "once", "here", "there", "when", "where",
                  "why", "how", "all", "both", "each", "few", "more", "most",
                  "other", "some", "such", "no", "nor", "not", "only", "own",
                  "same", "so", "than", "too", "very", "just", "because", "but",
                  "and", "or", "if", "while", "about", "up", "me", "my", "i",
                  "we", "our", "you", "your", "he", "she", "it", "they", "them",
                  "what", "which", "who", "whom", "this", "that", "these", "those",
                  "am", "its", "also", "get", "got", "make", "made", "go", "going",
                  "come", "came", "take", "took", "know", "knew", "think", "thought",
                  "say", "said", "tell", "told", "give", "gave", "well", "back",
                  "even", "still", "way", "much", "many", "thing", "things",
                  "help", "need", "want", "like", "look", "see", "find", "found",
                  "entry", "level", "expert", "suggestions", "ideas", "tips",
                  "guide", "overview", "introduction", "request", "question"}

    title_words = re.findall(r'[a-zA-Z][a-zA-Z0-9_-]{2,}', title)
    for word in title_words:
        w = word.lower()
        if w not in stop_words and w not in tags and len(tags) < 8:
            covered = False
            for t in tags:
                if w in t or t in w:
                    covered = True
                    break
            if not covered:
                tags.append(w)

    # Ensure 3-8 tags
    if len(tags) < 3 and category not in tags:
        tags.append(category)
    if len(tags) < 3:
        tags.append("gpt-conversation")
    if len(tags) > 8:
        tags = tags[:8]

    return tags


def detect_sentiment(user_turns):
    """Detect sentiment from user turns."""
    text = user_turns.lower()

    if any(kw in text for kw in ["stuck", "can't figure", "can't get", "not working",
                                   "doesn't work", "help me", "don't know how",
                                   "how do i", "what should i", "confused", "lost",
                                   "no idea", "not sure how"]):
        return "stuck"

    if any(kw in text for kw in ["frustrated", "annoyed", "angry", "hate", "terrible",
                                   "awful", "worst", "broken", "failed", "failing",
                                   "giving up", "waste of time"]):
        return "frustrated"

    if any(kw in text for kw in ["build", "create", "implement", "deploy", "launch",
                                   "start building", "working on", "making", "developing",
                                   "progress", "completed", "finished", "done", "ship"]):
        return "building"

    if any(kw in text for kw in ["now", "next step", "continue", "keep going",
                                   "proceed", "execute", "run this"]):
        return "executing"

    if any(kw in text for kw in ["what is", "how does", "why does", "explain",
                                   "tell me about", "curious", "wondering", "learn",
                                   "understand", "difference between", "vs", "versus",
                                   "compare", "what are"]):
        return "curious"

    return "exploratory"


def detect_resolution(user_turns):
    """Detect if the conversation reached a resolution."""
    text = user_turns.lower()

    if any(kw in text for kw in ["thank you", "thanks", "perfect", "great", "awesome",
                                   "exactly what i needed", "that works", "solved",
                                   "fixed", "resolved", "got it", "understood", "helpful",
                                   "that helps", "makes sense", "clear now"]):
        return "resolved"

    if any(kw in text for kw in ["still not", "still doesn't", "still can't",
                                   "not sure", "confused", "unresolved",
                                   "need more help", "what else", "any other"]):
        return "unresolved"

    if any(kw in text for kw in ["partial", "somewhat", "kind of", "sort of",
                                   "almost", "close", "nearly", "partially"]):
        return "partial"

    return "resolved"


def parse_frontmatter(content):
    """Parse YAML frontmatter from a markdown file."""
    if not content.startswith("---"):
        return None, content

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None, content

    fm_text = match.group(1)
    body = content[match.end():]

    fm = {}
    for line in fm_text.split('\n'):
        line = line.strip()
        if ':' not in line:
            continue
        key, _, value = line.partition(':')
        key = key.strip()
        value = value.strip()

        if value.startswith('[') and value.endswith(']'):
            inner = value[1:-1].strip()
            if not inner:
                fm[key] = []
            else:
                items = re.findall(r"'([^']*)'", inner)
                fm[key] = items
        else:
            fm[key] = value

    return fm, body


def write_frontmatter(fm):
    """Write frontmatter dict to YAML string."""
    lines = ["---"]
    for key in ["id", "source", "date"]:
        if key in fm:
            val = fm[key]
            if isinstance(val, list):
                lines.append(f"{key}: [{', '.join(repr(v) for v in val)}]")
            else:
                lines.append(f"{key}: {val}")

    for key in ["tags", "category", "sentiment", "resolution", "linked_projects", "linked_nodes"]:
        if key in fm:
            val = fm[key]
            if isinstance(val, list):
                lines.append(f"{key}: [{', '.join(repr(v) for v in val)}]")
            else:
                lines.append(f"{key}: {val}")

    lines.append("---")
    return "\n".join(lines) + "\n"


def extract_user_turns(content):
    """Extract USER turns from a conversation file."""
    fm, body = parse_frontmatter(content)
    if fm is None:
        body = content

    user_lines = []
    in_user = False
    for line in body.split('\n'):
        stripped = line.strip()
        if stripped in ("### USER", "### HUMAN"):
            in_user = True
            continue
        if stripped.startswith("### ") and stripped not in ("### USER", "### HUMAN"):
            in_user = False
            continue
        if in_user and stripped:
            user_lines.append(stripped)

    return "\n".join(user_lines)


def process_file(filepath, dry_run=False, verbose=False):
    """Process a single GPT file. Returns (was_fixed, old_fm, new_fm)."""
    filename = os.path.basename(filepath)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_fm, body = parse_frontmatter(content)
    if old_fm is None:
        return False, None, None

    old_category = old_fm.get("category", "")
    old_tags = old_fm.get("tags", [])
    old_projects = old_fm.get("linked_projects", [])

    user_turns = extract_user_turns(content)
    title = filename.replace('.md', '').replace('_', ' ')

    if not user_turns.strip():
        return False, None, None

    new_category, confidence = classify_category(title, user_turns)
    new_tags = generate_tags(title, user_turns, new_category)
    new_sentiment = detect_sentiment(user_turns)
    new_resolution = detect_resolution(user_turns)
    new_projects = detect_projects(user_turns)

    # Validate
    if new_category not in VALID_CATEGORIES:
        new_category = "general"
    if new_sentiment not in VALID_SENTIMENTS:
        new_sentiment = "exploratory"
    if new_resolution not in VALID_RESOLUTIONS:
        new_resolution = "resolved"
    new_projects = [p for p in new_projects if p in PROJECTS]

    new_fm = dict(old_fm)
    new_fm["tags"] = new_tags
    new_fm["category"] = new_category
    new_fm["sentiment"] = new_sentiment
    new_fm["resolution"] = new_resolution
    new_fm["linked_projects"] = new_projects

    changed = (
        old_category != new_category or
        old_tags != new_tags or
        old_projects != new_projects
    )

    if changed and verbose:
        print(f"  FIX {filename}:")
        print(f"    cat: {old_category} -> {new_category} ({confidence})")
        print(f"    tags: {old_tags} -> {new_tags}")
        print(f"    proj: {old_projects} -> {new_projects}")

    if changed and not dry_run:
        fm_str = write_frontmatter(new_fm)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fm_str)
            f.write(body)

    return changed, old_fm if changed else None, new_fm if changed else None


def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    files = sorted(glob.glob(os.path.join(GPT_DIR, "*.md")))
    print(f"Found {len(files)} GPT files to process")
    print(f"Dry run: {dry_run}")
    print()

    total = len(files)
    fixed = 0
    skipped = 0
    errors = 0
    category_changes = defaultdict(lambda: defaultdict(int))
    log_lines = []
    log_lines.append(f"# GPT Enrichment Fix Log\n")
    log_lines.append(f"Started: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_lines.append(f"Total files: {total}\n")
    log_lines.append(f"Dry run: {dry_run}\n\n")

    start_time = time.time()

    for i, filepath in enumerate(files):
        filename = os.path.basename(filepath)

        if (i + 1) % 100 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            print(f"  Progress: {i+1}/{total} ({fixed} fixed, {skipped} skipped, {errors} errors) [{rate:.0f} files/s]")

        try:
            was_fixed, old_fm, new_fm = process_file(filepath, dry_run=dry_run, verbose=verbose)
            if was_fixed:
                fixed += 1
                old_cat = old_fm.get("category", "?")
                new_cat = new_fm.get("category", "?")
                category_changes[old_cat][new_cat] += 1
                log_lines.append(f"FIXED: {filename}\n")
                log_lines.append(f"  {old_cat} -> {new_cat}\n")
                log_lines.append(f"  tags: {old_fm.get('tags', [])} -> {new_fm.get('tags', [])}\n")
                log_lines.append(f"  projects: {old_fm.get('linked_projects', [])} -> {new_fm.get('linked_projects', [])}\n\n")
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"  ERROR on {filename}: {e}")
            log_lines.append(f"ERROR: {filename}: {e}\n")

    elapsed = time.time() - start_time

    summary = f"""
{'='*60}  SUMMARY  {'='*60}
Total files:    {total}
Fixed:          {fixed}
Skipped:        {skipped}
Errors:         {errors}
Time:           {elapsed:.1f}s

Category changes:
"""
    for old_cat in sorted(category_changes.keys()):
        for new_cat in sorted(category_changes[old_cat].keys()):
            count = category_changes[old_cat][new_cat]
            summary += f"  {old_cat} -> {new_cat}: {count}\n"

    print(summary)

    log_lines.append(f"\n{summary}")
    log_lines.append(f"\nCompleted: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    if not dry_run:
        with open(LOG_PATH, 'w', encoding='utf-8') as f:
            f.writelines(log_lines)
        print(f"Log written to: {LOG_PATH}")
    else:
        print(f"[DRY RUN] Log would be written to: {LOG_PATH}")
        dry_run_log = LOG_PATH + ".dryrun"
        with open(dry_run_log, 'w', encoding='utf-8') as f:
            f.writelines(log_lines)
        print(f"[DRY RUN] Preview log written to: {dry_run_log}")


if __name__ == "__main__":
    main()
