---
category: homelab
date: 2026-03-09
id: 488917
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: CLAUDE
summary: Bryan was looking for a Vortex mod manager alternative on CachyOS for games
  like Cyberpunk and Elden Ring, evaluating options like ModOrganizer2, Nexus Mods
  App, and r2modman.
tags:
- vortex
- mod-manager
- modorganizer2
- nexus-mods
- cachyos
- linux-gaming
---
# Vortex mod manager alternatives

### HUMAN
best vortex mod manager alternative cachyos?

### ASSISTANT
```
This block is not supported on your current device yet.
```

Here are the best Vortex alternatives for CachyOS (Arch-based Linux):

### 🥈 **Nexus Mods App** — Best Future-Proof Option
Nexus Mods is building a new app as a replacement for Vortex, implementing lessons learned from Vortex's development, with a focus on always providing an "undo" feature — solving the problem of mods breaking installs or game updates wrecking mod setups. It has **native Linux support** and is available as an AppImage. It's still maturing but already usable.

### Also worth mentioning:
- **Limo** — a newer Linux-native mod manager, lightweight and promising for CachyOS/Arch users (available on AUR)

**A heads up on game support** — the Nexus Mods App is still in active development; Bethesda game support (Skyrim, Fallout) was temporarily pulled while they rework it, but games like Stardew Valley and Cyberpunk work well.

What game are you trying to mod? That'll help narrow down the best tool for your specific case.

### HUMAN
mainly cyberpunk, elden ring, repo come to mind but i need something gen purpose primarily

### ASSISTANT
Good news — Cyberpunk is actually one of the best-supported games on the Nexus Mods App. For your lineup:

- **Cyberpunk 2077** ✅ fully supported
- **REPO** ✅ on Thunderstore, use **r2modman** (also on Flathub)
- **Elden Ring** ⚠️ limited — most Elden Ring mods are manual installs or need special tools

Since you want something general purpose, **Nexus Mods App** is your best starting point. Install it with the commands above and it'll cover Cyberpunk well out of the box.

For REPO specifically, grab r2modman alongside it:
```fish
paru -S r2modman-bin
```
or via Flatpak:
```fish
flatpak install flathub com.github.ebkr.r2modman
```

