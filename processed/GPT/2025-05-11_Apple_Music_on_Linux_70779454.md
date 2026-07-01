---
source: GPT
date: 2025-05-11
category: coding
id: 70779454
linked_nodes: ['nodes/people/bryan.md']
---
# Apple Music on Linux

### USER
How does gpu pass through work when using Linux to also be able to use a windows VM at the same time? Is that even possible?

### ASSISTANT
Great question — it really comes down to **your needs and priorities**. Here's a **no-BS comparison** between dual booting and GPU passthrough to help you decide which is better for *you*:

### **Dual Booting**  
**Pros:**
- **Full, native performance** for both OSes
- Simple setup (just install both and pick at boot)
- No worries about hardware compatibility, VM configs, or passthrough bugs

**Cons:**
- **Reboot required** every time you want to switch OSes
- No multitasking between Linux and Windows
- Can cause issues with **shared drives**, time sync, and bootloaders (esp. with Secure Boot and BitLocker)

**Best if you:**
- Mostly use one OS at a time
- Want plug-and-play performance without fiddling
- Are gaming or working in Windows 80%+ of the time

If you're up for the initial setup cost (time + config), **GPU passthrough is the most elegant and powerful solution** — especially with a card like the 3070.

Would you like a GPU passthrough setup checklist or a comparison using your specific hardware?

### USER
How well would that work with a 3070 as far as latency goes and things like that?

### ASSISTANT
Yes, you can use Apple Music on Linux, even though Apple doesn't offer an official Linux app. Here are the most effective ways to access your Apple Music library on a Linux system:

### 2. **Cider – Open Source Apple Music Client**
Cider is a cross-platform, open-source Apple Music client built with Electron and Vue.js. It offers a native app-like experience on Linux, supporting features like lyrics, mini-player mode, and playlist management. citeturn0search5

- Available via Flatpak, AppImage, DEB, or AUR for various Linux distributions.
- Note: Cider streams music in AAC format, not Apple's lossless tier. citeturn0search9

For more information and downloads, visit [Cider's official website](https://cider.sh/).

### Summary
| Method                  | Pros                         | Cons                                 |
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
---|
| **Web Player**          | No setup, full library access | No offline playback                  |
| **Cider**               | Native-like app, extra features | No lossless audio, third-party app   |
| **iTunes via Wine**     | Legacy support               | Unstable, limited functionality      |

For most users, the web player or Cider will provide the best experience on Linux.

### **Performance & Latency (RTX 3070 Passthrough)**

- **Raw performance:** Near-native (~95–99% of bare metal) once inside the VM.
- **Gaming latency:** Practically indistinguishable *if* you're outputting directly to a monitor plugged into the 3070.
- **Streaming latency (e.g., with Looking Glass):**
  - Adds **~2–5 ms** latency, depending on system tuning.
  - Still good enough for most users, even for fast-paced games.
- **CUDA/OpenCL performance**: Full acceleration works as expected inside the VM.

### **Real-World Example Use Case:**

**Linux Host:** Running lightweight tiling WM or GNOME/KDE  
**Windows Guest:** Passed-through RTX 3070 with 8 cores and 16GB RAM  
**Result:**  
- Plays games like **Cyberpunk 2077 or Elden Ring** inside VM at ultra settings  
- **Less than 5% performance drop** compared to native Windows  
- Latency is negligible if using a direct HDMI/DisplayPort connection

Want a full beginner-friendly guide tailored for your 3070 setup?

### USER
Can you use Apple Music on Linux?

### USER
Is it better to dual boot or do this?

### ASSISTANT
Yes, GPU passthrough absolutely *is* possible on Linux — and it's a powerful way to run a **Windows virtual machine (VM)** with **near-native performance** using your GPU, while keeping Linux as your host system. Here's a breakdown of **how it works** and **what you need**:

### **How It Works (Simplified):**

1. **Linux runs as the host OS**, using a **hypervisor** like **KVM/QEMU**.
2. A second GPU (or your primary one with IOMMU isolation) is **assigned to the Windows VM**.
3. When the VM starts, it **takes control of the GPU**, bypassing the Linux host.
4. You access the VM via a **display connected to that GPU** or stream it via **Looking Glass** (for no dual-monitor setup).

### **Basic Workflow:**

1. **Enable virtualization and IOMMU** in your BIOS.
2. **Isolate the GPU** from the host using VFIO (prevents Linux from using it).
3. **Create a Windows VM** using virt-manager or CLI.
4. **Pass the GPU and its audio device** into the VM using QEMU/KVM config.
5. **Install GPU drivers inside the Windows VM**.

### **Drawbacks / Considerations**
- Setup is **technical** — not plug-and-play.
- Some **GPUs have a reset bug** (especially NVIDIA consumer cards), requiring patches.
- **NVIDIA might block passthrough** on non-Quadro cards (though workarounds exist).
- You may need **a second monitor**, or use Looking Glass for headless use.
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]