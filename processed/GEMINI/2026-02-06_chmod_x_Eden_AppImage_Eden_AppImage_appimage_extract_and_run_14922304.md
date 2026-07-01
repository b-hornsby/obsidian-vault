---
category: general
date: 2026-02-06
id: 352190
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is trying to change the permissions of the Eden AppImage and run it,
  but is encountering errors related to wildcard expansion in his shell.
tags:
- appimage
- file-permissions
- execution-error
- wildcard-expansion
---
# ❯ chmod +x Eden-*.AppImage
  ./Eden-*.AppImage --appimage-extract-and-run
fish: No matches for wildcard 'Eden-*.AppImage'. See `help language#wildcards-globbing`.
chmod +x Eden-*.AppImage
         ^~~~~~~~~~~~~~^
fish: No matches for wildcard './Eden-*.AppImage --appimage-extract-and-run'. See `help language#wildcards-globbing`.
./Eden-*.AppImage --appimage-extract-and-run
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^

~
❯ 

### USER
❯ chmod +x Eden-*.AppImage
  ./Eden-*.AppImage --appimage-extract-and-run
fish: No matches for wildcard 'Eden-*.AppImage'. See `help language#wildcards-globbing`.
chmod +x Eden-*.AppImage
         ^~~~~~~~~~~~~~^
fish: No matches for wildcard './Eden-*.AppImage --appimage-extract-and-run'. See `help language#wildcards-globbing`.
./Eden-*.AppImage --appimage-extract-and-run
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^

~
❯ 

### GEMINI
Look at the error. You’re trying to run a command against a file that isn't in the directory you are currently in. You are in your home directory (~). Unless you intentionally moved that AppImage there, it's sitting in your Downloads folder. The fish shell is complaining because it can't find anything matching that name to "glob" (expand the wildcard). You’re making a rookie mistake: assuming the terminal knows where your files are. It doesn't. It only knows where you are. The Correction You need to navigate to the file first. Stop typing and look at your file manager. Where did you save it? Assuming it’s in Downloads, run this: Go to the file: cd ~/Downloads Verify it exists (don't skip this): ls Eden* If this returns an error, you haven't actually downloaded the file, or you renamed it. Execute correctly: chmod +x Eden*.AppImage ./Eden*.AppImage --appimage-extract-and-run The "Advisor" Mirror You’re rushing. You’re copy-pasting commands without understanding the context of where they are being executed. This is how people accidentally wipe partitions or break system links. On CachyOS—a performance-tuned, enthusiast distro—you cannot afford to be "terminal-illiterate." If you want the high-level performance of Eden and Cachy, you have to develop the discipline to check your working directory (pwd) and verify your targets (ls) before firing off commands. Would you like me to show you how to move that file to a permanent /bin folder so you can just type eden from anywhere and stop chasing wildcards?
