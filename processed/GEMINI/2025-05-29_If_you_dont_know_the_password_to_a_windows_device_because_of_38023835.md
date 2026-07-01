---
category: homelab
date: 2025-05-29
id: 422894
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking about the correct method to reset a Windows device password
  when locked out by a BIOS admin password.
tags:
- windows-password-reset
- bios-password
- cmos-replacement
- system-security
---
# If you don’t know the password to a windows device because of bios admin password you would replace cmos yes?

### USER
If you don’t know the password to a windows device because of bios admin password you would replace cmos yes?

### GEMINI
If you don't know the BIOS admin password on a Windows device, removing the CMOS battery can sometimes reset the BIOS settings, including the password, to their factory defaults. This is a common troubleshooting step. Here's how it generally works and why it might (or might not) succeed: CMOS (Complementary Metal-Oxide-Semiconductor) Memory: The BIOS settings, including the password, are stored in a small amount of memory called CMOS. This memory is kept alive by a small, coin-cell battery (the CMOS battery) on the motherboard, even when the computer is turned off. Removing the CMOS Battery: When you remove the CMOS battery and leave it out for a short period (usually 15-30 minutes, or even less on some modern boards, but sometimes longer is recommended to ensure all residual power drains), the CMOS memory loses power and clears its stored settings. When power is restored (by reinserting the battery), the BIOS typically defaults to its factory settings, which would include no password. Other Methods: CMOS Jumper: Many motherboards have a "CLR_CMOS" or "RESET" jumper. Moving this jumper to a specific position for a few seconds can also clear the CMOS settings without removing the battery. This is often the preferred method as it's less invasive. Manufacturer-Specific Backdoors/Utilities: Some manufacturers might have specific backdoor passwords or tools to reset BIOS passwords, but these are less common and often require contacting support and proving ownership. Third-Party Tools: There are some third-party tools that claim to be able to reset BIOS passwords, but their effectiveness varies greatly, and they can be risky to use. Important Considerations and Caveats: Modern Laptops and Desktops: Increasingly, especially on modern laptops and some desktops, simply removing the CMOS battery or using a jumper might not clear the BIOS password. Manufacturers have implemented more robust security measures to prevent unauthorized access. The password might be stored in non-volatile memory (NVRAM) or other security chips that are not reset by clearing the CMOS. Physical Access Required: All these methods require physical access to the inside of the computer. Loss of Other Settings: Clearing the CMOS will reset all BIOS settings to their defaults. This means you might need to reconfigure things like boot order, date/time, and other specific hardware settings. Potential for Damage: If you're not comfortable working inside a computer, you could accidentally damage components. Windows Password vs. BIOS Password: It's crucial to distinguish between a BIOS password and a Windows login password. Clearing the BIOS password will not remove a Windows login password. You'll still need to deal with the Windows password separately if you don't know it (e.g., using a password reset disk, or reinstallation in extreme cases). Warranty: Tampering with the internal components might void your warranty. In summary: While removing the CMOS battery (or using a CMOS jumper) is a valid and often effective method for resetting a forgotten BIOS admin password on many older or less secure systems, it's not a guaranteed solution for all modern devices. If you're dealing with a modern device or a highly secure system, you might need to contact the manufacturer's support for specific instructions or a professional technician.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
