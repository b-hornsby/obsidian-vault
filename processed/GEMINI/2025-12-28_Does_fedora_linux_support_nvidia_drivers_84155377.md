---
category: homelab
date: 2025-12-28
id: 728824
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if Fedora Linux supports NVIDIA drivers.
tags:
- fedora
- nvidia-drivers
- linux-compatibility
- hardware-support
---
# Does fedora linux support nvidia drivers? 

### USER
Does fedora linux support nvidia drivers? 

### GEMINI
Fedora supports Nvidia drivers, but they are not included in the default installation. Because Fedora adheres strictly to a free and open-source software (FOSS) policy, the proprietary Nvidia driver is hosted in external repositories—specifically RPM Fusion. Here is the objective reality: If you just install Fedora and do nothing, you’ll be stuck with the "Nouveau" open-source driver. It’s stable for basic tasks, but useless for gaming, 3D rendering, or AI workloads. The Support Landscape Fedora 41+ has made this significantly easier. While the project doesn't ship the driver, they’ve built "on-ramps" to get it. FeatureSupport StatusNoteWayland SupportExcellentRecent updates (2024–2025) have fixed major flickering and sync issues.Secure BootSupportedYou must enroll a "Machine Owner Key" (MOK) to sign the driver.InstallationEasy to ModerateCan be done via GNOME Software or terminal.UpdatesAutomatedHandled via akmods, which rebuilds the driver when the kernel updates. How to Do It Right (The Only Method I Recommend) Don't download drivers from Nvidia’s website. You will break your system during the next kernel update. Use RPM Fusion. 1. Enable the Repositories Open your terminal and run: sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm 2. Install the Driver sudo dnf update -y sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda 3. The "Wait" Period (CRITICAL) After the installation finishes, do not reboot immediately. Fedora uses akmods to build the driver for your specific kernel in the background. If you reboot too early, the driver won't be ready, and you'll fall back to Nouveau. Wait 3–5 minutes. Check progress with: modinfo -F version nvidia. If it returns a version number, you’re safe to reboot. The "Secure Boot" Blind Spot If you have Secure Boot enabled in your BIOS, the driver will not load unless it is signed. Fedora now automates this via kmodtool and mokutil. During installation, it will likely ask for a password to create a key. On reboot, you will see a blue "MOK Management" screen. Do not ignore this. Select "Enroll MOK," enter the password you chose, and continue. If you skip this, your Nvidia card will be invisible to the OS. Strategy & Mindset If you’re coming from Windows, stop looking for an .exe or a "GeForce Experience" app. Fedora’s strength is in its package manager. If you try to bypass it by "manually" installing drivers, you are creating a maintenance nightmare. Stick to RPM Fusion, follow the Secure Boot prompts, and you’ll have a workstation-grade setup. Would you like me to provide the specific commands to verify your Secure Boot status before you begin?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
