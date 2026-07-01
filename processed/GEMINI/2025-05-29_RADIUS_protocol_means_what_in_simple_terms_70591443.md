---
category: homelab
date: 2025-05-29
id: 730246
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking for a simple explanation of the RADIUS protocol.
tags:
- radius-protocol
- network-authentication
- network-security
- access-control
---
# RADIUS protocol means what in simple terms?

### USER
RADIUS protocol means what in simple terms?

### GEMINI
In simple terms, RADIUS (Remote Authentication Dial-In User Service) is like a bouncer for your network. Imagine you're trying to get into a club (your network, like Wi-Fi, VPN, or a corporate network). The bouncer (the device you're connecting to, like a Wi-Fi access point or VPN server) doesn't know you personally. Here's how RADIUS helps: Authentication (Who are you?): You tell the bouncer your name and show your ID (you enter your username and password). The bouncer doesn't have a list of all members, so he sends your info to a central "membership office" (the RADIUS server). The RADIUS server checks if your name and ID match its records. Authorization (Can you come in, and what can you do?): If your info is correct, the RADIUS server tells the bouncer, "Yes, this person is a member!" It might also add, "And they are allowed to go to the VIP section" (this is like telling the network device what level of access or services you're allowed). Accounting (What did you do while you were here?): Once you're in, the RADIUS server can also keep a log of what you do: when you entered, when you left, how much data you used, etc. This is for things like billing, monitoring, or security audits. So, in essence, RADIUS provides a centralized way to manage who can access your network, what they can do once they're in, and to keep a record of their activity. This is much more efficient than having to set up separate accounts on every single network device.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
