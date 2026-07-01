---
id: 377851
source: GEMINI
date: 2026-03-11
tags: ['security', 'networking', 'vpn', 'tailscale', 'firewall']
category: homelab
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was asking whether additional security tools are needed beyond his current VPN/networking setup.
---
# Is there any other tool required for security purposes?

### USER
Is there any other tool required for security purposes?

### GEMINI
If you use Tailscale, you have already bypassed 99% of the security risks associated with game streaming. By using an encrypted tunnel instead of opening ports on your router, your PC remains invisible to the public internet. However, to ensure your CachyOS setup is "bulletproof," here are the final three layers of security you should verify: 1. Disable UPnP in Sunshine Since you are using Tailscale for remote access, you do not want Sunshine trying to automatically "punch holes" in your router’s firewall. Open the Sunshine Web UI (https://localhost:47990). Go to Configuration > Network. Find UPnP and ensure it is set to Disabled. Click Save and restart Sunshine. 2. Lock Down the Web UI Credentials The Sunshine Web UI is the "keys to the kingdom"—anyone with access to it can add applications or see your PC's activity. Unique Password: Do not use a simple or reused password for the Sunshine login. CachyOS Tip: If you ever forget your credentials or want to change them via terminal, you can reset them with: sunshine --creds [new-username] [new-password] 3. The "Kill Switch" (Optional but Pro) If you are paranoid about leaving the "door" open while you aren't gaming, you can toggle the Sunshine service on CachyOS only when you need it. To stop the service: systemctl --user stop sunshine To start the service: systemctl --user start sunshine Note: If you do this, you won't be able to start a stream remotely unless the service is already running. Summary Checklist for a Secure Setup: FeatureSettingWhy?Access MethodTailscale (VPN)Encrypts traffic and hides your PC from hackers.Port ForwardingOFFPrevents random scans of your home network.UPnPDisabledStops Sunshine from overriding your router security.Sunshine UIStrong PasswordProtects the "server" settings from unauthorized local/remote changes. Final Sanity Check Before you head out, test your "Away from Home" setup: Turn off Wi-Fi on your Steam Deck and connect it to your phone's mobile hotspot. Ensure Tailscale is "Connected" on both the PC and the Deck. Launch Moonlight and try to connect using the Tailscale IP (100.x.x.x). Would you like me to show you how to set up "Wake on LAN" so you can leave your PC turned off and only "wake" it when you're ready to play from your Deck?
