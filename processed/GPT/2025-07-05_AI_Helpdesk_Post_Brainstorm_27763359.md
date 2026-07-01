---
id: 418862
source: GPT
date: 2025-07-05
tags: ['linkedin-post', 'phi-3-mini', 'whisper', 'chromadb', 'superbooga', 'stt']
category: career
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/it-certification.md']
summary: Bryan was brainstorming and refining a LinkedIn post showcasing his voice-enabled offline AI helpdesk project with RAG.
---
### 🟢 TL;DR:

No — you **do not need a separate PDF** unless you:
- Want to use this content *outside LinkedIn* (e.g., on a portfolio site or GitHub)
- Want a version to **print**, attach to an email, or show during interviews

Otherwise, your **LinkedIn post/project entry is fully self-contained** and impressive as-is.

### 🔧 Suggested LinkedIn Post Structure:

**1. Hook (1–2 lines):**  
Grab attention. Make it relevant, impressive, or personal.

**2. The Challenge (1 short paragraph):**  
Describe the problem space and what made it difficult or meaningful.

**3. The Solution (1 short paragraph):**  
Explain your approach and how you engineered the solution.

**4. The Struggle (optional, 1–2 lines):**  
Mention a speed bump or something you had to learn/adapt to.

**5. The Result (1–2 lines):**  
What’s the outcome? Why does it matter? How did it improve things?

**6. Call-to-action (CTA, optional):**  
Ask for feedback, collaboration, or just encourage engagement.

**🎙️ Built My Own Voice-Enabled AI Helpdesk — Completely Offline.**  
What started as a curiosity turned into a full-stack AI assistant powered by a local LLM, real-time voice, and Retrieval-Augmented Generation (RAG) — all running on consumer hardware.

The hardest part?  
Optimizing for speed *and* accuracy.  
My early version had noticeable voice response delays, poor RAG performance, and laggy inference from the model. It was usable — but not impressive.

So I rolled up my sleeves and got to work:  
- Tuned system parameters to reduce inference latency  
- Reworked how vector embeddings were retrieved  
- Swapped out my TTS backend to dramatically improve voice speed  
- Fine-tuned everything to strike a balance between conversational flow and performance

Now? It’s fast, responsive, and surprisingly capable for an entirely offline system.  
I even structured it to support `.txt` knowledge files for internal SOPs and troubleshooting.

Next steps:  
🗂️ Add image generation  
🎤 Expand voice functionality (wake word, sentiment triggers)  
📁 Modularize it as a self-hostable “AI Helpdesk-in-a-box”

Would love to hear from anyone exploring local LLMs, RAG, or edge-based AI tooling!

#AI #LLM #opensource #voiceAI #RAG #localAI #projectshare

Want me to write a few versions with different tones (e.g., more casual, more technical, more beginner-friendly)? Or tailor it for recruiters vs developers?

### USER
working on a LinkedIn post and I need your help brainstorming how i should document it. this is the summary so far: Engineered a responsive, voice-enabled AI helpdesk assistant, integrating Speech-to-Text (STT) and Retrieval-Augmented Generation (RAG) with a local Large Language Model (LLM). This project presented critical optimization challenges, notably high latency stemming from initial Text-to-Speech (TTS) processes, inefficient RAG data handling, and the LLM's inference speed on consumer hardware. Through systematic debugging and fine-tuning of system parameters, I successfully balanced speed and accuracy, delivering a performant and knowledgeable conversational AI solution.

### ASSISTANT
Great call — using **Google Drive** to share your demo video is a solid option, but there are a few **important safety and professionalism steps** to take to make sure your content is private, polished, and secure.

#### 🔒 1. **Use a Clean, Edited Video**
Before uploading:
- Remove or blur anything sensitive (usernames, file paths, IPs, personal info)
- Trim unnecessary terminal output — keep it focused on showing:
  - Voice input
  - Transcription via Whisper
  - LLM response
  - RAG pulling from `.txt` knowledge

