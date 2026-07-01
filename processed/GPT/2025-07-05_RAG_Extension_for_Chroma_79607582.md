---
source: GPT
date: 2025-07-05
category: ai-tools
id: 79607582
linked_nodes: ['nodes/people/bryan.md']
---
# RAG Extension for Chroma

### ASSISTANT
Here are some solid options for enabling RAG on your Oobabooga (text-generation-webui) setup using a local vector DB like Chroma:

## 📚 2. **superbooga2** extension (community favorite)  
From Reddit discussions, users have successfully used **superbooga2** with Chroma-based workflows:  

> “You install superbooga2. Upload your document. … start your prompts with `!c` to refer to the document.” citeturn0search1  

**Setup details:**  
- Supports local docs (e.g., PDF → auto‑convert via Pandoc / txt)  
- Upload via UI’s sidebar, then use `!c` before prompts to trigger context retrieval  
- Option to toggle autoinsert (no manual `!c`)  
- Integrates seamlessly with Chroma-stored embeddings  

👉 This seems like exactly what you’re looking for: local Chroma + Oobabooga RAG UI.

### ✅ TL;DR + Recommendation  
- **Best match:** **superbooga2** — built for local RAG, works with Chroma, lets you upload docs and use `!c` or auto-flagged context in Oobabooga chat.  
- **Alternative:** use **long_term_memory** + custom script for heavy-duty vector ingestion into Chroma.  
- **Other use-case:** **web_rag** if you prefer retrieving from live web instead of local DB.
---
### USER
can you find me a web RAG extension for oobabooga? Look for an extension that specifically supports local vector databases like Chroma (which i'm already using for db).