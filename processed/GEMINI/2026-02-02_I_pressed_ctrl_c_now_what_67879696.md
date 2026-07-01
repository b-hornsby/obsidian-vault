---
id: 139546
source: GEMINI
date: 2026-02-02
tags: ['cachyos', 'ctrl-c', 'process-interrupt']
category: homelab
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan pressed Ctrl+C during a process on CachyOS and is asking what to do next.
---
# I pressed ctrl c, now what?

### USER
I pressed ctrl c, now what?

### GEMINI
Look at the numbers in your screenshot: [6709/54360]. You were only 12% of the way through. At that rate, you would have been sitting there for hours watching your terminal scroll. You made the right call to kill it. Now, you need to clean up the mess and install the version that’s actually meant for humans who value their time. Step 1: Clean the Build Cache When you aborted, yay left a few gigabytes of half-baked source code in your cache. Let's wipe that out so it doesn't sit there eating your disk space. rm -rf ~/.cache/yay/ungoogled-chromium Step 2: Install the Pre-Compiled Binary Since you are on CachyOS, you have access to their optimized repositories. Try the standard command first; it should pull the binary from the Cachy/Arch repos. sudo pacman -S ungoogled-chromium If that fails (not found): Use the AUR binary version: yay -S ungoogled-chromium-bin The Next Level: Hardware Wallet Prep Once it's installed, Phantom will still fail to see your Ledger unless you tell Linux how to handle the USB connection. This is the most common "blind spot" for Linux crypto users—they blame the browser when it's actually a system permission issue. Run this to ensure your system recognizes the Ledger: # Install the necessary UDEV rules yay -S libu2f-host ledger-udev # Add your user to the plugdev group (if it exists) sudo usermod -aG plugdev $USER Crucial Note: After running the above, unplug your Ledger and plug it back in. ### One Final Warning Ungoogled Chromium is "bare metal." It doesn't even have a way to search from the address bar by default (you have to set a search engine manually) and it blocks all extensions by default. To get Phantom working, you'll need to: Open chrome://flags Search for "Handling of extension" or "Extension" settings to ensure you can actually side-load them, OR install the "Chromium Web Store" extension from GitHub first. Do you want the link to the Chromium Web Store setup so you can actually download Phantom without jumping through hoops?
