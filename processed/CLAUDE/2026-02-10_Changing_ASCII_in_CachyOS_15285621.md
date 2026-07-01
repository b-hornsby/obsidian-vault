---
id: 536704
source: CLAUDE
date: 2026-02-10
tags: ['cachyos', 'ascii-art', 'konsole', 'terminal-customization', 'kde-plasma']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan wanted to change the ASCII art displayed in his CachyOS terminal/Konsole.
---
# Changing ASCII in CachyOS

### HUMAN
how do i change the ascii in cachyos? these are my specs: CachyOS x86_64, Linux 6.18.9-2-cachyos, fish 4.4.0, KDE Plasma 6.5.5,

### ASSISTANT
In CachyOS, you can change the ASCII art that appears in system information tools like `neofetch` or `fastfetch`. Here's how:

## For fastfetch (most common in CachyOS)

1. **Find your config file:**
   ```fish
   ~/.config/fastfetch/config.jsonc
   ```

2. **Edit the logo:**
   You can either:
   - Change to a different distro logo: Add `"logo": "arch"` (or any other distro name) in the config
   - Use a custom ASCII file: Add `"logo": {"source": "/path/to/your/ascii.txt", "type": "file"}`
   - Disable the logo: Add `"logo": "none"`

3. **Example config edit:**
   ```jsonc
   {
       "logo": "arch",  // or "debian", "ubuntu", etc.
       // rest of your config...
   }
   ```

## For neofetch (if you're using it)

1. **Edit the config:**
   ```fish
   nano ~/.config/neofetch/config.conf
   ```

2. **Find the ascii_distro line and change it:**
   ```bash
   ascii_distro="Arch"  # or any other distro name
   ```

## Custom ASCII Art

To use completely custom ASCII art:

1. Create a text file with your ASCII art
2. For fastfetch: reference it in the config as shown above
3. For neofetch: use `--ascii /path/to/file.txt` or set `image_source="/path/to/file.txt"` in the config

Which tool are you using - fastfetch or neofetch?
