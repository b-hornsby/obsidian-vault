---
id: 131566
source: GEMINI
date: 2026-03-11
tags: ['steam-deck', 'css-loader', 'home-page', 'ui-customization', 'game-library']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was looking for a way to filter the Steam Deck home page to only show installed games, possibly via CSS Loader.
---
# Is there a way to only show what’s installed on the home page on the steam deck? Even if it’s a css loader solution that’s fine my home page is just too cluttered and I don’t wanna just simply hide the games because then they’re hidden on my desktop too 

### USER
Is there a way to only show what’s installed on the home page on the steam deck? Even if it’s a css loader solution that’s fine my home page is just too cluttered and I don’t wanna just simply hide the games because then they’re hidden on my desktop too 

### GEMINI
There is no official toggle for the home page (the "Recent Activity" shelf), but since you are willing to use Decky Loader, there are a couple of ways to achieve a cleaner, "installed-only" feel without hiding games from your library entirely. 1. The "TabMaster" Plugin (Best Alternative) While it doesn’t directly delete uninstalled games from the "Recent" list on the home page, TabMaster allows you to redefine your landing experience. What it does: It lets you hide, reorder, and rename the tabs in your Library (Great Circle/Steam Button > Library). The Workflow: You can set "Installed" as your first tab and use it as your primary "Home" by training yourself to hit the Library button instead of relying on the default landing page. It’s the most stable way to ensure you only see what’s ready to play. 2. CSS Loader: "Hide Home Library" or "Clean Home" If you specifically want to nuke the "Recent Games" clutter on the main screen, look for these themes within the CSS Loader marketplace: No Home Shelf / Hide Recent Activity: Some CSS snippets are designed specifically to hide the horizontal "Recent" shelf entirely. The Catch: CSS Loader is purely visual. It can hide elements, but it cannot "filter" them. It can't distinguish between an installed "Recent" game and an uninstalled one; it can only hide the whole row or specific UI elements. If you use a "Hide Home" CSS, your home screen will just show your background and the bottom buttons, forcing you to go to the Library (where you can filter for installed). 3. "Deck Settings" Plugin In the Decky marketplace, check for a plugin called Deck Settings. Some versions have included toggles to tweak the behavior of the Home screen, though this is often broken by SteamOS updates. The Reality Check The Steam Deck UI is essentially a web wrapper (Chromium-based). Because of how Valve handles "Recent Activity," that list is synced to your account cloud, not your local storage. The "Hiding" Trap: As you noted, using the official "Hide this game" feature is global. If you hide it on the Deck, it disappears from your PC too. The Opportunity Cost: If you spend hours trying to "fix" the home page with CSS, you’re fighting the system's design. The most strategic move is to ignore the Home page and make the Library (Filtered to Installed) your default mental "start" point. Would you like me to walk you through the steps to install Decky Loader if you haven't set it up yet?
