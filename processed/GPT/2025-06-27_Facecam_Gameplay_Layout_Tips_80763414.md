---
id: 115899
source: GPT
date: 2025-06-27
tags: ['tiktok-streaming', 'facecam-layout', 'obs', 'streaming-overlay']
category: streaming
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan wanted to set up a TikTok stream layout with facecam on top and full-screen gameplay on the bottom.
---
# Facecam Gameplay Layout Tips

### USER
{'asset_pointer': 'file-service://file-Byn3SxjAtHGfSr175eknds', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1536, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 313611, 'width': 708}I want it to kind of look like this with the gameplay full screen at the bottom

### ASSISTANT
Perfect — this style is very clean and effective for TikTok vertical streams. The top is a tight facecam crop, and the **bottom is true full-screen gameplay** — no black bars, no overlays, and it fills the entire screen width. Here's exactly how to replicate this layout using **TikTok LIVE Studio**:

### 🔧 HOW TO SET IT UP IN TIKTOK LIVE STUDIO:

#### 1. **Canvas Setup**
- Set your **canvas resolution** to **1080x1920** (Vertical/9:16)  
  - *Settings > Video > Canvas Resolution*

#### 3. **Add Facecam (Top Crop Style)**
- Add your **Camera Source**.
- Resize it to a **horizontal rectangle** (like a webcam strip).
- Drag it to the **top of the canvas**, just like in the example.
- Use cropping (`Alt` + drag) to remove background/shoulders so it's focused on your face.
- For bonus polish, add a **rounded mask**:
  - Right-click > Filters > **Image Mask/Blend**
  - Use a rectangle mask PNG if you want soft edges

### 🧪 Optional: OBS Alternative
If TikTok LIVE Studio doesn’t give you enough control:
- Use **OBS** with the **Vertical Plugin** (adds 1080x1920 canvas)
- Set up the same way, then **stream to TikTok via Stream Key** (can use platforms like Streamlabs or Loola for that)

Want help making a **custom overlay template** or mask to match this look perfectly? I can design one for you or show you how to build it fast.

### USER
{'asset_pointer': 'file-service://file-QVPHUDBYSTi7MFJ7bQiNVf', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1536, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 3469124, 'width': 1152}If I wanted my stream on TikTok to be facecam up top and the bottom just be full screen gameplay (no bottom bar or anything, kind of like this), how would I do that? I’m not a big fan of it being zoomed in all the way the way it is that’s why I ask

### ASSISTANT
You're on the right track using **TikTok LIVE Studio**, and it looks like you're using a vertical layout optimized for mobile. To achieve your desired layout — **facecam at the top, full-screen gameplay underneath without zoom or black bars** — follow these steps:

### 🔧 STEP-BY-STEP SETUP:

#### 1. **Set Up Vertical Canvas**
- In TikTok LIVE Studio:
  - Go to the **Scene layout**
  - Set the **canvas resolution** to **1080x1920 (9:16)** — this keeps it vertical like TikTok expects.

#### 2. **Add Your Gameplay Source**
- Add a **Display Capture** or **Game Capture**.
- Resize it to fill the **bottom 3/4 of the canvas** (you can use snapping or hold **Shift** to move freely).
- **DON’T scale it up too much** — you want the full game window visible without cutting anything off.
  - If it's not filling vertically, try **stretching** it slightly, or increase your game’s resolution (e.g., run it at 1080p instead of 720p).

#### 3. **Add Your Facecam**
- Add your **Camera Source** on top.
- Resize it to sit in the **upper portion** of the canvas.
- Try placing it in a **clean corner or centered bar**, like in your screenshot.
- Use a **mask or rounded border** if you want a polished look (you can right-click the camera source → **Filters** → **Image Mask/Blend**).

#### 4. **Tweak Layer Order**
- Make sure your gameplay is underneath the camera in the **scene list**.

#### 5. **Remove Bottom Bar**
- If you’re seeing a bottom bar (like app icons, taskbar, or overlays), either:
  - Use **Game Capture** instead of Display Capture.
  - Or, crop it out: hold **Alt** while dragging the crop edge in TikTok LIVE Studio.

Would you like a custom template overlay (e.g., clear box for cam, game area borders) to use for a cleaner layout? I can help design one for you.