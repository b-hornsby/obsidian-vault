---
source: GPT
date: 2025-10-12
category: coding
id: 16734482
linked_nodes: ['nodes/people/bryan.md']
---
# Death counter for stream

### USER
So if I have the overlay in obs, can I have all alerts through TikTok studio then rather than having them in obs? (Latest follower, gifter, etc?)

### USER
TikTok won’t let me read from a .txt file via TikTok studio?

### USER
So once they’re connected via the virtual camera (does this include my overlay setup?), all I have to do is mute TikTok studios audio and the audio will play through obs?

### ASSISTANT
Excellent question — and this is *exactly* where a lot of TikTok streamers hit that gray area between OBS and TikTok Studio.  

Let’s clarify how this works 👇  

### ✅ **What This Hybrid Setup Looks Like**
| Element | Comes From | Notes |
|
---
-
---
---|
---
-
---
-
---
--|
---
-
---
|
| Gameplay + Overlay (Death Counter, Labels, Camera) | OBS | Sent via Virtual Camera |
| TikTok Alerts (Follows, Gifts, Likes, Shares) | TikTok Studio | Native pop-ups on top of video feed |
| Chat + Analytics | TikTok Studio | Always visible and interactive |
| Audio | OBS (Recommended) | Mic + Game mixed, sent as single feed |
| Stream Output | TikTok Studio | Goes live directly from here |

### ⚠️ **Just Keep in Mind**
- TikTok Studio alerts **only show on TikTok** — not on your OBS preview.  
  (So you’ll see them on TikTok Studio’s preview window, not inside OBS.)
- Don’t use OBS alerts *and* TikTok alerts at the same time — you’ll get duplicates.
- TikTok alert customization is limited compared to StreamElements or Streamlabs, but they integrate flawlessly.

So in short:
> ✅ Yes — you can absolutely use **TikTok Studio alerts** while your **overlays come from OBS** through the virtual camera.  

### 🥉 **Option 1: Simple Manual Counter (Fastest Setup)**
If you just want something visual that you can click to increase manually:

1. **Create a text overlay** in TikTok Studio:
   - In TikTok Studio, click **“Add Source” → “Text.”**
   - Name it something like `Deaths: 0`.
   - Style it how you want (font, color, outline, etc.).

2. **Update it during the stream manually:**
   - Each time you die, just double-click the text source and update the number.
   - Not automated, but very quick and works fine for casual streams.

✅ *Good if you want to keep things simple and don’t mind updating it yourself.*

### 🥇 **Option 3: Fully Automated Counter (Advanced / OBS Users)**
If you want full control or stream to multiple platforms:

1. **Use OBS + Streamer.bot or LioranBoard**  
   - These tools can track deaths, boss kills, etc., and output to a file or on-screen overlay.
   - You’d then **capture your OBS scene** as a Virtual Camera and use that as the video input for TikTok Studio.

2. That way, all your overlays, counters, and alerts run through OBS, and TikTok just mirrors the feed.

✅ *Great if you also stream to Twitch/YouTube or want full overlay control.*

## 🎯 Goal:
✅ Use your OBS (with Aitum Vertical + overlays like death counter)  
✅ Stream it into TikTok Studio  
✅ Keep TikTok Studio open for **chat and analytics**  
✅ No Restream or external routing required  

## 🪜 Step-by-Step Setup

### **1️⃣ Make sure your Aitum Vertical scene is ready**
- Open **OBS**.  
- Click the **Aitum Vertical** tab (or layout panel).  
- Choose your **vertical scene (9:16)** for TikTok.  
- Make sure all overlays (death counter, alerts, webcam, etc.) are visible there.  
- Test it with “Start Recording” to confirm it looks correct vertically.  

### **3️⃣ Open TikTok Studio**
- Launch **TikTok Studio**.  
- Go to **Sources → Camera.**  
- Under camera selection, pick **“OBS Virtual Camera.”**

