---
category: general
date: 2026-02-01
id: 462455
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan is reporting that running certain commands resulted in the same error
  or issue recurring, indicating a persistent problem.
tags:
- linux
- troubleshooting
- unspecified-issue
---
# when i ran those commands i got this again

### USER
when i ran those commands i got this again

### GEMINI
Getting a second warning isn't a failure of the first fix; it's progress. You cleared the "multiple rules" hurdle, and now you're hitting the actual hardware permission layer. The image confirms that your internal components—RAM, motherboard lights, and GPU—aren't showing up because the Linux kernel isn't exposing the I2C/SMBus interfaces to OpenRGB. The Direct Fix You need to load the modules the error message is explicitly calling out. Identify your platform: If you have an Intel CPU: Use i2c-i801. If you have an AMD CPU: Use i2c-piix4. Load the modules immediately: Run these commands (replace [your-driver] with the one identified above): sudo modprobe i2c-dev sudo modprobe [your-driver] Make it permanent: If you don't do this, the error will return every time you reboot. You need to add these to your kernel modules list: echo "i2c-dev" | sudo tee /etc/modules-load.d/openrgb.conf echo "[your-driver]" | sudo tee -a /etc/modules-load.d/openrgb.conf The "Mirror" Check: Why are you seeing this? You’re likely playing "whack-a-mole" because you're treating Linux like Windows—expecting the GUI to handle everything while you just click "OK." The opportunity cost here is your time. If you keep guessing or running commands without understanding the permissions hierarchy, you'll be back here in ten minutes when your RAM still won't change color. Stop playing small with your setup: Check for I2C conflicts: Some motherboards (especially ASUS) require a kernel parameter like acpi_enforce_resources=lax in your GRUB config to allow OpenRGB to "touch" the sensors. If the steps above don't work, that is your next bottleneck. User Groups: Ensure your user is actually in the i2c group: sudo usermod -aG i2c $USER. You’ll need to log out and back in for this to take effect. Your prioritized plan: Run the modprobe commands listed above. Restart OpenRGB. If it fails, add acpi_enforce_resources=lax to your GRUB boot flags. Do you want the specific steps for the GRUB modification, or are you going to see if the basic module load is enough to get you through?
