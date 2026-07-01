---
category: homelab
date: 2026-03-15
id: 634231
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan had 470GB free on his drive and wanted to allocate exactly 300GB for
  Tiny11, asking what value to enter for free space proceeding in GParted.
tags:
- gparted
- partition-resize
- free-space-calculation
- tiny11-allocation
- disk-management
---
# So currently I have 470 gigs left on my drive. I only want 300 of that to be used for the Tiny 11. So when I go to do the resize for free space proceeding what does that need to be?

### USER
So currently I have 470 gigs left on my drive. I only want 300 of that to be used for the Tiny 11. So when I go to do the resize for free space proceeding what does that need to be?

### GEMINI
For Free space preceding, you can just leave that as zero. The box you want to change is called New size. Since you want to leave about 300 gigabytes for Tiny11, you'll want to put 300,000 or 500,000 MiB there, like we talked about before. That will resize your CachyOS partition and create the correct amount of unallocated space for Windows. How does that sound?
