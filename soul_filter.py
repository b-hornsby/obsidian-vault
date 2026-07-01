import json
import re
import html
from datetime import datetime
from pathlib import Path

# === CORRECT PATHS ===
BASE_DIR = Path(r"C:\Users\toastedmel0n\Obsidian\Tw1n\raw")
OUT_DIR = Path(r"C:\Users\toastedmel0n\Obsidian\Tw1n\processed")

for src in ["GPT", "GEMINI", "CLAUDE", "GROK"]:
    (OUT_DIR / src).mkdir(parents=True, exist_ok=True)

def clean_text(text):
    if not text: return ""
    text = html.unescape(re.sub(r'<[^>]*>', '', str(text)))
    return re.sub(r'\s+', ' ', text).strip()

def safe_filename(name):
    name = re.sub(r'[^\w\s-]', '', str(name)).strip()
    return re.sub(r'[\s-]+', '_', name)[:60]

def write_note(source, date, title, body):
    if not body or not body.strip(): 
        return
    hash_id = str(abs(hash(body[:300])))[:8]
    filename = f"{date}_{safe_filename(title)}_{hash_id}.md"
    out_path = OUT_DIR / source / filename
    
    if out_path.exists(): 
        return

    content = f"""---
id: {str(hash(body))[-6:]}
source: {source}
date: {date}
---

# {title}

{body.strip()}
"""
    out_path.write_text(content, encoding='utf-8')
    print(f"✅ [{source}] {filename}")


# ====================== PARSERS ======================

def parse_gpt():
    print("🔄 Parsing ChatGPT...")
    for json_file in (BASE_DIR / "chat gpt").rglob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding='utf-8'))
            chats = data if isinstance(data, list) else [data]
            for chat in chats:
                title = chat.get("title") or "Untitled GPT"
                ts = chat.get("create_time") or chat.get("createTime") or 0
                date = datetime.fromtimestamp(ts).strftime("%Y-%m-%d") if ts > 0 else "unknown"
                
                body = ""
                for node in chat.get("mapping", {}).values():
                    msg = node.get("message", {})
                    content = msg.get("content", {})
                    if content.get("parts"):
                        role = msg.get("author", {}).get("role", "USER").upper()
                        text = "".join(str(p) for p in content["parts"] if isinstance(p, (str, dict)))
                        if text.strip():
                            body += f"### {role}\n{text.strip()}\n\n"
                if body:
                    write_note("GPT", date, title, body)
        except Exception as e:
            print(f"   ⚠️  GPT error in {json_file.name}: {e}")


def parse_claude():
    print("🔄 Parsing Claude...")
    for json_file in (BASE_DIR / "claude").rglob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding='utf-8'))
            chats = data if isinstance(data, list) else [data]
            for chat in chats:
                title = chat.get("name") or chat.get("title", "Untitled Claude")
                date_str = str(chat.get("created_at") or chat.get("createdAt", ""))[:10] or "unknown"
                body = ""
                for m in chat.get("chat_messages", []):
                    sender = m.get("sender", "USER").upper()
                    text = m.get("text", "")
                    if text.strip():
                        body += f"### {sender}\n{text.strip()}\n\n"
                if body:
                    write_note("CLAUDE", date_str, title, body)
        except Exception as e:
            print(f"   ⚠️  Claude error in {json_file.name}: {e}")


def parse_gemini():
    print("🔄 Parsing Gemini...")
    for json_file in (BASE_DIR / "gemini").rglob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding='utf-8'))
            entries = data if isinstance(data, list) else [data]
            for entry in entries:
                title = str(entry.get("title", "")).replace("Prompted ", "") or "Untitled Gemini"
                date_str = str(entry.get("time", ""))[:10] or "unknown"
                body = f"### USER\n{title}\n\n"
                
                if "safeHtmlItem" in entry:
                    for item in entry.get("safeHtmlItem", []):
                        body += f"### GEMINI\n{clean_text(item.get('html', ''))}\n\n"
                elif "response" in entry:
                    body += f"### GEMINI\n{clean_text(entry.get('response',''))}\n\n"
                
                if body:
                    write_note("GEMINI", date_str, title, body)
        except Exception as e:
            print(f"   ⚠️  Gemini error in {json_file.name}: {e}")


def parse_grok():
    print("🔄 Parsing Grok...")
    for json_file in (BASE_DIR / "grok").rglob("*.json"):
        try:
            data = json.loads(json_file.read_text(encoding='utf-8'))
            convos = data.get("conversations", []) if isinstance(data, dict) else (data if isinstance(data, list) else [data])
            for convo in convos:
                meta = convo.get("conversation", convo)
                title = meta.get("title", "Untitled Grok")
                date_str = str(meta.get("create_time") or meta.get("created_at", ""))[:10] or "unknown"
                body = ""
                responses = convo.get("responses", []) or convo.get("messages", [])
                for r in responses:
                    rd = r.get("response", r)
                    sender = rd.get("sender", "GROK").upper()
                    text = rd.get("message") or rd.get("content", "")
                    if text.strip():
                        body += f"### {sender}\n{text.strip()}\n\n"
                if body:
                    write_note("GROK", date_str, title, body)
        except Exception as e:
            print(f"   ⚠️  Grok error in {json_file.name}: {e}")


# ====================== RUN ======================
if __name__ == "__main__":
    print("🚀 SOUL FILTER v2.2 — Starting...\n")
    parse_gpt()
    parse_claude()
    parse_gemini()
    parse_grok()
    print("\n✅ Soul Filter finished! Check the 'processed' folder.")