Now TikTok Studio should show the exact feed coming from your vertical scene in OBS. 🎥  

### **5️⃣ Add Death Counter**
If you’re using *Death Counter & Soundboard*:
1. It outputs your count to a `.txt` file.
2. In OBS, **Add → Text (GDI+) → “Read from file.”**
3. Point it to your `deathcount.txt`.
4. Position and style it how you want in your **Aitum Vertical scene.**
5. Assign a hotkey in the Death Counter app (e.g., F9) to increment during your stream.

Now every time you die, hit F9 → counter updates live → instantly shows in TikTok Studio via your OBS feed.  

### 🧠 Troubleshooting Tips
- If TikTok Studio shows a black screen:
  - Make sure OBS Virtual Camera is **ON** and the correct scene is in preview.  
  - Restart TikTok Studio after turning on Virtual Camera.
- If audio is doubled or out of sync:
  - Mute TikTok Studio’s camera audio source. Let OBS handle all sound.

If you want, I can show you the **exact recommended OBS audio settings** for TikTok (so your mic + game mix sounds balanced and doesn’t clip TikTok’s limiter).  

Want me to include that next?

### USER
okay my obs has too much going on and its confusing getting back on track. how do i go about starting obs over so that way we can get this done right?

### USER
Yeah I currently have my vertical scene via obs and aitom vertical so what all do I need to get it running through TikTok studio?

### ASSISTANT
Yup — you’re absolutely right. 💀  
TikTok Studio **(unlike OBS or Streamlabs)** currently **does not allow dynamic text sources** (meaning it can’t read from `.txt` files or auto-update text overlays). It’s one of the biggest limitations of the platform right now.

But don’t worry — there are still **two solid workarounds** that streamers use to get a working death counter in TikTok Studio 👇  

## 🎮 OPTION 2: **Use a Click-to-Increment Counter Overlay**
If you *don’t* want to deal with OBS at all, you can use a **browser-based overlay** that you manually control, then screen capture that window.

