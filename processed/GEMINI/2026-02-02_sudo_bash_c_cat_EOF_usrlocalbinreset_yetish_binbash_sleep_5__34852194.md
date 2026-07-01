---
id: 239196
source: GEMINI
date: 2026-02-02
tags: ['linux', 'scripting', 'bash', 'yeti-microphone', 'usb-reset']
category: homelab
sentiment: executing
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is creating a bash script to reset his Yeti microphone using usbreset.
---
# ❯ sudo bash -c 'cat <<EOF > /usr/local/bin/reset_yeti.sh
  #!/bin/bash
  sleep 5
  /usr/bin/usbreset 046d:0ab7
  EOF' && sudo chmod +x /usr/local/bin/reset_yeti.sh
[sudo] password for toastedmel0n: 

~
❯ 

### USER
❯ sudo bash -c 'cat <<EOF > /usr/local/bin/reset_yeti.sh
  #!/bin/bash
  sleep 5
  /usr/bin/usbreset 046d:0ab7
  EOF' && sudo chmod +x /usr/local/bin/reset_yeti.sh
[sudo] password for toastedmel0n: 

~
❯ 

### GEMINI
The reason it's still failing is a subtle syntax error in the command I gave you. Because of the spaces before EOF, the shell didn't realize the "here-doc" was over. It probably swallowed your command and did nothing. Let's stop trying to be clever with cat and EOF in a shell that's fighting us. We are going to use a simple, "brute force" printf that works perfectly in Fish, Bash, and Zsh. 1. The "Brute Force" Fix Copy and paste this exactly. It writes the file and sets the permissions in one go: sudo printf "#!/bin/bash\nsleep 5\n/usr/bin/usbreset 046d:0ab7\n" | sudo tee /usr/local/bin/reset_yeti.sh > /dev/null && sudo chmod +x /usr/local/bin/reset_yeti.sh 2. The Verification (Don't skip this) Run this to see the content of the file. It must look like three clean lines: cat /usr/local/bin/reset_yeti.sh It should look like this: #!/bin/bash sleep 5 /usr/bin/usbreset 046d:0ab7 3. Test it now Now try to run it: /usr/local/bin/reset_yeti.sh If it waits 5 seconds and returns to the prompt: You’ve finally won the software battle. If it says "Permission denied": Run sudo chmod 755 /usr/local/bin/reset_yeti.sh. The Advisor's Cold Truth We are doing "surgery" on a $50 microphone's feelings because its hardware is garbage. If the command above works, your autostart entry (~/.config/autostart/yeti-fix.desktop) will finally have a real script to execute. One last check of your blind spots: If you log in and the mic works, but then stops working 10 minutes later, it’s because you didn't Disable C-states or Disable S5 USB Power in the BIOS as we discussed. Those settings are the root cause; the script is just the cleanup crew. Does the cat command show the three lines correctly now? If yes, reboot and enjoy your hands-free microphone.
