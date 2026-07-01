---
id: 102903
source: GEMINI
date: 2026-02-27
tags: ['gemini-cli', 'npm-install', 'ai-tools', 'environment-setup']
category: ai-tools
sentiment: executing
resolution: resolved
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
summary: Bryan was installing the Google Gemini CLI globally via npm in the immortal agent project directory.
---
# ❯ npm install -g @google/gemini-cli
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
npm warn deprecated glob@10.5.0: Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me
npm warn deprecated prebuild-install@7.1.3: No longer maintained. Please contact the author of the relevant native addon; alternatives are available.

added 617 packages in 12s

171 packages are looking for funding
  run `npm fund` for details

~/vc projects/immortal agent 12s
❯ 

### USER
❯ npm install -g @google/gemini-cli
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
npm warn deprecated glob@10.5.0: Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me
npm warn deprecated prebuild-install@7.1.3: No longer maintained. Please contact the author of the relevant native addon; alternatives are available.

added 617 packages in 12s

171 packages are looking for funding
  run `npm fund` for details

~/vc projects/immortal agent 12s
❯ 

### GEMINI
Great. The installation finished, and you’ve successfully ignored a wall of npm deprecation warnings—most of which are noise, though they hint that the ecosystem is moving faster than the packages you just pulled. Since you are in a directory named immortal agent, I’m assuming you aren't just playing around with a chatbot. You're likely trying to build an autonomous loop or a high-context agent. The Brutal Reality Check You just added 617 packages to your global node modules to get a CLI wrapper for an API. The Trap: If your "Immortal Agent" project relies on this CLI as a primary interface, you are building on top of a volatile, high-abstraction layer that Google could deprecate or change next Tuesday. The Opportunity Cost: If you are a high-level developer, you should be calling the Google Generative AI SDK directly in your code, not shell-scripting through a CLI. Using a CLI inside an IDE (Cursor) that is itself an AI wrapper is "Inception-level" redundancy. Immediate Next Steps (Execution) Now that it’s installed, you need to initialize it and see if your environment is actually ready for it. Run these two commands in order: Authenticate (The Gatekeeper): gemini login Stop here if this fails. If it doesn't open a browser, your Node environment or permissions are borked. Test the Context (The "Why" Test): Once logged in, run: gemini "Analyze the current directory structure and tell me if 'immortal agent' is a scalable architecture or just a collection of scripts." Strategy for Your "Immortal Agent" If you are building an agent that is supposed to be "immortal" or persistent: Don't rely on gemini-cli for logic. Use it for quick terminal debugging only. Audit your dependencies. 617 packages for a CLI is a massive attack surface. If this agent is meant to be secure or production-grade, you’re starting with a heavy "dependency debt." What is the specific architectural goal for "Immortal Agent"? I can tell you right now if using this CLI is a shortcut or a dead end for what you're trying to build.
