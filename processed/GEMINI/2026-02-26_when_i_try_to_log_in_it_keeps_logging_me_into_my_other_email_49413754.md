---
category: general
date: 2026-02-26
id: 737607
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is having trouble logging into a new account, as it keeps defaulting
  to his other email.
tags:
- account-login
- email-authentication
- troubleshooting
---
# when i try to log in it keeps logging me into my other email, not the one i just made 

### USER
when i try to log in it keeps logging me into my other email, not the one i just made 

### GEMINI
This is a classic OAuth Cookie Loop. Because you previously logged into the Phantom Developer Portal with "Email A," your browser has saved a session cookie that is fighting your attempt to use "Email B." The "Brutally Honest" truth: Computers are lazy. They will always try to use the last valid session they found unless you physically kick them out. The 3-Minute "Clean Slate" Fix Do exactly this, in this order: Nuclear Logout: Go to accounts.google.com/Logout (this force-signs you out of all Google sessions in that browser). Go to developers.phantom.app and click "Logout" if the button is visible. Clear the "Ghost" Cookies: In your browser (Chrome/Brave), press F12 to open Developer Tools. Go to the Application tab -> Storage -> Cookies. Right-click https://auth.phantom.app and https://developers.phantom.app and select Clear. The "Incognito" Trick (Highly Recommended): Open a New Incognito Window (Ctrl+Shift+N or Cmd+Shift+N). Go to developers.phantom.app. Sign in using Email B. Create your project and copy the App ID. Why this matters for the "Hands" (Test 2) When you run the terminal command npx @phantom/mcp-server, it’s going to open your default browser. The Trap: If your default browser is still logged into "Email A," the MCP server will try to link the session to that email, but your PHANTOM_APP_ID (created with Email B) will cause a 403 Signature Mismatch. The Solution: Before you run the command, make sure your default browser is either logged into Email B or has all other Google accounts signed out. Your Tactical Move Once you have the App ID from the Incognito window, run this: PHANTOM_APP_ID=ID_FROM_EMAIL_B npx @phantom/mcp-server When the browser opens, force it to use Email B. If you see "Session saved to ~/.phantom-mcp/session.json", you have officially won the battle against the OAuth Loop. Did the Incognito window let you get the ID, or is the browser still being stubborn?