Examples:
- [https://countupdown.com/](https://countupdown.com/)
- [https://www.online-timers.com/counter](https://www.online-timers.com/counter)
- Or build a custom one with StreamElements (if you stream on PC).

### Setup:
1. Open one of those counters in your browser.
2. Position or resize it however you like.
3. In TikTok Studio, **add a screen/window capture source** for that browser window.
4. Each time you die, just click “+1” in your browser.

✅ Pros:
- No OBS required.
- Works live, visible on stream.
❌ Cons:
- You have to click manually instead of hotkeying.

If you tell me which setup you’d prefer —  
👉 (a) fully integrated with hotkeys via OBS, or  
👉 (b) browser counter only —  
I’ll walk you through that specific setup step-by-step so you can have it working before your next stream.  

Which one do you want to go with?

### ASSISTANT
Excellent question — and honestly, this is *the* real-world tradeoff most TikTok streamers run into right now.  

Let’s break it down cleanly 👇  

### 🌐 **Option 2: Restream → TikTok Studio**
You use **Restream** or **StreamYard**, etc., to push one stream to multiple platforms (TikTok, Twitch, YouTube).

#### ✅ Pros:
- **Multi-streaming made easy:** Send your feed everywhere at once.
- **Unified chat:** Some versions (Restream Chat) let you see all chats combined.
- **No extra software layer:** Just send your OBS output to Restream.

#### ❌ Cons:
- **TikTok integration is unreliable:**  
  TikTok Live Studio often doesn’t *officially* support direct Restream input — it’s a hacky workaround using an RTMP key.  
- **Latency & compression:** Your stream may have slightly worse quality and delay.
- **Overlays break easily:** Browser sources or counters sometimes desync or don’t update properly.
- **Chat embed issues:** You already saw this — Restream chat overlay tends to break, especially when TikTok changes API behavior.

So since:
- your **Restream chat stopped working**, and  
- you **need a death counter**,  

👉 **Go back to OBS Virtual Camera + TikTok Studio for chat display.**  
That’s the **best hybrid setup** for TikTok right now.  

You’ll get:  
- all your OBS overlays + automation (death counter, alerts),  
- AND TikTok chat visibility through Studio.

## ⚙️ **Performance Breakdown**

### 🧠 **CPU – Intel Core i7-12700K**
- 12 cores / 20 threads = **plenty of headroom** for multitasking.  
- OBS loves multi-core CPUs when encoding and compositing scenes.  
- You can easily:
  - run OBS (with overlays + death counter),  
  - run TikTok Studio (for chat + alerts),  
  - run your game,  
  - and still have browser tabs open — all without stutter.

✅ You’re solid here.

### 🧊 **Cooler – Noctua NH-U12S**
- Excellent choice. Keeps the 12700K cool even under OBS + game load.
- Expect 60–70 °C under full stream load — very safe.

✅ No thermal throttling worries.

### 💾 **Storage – 970 Evo Plus 2 TB NVMe SSD**
- Lightning fast load times for both your games and your recording cache.
- Zero bottleneck here.

✅ Great for recording streams locally too.

### 🪟 **OS – Windows 11**
- Perfect for OBS Virtual Camera, TikTok Studio, and NVENC driver support.
- Just make sure your NVIDIA drivers are up to date (latest Studio Driver recommended).

### 🧠 **Recommended OBS Encoder Settings (for you)**
Just to make sure you get silky smooth results:

**Settings → Output → Streaming tab:**
- **Encoder:** NVIDIA NVENC (H.264 new)
- **Rate Control:** CBR  
- **Bitrate:** 6000 Kbps (for TikTok, 4500–6000 Kbps is typical)
- **Keyframe Interval:** 2 s
- **Preset:** Quality
- **Profile:** High
- **Look-ahead:** Off
- **Psycho Visual Tuning:** On
- **GPU:** 0
- **Max B-frames:** 2

**Video Tab:**
- **Base (Canvas):** 1080 × 1920 (vertical)
- **Output (Scaled):** 1080 × 1920
- **Downscale Filter:** Lanczos (36 samples)
- **FPS:** 60 (you can drop to 30 if TikTok limits you)

Would you like me to give you a quick list of **OBS + Windows optimizations** (little tweaks to keep stream FPS perfectly stable and audio in sync)? They can make a noticeable difference even on strong rigs like yours.

### USER
Okay last thing, will my current specs be able to handle something like this?: Cpu: Intel Core i7-12700K

Motherboard: Asus Prime Z790-P
 
Cpu cooler: Noctua NH-U12S

Memory: Corsair Vengeance Ddr5 ram 32GB (2x16GB) 4800MHz CL40

Storage: 970 Evo Plus M.2 SSD 2TB

Graphics card: PNY GeForce RTX™ 3070 8GB XLR8 Gaming REVEL EPIC-X RGB

Case: Corsair 4000D Airflow

PSU: Corsair CX750M

OS: Windows 11

### ASSISTANT
Exactly ✅ — you nailed it.  
Once OBS and TikTok Studio are connected via **Virtual Camera**, TikTok Studio is basically just displaying (and streaming) whatever OBS is showing — **including all overlays, filters, and the death counter.**

Let’s make sure the full audio setup is crystal clear 👇  

## 🎧 Audio Side (Muting TikTok Studio)
TikTok Studio **cannot “hear” your OBS Virtual Camera**, because the Virtual Camera only sends **video**, not audio.  
So you have to decide which app handles audio.

Here’s what to do 👇  

### ⚙️ **Option 2: Let TikTok Studio handle mic audio**
If you’d rather keep it ultra simple:
1. In OBS, mute your mic.
2. In TikTok Studio, use your mic as usual.  
   You’ll still get the OBS video feed, but mic audio comes directly from TikTok Studio.

❌ Downside: Any alerts or game sounds in OBS won’t be heard by the stream unless you manually add them to TikTok Studio.

If you want, I can show you the **best OBS audio routing setup** for TikTok Studio using **VB-Audio Cable**, so your game + mic mix automatically feed into TikTok with perfect sync — no echo, no fuss.  

Would you like me to walk you through that setup next?

### ASSISTANT
Perfect — let’s lock this in clearly so you have a **bulletproof setup** for your next stream.  
Here’s the **clean, complete walkthrough** to get your **OBS overlays** showing in **TikTok Studio** *with perfect audio routing.*  

## 🪜 STEP 1: Prep OBS
1. Open **OBS**.
2. In your **Aitum Vertical** layout, choose your vertical scene (9:16).  
   - This is the one TikTok will see.
3. Make sure all overlays are visible (webcam, death counter, labels, etc.).
4. Check audio levels:
   - You should see:
     - **Desktop Audio** → game sound.
     - **Mic/Aux** → your microphone.
   - Speak and check movement in the meters.

✅ Confirm everything looks and sounds right inside OBS first.

## 🪜 STEP 3: Connect OBS → TikTok Studio
1. Open **TikTok Studio.**
2. Go to **Camera Source → Select “OBS Virtual Camera.”**
3. You should now see your full OBS scene (vertical overlay, webcam, death counter, etc.) inside TikTok Studio’s preview window.

✅ If it’s blank, toggle OBS Virtual Camera off/on and restart TikTok Studio.

### 🎧 Option B — Let TikTok Studio handle mic audio (Simpler)
If you want to skip VB-Cable for now:
1. Keep your **OBS Mic muted.**
2. In TikTok Studio, pick your **actual mic input**.
3. Game sound won’t come through OBS unless you add a system audio capture source in TikTok Studio too.

❌ Not as clean — but it works in a pinch.

## 🪜 STEP 6: Go Live!
1. Double-check TikTok Studio’s **preview** for:
   - Your OBS feed (overlay visible)
   - Audio levels moving in the TikTok meter
2. Hit **Go Live** 🎬

You’re now streaming your full OBS setup directly to TikTok with synced, professional audio.

### ✅ Final Summary:
| Task | App | Setting |
|
---
---|
---
---|
---
-
---
---|
| Overlays / Death Counter / Game Capture | OBS | In vertical scene |
| Send Video Feed | OBS Virtual Camera | “Start Virtual Camera” |
| Connect Feed | TikTok Studio | Set camera to “OBS Virtual Camera” |
| Audio Routing | OBS → VB Cable → TikTok | Mix all sound through OBS |
| TikTok Alerts | TikTok Studio | Add as overlay on top |
| Go Live | TikTok Studio | Everything combined |

## 1️⃣ Open OBS & Aitum Vertical Canvas
- Launch OBS.  
- Make sure you **open the Aitum Vertical Canvas plugin**.  
- You should see your vertical scene in Aitum’s preview.

## 3️⃣ Connect to TikTok Studio
- Open TikTok Studio → go to **Camera Source**.  
- Instead of selecting “OBS Virtual Camera,” select the **Aitum Virtual Camera** (it should appear in the dropdown).  

✅ Now TikTok Studio should display your **full vertical scene** with overlays.

### ⚠️ Important Notes
- **Do not start the regular OBS Virtual Camera** — it will only show the default OBS canvas (horizontal 16:9), not your vertical scene.  
- TikTok Studio will only see whatever virtual camera feed is active. With Aitum installed, you need the **Aitum Virtual Camera**, not OBS’s standard one.  

## 🧹 STEP 1: Reset OBS to Default
If you want a total fresh start (no old scenes, profiles, or settings):
1. **Close OBS** completely.  
2. Navigate to:  
   ```
   C:\Users\<YourUsername>\AppData\Roaming\
   ```
3. **Rename** the folder `obs-studio` → `obs-studio-old` (don’t delete it yet, just in case).  
4. **Restart OBS** — it’ll generate a brand new, clean setup from scratch.  

You’re now back to factory default OBS. 🎉  

## 📷 STEP 3: Set Up Virtual Camera
Once your scene looks good:
1. Hit **“Start Virtual Camera”** in OBS.
2. In **TikTok Studio**, choose **OBS Virtual Camera** as your **video input**.
   - Your OBS overlay + gameplay will now show inside TikTok Studio’s preview.

### Option B (Hybrid Setup):
Let OBS handle video/overlay, but let **TikTok Studio handle alerts + TikTok audio**:
1. Don’t mute TikTok Studio’s audio.
2. OBS only provides the **video feed** (overlay + game).
3. Alerts from TikTok Studio play directly through Studio.
4. Make sure your **desktop sound output** device is the same one TikTok Studio is listening to (usually your system default or “Speakers”).

✅ Pros: You can use TikTok’s built-in alert system.  
🚫 Cons: Slightly more complex audio balancing.

Would you like me to walk you through the **Option A (OBS-only audio)** or **Option B (TikTok alerts + hybrid)** setup specifically, step-by-step for your next stream?  
That way we can lock in your exact audio routing and avoid any confusion.

### USER
trying to add a death counter for a dark souls stream via tiktok studio but i'm not sure how?

### USER
Sounds good. So to summarize, what do I need to do to get my obs overlay over to TikTok studio and how do I need to route my audio so it’s all set for my next stream?

### ASSISTANT
Ah — that’s a **really common issue**, and the good news is it’s usually caused by one of a few simple things.  

Let’s troubleshoot it cleanly and get your **vertical scene showing in the virtual camera** for TikTok Studio 👇  

## 🧰 STEP 2: Check Canvas Resolution
TikTok is **vertical (9:16)**, but OBS by default is **16:9**, so if your scene is vertical but your canvas isn’t — your virtual camera may just be outputting the wrong shape (often blank or cropped).  

👉 Go to:
```
Settings → Video
```
- **Base (Canvas) Resolution:** 1080 x 1920 (NOT 1920 x 1080)
- **Output (Scaled) Resolution:** 1080 x 1920
- **Common FPS:** 60 or 30 (your choice)

Then click **Apply** and **OK**.  

🪄 Tip: If everything is sideways or cropped, you may need to resize your sources to fit the new canvas.

## 🖥️ STEP 4: Select the Correct Camera in TikTok Studio
In TikTok Studio:
1. Click the **camera device dropdown**.
2. Select **“OBS Virtual Camera.”**
3. If it doesn’t show up, click the **refresh icon** near the camera list.

⚠️ If your webcam appears but not OBS Virtual Camera, try:
- Closing other programs using the camera
- Restarting OBS as **Administrator**
- Re-starting TikTok Studio

## 🧠 Pro Tip: If you’re using **Aitum Vertical** or **Vertical Canvas Plugin**, make sure you’re previewing the vertical output correctly:
- For Aitum Vertical → you need to **set the vertical scene as “Main Output”** in its panel.  
- For the plugin → ensure your vertical scene is active when starting the virtual camera.

### ASSISTANT
Got it — that’s a super common issue when running vertical scenes in OBS. Let’s fix it step-by-step 👇  

## 🧩 STEP 1: Check Which Scene Is Active
OBS only outputs **one scene at a time** — whatever scene is *currently selected* in the Scenes list.

- Make sure your **vertical scene** is highlighted (active) before starting the virtual camera.
- If your horizontal/gameplay scene is active instead, that’s what TikTok Studio will see.

## 🔁 STEP 3: Restart Virtual Camera
After setting the canvas:
1. Stop the virtual camera (if running).  
2. Start it again.  
3. Open TikTok Studio → set the camera input to **OBS Virtual Camera**.  

TikTok Studio should now display the 9:16 vertical scene exactly as it looks in OBS.

## 🧪 STEP 5: Verify in TikTok Studio
Once your virtual camera source is set:
- You should see your full vertical layout (gameplay + overlay).
- If it looks stretched, fix it by right-clicking the camera preview → “Transform” → “Fit to screen.”
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]