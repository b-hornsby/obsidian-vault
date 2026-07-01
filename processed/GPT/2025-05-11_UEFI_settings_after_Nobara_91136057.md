---
source: GPT
date: 2025-05-11
category: homelab
id: 91136057
linked_nodes: ['nodes/people/bryan.md']
---
# UEFI settings after Nobara

### USER
How do I do that on my asus motherboard

### USER
{'asset_pointer': 'file-service://file-64SKZXtDcjwyqjY62WK5cL', 'content_type': 'image_asset_pointer', 'fovea': None, 'height': 1152, 'metadata': {'asset_pointer_link': None, 'container_pixel_height': None, 'container_pixel_width': None, 'dalle': None, 'emu_omit_glimpse_image': None, 'emu_patches_override': None, 'generation': None, 'gizmo': None, 'is_no_auth_placeholder': None, 'lpe_delta_encoding_channel': None, 'lpe_keep_patch_ijhw': None, 'sanitized': True, 'watermarked_asset_pointer': None}, 'size_bytes': 2856247, 'width': 1536}

### USER
So if I primarily use windows and I just wanted to make that bootable drive just to see what nobara was like, do I need to change anything back since I don’t plan on using Linux just yet?

### USER
Do I need to change those uefi and other settings back after that whole nobara thing?

### ASSISTANT
Here’s how to check and change those settings on an **ASUS motherboard**—most ASUS boards use the same UEFI BIOS layout, so this should apply in general:

### **Once You're in BIOS (EZ Mode):**

#### 1. **Switch to Advanced Mode**
- Press **F7** to enter **Advanced Mode** (if you're not already there)

### **Save and Exit**
- Press **F10**, then choose **Yes** to save and reboot

### **Steps to Re-enable Secure Boot Properly:**

1. **Secure Boot Mode** (what you see now):
   - Set it to **Standard** instead of **Custom**  
     (Custom is mainly for advanced key management; Standard loads factory default Microsoft keys)

2. If it gives you an error about missing keys:
   - Go to **Key Management** just below
   - Choose **Install Default Secure Boot Keys**

3. **OS Type**:
   - Make sure this is set to **Windows UEFI mode** (which it is now—good)

4. Press **F10** to save and exit the BIOS

### **What you may have changed (and what to do now):**

1. **Secure Boot** –  
   - **If you disabled it**:  
     - You can **turn it back on**, especially if you use BitLocker, Windows Hello, or other security features.
     - Most modern Windows setups expect Secure Boot to be on.
   - **If it was already off**: no need to change anything.

2. **TPM (Trusted Platform Module)** –  
   - Should stay **enabled** for Windows 11. Leave it on.

3. **Boot Mode (UEFI vs Legacy/CSM)** –  
   - If you changed to **Legacy/CSM**:  
     - Change back to **UEFI** mode. Windows 10/11 uses UEFI.
   - If you stayed on UEFI: you're good.

4. **Boot Order** –  
   - If you changed boot priority to USB or something else, feel free to move Windows Boot Manager back to the top for faster boots.

5. **Fast Boot** –  
   - If you disabled it to help Linux boot:  
     - You can **re-enable it** in BIOS if you want slightly faster Windows startup.
     - Optional—can leave it off too.
---
### TL;DR:
If you're done with Linux for now, just:
- Re-enable **Secure Boot** (if you disabled it)
- Make sure you're in **UEFI** mode, not Legacy/CSM
- Put **Windows Boot Manager** back at the top of the boot order

You’re good to go after that.

Want help checking these settings or getting into your BIOS again?

### ASSISTANT
If you're talking about changes you made in the BIOS/UEFI (like Secure Boot, TPM, CSM, virtualization, etc.) to install or run **Nobara Linux**, here's the general rule:

### You **usually don't need** to change them back **unless**:
- You're going back to **Windows** or dual-booting and something broke.
- You **disabled Secure Boot**, and now want to use software or an OS that **requires it**.
- You changed boot mode from **UEFI to Legacy/CSM**, and your main OS needs UEFI.
- You plan to use **BitLocker** on Windows (it needs TPM and Secure Boot enabled).

### Quick checklist:
- **Secure Boot**: Often disabled for Linux. Only re-enable if something needs it.
- **CSM/Legacy Boot**: Leave it off (UEFI only) unless your OS needs Legacy booting.
- **TPM**: Can leave on—harmless for Linux, required for Windows BitLocker.
- **Virtualization (VT-x/AMD-V)**: Good to keep on for performance/testing.

Want to tell me exactly what you changed? I can be more specific.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]