---
id: 422631
source: GEMINI
date: 2026-01-19
tags: ['docker', 'installation-verification', 'service-status', 'wsl']
category: ai-tools
sentiment: building
resolution: resolved
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan verified Docker was installed and running successfully on his WSL environment by checking version and service status.
---
# this is what we have so far: toastedmelon@DESKTOP-NG2I0P2:~$ docker --version
Docker version 29.1.5, build 0e6fee6
toastedmelon@DESKTOP-NG2I0P2:~$ sudo service docker status
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Mon 2026-01-19 12:58:32 EST; 46s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 43520 (dockerd)
      Tasks: 15
     Memory: 24.9M (peak: 29.5M)
        CPU: 182ms
     CGroup: /system.slice/docker.service
             └─43520 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.466652776-05:00" level=info msg="Restoring containers: start."
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.504413400-05:00" level=info msg="Deleting nftables IPv4 rules" error="exit >
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.528242502-05:00" level=info msg="Deleting nftables IPv6 rules" error="exit >
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.715099090-05:00" level=info msg="Loading containers: done."
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.719815602-05:00" level=info msg="Docker daemon" commit=3b01d64 containerd-s>
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.720032134-05:00" level=info msg="Initializing buildkit"
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.755841516-05:00" level=info msg="Completed buildkit initialization"
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.760121191-05:00" level=info msg="Daemon has completed initialization"
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.760167845-05:00" level=info msg="API listen on /run/docker.sock"
Jan 19 12:58:32 DESKTOP-NG2I0P2 systemd[1]: Started docker.service - Docker Application Container Engine.
lines 1-22/22 (END)

### USER
this is what we have so far: toastedmelon@DESKTOP-NG2I0P2:~$ docker --version
Docker version 29.1.5, build 0e6fee6
toastedmelon@DESKTOP-NG2I0P2:~$ sudo service docker status
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Mon 2026-01-19 12:58:32 EST; 46s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 43520 (dockerd)
      Tasks: 15
     Memory: 24.9M (peak: 29.5M)
        CPU: 182ms
     CGroup: /system.slice/docker.service
             └─43520 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.466652776-05:00" level=info msg="Restoring containers: start."
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.504413400-05:00" level=info msg="Deleting nftables IPv4 rules" error="exit >
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.528242502-05:00" level=info msg="Deleting nftables IPv6 rules" error="exit >
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.715099090-05:00" level=info msg="Loading containers: done."
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.719815602-05:00" level=info msg="Docker daemon" commit=3b01d64 containerd-s>
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.720032134-05:00" level=info msg="Initializing buildkit"
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.755841516-05:00" level=info msg="Completed buildkit initialization"
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.760121191-05:00" level=info msg="Daemon has completed initialization"
Jan 19 12:58:32 DESKTOP-NG2I0P2 dockerd[43520]: time="2026-01-19T12:58:32.760167845-05:00" level=info msg="API listen on /run/docker.sock"
Jan 19 12:58:32 DESKTOP-NG2I0P2 systemd[1]: Started docker.service - Docker Application Container Engine.
lines 1-22/22 (END)

### GEMINI
You have successfully crossed the finish line. The output shows Active: active (running) and you’re on version 29.1.5. You stopped guessing and started executing properly. However, you are still inside a "locked room"—the (END) at the bottom of your screen means you are stuck in the systemctl pager. Press q on your keyboard to get your terminal prompt back. The Automation Move (Next Level Efficiency) Right now, if you restart your computer or shut down WSL, Docker will likely not start by itself when you come back. You’ll be back here typing sudo service docker start like a novice. To ensure Docker is always ready when you open your terminal, add the start command to your .bashrc file. Run this command to automate the startup: echo "sudo service docker start" >> ~/.bashrc Note: Because this requires sudo, it may ask for your password the first time you open a new terminal window. This is the trade-off for not using Docker Desktop on Windows. The Direct Truth: What’s Next? You have the tool installed, but you haven't built anything yet. Having Docker installed and not running a container is like owning a Ferrari and leaving it in the garage because you’re afraid to drive. Your immediate priority list: Test the engine: Run sudo docker run hello-world to confirm you can actually pull images from the internet. Fix Permissions: If you haven't already, run sudo usermod -aG docker $USER so you can stop typing sudo for every command. Learn the Architecture: You need to understand how the Docker Client, Host, and Registry interact, or you will be back here confused the moment a port mapping fails. Would you like me to explain the most common Docker commands you'll actually use for development, or are you ready to try running your first real web server (like Nginx) in a container?
