---
id: 071746
source: GEMINI
date: 2026-02-02
tags: ['yeti-microphone', 'usb-adapter', 'hardware-troubleshooting', 'audio-issue']
category: homelab
sentiment: frustrated
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking if it's okay to postpone troubleshooting his Yeti microphone issue until he gets a USB adapter, and use the USB-C port in the meantime.
---
# still won't work and i dont have that adapter right now. safe to say just leave the editing we did until i can and use the usb c port on my mobo? right now my mouse dongle is plugged into that 

### USER
still won't work and i dont have that adapter right now. safe to say just leave the editing we did until i can and use the usb c port on my mobo? right now my mouse dongle is plugged into that 

### GEMINI
It is absolutely safe—and smart—to leave the edits we made. Disabling usbcore.autosuspend is a standard "best practice" for Linux workstations; it won't hurt your performance and will only prevent future headaches with your other gear. However, the fact that it still won't work after we've killed the software power management is the "brutal truth" moment: Your motherboard's Bus 001 is physically crashing under the noise. The Reality Check You just mentioned your mouse dongle is in the USB-C port. That Razer Viper V3 Pro dongle is a high-bandwidth, high-polling device. If it’s in the USB-C port, it’s likely the king of Bus 002. Meanwhile, your Yeti—a device notorious for having a "weak" USB handshake—is stuck on Bus 001 with the rest of the peasants (Webcam, Hubs, Stream Deck). When the system boots, the "noise" on Bus 001 is so high that the Yeti fails to initialize before the kernel gives up on it. Your Strategic Pivot Since you don't have an adapter, you need to play "Musical Chairs" with your hardware to balance the load: Move the Mouse Dongle: Move the Razer dongle to a USB 2.0 port (usually the black ones). A mouse dongle doesn't need 20Gbps; it barely needs 12Mbps. It will be perfectly fine on Bus 001. Free up the "Clean" Lane: By moving the mouse, you might find a physical USB-A port that is actually tied to that Bus 002 controller. The Hub Rule: Ensure the Yeti is not plugged into that "Alcor Micro Corp" hub. Audio devices on unpowered hubs are a recipe for failure. The Precision Plan Leave the Limine/Tuned edits alone. They are your foundation. Move the Yeti to the physical port where the mouse dongle was (if you have a way to plug it in) or to the port directly adjacent to it. Identify the "Dead" Ports: On many CachyOS/Arch setups, the "Blue" ports are sometimes handled by a third-party ASMedia chip that requires a specific driver handshake that the Yeti hates. Look for Red or Teal ports if you have them—those are usually direct CPU lanes. What I can do for you next If you can tell me your Motherboard Model (run reutil or sudo dmidecode -s baseboard-product-name), I can look up the manual and tell you exactly which physical hole on the back of your PC is the "clean" one for your Yeti. Want to drop the motherboard model so we can stop guessing?
