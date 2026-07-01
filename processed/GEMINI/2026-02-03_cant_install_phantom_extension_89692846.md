---
category: general
date: 2026-02-03
id: 960140
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is unable to install the Phantom browser extension and is seeking help
  troubleshooting the issue.
tags:
- phantom-extension
- browser-extension
- installation-failure
---
# cant install phantom extension?

### USER
cant install phantom extension?

### GEMINI
If you’re trying to install the Phantom wallet extension on Chromium and it’s failing, you’re likely hitting a wall because you’re using a "de-googled" or stripped-down version of Chromium that lacks the background machinery to talk to the Chrome Web Store. Stop clicking "Add to Chrome" and expecting it to work if the browser is intentionally broken for privacy. Here is the reality of why it’s failing and how to force it to work. Why It’s Failing (The Blind Spots) Missing Web Store API: If you are using Ungoogled-Chromium, the browser is hardcoded to block requests to Google servers. It won't "just work." Sync/Account Requirements: Some Chromium builds require you to be signed in to a Google account to install extensions from the official store—which defeats your privacy goal. Developer Mode Restrictions: Chromium sometimes blocks third-party extensions unless you explicitly tell it you’re a power user. The Strategic Fixes 1. The "Ungoogled" Workaround If you are using Ungoogled-Chromium, you cannot use the "Add to Chrome" button. You have to sideload it. Download the Chromium Web Store extension (from GitHub) which re-enables the "Add to Chrome" functionality. Alternatively: Use a tool like CRX Extractor to download the Phantom .crx file manually, go to chrome://extensions, enable Developer Mode, and drag-and-drop the file into the window. 2. Enable Developer Mode You might simply be blocked by default security settings. Go to chrome://extensions. Toggle the Developer mode switch in the top right to ON. Try the installation again. 3. Check for Architecture Mismatch If you are on an ARM-based machine (like an M1/M2 Mac or certain Surface Pro models) and using a specific Linux build of Chromium, some extension binaries might hang. Ensure your Chromium build matches your OS architecture perfectly. The "Advisor" Reality Check If you are trying to run a Crypto Wallet (Phantom) on a high-privacy browser like Chromium, you are creating a paradox for yourself. The Risk: By sideloading extensions or using "workarounds" to get Phantom running, you are potentially bypassing the very security sandboxing that protects your private keys. The Opportunity Cost: You are spending time "fixing" a browser to accept a wallet. If your goal is secure, private DeFi usage, you are better off using Brave (which is Chromium-based, supports DDG, and has native Phantom support) or a hardened Firefox profile. Stop fighting the tool. If the tool (Chromium) is designed to be "Ungoogled" and you are trying to force Google-dependent extensions onto it, you are wasting time on a friction-filled setup. Would you like the specific steps to manually download and sideload the Phantom CRX file, or should we audit your browser choice to see if it actually aligns with your crypto security needs?
