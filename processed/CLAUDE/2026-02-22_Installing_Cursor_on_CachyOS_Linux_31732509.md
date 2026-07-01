---
category: ai-tools
date: 2026-02-22
id: 891255
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: CLAUDE
summary: Bryan wanted to install the Cursor IDE on CachyOS Linux.
tags:
- cursor
- ide
- cachyos
- linux-installation
- aur
---
# Installing Cursor on CachyOS Linux

### HUMAN
how do i install cursor on linux? specifically cachyos

### ASSISTANT
CachyOS is Arch-based, so you have a couple easy options:

**Via AUR (easiest)**

```bash
yay -S cursor-bin
# or with paru
paru -S cursor-bin
```

**Via AppImage (manual)**

1. Go to [cursor.sh](https://cursor.sh) and download the Linux AppImage
2. Make it executable and run it:
```bash
chmod +x cursor-*.AppImage
./cursor-*.AppImage
```

Or to install it more permanently:
```bash
chmod +x cursor-*.AppImage
sudo mv cursor-*.AppImage /usr/local/bin/cursor
```

**The AUR method is recommended** for CachyOS since it integrates cleanly with your package manager and handles updates automatically. `cursor-bin` is the prebuilt binary package, which is faster to install than building from source.
