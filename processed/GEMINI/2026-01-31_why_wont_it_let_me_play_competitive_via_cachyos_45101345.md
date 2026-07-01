---
category: homelab
date: 2026-01-31
id: 6749
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is frustrated that competitive games won't work on CachyOS, likely
  due to anti-cheat incompatibility.
tags:
- cachyos
- anti-cheat
- competitive-gaming
- linux-gaming
---
# why won't it let me play competitive via cachyos? 

### USER
why won't it let me play competitive via cachyos? 

### GEMINI
Look, if you're trying to play Counter-Strike 2 (or any Valve game) competitive on CachyOS and getting a "VAC was unable to verify" or "invalid signatures" error, you’re almost certainly sabotaging yourself with Proton. Here is the cold, hard reality of your situation: 1. Stop Using Proton The #1 reason Linux users can't join competitive matches is that they've "Forced a specific Steam Play compatibility tool" (Proton) in the game's properties. The Fact: VAC (Valve Anti-Cheat) does not support CS2 running via Proton. The Fix: Right-click CS2 in Steam → Properties → Compatibility → Uncheck "Force the use of a specific Steam Play compatibility tool." The Result: Steam will download the Native Linux version. This is the only version that allows you to play on VAC-secured competitive servers. 2. Clean Up Your Launch Options If you’ve been copying "performance guides" and pasting strings of commands into your launch options, you’ve likely included something that triggers a signature mismatch. The Blind Spot: Commands like -allow_third_party_software or -insecure will instantly block you from competitive play. The Fix: Clear your Launch Options completely. Start with a blank slate. If you must use something, stick to -novid. 3. Verify Game Files Since you're on CachyOS, you're likely using an optimized kernel or filesystem (like XFS or BTRFS). If there was even a minor hiccup during an update, your file signatures won't match what the VAC server expects. Action: Properties → Installed Files → Verify integrity of game files. Do this after you switch back to the Native version. 4. The CachyOS Edge Case CachyOS users often use proton-cachyos or custom wrappers. While these are great for single-player games, VAC is a closed wall. If you are running Steam as a Flatpak, ensure you have the necessary permissions enabled, or better yet, use the native steam package from the CachyOS repositories to avoid sandbox interference. The Brutal Advice: You're playing on a high-performance distro like CachyOS presumably to get an edge. By trying to run the Windows version via Proton (likely for "better FPS"), you've rendered the game unplayable. You are trading access for a performance metric that doesn't matter if you're stuck in the lobby. Switch to Native Linux, verify your files, and stop over-complicating your setup. Would you like me to walk you through the specific terminal commands to ensure your CachyOS system libraries aren't conflicting with Steam's runtime?
