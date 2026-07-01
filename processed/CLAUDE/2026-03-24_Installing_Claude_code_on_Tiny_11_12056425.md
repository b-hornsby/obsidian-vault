---
category: ai-tools
date: 2026-03-24
id: 265470
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- operation-immortal-agent
resolution: partial
sentiment: stuck
source: CLAUDE
summary: Bryan is trying to install Claude Code and Gemini CLI on his Tiny 11 system,
  encountering issues with Winget, NPM, and PowerShell execution policies.
tags:
- claude-code
- tiny11
- installation-issues
- winget
- gemini-cli
- npm
---
# Installing Claude code on Tiny 11

### HUMAN
Im on tiny 11 now. within cursor, how do i install claude code so i can use it within my terminal?

### ASSISTANT
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good news and bad news here. Since you're on Tiny11 (stripped Windows 11), here's what you need to know:

**The recommended method now is the native PowerShell installer** — no Node.js required. Open PowerShell and run:

```powershell
winget install Anthropic.ClaudeCode
```

Or the direct PowerShell installer (from the official docs):
```powershell
irm https://claude.ai/install.ps1 | iex
```

Claude Code on Windows requires Git for Windows or WSL. You can launch it from PowerShell, CMD, or Git Bash — no need to run as Administrator.

**Steps:**

1. **Install Git for Windows** if you don't already have it — grab it from git-scm.com. This is what Claude Code uses internally to run commands on Windows.

2. **Run the installer** in PowerShell (either `winget` or the `irm` command above)

3. **Verify it worked:**
   ```powershell
   claude --version
   ```

4. **Authenticate** — first launch will open your browser to log in with your Anthropic account (Pro/Max required)