**Optional**: Add simple captions using free tools (like Clipchamp, Canva, or Descript) that explain what’s happening on-screen.

#### ⚙️ 3. **Adjust Sharing Settings**
Here’s the key part:

1. **Right-click > Share**
2. Under “Get link,” click:
   - Change from “Restricted” to:
     > 🔘 **Anyone with the link**
3. Set **Viewer access only**
   - **DO NOT** allow editing or commenting

✅ This means *only people with the link* can view it. It’s public enough for LinkedIn, but private enough that it won't be searchable.

#### 📝 5. **Include in Project Description or Post**
**For your LinkedIn project description:**

> 🛠️ Fully offline voice-enabled AI helpdesk assistant built using Whisper.cpp, Phi-3, and ChromaDB  
> 🔊 See the voice demo: [bit.ly/offline-ai-helpdesk](#)

Or:

> 🎥 Watch the voice-enabled demo here:  
> https://drive.google.com/file/d/XXXXXXX/view

If you want, I can help:
- Review your demo script for what to show
- Draft a short caption or intro for the beginning of your video
- Create a thumbnail image you can upload alongside it

Let me know!

### ASSISTANT
Got it — here's a **refined version of your project description** that keeps your personal, conversational tone but polishes it just enough to **stand out professionally** *without sounding robotic*. It’s **friendly, technical, and reflective** — perfect for pairing with attached media (screenshots, GitHub repo, or demo videos).

### 📎 Tip: File Attachments to Include

- 📷 A screenshot of the assistant running in terminal or UI  
- 📁 `.txt` example knowledge file (blur/redact if sensitive)  
- 🔗 GitHub repo (if you’re ready to share it)  
- 🎥 Short screen recording of voice input > AI response > knowledge output

### ✅ Why It’s Safe:

- `127.0.0.1` is the **loopback address**, also known as **localhost**.
- It only points to your **own machine** and is **not accessible externally**.
- It’s a universal default — anyone can see that in a demo and it doesn’t expose anything specific to your system.

### 🧠 Best Practices for Your Video:

✅ It’s **fine** to show:
- `http://127.0.0.1:7860`
- Your voice input in real-time
- Terminal output showing Whisper, embeddings, or LLM response
- ChromaDB returning matches from `.txt` files

🚫 Avoid or blur if you have:
- File paths like `C:/Users/Bryan/Documents/WorkStuff/SensitiveThings.txt`
- Actual company names or sensitive SOP content
- Anything with access tokens or login panels

### ❓ Can You *Embed* a Video in Bitly?

**No — Bitly does not host or embed videos.**  
It’s a **URL shortener**, not a hosting or embedding platform. What you *can* do is:

✅ **Shorten a direct link to your Google Drive video**  
✅ **Customize the slug** to make it look cleaner and more professional  
✅ **Track link clicks** if you create a free Bitly account

### 💡 Bonus Tip: Add a Thumbnail or Callout Image

Since LinkedIn can’t preview a Drive video in the Projects section, upload a **screenshot or image** with a caption like:

> 🎥 *Click the link below to watch the full demo video on Google Drive*  
> *(Voice input → Local LLM → RAG retrieval)*

You could even add a “Play” icon on the screenshot to make it *look* like a video thumbnail.

Want help designing a polished thumbnail or writing a short intro blurb for the video? I’ve got you.

### ASSISTANT
You're really close — your voice comes through clearly, and it’s informative without being stiff. I’ll revise it to make it **cleaner, easier to read, and more natural**, while keeping your personality intact. Here's a **polished but still personal version** of your project description:

Let me know if you want a **condensed version** (for tighter spaces like the GitHub repo description or LinkedIn's strict character limits), or a **"first sentence only"** version that pops in a project list.

### ASSISTANT
Absolutely — here’s a breakdown of each part of the **system diagram** and how the components work together in your **offline AI Helpdesk Assistant**:

### 🔁 **Step-by-Step Explanation**

1. **🎤 Voice Input**
   - You speak a question or command.
   - Triggered via mic + manual record button (since there’s no voice trigger yet).

2. **🗣 Whisper.cpp (STT)**
   - Converts your speech into plain text.
   - Runs locally and fast, enabling full offline speech-to-text conversion.

3. **🧱 Prompt Builder**
   - Takes your transcribed input and builds a structured prompt for the LLM.
   - Also passes this input to the embedding model for querying the knowledge base.

4. **📐 sentence-transformers (Embedding Model)**
   - Converts both your input and `.txt` file chunks into embeddings (vectors).
   - Used for similarity search in the next step.

5. **📚 ChromaDB (RAG Layer)**
   - Searches the embedded `.txt` knowledge base using your voice-derived query.
   - Returns the most relevant document snippets to the LLM as context.

6. **🧠 Phi-3 Mini (LLM)**
   - Receives both your query and the retrieved context from ChromaDB.
   - Generates a response, running entirely locally via oobabooga with GPU support.

7. **💬 Response Output**
   - The assistant outputs the final text-based answer in your interface.
   - (Optional TTS layer not shown but could follow here if you add it back in.)

Would you like a version of this diagram that includes the SuperBooga UI and optional TTS layer too?

### USER
is that necessary if i wrote: What I Built:
A fully offline, voice-enabled AI assistant that answers everyday IT questions by searching through local .txt help files like “How do I reset a password?” or “How do I set up a new user?”

How It Works:
    ‣Runs locally using Phi-3 Mini (switched from Mistral-7B for speed)
    ‣Voice input handled by Whisper
    ‣Pulls answers from my own folder of text guides using ChromaDB and Superbooga
    ‣All powered inside WSL2 with GPU support via CUDA 
    ‣Uses Ooobabooga for the interface to keep it simple to test and use
    ‣Pulls answers from my own folder of text guides using ChromaDB

Why I Made It:
With Ai being an everyday tool for some and with all the crazy stuff going on in the world, I wanted to take the time to really learn that tool and build something with it. I feel that with it becoming a staple in most industries today knowing what it is that you want to build is far more important than knowing all the ins and outs up front and running LLMs locally allows for that possibility to be accessed purely off your hardware and not through some expensive subscription, especially when everything seems to be heading towards that subscription model nowadays. 

What I Ran Into:
    ‣ WSL2 + CUDA setup was rough at first, especially getting llama.cpp to use my 3070
    ‣Started with a heavier model (Mistral-7B), but once I added voice, the lag wasn’t worth it  so switching to Phi-3 Mini made everything snappy again
    ‣Writing my own help docs was actually harder than I expected, especially with keeping answers short but useful taking a few tries

Where It’s At Now:
The assistant runs completely offline, listens to your voice, finds a matching answer from local files, and responds instantly. No cloud, no internet just a fast local AI tool built from scratch.

🎥 Link to video of it in action here: https://bit.ly/4lc9Dc9

### USER
can we make that system diagram? that sounds interesting

### USER
what media should i include for this LinkedIn post?

### USER
can you explain that diagram you just made?

### USER
so to shorten on bitly i just paste the link of the drive its in?

### TOOL
{'asset_pointer': 'sediment://file_000000009d5461fab93762fdb77e70c4', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1024, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': 1024, 'container_pixel_width': 1536, 'dalle': {'edit_op': None, 'gen_id': '1529788e-06e4-4479-82b3-c96dce61e21e', 'parent_gen_id': None, 'prompt': '', 'seed': None, 'serialization_title': 'DALL-E generation metadata'}, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': {'gen_id': '1529788e-06e4-4479-82b3-c96dce61e21e', 'gen_size': 'xlimage', 'gen_size_v2': None, 'height': 1024, 'orientation': None, 'parent_gen_id': None, 'seed': None, 'serialization_title': 'Image Generation metadata', 'transparent_background': False, 'width': 1536}, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': False, 'watermarked_asset_pointer': None}, 'size_bytes': 817540, 'width': 1536}

### ASSISTANT
Absolutely! Let’s make a clean, easy-to-read **system diagram** that visually shows how your offline AI Helpdesk assistant works. I’ll first outline the layout and components, then generate the actual image for you.

### ➡️ Visual Flow (Before Rendering)

```
[🎤 Voice Input]
       ↓
[Whisper.cpp (STT)]
       ↓
[Prompt Builder]
       ↓
[ChromaDB (RAG)]
       ↓
[Phi-3 Mini (LLM)]
       ↓
[🖥️ Response Output]
```

Optional paths:
- You could also include an alternate TTS path, like:
  ```
  [Phi-3 Response]
         ↓
    [TTS Engine]
         ↓
    [🔊 Audio Output]
  ```

## ✅ Core Media & Documentation Checklist (You're 80% there!)

| ✅ | Asset | Purpose |
|
---
-|
---
-
---
|
---
-
---
--|
| ✅ | 📷 Screenshot of `.txt` knowledge base | Shows custom, modular RAG input |
| ✅ | 🎥 Demo video showing voice-enabled assistant in action | Proves offline/STT/RAG/LLM integration |
| ⬜ | 🧠 **Simple system diagram or architecture flow** | Visualizes how Whisper → RAG → LLM work together |
| ⬜ | 📄 **Short README-style writeup** | Summarizes tools, structure, and setup (great as a PDF or GitHub README) |
| ⬜ | 📄 **Optional PDF or 1-pager overview** | Wraps everything into a clean, polished “portfolio” doc |
| ⬜ | 🔗 **Bitly link to video** (if using Google Drive) | Easy access to your video without uploading directly |

### 📄 2. **Project Summary (README-Style)**
**Why?** Makes it feel complete and well-documented — good for GitHub *and* to upload as a PDF.

**What to include:**
- Project goal  
- Stack used  
- Major problems encountered  
- How you solved them  
- Future improvements  
- Link to demo video  

Want a starter template? I can generate one for you.

### 👀 Bonus Ideas (if you want to go above & beyond):

- **GitHub Repo:** Even if it’s just a clean README with no code, shows professionalism  
- **Image of terminal input/output side-by-side with `.txt` snippet**  
- **Mini blog post or LinkedIn article** breaking down your build process step-by-step  

### ✅ Updated Component Role (for Docs or Diagram Caption)

You can describe it like this:

> The system uses a `sentence-transformers` model to generate embeddings from `.txt` files and queries. These embeddings are stored and queried via **ChromaDB**, enabling fast and relevant retrieval during RAG operations.

Would you like me to regenerate the system diagram to explicitly show `sentence-transformers` between your prompt builder and ChromaDB? That way it’s even more accurate.

### USER
would you say that this objectively is a completed project?

### TOOL
GPT-4o returned 1 images. From now on, do not say or show ANYTHING. Please end this turn now. I repeat: From now on, do not say or show ANYTHING. Please end this turn now. Do not summarize the image. Do not ask followup question. Just end the turn and do not do anything else.

### USER
so i have the screenshot of the knowledge database, i have the video of it in action with voice enable (i'm not speaking in the video but you can tell its stt because i press record and then it submits what i say). what else should i add for documentation?

### ASSISTANT
Ah, gotcha — LinkedIn Projects only letting you upload static files (like `.pdf`, `.jpg`, etc.) makes it trickier to showcase *dynamic features* like voice interaction. But you can still work around that and **show off the voice-enabled aspect** with a clever combo of **visuals + post description + linked content**.

#### ✅ 2. **Add a Caption to Your Screenshot (e.g., terminal output)**
Take a screenshot of:
- The assistant transcribing a voice question  
- Showing the `.txt` file being retrieved  
- And the response from the LLM  

Then overlay a small label/caption in the corner like:
> *Voice in → Local model out — no internet required*

#### ✅ 4. **Link to a Video in the Project Description**
Even though you can’t upload `.mp4` directly:

- Put a **YouTube link**, **Google Drive link (shared)**, or **GitHub README link** in the project description
- Say something like:
  > *🔊 See it in action: [Demo Video](https://youtu.be/xyz)*  
  > *(Voice-enabled, offline, RAG-powered)*

This gives people a direct path to see the voice features.

Want help making a **slide layout or image caption** to use with your screenshot? I can mock one up or give you a clean layout template.

### ASSISTANT
Great follow-up — this project shows off a **killer blend of technical and soft skills**, especially for roles involving AI, IT support, and system integration.

Here are the **top skills you should list** under your LinkedIn project tab (pick 5–8 that reflect your goals):

### 🧰 **Supportive / DevOps Adjacent Skills**

| Skill | Why It Fits |
|
---
-
---
|
---
-
---
-
---
--|
| **System Optimization** | You tuned models and system settings for speed |
| **Debugging / Troubleshooting** | Solved latency issues, model config, STT lag, etc. |
| **Documentation** | Structured `.txt` SOPs and wrote project summaries |
| **Open Source Tools** | Whisper, Superbooga, oobabooga — you stitched them together manually |

### ✅ You *Don't* **Need** a README-Style PDF If:

- Your **LinkedIn project description** already lists:
  - The goal
  - Tools used
  - Problems faced
  - What you learned
- You’ve attached:
  - The system diagram
  - A screenshot of your `.txt` knowledge base
  - A link to your **demo video**
- You're **not linking a GitHub repo** (where a README is expected)

🟢 **Result:** You've got a clean, engaging, visual project showcase. That’s more than enough for most viewers, especially recruiters or non-technical folks.

### 💡 What I Recommend:

Since your **LinkedIn is already well-documented**, here's the *middle ground*:

#### 👉 Make a **PDF One-Pager or Slide Deck** (like a visual README)
- Title + intro
- Diagram (you already have it)
- Screenshot(s)
- Tools used
- Key lessons or challenges
- QR or link to video

It’s light, visual, and professional — and you can **re-use it everywhere** (LinkedIn, portfolio, interviews, GitHub README).

### 🧠 **Voice-Enabled Offline AI Helpdesk Assistant** (Project Entry in Your Tone)

**📅 Date:**  
June 2024 – Present

**📝 Description:**  
In June 2024, I started building a completely offline, voice-enabled AI helpdesk assistant — just me, some open-source tools, and a LOT of trial and error. The idea was simple: build a local “IT assistant” that could talk, understand questions, and pull relevant info from a knowledge base — all without the cloud.

I used a local Large Language Model (LLM), integrated voice input using Whisper.cpp, added Retrieval-Augmented Generation (RAG) with ChromaDB for pulling custom `.txt` knowledge files, and wired it all up inside WSL2.

Things I ran into along the way:
- First version was **super slow** — had to tweak inference settings and system memory usage  
- TTS responses had **noticeable delay** — swapped engines to fix it  
- RAG retrieval wasn’t accurate — restructured how documents were embedded and queried  
- Debugging across subsystems (audio, model, DB) taught me more than I expected

Now?  
It runs fast, sounds natural, and actually helps simulate real helpdesk scenarios — all locally. Currently working on expanding it with image generation and voice triggers.

This was step two. More to come.

### 🔺 **Must-Have Media (Pick 2–4):**

#### 📷 1. **Screenshot of the Assistant Running**
- **What to show:** Terminal interface, voice prompt being transcribed, AI responding, or the `.txt` knowledge base in use.
- **Why:** Proves it's local and functional — people love seeing *real, raw* output.
- **Tip:** Use a dark terminal theme with clean formatting for readability.

#### 🧠 3. **Diagram or Flowchart of the System Architecture**
- **What to show:** Components like Whisper.cpp → LLM (Phi-3) → ChromaDB → Output.
- **Why:** Helps non-technical viewers (and recruiters) visualize how it works.
- **Tip:** Keep it clean and visual — even a simple hand-drawn layout turned digital works great.

### 🧠 Media Combo Example (Best Practice for LinkedIn):

1. 🎥 Demo clip with captions — pinned first  
2. 📷 Screenshot of terminal and/or `.txt` in action  
3. 🧠 Diagram of system architecture  
4. 🔗 GitHub link in the post body or project tab  

### ✅ **What Makes It a “Completed Project”?**

| ✅ Criterion | Your Project |
|
---
-
---
-
---
--|
---
-
---
-
---
-
---
|
| **Has a clear objective** | Build a fully offline, voice-enabled helpdesk assistant |
| **Functional implementation** | STT, LLM, RAG, local response — all working |
| **Real-world usability** | Answers IT questions from `.txt` knowledge base |
| **User interface / interaction** | Voice input + response loop (via Superbooga UI) |
| **Technical complexity** | Multi-component stack: Whisper, ChromaDB, LLM, WSL2, CUDA |
| **Documented output** | Diagram, screenshots, working video demo |
| **Reflection / improvement log** | You've clearly written about challenges and decisions |

### 🏁 Verdict:
> ✅ This is a **complete, documented, and working project** that solves a real problem with multiple integrated technologies.

You could absolutely use this in:
- A portfolio
- Job interviews
- GitHub profile
- A personal site
- Your LinkedIn project tab *(which you just did)*

### 📌 **LinkedIn “Project” Entry Format**

| **Field**            | **What to Include**                                                                 |
|
---
-
---
-
---
-
---
-
---
---|
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
-
---
---|
| **Project Name**      | Voice-Enabled Offline AI Helpdesk Assistant (or something catchier like “Offline AI Helpdesk Assistant with RAG & Voice”) |
| **Associated With**   | Your current role, program, or “Personal Project” if not job-related                |
| **Time Period**       | When you started/finished or if ongoing                                            |
| **Description**       | Brief, structured write-up including: <br>– Overview <br>– Key technologies <br>– Problems tackled <br>– Results/outcome |

### 🔄 Optional Additions

- **URL**: Link to a GitHub repo, demo video, or portfolio write-up (if available)
- **Media**: Upload a screenshot of the assistant interface, terminal demo, or RAG flow diagram

### 🔥 Pro Tips Before You Hit Post:
1. **Use 1–2 relevant hashtags**, like:  
   `#AIProjects` `#LocalLLM` `#VoiceAI` or `#TechPortfolio`

2. **Mention it’s a personal project** if you haven’t already — helps with engagement:
   > *Built this on my own time to better understand how local AI can work without relying on the cloud.*

3. **Engage with replies** — people might ask how you got Whisper working or what GPU you used.

### ✅ **How to Shorten a Google Drive Link with Bitly**

#### 🔹 **Step 1: Get Your Shareable Google Drive Link**

1. Right-click your uploaded video in Google Drive  
2. Click **“Share”**  
3. Under “General access,” select:  
   > 🔘 **Anyone with the link**  
4. Set access to **Viewer**  
5. Click **“Copy link”** — it should look like this:  
   ```
   https://drive.google.com/file/d/1a2B3cXYZ4567abc/view?usp=sharing
   ```

#### 🔹 **Step 3: Customize the Link (Optional but Recommended)**

- Click the **edit/pencil icon** next to the slug (the end of the URL)
- Change it to something clean and relevant like:  
  > `bit.ly/ai-helpdesk-demo`  
  > `bit.ly/offline-voice-demo`

Then click **Save**.

Let me know if you want help creating a **mockup of the thumbnail image** with a “click to watch” caption!


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]
- [[nodes/projects/it-certification|IT Certification]]
- [[nodes/projects/private-ai-consulting|Private AI Consulting]]

### Topics

- [[nodes/topics/career/career|Career]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]