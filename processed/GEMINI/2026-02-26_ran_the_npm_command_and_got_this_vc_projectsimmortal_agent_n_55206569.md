---
category: coding
date: 2026-02-26
id: 874394
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan encountered a permission denied error when trying to globally install
  @anthropic-ai/claude-code via npm on CachyOS.
tags:
- npm-install
- claude-code
- EACCES
- permission-denied
- cachyos
---
# ran the npm command and got this?: ~/vc projects/immortal agent
❯ npm install -g @anthropic-ai/claude-code
npm error code EACCES
npm error syscall mkdir
npm error path /usr/lib/node_modules/@anthropic-ai
npm error errno -13
npm error Error: EACCES: permission denied, mkdir '/usr/lib/node_modules/@anthropic-ai'
npm error     at async mkdir (node:internal/fs/promises:855:10)
npm error     at async /usr/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:572:20
npm error     at async Promise.allSettled (index 0)
npm error     at async #reifyPackages (/usr/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:309:11)
npm error     at async Arborist.reify (/usr/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:121:5)
npm error     at async Install.exec (/usr/lib/node_modules/npm/lib/commands/install.js:152:5)
npm error     at async Npm.exec (/usr/lib/node_modules/npm/lib/npm.js:209:9)
npm error     at async module.exports (/usr/lib/node_modules/npm/lib/cli/entry.js:67:5) {
npm error   errno: -13,
npm error   code: 'EACCES',
npm error   syscall: 'mkdir',
npm error   path: '/usr/lib/node_modules/@anthropic-ai'
npm error }
npm error
npm error The operation was rejected by your operating system.
npm error It is likely you do not have the permissions to access this file as the current user
npm error
npm error If you believe this might be a permissions issue, please double-check the
npm error permissions of the file and its containing directories, or try running
npm error the command again as root/Administrator.
npm notice
npm notice New minor version of npm available! 11.10.1 -> 11.11.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.11.0
npm notice To update run: npm install -g npm@11.11.0
npm notice
npm error A complete log of this run can be found in: /home/toastedmel0n/.npm/_logs/2026-02-26T13_58_11_092Z-debug-0.log

~/vc projects/immortal agent
❯ 

### USER
ran the npm command and got this?: ~/vc projects/immortal agent
❯ npm install -g @anthropic-ai/claude-code
npm error code EACCES
npm error syscall mkdir
npm error path /usr/lib/node_modules/@anthropic-ai
npm error errno -13
npm error Error: EACCES: permission denied, mkdir '/usr/lib/node_modules/@anthropic-ai'
npm error     at async mkdir (node:internal/fs/promises:855:10)
npm error     at async /usr/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:572:20
npm error     at async Promise.allSettled (index 0)
npm error     at async #reifyPackages (/usr/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:309:11)
npm error     at async Arborist.reify (/usr/lib/node_modules/npm/node_modules/@npmcli/arborist/lib/arborist/reify.js:121:5)
npm error     at async Install.exec (/usr/lib/node_modules/npm/lib/commands/install.js:152:5)
npm error     at async Npm.exec (/usr/lib/node_modules/npm/lib/npm.js:209:9)
npm error     at async module.exports (/usr/lib/node_modules/npm/lib/cli/entry.js:67:5) {
npm error   errno: -13,
npm error   code: 'EACCES',
npm error   syscall: 'mkdir',
npm error   path: '/usr/lib/node_modules/@anthropic-ai'
npm error }
npm error
npm error The operation was rejected by your operating system.
npm error It is likely you do not have the permissions to access this file as the current user
npm error
npm error If you believe this might be a permissions issue, please double-check the
npm error permissions of the file and its containing directories, or try running
npm error the command again as root/Administrator.
npm notice
npm notice New minor version of npm available! 11.10.1 -> 11.11.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.11.0
npm notice To update run: npm install -g npm@11.11.0
npm notice
npm error A complete log of this run can be found in: /home/toastedmel0n/.npm/_logs/2026-02-26T13_58_11_092Z-debug-0.log

~/vc projects/immortal agent
❯ 

### GEMINI
This error is a classic permission wall. You’re trying to install a global package into a system directory (/usr/lib/node_modules) that your user account doesn't "own." The "Quick Fix" (Not Recommended) You could just run sudo npm install -g @anthropic-ai/claude-code. Why I advise against it: It creates a "Permission Hell" cycle where you'll constantly need sudo for updates, and it can mess up your file ownership later. The "Advisor's Choice" (Do this instead) The cleanest way to handle this without breaking your system or needing sudo every five minutes is to tell npm to install global packages into a folder in your home directory. Run these three commands in order: Create the local global folder: mkdir ~/.npm-global Configure npm to use it: npm config set prefix '~/.npm-global' Link it to your System Path: Open your shell config file (usually ~/.zshrc or ~/.bashrc) in Cursor: code ~/.zshrc # or ~/.bashrc if you aren't using Zsh Add this line to the very bottom of that file: export PATH=~/.npm-global/bin:$PATH Save the file, then restart your terminal (or run source ~/.zshrc). Now, try the install again: npm install -g @anthropic-ai/claude-code It should now install without asking for a password or throwing an EACCES error. One Reality Check: You are naming your folder immortal agent. If you are building an autonomous agent, Claude Code is significantly better for this than Cursor's built-in chat. It can actually execute the files it writes, see the output, and fix its own bugs. Watch out for: "Looping." Claude Code is aggressive. If you give it a vague prompt like "make this work," it might run 20 commands in a row, burning through your Claude Pro usage limits in 15 minutes. Always review the plan it shows you before hitting "y". Would you like me to show you how to set up a CLAUDE.md file now so the agent understands the architecture of "Immortal Agent" from the jump?