**Within Cursor specifically**, just open the integrated terminal (`` Ctrl+` ``) and run `claude` from there. It'll work the same as any terminal since Cursor uses PowerShell/CMD under the hood on Windows.

**One caveat for Tiny11:** Since it's a stripped build, `winget` might be missing or broken. If that's the case, try the `irm` PowerShell method directly, or fall back to the npm route — which *would* require Node.js 18+ installed first.

Want me to walk through the Git for Windows install or troubleshoot if winget is missing on your Tiny11 build?

### HUMAN
PS C:\WINDOWS\system32> winget install Anthropic.ClaudeCode
The `msstore` source requires that you view the following agreements before using.
Terms of Transaction: https://aka.ms/microsoft-store-terms-of-transaction
The source requires the current machine's 2-letter geographic region to be sent to the backend service to function properly (ex. "US").
Do you agree to all the source agreements terms?
[Y] Yes  [N] No:

### ASSISTANT
Type **Y** and hit Enter. That's just winget asking permission to use the Microsoft Store source — standard prompt, nothing sketchy. It'll proceed with the Claude Code install after you agree.

### HUMAN
PS C:\WINDOWS\system32> winget install Anthropic.ClaudeCode
The `msstore` source requires that you view the following agreements before using.
Terms of Transaction: https://aka.ms/microsoft-store-terms-of-transaction
The source requires the current machine's 2-letter geographic region to be sent to the backend service to function properly (ex. "US").
Do you agree to all the source agreements terms?
[Y] Yes  [N] No:

### ASSISTANT
Type **Y** and hit Enter. That's just winget asking permission to use the Microsoft Store source — standard prompt, nothing sketchy. It'll then pull and install Claude Code.

### HUMAN
Do you agree to all the source agreements terms?
[Y] Yes  [N] No: y
Found Claude Code [Anthropic.ClaudeCode] Version 2.1.81
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses to, third-party packages.
Downloading https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases/2.1.81/win32-x64/claude.exe
  ██████████████████████████████   231 MB /  231 MB
Successfully verified installer hash
Starting package install...
Path environment variable modified; restart your shell to use the new value.
Command line alias added: "claude"
Successfully installed
PS C:\WINDOWS\system32>

### ASSISTANT
Clean install. Now just **close PowerShell and reopen it** (or restart Cursor's terminal) so it picks up the updated PATH, then run:

```powershell
claude
```

It'll open a browser window to authenticate with your Anthropic account. Once you log in you're good to go.

### HUMAN
PS C:\Users\toastedmel0n> claude 
Claude Code on Windows requires git-bash (https://git-scm.com/downloads/win). If installed but not in PATH, set environment variable pointing to your bash.exe, similar to: CLAUDE_CODE_GIT_BASH_PATH=C:\Program Files\Git\bin\bash.exe
PS C:\Users\toastedmel0n>

### ASSISTANT
Yep, just needs Git for Windows. Grab it from git-scm.com/downloads/win — run the installer with all defaults, that's fine.

Once installed, close and reopen your terminal and try `claude` again. It should find Git Bash automatically. If it still complains, you can set the env variable it mentioned:

```powershell
$env:CLAUDE_CODE_GIT_BASH_PATH = "C:\Program Files\Git\bin\bash.exe"
```

Then run `claude` again in the same window. Go grab Git and report back.

### HUMAN
how about gemini cli? how do i install it?

### ASSISTANT
```
This block is not supported on your current device yet.
```

Gemini CLI needs Node.js, unlike Claude Code. Here's the quickest path on your Tiny11:

**Step 1 — Install Node.js** (if not already on the system):
```powershell
winget install OpenJS.NodeJS.LTS
```
Then close and reopen PowerShell.

**Step 2 — Install Gemini CLI globally:**
```powershell
npm install -g @google/gemini-cli
```

**Step 3 — Run it:**
```powershell
gemini
```

It'll prompt you to pick a theme, then choose "Login with Google" for the free tier — 60 requests/minute and 1,000 requests/day. A browser window opens, you sign into your Google account, and you're in.

**Notable thing:** Gemini CLI gives you access to Gemini 3 models with a 1M token context window, built-in Google Search grounding, file ops, shell commands, and MCP support. Pretty solid free tier for experimentation alongside Claude Code.

Check if you already have Node first though — run `node --version` in PowerShell. If it's 18+ you can skip Step 1 and go straight to the npm install.

### HUMAN
PS C:\WINDOWS\system32> npm install -g @google/gemini-cli
npm : File C:\Program Files\nodejs\npm.ps1 cannot be loaded because running scripts is disabled on this system. For
more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ npm install -g @google/gemini-cli
+ ~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
PS C:\WINDOWS\system32>

### ASSISTANT
Classic Windows PowerShell execution policy block. Easy fix — run this first:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Type **Y** when prompted, then run the npm install again:

```powershell
npm install -g @google/gemini-cli
```

This only changes it for your user profile, not system-wide, so it's safe on Tiny11.

### HUMAN
PS C:\WINDOWS\system32> npm install -g @google/gemini-cli
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
npm warn deprecated prebuild-install@7.1.3: No longer maintained. Please contact the author of the relevant native addon; alternatives are available.
added 641 packages in 22s
171 packages are looking for funding
  run `npm fund` for details
npm notice
npm notice New minor version of npm available! 11.9.0 -> 11.12.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.12.0
npm notice To update run: npm install -g npm@11.12.0
npm notice
PS C:\WINDOWS\system32>

### ASSISTANT
Installed. Now just run:

```powershell
gemini
```

The deprecation warnings are harmless — that's just npm being noisy about some of its dependencies. You're good.

### HUMAN
no what do those warnings mean?

### ASSISTANT
They're just informational, nothing that'll break anything. Here's what each one means:

**`node-domexception@1.0.0: Use your platform's native DOMException instead`**
This package polyfills a browser API (`DOMException`) for older Node.js versions. Newer Node has it built in, so the package is no longer needed and the author marked it deprecated. It still works fine, it's just unnecessary on modern Node.

**`prebuild-install@7.1.3: No longer maintained`**
This is a tool that installs pre-compiled native binaries for packages that use C++ under the hood. The author abandoned it and recommends alternatives, but again — it still functions, it's just not getting updates or security patches going forward.

Both of these are dependencies of Gemini CLI's dependencies, not anything you installed directly. You'd have to wait for Google to update their package to get rid of them. Totally safe to ignore.

### HUMAN
how do i move the cursor chat window to the right rather than the left side?

### ASSISTANT
In Cursor, right-click the chat panel tab/header and look for **"Move Panel Right"** or **"Move to Right"** — similar to how VS Code handles panel positioning.

If that doesn't work: go to **View → Appearance → Secondary Side Bar** and toggle it, then drag the chat over to the right side.

Alternatively you can just drag the chat tab itself to the right edge of the window until you see the drop zone highlight, then release.

The exact option might vary slightly depending on your Cursor version — what do you see when you right-click the chat panel?

### HUMAN
okay last question. i have my project backed up on github but it private. switched to tiny 11 so i need to get the project back local and back to work on that project

### ASSISTANT
Simple — just clone it. In PowerShell or Cursor's terminal:

```powershell
git clone https://github.com/yourusername/your-repo-name.git
```

It'll ask for your GitHub credentials. Since it's private, you'll need a **Personal Access Token (PAT)** instead of your password — GitHub stopped accepting passwords for git operations.

If you don't have one:
1. Go to **github.com → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)**
2. Generate new token, check the **repo** scope
3. Copy it and use it as your password when git prompts you

