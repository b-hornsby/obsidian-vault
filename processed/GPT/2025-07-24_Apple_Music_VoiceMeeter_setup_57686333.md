---
source: GPT
date: 2025-07-24
category: homelab
id: 57686333
linked_nodes: ['nodes/people/bryan.md']
---
# Apple Music VoiceMeeter setup

### USER
how do i get apple music to be routed in voicemeter banana so it is playing through the cable a output on windows 11?

### USER
what are the best audio settings/filters for a blue yeti microphone on obs? i have 0 foam panels so keep that in mind as well

### ASSISTANT
Perfect — thanks for clarifying! If you want **Apple Music audio to be isolated** and routed **only through Cable A**, while keeping all other system audio separate, here’s the **cleanest and most reliable setup** on **Windows 11** using **VoiceMeeter Banana**:

## 🧩 Step-by-Step Setup

### ✅ 2. **Route Apple Music (only) through Cable A**
Now isolate Apple Music and force it through **CABLE A Input (VB-Audio Cable A)**:

#### Option A – Microsoft Store version of Apple Music:
- Open `Settings` → `System` → `Sound` → `Advanced` → `Volume Mixer`
- Find **Apple Music** under “Apps”
- Set its **Output** to:  
  ➤ `CABLE-A Input (VB-Audio Cable A)`

> This isolates Apple Music to Cable A only.

#### Option B – iTunes Desktop App:
Same process:
- Launch iTunes
- Then go to **Settings → System → Sound → Volume Mixer**
- Find **iTunes** and set its Output to `CABLE-A Input`

#### Option C – Apple Music in a Web Browser:
- Same as above – launch the browser (Chrome, Edge, etc.)
- Go to Volume Mixer
- Route **that browser app** to `CABLE-A Input`

### ✅ 4. (Optional) Mute Apple Music from General Outputs
If for any reason Apple Music leaks into your default system output:
- Double-check that Apple Music’s output is **not set to Default** in Volume Mixer
- Confirm that it's exclusively set to `CABLE-A Input`

Let me know:
- What you're outputting to (headphones, OBS, Discord, etc.)
- Whether you want to *hear* Apple Music yourself or just route it somewhere

And I can help fine-tune your routing buttons (`A1/B1/etc.`)!

### USER
{'asset_pointer': 'file-service://file-McTcfYNud6PYMRemQTk5bJ', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 359, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 26273, 'width': 1039}i tried that and apple music still keeps going through voicemeeter VAIO

### USER
i want apple music to be isolated to clarify

### ASSISTANT
Thanks for the screenshot — it clears things up.

You're doing the **right thing** by setting **Apple Music's output to `CABLE-A Input (VB-Audio Cable A)`**, but it looks like Windows is still duplicating it or overriding it.

Let’s fix that cleanly:

### 2. ✅ Set Windows System Default Output to **VoiceMeeter VAIO**
If you haven’t yet:
- Go to `Settings → System → Sound → Output`
- Set your **Default Output** to:  
  ➤ `VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)`

**Do not** set CABLE-A as the default system output. That would send **everything** to it.

### 4. 🔄 Re-check Volume Mixer
After restart:
- Open `Settings → Sound → Volume Mixer`
- Ensure only **one Apple Music instance** is showing
- Make sure it's set to:  
  ➤ `CABLE-A Input (VB-Audio Cable A)`

## 🧠 Bonus Tip:
If you're still getting Apple Music on **both** VAIO and Cable A even after this:

- Try **reinstalling Apple Music as the desktop (iTunes-style) version** instead of the Microsoft Store UWP version.
  - UWP apps sometimes have unpredictable behavior with audio routing due to their sandboxing.

## 🎙️ Best OBS Filters for a Blue Yeti (No Foam Panels)

Here’s the **ideal filter stack**, in order, with recommended settings and explanations:

### ✅ 2. **Noise Gate**
**Purpose:** Stops the mic from picking up sound when you’re not speaking (like keyboard/mouse noise or room echo).

- **Open Threshold:** `-30 dB` (starts picking up your voice)
- **Close Threshold:** `-35 dB` (stops picking up quiet room noise)
- **Attack Time:** `10 ms`
- **Hold Time:** `200 ms`
- **Release Time:** `150 ms`

🎧 **Tip:** Speak normally and monitor the meter to dial these in. Tweak based on your mic distance and loudness.

### ✅ 4. **Limiter**
**Purpose:** Prevents clipping/distortion if you shout or get loud.

- **Threshold:** `-3 dB`
- **Release:** `60 ms`

🔒 This is your safety net.

## 🎯 Bonus: Mic Positioning Tips (No Foam Panels)

- **Set mic to “Cardioid” mode** (the heart symbol on the back) to reduce pickup from sides/back
- **Use a boom arm** (if possible) to isolate from desk vibrations
- **Distance:** Keep your mouth **6–10 inches** away
- **Angle it off-axis slightly** (not directly in front of your mouth) to reduce plosives and breath noise
- **Add a pop filter or foam windscreen** — cheap and helps a lot

Want me to walk you through how to install and use the **ReaEQ** plugin inside OBS step-by-step? Or do a sample export of a config file? Just let me know.

### ASSISTANT
To route **Apple Music** through **VoiceMeeter Banana** and have it output through **Cable A** (usually **VB-Audio Cable A / CABLE Input (VB-Audio Cable A)**), you need to configure both VoiceMeeter and Windows properly.

Here’s a step-by-step walkthrough:

### ✅ 2. **Set Cable A as your Windows Default Playback Device**
This routes all system audio (including Apple Music) through Cable A.

#### How:
- Right-click the **speaker icon** in your system tray → `Sound settings`
- Scroll to **"Output"** → Click **“Choose where to play sound”**
- Set output to **"CABLE-A Input (VB-Audio Cable A)"**

### ✅ 4. **Route the Cable A input to whatever output you want**
Let’s say you want to hear it through your speakers or headphones connected to **A1**:

- Under the **"Hardware Input"** that shows **CABLE A**, press the buttons:
  - **A1** (to send it to your main output, like headphones)
  - Or **B1/B2** if you're routing it to a virtual output

### ✅ Optional (per-app routing)
If you only want **Apple Music** to go through Cable A but keep other apps on a different output:

- Press **Win + I → System → Sound → Advanced → App volume and device preferences**
- Set **Apple Music (iTunes or Apple Music app)** output to **CABLE-A Input**
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]