---
source: GPT
date: 2025-05-11
category: ai-tools
id: 31815713
linked_nodes: ['nodes/people/bryan.md']
---
# Create Nobara Bootable USB

### USER
How do I enable the proper settings for this on an asus motherboard

### ASSISTANT
To create a **bootable USB drive for Nobara Linux** (a Fedora-based distro optimized for gaming) and **test it without installing**, follow this step-by-step guide tailored to your **Intel i7-12700K + RTX 3070** build.

### ✅ 2. **Flash the ISO to USB (Bootable Drive)**
Use **[Rufus](https://rufus.ie/)** on Windows:

1. Plug in a **16GB+ USB stick**.
2. Open Rufus.
3. Select your USB.
4. Click **"SELECT"** and choose the Nobara ISO.
5. Leave partition scheme as **GPT** and target system as **UEFI**.
6. Hit **START**.
7. If prompted about **ISO or DD mode**, choose **ISO mode**.

### ✅ 4. **Boot Into Nobara Live Mode**
1. Plug in your USB.
2. Reboot and spam the boot key (**F12**, **F11**, or **ESC** depending on your motherboard).
3. Choose your USB drive.
4. Select **"Start Nobara Linux (Live)"**.

You’ll boot into the full desktop environment **without installing**.

### ⚠️ Optional Troubleshooting
If you get a black screen:
- Try adding the boot parameter `nomodeset` (press `e` in GRUB and add it to the `linux` line).
- Make sure you're using the **NVIDIA ISO**, not the default one.

### **Secure Boot Settings for Nobara + NVIDIA**

From your screenshot:

- **OS Type**: Currently set to **Windows UEFI mode** — **change this to**:  
  **→ Other OS**

- **Secure Boot Mode**: Currently set to **Custom** — that’s fine, but it'll disappear once Secure Boot is disabled.

### How to Save and Exit:
- Press **F10** to save and exit the BIOS.
- Then boot from your USB stick (use **F8** or **F12** during boot to select the device).

You should now be able to run **Nobara Live Mode** without NVIDIA-related boot issues.

Want help checking if the NVIDIA driver loads properly once you're in?

### ASSISTANT
Thanks — that screen shows you're stuck in the **GRUB rescue shell**, meaning the bootloader didn’t find the actual bootable system files on the Nobara USB.

This often happens due to:
1. A bad USB flash process.
2. BIOS/UEFI boot mismatch.
3. Corrupted ISO or incompatible ISO mode.

#### ✅ 2. **Double-Check BIOS Boot Settings**
In your ASUS BIOS:
- `Boot > CSM`: **Disabled**
- `Boot > Secure Boot > OS Type`: **Other OS**
- Boot from: **UEFI: [Your USB Drive Name]**, not the non-UEFI one

(If you see 2 options for your USB in the boot menu, always pick the one prefixed with **UEFI**.)

Let me know if you'd like help verifying the ISO file or going through the Rufus setup step-by-step.

### USER
I’ll send a picture of what I see on the secure boot page

### USER
{'asset_pointer': 'file-service://file-VaPNSeBeFikLAJ1R7maRSn', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1536, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 2441782, 'width': 1152}

### ASSISTANT
Good question — **no manual deletion needed**.

### If you're using **Rufus** or **Etcher**, they'll:
- **Automatically erase** the USB drive,
- **Repartition it correctly**, and
- **Write a fresh bootable image**.

That means:
- You can just plug in the USB,
- Reflash it using Rufus or Etcher,
- And boot again — no cleanup required.

Once you have that ISO, flash it with **Rufus** (or **BalenaEtcher** if you prefer simpler tools), boot into Live mode, and you’re good to test.

Would you like a command to verify the ISO checksum after download for safety?

### USER
{'asset_pointer': 'file-service://file-WGc39eiyVuQkbai6bnBSVE', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1536, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 2739611, 'width': 1152}

### ASSISTANT
Exactly — you got it.

✅ If you want **KDE** (instead of GNOME), download:  
**`Nobara-41-KDE-Nvidia-2025-02-20.iso`**

### Quick Summary of Options:
| ISO Filename | Desktop Environment | NVIDIA Drivers Included? | Good for RTX 3070? |
|
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
--|
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
--|
| `Nobara-41-Official-Nvidia...` | GNOME (default) | ✅ Yes | ✅ Yes |
| `Nobara-41-KDE-Nvidia...`      | KDE Plasma        | ✅ Yes | ✅ Yes |
| `Nobara-41-XFCE-Nvidia...`     | XFCE (lightweight) | ✅ Yes | ✅ Yes |

### ✅ Step-by-Step: BIOS Settings for ASUS Motherboards

#### 1. **Enter BIOS**
- On boot, press **Del** or **F2** repeatedly until the BIOS menu opens.

#### 2. **Switch to Advanced Mode**
- Press **F7** to enter **Advanced Mode** if you’re in the simplified "EZ Mode".

### ✅ Save and Boot
- Plug in your **Nobara USB drive**.
- Press **F8** or **F10** to open the **Boot Menu** (can vary by board).
- Select the **UEFI USB drive** (e.g., `UEFI: SanDisk Cruzer`).
- Boot into **Live Mode**.
---
### USER
how do i make a bootable drive for nobara on a intel i7-12700k and rtx 3070 build so that way its compatible. im not trying to install that os, i just want to be able to try and see if i like it


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]