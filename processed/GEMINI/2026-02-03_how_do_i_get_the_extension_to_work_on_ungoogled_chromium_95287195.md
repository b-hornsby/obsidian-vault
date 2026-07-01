---
category: homelab
date: 2026-02-03
id: 353093
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was asking how to get a specific browser extension to function correctly
  in Ungoogled Chromium.
tags:
- ungoogled-chromium
- browser-extension
- troubleshooting
- browser-configuration
---
# how do i get the extension to work on ungoogled chromium?

### USER
how do i get the extension to work on ungoogled chromium?

### GEMINI
To get the Phantom extension running on Ungoogled Chromium, you have to stop trying to use the "Add to Chrome" button. By design, your browser has had the "Google communication" guts ripped out of it. It doesn't know how to talk to the Web Store. You have two choices: the Permanent Fix (restoring Web Store functionality) or the Manual Sideload (one-time install). Option 1: The Permanent Fix (Highly Recommended) If you plan on using more than one extension, do this. It installs a "bridge" that allows Ungoogled Chromium to download from the store again. Change the Flags: Paste chrome://flags/#extension-mime-request-handling into your address bar. Set it to "Always prompt for install" and relaunch. Download the Bridge: Go to the Chromium Web Store GitHub and download the latest .crx file. Install the Bridge: * Open chrome://extensions. Turn on Developer Mode (top right toggle). Drag and drop the downloaded .crx file into that window. Install Phantom: Now, go to the Phantom Web Store page. The "Add to Chrome" button will still be greyed out, but you can now right-click the button or use the new "Chromium Web Store" icon in your toolbar to force the install. Option 2: The Manual Sideload (No Extra Extensions) If you don't want to install a "bridge," you have to do the manual labor yourself. Get the ID: The Phantom extension ID is bfnaelmomeimhlpmgjnjophhpkkoljpa. Download the File: Since you can't download it from the store directly, use a third-party service like CRX Extractor or UngoogledExtensions.com to download the .crx for that ID. Install: Go to chrome://extensions, enable Developer Mode, and drag the .crx file onto the page. The Advisor's Warning: Blind Spots Update Failure: Manually installed extensions (Option 2) do not auto-update. If there is a security patch for Phantom, your browser won't get it. You will be sitting on a vulnerable wallet while the rest of the world moves on. Use Option 1 if you value your funds. The "Why": You are using a browser built for maximum privacy, yet you are trying to install a hot wallet that records your financial footprint on a public ledger. If you are doing this for "privacy," make sure you're using a fresh, non-linked wallet address, otherwise, the browser's privacy is moot. Scam Risk: Never download a Phantom .crx from a random "crypto-help" site. Only use the official Store link or a reputable CRX extractor. Would you like me to walk you through the specific security settings inside Ungoogled Chromium to make sure your new wallet isn't leaking your IP address to every site you visit?
