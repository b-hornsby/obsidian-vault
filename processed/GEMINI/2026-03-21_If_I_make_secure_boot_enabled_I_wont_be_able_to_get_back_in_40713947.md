---
category: homelab
date: 2026-03-21
id: 518654
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is concerned that enabling secure boot will prevent him from accessing
  his system.
tags:
- secure-boot
- boot-issues
- system-access
- troubleshooting
---
# If I make secure boot enabled I won’t be able to get back in?

### USER
If I make secure boot enabled I won’t be able to get back in?

### GEMINI
Correct. If you enable Secure Boot right now without clearing the keys first, you will be met with that same red "Secure Boot Violation" box and be locked out again. The "Brutally Honest" Reality The BIOS is currently a bouncer holding an old guest list. Your updated CachyOS files aren't on it. If you turn the bouncer back on, he’s going to kick you out. To fix this for good so you can play Valorant, you have to follow this exact logic: Clear the Guest List: In BIOS, "Clear/Delete Secure Boot Keys." This puts the BIOS in Setup Mode. Let the New Files In: Boot into CachyOS (since the "bouncer" is now in Setup Mode, he'll let you pass). Create a New Guest List: Run sudo sbctl enroll-keys -m. This tells the BIOS "Here is the new list of people I trust (Microsoft + My Linux files)." Tag the Files: Run the sbctl sign commands. This "tags" your kernel and Minegrub so the BIOS recognizes them as authorized. The Opportunity Cost If you don't do this "Clear Keys" step, you are stuck in a loop of turning Secure Boot off every time you want to use Linux, and turning it back on (and potentially failing) every time you want to play Valorant. The Plan: Step 1: Go to BIOS. Clear/Delete Secure Boot Keys. Step 2: Ensure Secure Boot is Enabled. Step 3: Save and Exit. Once you hit your desktop after that, your BIOS will be in "listening" mode, and we can run the sbctl commands to lock everything down properly. Do you want me to stay on standby while you head into the BIOS to clear those keys?