Then `cd` into the cloned folder and you're back where you left off. You'll also want to make sure your dependencies are restored — is it a Node project (Immortal Agent)? If so you'd run `npm install` after cloning to pull everything back down.

### HUMAN
it allowed me to auth through my browser and i got this message in the terminal: PS C:\Users\toastedmel0n> git clone https://github.com/toastedmel0n/self_sustained_agent
Cloning into 'self_sustained_agent'...
info: please complete authentication in your browser...
remote: Enumerating objects: 55, done.
remote: Counting objects: 100% (55/55), done.
remote: Compressing objects: 100% (36/36), done.
Receiving objects: 100% (55/55), 76.56 KiB | 1.70 MiB/s, done.
remote: Total 55 (delta 17), reused 51 (delta 13), pack-reused 0 (from 0)
Resolving deltas: 100% (17/17), done.
PS C:\Users\toastedmel0n>

### ASSISTANT
Perfect, that's a clean clone. Now:

```powershell
cd self_sustained_agent
npm install
```

That'll restore all your dependencies from `package.json`. Once it's done you're back in business. Open the folder in Cursor with `cursor .` and you're good to go.

### HUMAN
PS C:\Users\toastedmel0n\self_sustained_agent> npm install
npm warn deprecated @mysten/sui.js@0.50.1: This package has been renamed to @mysten/sui, please update to use the renamed package.
added 324 packages, and audited 325 packages in 12s
60 packages are looking for funding
  run `npm fund` for details
8 high severity vulnerabilities
To address issues that do not require attention, run:
  npm audit fix
To address all issues possible (including breaking changes), run:
  npm audit fix --force
Some issues need review, and may require choosing
a different dependency.
Run `npm audit` for details.
PS C:\Users\toastedmel0n\self_sustained_agent>

### ASSISTANT
You're good to go. Few things to note:

**`@mysten/sui.js` renamed warning** — this is relevant to your project since it's Solana-adjacent Web3 stuff. Worth updating eventually: swap `@mysten/sui.js` for `@mysten/sui` in your `package.json` when you get a chance, but not urgent right now.

**8 high severity vulnerabilities** — don't panic. Run `npm audit` to see what they actually are:

```powershell
npm audit
```

Most of the time these are in dev dependencies or deeply nested packages that don't actually affect your running code. I'd hold off on `npm audit fix --force` for now — the "force" flag can swap in breaking versions and mess up your project.

You're cloned, deps installed, ready to work. `cursor .` to open it up.

### HUMAN
PS C:\Users\toastedmel0n\self_sustained_agent> npm audit
# npm audit report
@hono/node-server  <1.19.10
Severity: high
@hono/node-server has authorization bypass for protected static paths via encoded slashes in Serve Static Middleware - https://github.com/advisories/GHSA-wc8c-qw6v-h7f6
fix available via `npm audit fix`
node_modules/@hono/node-server
bigint-buffer  *
Severity: high
bigint-buffer Vulnerable to Buffer Overflow via toBigIntLE() Function - https://github.com/advisories/GHSA-3gc7-fjrx-p6mg
No fix available
node_modules/bigint-buffer
  @solana/buffer-layout-utils  *
  Depends on vulnerable versions of bigint-buffer
  node_modules/@solana/buffer-layout-utils
    @solana/spl-token  >=0.2.0-alpha.0
    Depends on vulnerable versions of @solana/buffer-layout-utils
    node_modules/@solana/spl-token
      @meteora-ag/dlmm  *
      Depends on vulnerable versions of @solana/spl-token
      node_modules/@meteora-ag/dlmm
      @phantom/mcp-server  >=0.1.1
      Depends on vulnerable versions of @solana/spl-token
      node_modules/@phantom/mcp-server