For **Elden Ring**, the reality on Linux is a bit rough — most mods require [Elden Mod Loader](https://www.nexusmods.com/eldenring/mods/117) dropped manually into the game folder, since the game uses an anti-tamper system that mod managers struggle with. The Nexus Mods App can still help you download and track them, even if deployment is manual.

**TL;DR setup:**
| Tool | Purpose |
|
---
|
---
|
| Nexus Mods App | Cyberpunk + general Nexus mods |
| r2modman | REPO + other Thunderstore games |
| Manual | Elden Ring |

### HUMAN
r2modman is great for repo, thats fine but for everything else im looking at something comparable to vortex like how i was using on win 11

### ASSISTANT
Yeah, the honest answer is that **nothing on Linux is quite at Vortex's level yet** for general Nexus modding. Your real options are:

**Nexus Mods App** — the closest 1:1 replacement
- Made by Nexus Mods themselves as Vortex's official successor
- Native Linux, actively developed
- Cyberpunk support is solid right now
- Bethesda games (Skyrim/Fallout) still being reworked
- Elden Ring not supported yet
- Still in beta but usable for day-to-day modding

**Mod Organizer 2 via Bottles/Wine** — most powerful but painful
- MO2 is what power users swear by for Bethesda games
- Running it through Bottles or a Wine prefix works but is finicky to set up
- Overkill if you're not deep into Skyrim/Fallout modding

Fair warning though — MO2 on Linux for **Cyberpunk** specifically is less proven than Nexus Mods App. MO2 really shines for **Bethesda games** (Skyrim, Fallout). For Cyberpunk, the Nexus Mods App is honestly better supported.

For your game lineup:
| Game | MO2 support |
|
---
|
---
|
| Cyberpunk | ⚠️ hit or miss |
| Elden Ring | ⚠️ manual either way |
| REPO | ❌ use r2modman |

Are you mainly going with MO2 for a specific game, or just preference? Might change the recommendation.

### HUMAN
gemini said this about the nexus mods app tho: As of March 2026, the situation with the Nexus Mods App (the native Linux/cross-platform one) has shifted significantly. Nexus Mods officially retired the standalone App in early January 2026 to consolidate their efforts back into Vortex, which is finally getting native Linux/SteamOS support.

However, since you're on CachyOS, you can still install the existing version of the Nexus Mods App from the AUR.

### ASSISTANT
That's worth verifying — let me check.
```
This block is not supported on your current device yet.
```

Gemini was right, I apologize for the outdated info. Here's the actual current situation:

Nexus stopped development on the Nexus Mods App in January 2026 and is focusing all efforts on Vortex instead.

As for Linux support, Nexus has committed to SteamOS support for Vortex in 2026, targeting "vanilla Steam hardware like the Steam Deck and Steam Machine" — and since SteamOS is Arch-based, community developers are free to extend support to other distros like CachyOS. But that's not here yet.

So right now your real options are:

- **MO2 via Bottles** — works today, best for Bethesda games, more setup involved
- **Vortex via Wine/Proton** — clunky but functional, and will get proper Linux support later in 2026
- **Manual modding** — for Elden Ring regardless

Honestly since you were already leaning toward MO2, that's probably the right call. It's the most stable option on Linux right now while Vortex's native support is still in progress. Want to go ahead with the Bottles setup for MO2?

### HUMAN
what is the best solution given the games im trying to mod on linux

### ASSISTANT
Given your specific games:

- **Cyberpunk 2077** — has its own built-in mod manager ecosystem. **REDmod** is the official tool and is built right into the game. For Nexus mods, most Cyberpunk modders on Linux just use the website to download + drop files manually since the folder structure is simple and well documented.

- **REPO** — r2modman, already sorted ✅

- **Elden Ring** — manual regardless of what manager you use on Linux, no way around it

Honestly none of your three games actually benefit much from a traditional mod manager like MO2 or Vortex. MO2 really shines for Bethesda games with massive load orders (Skyrim with 200+ mods etc). For your lineup it's kind of overkill and adds complexity for little gain.

**The practical setup for you:**
| Game | Best approach |
|
---
|
---
|
| Cyberpunk | REDmod + manual Nexus downloads |
| REPO | r2modman ✅ |
| Elden Ring | Manual + Elden Mod Loader |

If you plan to get into Skyrim or Fallout heavily down the line then MO2 via Bottles is worth the setup. But for what you're playing right now, a dedicated mod manager might just be friction you don't need.

Does that change your thinking or are there more games you're planning to mod?

### HUMAN
i just want something similar experience wise to vortex on win 11

### ASSISTANT
Then honestly your best bet right now is just **Vortex through Wine/Proton** — since that's literally Vortex, the same experience you're used to.

Easiest way is through **Bottles**:

```fish
paru -S bottles
```

or Flatpak:
```fish
flatpak install flathub com.usebottles.bottles
```

Then inside Bottles:
1. Create a new bottle → **Gaming** preset
2. Search for **Vortex** in the installer list — it's in there
3. Install and configure it

It's not perfect through Wine but it's functional for Cyberpunk, and it's the exact UI and workflow you already know. Plus official SteamOS/Linux support for Vortex is coming later in 2026, so running it through Bottles now is essentially just a temporary bridge until native support lands.

That's the most honest answer — nothing else on Linux right now gives you the Vortex experience except Vortex itself.

### HUMAN
i dont see vortex at all in the installer

### ASSISTANT
Try installing it manually inside Bottles. First download the Vortex installer from Nexus, then:

1. In Bottles, open your Gaming bottle
2. Click **Run Executable**
3. Point it at the downloaded Vortex `.exe` installer
4. Let it install normally like you would on Windows

Alternatively, Lutris has a dedicated Vortex install script which handles a lot of the Wine config automatically:

```fish
flatpak install flathub net.lutris.Lutris
```

Then go to **lutris.net**, search for Vortex, and hit Install — it'll pull the correct Wine prefix setup automatically. This is actually the more proven route for Vortex on Linux and what most people use.

Which do you have installed already, Bottles or Lutris?

### HUMAN
yeah bottles doesnt seem to work for me

### ASSISTANT
Go with Lutris then, it's the more proven route for Vortex anyway:

```fish
flatpak install flathub net.lutris.Lutris
```

Then either:
- Go to **lutris.net/games/vortex-mod-manager** in your browser and click **Install**
- Or inside Lutris, click the **+** button → search "Vortex" → install from there

Lutris has a community-maintained install script specifically for Vortex that handles all the Wine prefix, .NET dependencies and symlinks automatically. It's the closest you'll get to a painless Vortex setup on Linux right now.

Give that a shot and let me know where you get to.