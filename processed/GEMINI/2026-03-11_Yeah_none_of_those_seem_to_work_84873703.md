---
category: general
date: 2026-03-11
id: 114467
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was frustrated that none of the suggested trading setup methods were
  working for him.
tags:
- trading
- troubleshooting
- failed-setup
- trading-platform
---
# Yeah none of those seem to work

### USER
Yeah none of those seem to work

### GEMINI
Since the standard CSS and Decky solutions haven't worked for you, it’s time to be blunt: you are fighting against the core architecture of SteamOS. The Home page is a cloud-synced "Recent Activity" feed, not a local file explorer. Because it's essentially a web view (Chromium), it doesn't "know" what is installed; it just knows what you last touched on any device. If you want a truly clean, installed-only experience without nuking your Desktop library, here is the strategic way forward: 1. The "TabMaster" Reverse-Engineered Fix Since you don't want to hide games globally, use TabMaster (via Decky Loader) to change how you interact with the Deck. The Logic: You can’t fix the Home page, so you bypass it. The Action: Use TabMaster to make the "Installed" tab the first thing you see when you open your Library. The Habit: Stop using the "Home" button. Treat the Library Button as your actual home screen. 2. The "Ghosting" Technique If a specific uninstalled game is haunting your home page (like a massive RPG you deleted but played recently on PC): The Fix: Boot up 10-15 small, installed indie games or apps on your Deck in rapid succession. The Result: This "pushes" the uninstalled games off the horizontal shelf. It’s a manual flush of the cache, but it's the only way to clear that row without using the "Hide" feature that ruins your desktop library. 3. The "Library Filter" CSS (Deep Customization) If you are comfortable with CSS Loader, look for "Centered Home" or "Minimal Home." These don't filter for installed games, but they often hide the entire Recent Activity row. * If the row is gone, the "clutter" is gone. You'll land on a clean screen with just your background and the "Continue" button for the very last game played. The Advisor's Truth You are looking for a precision scalpel (show only installed) in a system designed to be a billboard for your entire Steam life. Every minute you spend hunting for a CSS snippet that likely doesn't exist is an opportunity cost spent not playing your games. Accept the limitation: The Home page is trash for organization. Use the Library (Filtered to Installed) as your true dashboard. Would you like me to find the specific CSS Loader theme names that can hide the "Recent Activity" row entirely to give you that clean start?
