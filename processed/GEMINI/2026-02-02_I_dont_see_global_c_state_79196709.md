---
category: homelab
date: 2026-02-02
id: 456069
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is reporting that he cannot find the 'Global C-State' setting in his
  BIOS, which he's likely trying to adjust for performance or stability reasons.
tags:
- bios
- cpu
- power-management
- c-states
- troubleshooting
---
# I don’t see global c state

### USER
I don’t see global c state

### GEMINI
If you don't see "Global C-state Control," it's likely buried one level deeper in your CPU configuration or named slightly differently because of your motherboard brand. Since you are using an AMD system, it is often tucked away under AMD CBS. Where to hunt for it: Look for "AMD CBS": Usually found under the Advanced tab. Go to "CPU Common Options": Once inside AMD CBS, this is the most common sub-menu. Find "Global C-state Control": It should be here. Set it to Disabled. If it’s still missing, look for "DF Cstates" or "Core C-states". Every motherboard manufacturer (ASUS, MSI, Gigabyte) loves to rename these settings just to make your life difficult. The Brutal Advisor Mirror You’re looking for a needle in a haystack, but that needle is what’s stabbing your Yeti. If you skip this, the voltage drops will continue to "stroke out" your microphone’s ancient USB controller, and no script—no matter how well-written—can fix a hardware-level power drop. Your Priority Check-list (Do not leave BIOS until these are done): USB Power Delivery in S5: Disabled. (This ensures the Yeti actually dies when the PC dies). Global C-state Control: Disabled. (This ensures the Yeti gets a steady "heartbeat" of power). ERP Ready: If you see this under Power Management, set it to Enabled (S4+S5). This is another way motherboards kill USB power when the system is off. Did you find the "USB Power Delivery in S5" setting and disable it yet? That is the "low-hanging fruit" that will yield the biggest result. If you can't find C-states, prioritize the S5 Power setting and the ERP setting. Reboot, test, and tell me if the Yeti is finally showing signs of life without the manual tug.
