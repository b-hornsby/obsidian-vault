---
id: 181066
source: GEMINI
date: 2026-03-25
tags: ['settings', 'configuration', 'troubleshooting']
category: general
sentiment: stuck
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan is noting that certain settings/features were not enabled, likely related to a troubleshooting discussion.
---
# I didn’t have any of these things turned on

### USER
I didn’t have any of these things turned on

### GEMINI
If you aren't using a VPN or Proxy, the system is misidentifying your network architecture or ISP behavior as a masked service. Since you're on a Steam Deck, which often involves extra layers for compatibility, there's a high chance your traffic is being "tunnelled" or translated in a way that looks suspicious to Plutonium's backend. Here is the objective breakdown of why you're getting flagged and what you need to change: 1. The CGNAT / Shared IP Issue If your ISP uses Carrier-Grade NAT (CGNAT)—very common with mobile providers, some fiber startups, or shared apartment building internet—you share one public IP with hundreds of other people. The Reality: If just one of those people used a "banned service" or got blacklisted on Plutonium, the entire IP is burned. * The Fix: Test this immediately by connecting your Deck to a mobile hotspot from your phone. If it works, your home internet IP is flagged. You'll need to contact your ISP and ask for a "static public IP" or a "non-CGNAT" connection. 2. DNS Leakage or Custom DNS Even if you don't have a "VPN" on, if you've manually set your DNS to something like AdGuard, NextDNS, or a custom privacy filter, Plutonium may flag the relay. The Action: Go into your Steam Deck's Desktop Mode -> System Settings -> Connections. Select your Wi-Fi and ensure the IPv4 and IPv6 tabs are set to "Automatic" for both Address and DNS. 3. Proton / Wine Translation Layer (The "Invisible" Tunnel) Plutonium isn't officially supported on Linux; you're running it through a compatibility layer. Sometimes, the way the network stack is handled in certain versions of Proton or Wine can make the outgoing traffic look like it's coming from a virtualized environment or a data center. The Action: If you are using a specific version of Proton GE, try switching to Proton Experimental or a standard stable version ($9.0$ or higher). 4. The "Dirty" IP Sometimes residential IPs just get flagged because they were previously used by a botnet or for malicious activity before you were assigned it. The Action: Power cycle your modem/router for at least 10 minutes. This often forces the ISP to assign you a fresh public IP address. Strategic Move: Don't waste time digging through menus yet. Try the mobile hotspot test right now. If the hotspot works, your home network is the "banned service." If the hotspot also fails, the issue is a setting on the Steam Deck itself. Which one should we investigate first?