express-rate-limit  8.2.0 - 8.2.1
Severity: high
express-rate-limit: IPv4-mapped IPv6 addresses bypass per-client rate limiting on servers with dual-stack network - https://github.com/advisories/GHSA-46wh-pxpv-q5gq
fix available via `npm audit fix`
node_modules/express-rate-limit
hono  <=4.12.6
Severity: high
Hono Vulnerable to Cookie Attribute Injection via Unsanitized domain and path in setCookie() - https://github.com/advisories/GHSA-5pq2-9x2x-5p6w
Hono Vulnerable to SSE Control Field Injection via CR/LF in writeSSE() - https://github.com/advisories/GHSA-p6xx-57qc-3wxr
Hono vulnerable to arbitrary file access via serveStatic vulnerability  - https://github.com/advisories/GHSA-q5qw-h33p-qvwr
Hono vulnerable to Prototype Pollution possible through __proto__ key allowed in parseBody({ dot: true }) - https://github.com/advisories/GHSA-v8w9-8mx6-g223
fix available via `npm audit fix`
node_modules/hono
8 high severity vulnerabilities
To address issues that do not require attention, run:
  npm audit fix
To address all issues possible (including breaking changes), run:
  npm audit fix --force
Some issues need review, and may require choosing
a different dependency.
PS C:\Users\toastedmel0n\self_sustained_agent>

### ASSISTANT
Here's the breakdown:

**Safe to fix right now:**
```powershell
npm audit fix
```
This will patch `@hono/node-server`, `express-rate-limit`, and `hono` — all have fixes available and it won't touch breaking changes.

**The unfixable one — `bigint-buffer`:**
This one has no fix available because it's baked into `@solana/spl-token` → `@meteora-ag/dlmm` and `@phantom/mcp-server`. Nobody upstream has patched it yet. Since this is a buffer overflow in a function (`toBigIntLE`), the real question is whether your code ever passes untrusted external input into it — for a self-contained trading agent it's pretty low actual risk, but worth keeping an eye on when those packages eventually update.

Run the safe fix first and report back what it says.

### HUMAN
PS C:\Users\toastedmel0n\self_sustained_agent> npm audit fix
changed 19 packages, and audited 325 packages in 15s
60 packages are looking for funding
  run `npm fund` for details
# npm audit report
bigint-buffer  *
Severity: high
bigint-buffer Vulnerable to Buffer Overflow via toBigIntLE() Function - https://github.com/advisories/GHSA-3gc7-fjrx-p6mg
fix available via `npm audit fix --force`
Will install @phantom/mcp-server@0.1.0, which is a breaking change
node_modules/bigint-buffer
  @solana/buffer-layout-utils  *
  Depends on vulnerable versions of bigint-buffer
  node_modules/@solana/buffer-layout-utils
    @solana/spl-token  >=0.2.0-alpha.0
    Depends on vulnerable versions of @solana/buffer-layout-utils
    node_modules/@solana/spl-token
      @meteora-ag/dlmm  *
      Depends on vulnerable versions of @solana/spl-token
      node_modules/@meteora-ag/dlmm
      @phantom/mcp-server  >=0.1.1
      Depends on vulnerable versions of @solana/spl-token
      node_modules/@phantom/mcp-server
5 high severity vulnerabilities
To address all issues possible (including breaking changes), run:
  npm audit fix --force
Some issues need review, and may require choosing
a different dependency.
PS C:\Users\toastedmel0n\self_sustained_agent>

### ASSISTANT
Good — down from 8 to 5, and all 5 remaining are just the `bigint-buffer` chain. 

Don't run `--force` on this one. It wants to downgrade `@phantom/mcp-server` to `0.1.0` which is a breaking change and could mess up whatever Phantom integration you have in the agent.

The real fix here is waiting for `@meteora-ag/dlmm` and `@phantom/mcp-server` to update their `@solana/spl-token` dependency upstream — that's out of your hands. Just leave it as-is for now and check back periodically with `npm audit` after updating your packages.

You're in a good spot — the actionable stuff is patched. Fire up Claude Code and get back to work on Immortal Agent.
