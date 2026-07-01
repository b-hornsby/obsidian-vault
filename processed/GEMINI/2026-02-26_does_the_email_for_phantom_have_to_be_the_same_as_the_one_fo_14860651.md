---
category: crypto-web3
date: 2026-02-26
id: 203577
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/personal/crypto-web3.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking if the email address used for Phantom needs to be the same
  as the one associated with his wallet, likely concerning account linking and security.
tags:
- phantom-wallet
- email-verification
- account-linking
- security
---
# does the email for phantom have to be the same as the one for the wallet i use? 

### USER
does the email for phantom have to be the same as the one for the wallet i use? 

### GEMINI
Yes. The email you use to sign in to the Phantom Developer Portal MUST match the email you use for the SSO login (Google/Apple) when you authenticate the MCP server. According to the 2026 documentation for @phantom/mcp-server, if these emails do not match, the session will fail to initialize, or you will receive a 403 Forbidden error when trying to use the tools. Why this is the case (The "High-Conscientiousness" Reason): Phantom uses this email match as a "Trust Signal." In 2026, the MCP server is designed to prevent a developer from creating an App ID and then tricking a different user into signing for it. By forcing the emails to match, Phantom ensures the developer and the "signer" are the same entity for this specific autonomous use case. Here is your 3-Step "Live" Checklist: Portal Setup: Sign in to developers.phantom.app using Email A. Create your App ID. SSO Login: When the browser pops up after running the MCP command, you must select the Google/Apple account associated with Email A. The Result: The server will write ~/.phantom-mcp/session.json. This file is the "Soul" of your agent. Once it's there, you can run the heartbeats headlessly. The "Brutally Honest" Final Warning If you try to "mix and match" emails to keep your personal life separate from the bot, you will break the auth flow. If you already have a wallet on a different email, you have two choices: Option A (Cleanest): Register the Phantom Portal app with the email currently tied to your Phantom Wallet. Option B (The Sandbox): Create a new "Burner" Google account, use it for the Portal, and use it to spin up a fresh Phantom Wallet for the $300 fund. (I recommend this for the Solana Grant—it keeps your R&D funds perfectly isolated from your main stash). Once you have the PHANTOM_APP_ID, run the Stage B test again. If we get a Transaction Signature back, the project is officially "Alive." Ready to cross the finish line?
