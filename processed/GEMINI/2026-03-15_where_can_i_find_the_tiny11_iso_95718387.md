---
category: homelab
date: 2026-03-15
id: 671815
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking where to download the Tiny11 ISO file.
tags:
- tiny11
- iso-download
- operating-system
---
# where can i find the tiny11 iso?

### USER
where can i find the tiny11 iso?

### GEMINI
Finding Tiny11 isn't as straightforward as a standard Microsoft download because it’s a community-modified project. You have two main paths: downloading a pre-made image or building it yourself (the safer option). 1. Pre-made ISOs (Archive.org) The developer, NTDEV, hosts the official versions on the Internet Archive. This is where you’ll find the most recent stable releases, including the 25H2 and 24H2 builds. Primary Source: NTDEV’s Archive.org Profile Direct Directory: tiny-11-NTDEV Directory 2. The DIY Method (GitHub - Recommended) Since you are downloading a modified operating system, security is a valid concern. The most transparent way to get Tiny11 is to use the tiny11builder script. This takes an official, untouched Windows 11 ISO from Microsoft and strips it down on your own machine. Repository: ntdevlabs/tiny11builder on GitHub How it works: 1. Download a standard Windows 11 ISO from Microsoft. 2. Run the .ps1 script from the GitHub repo. 3. The script generates a new, debloated ISO for you. Key Versions to Know VersionBest ForTiny11 25H2The latest build (released late 2025/early 2026), based on the newest Windows update.Tiny11 2311High compatibility; based on the 23H2 release and fully updateable.Tiny11 CoreUltra-minimal (2GB RAM requirement). Warning: Does not support Windows Updates. Quick Reality Check Activation: You still need a valid Windows 11 (or 10) license key. Tiny11 is "free" in terms of the tool, but the OS itself is not pirated. Security: Pre-made ISOs have Windows Defender removed or disabled by default to save resources. If you're using this for anything other than a VM or a dedicated gaming/test rig, be aware of the reduced security layer. Would you like me to walk you through the PowerShell commands to run the builder script safely?
