---
id: 005508
source: GEMINI
date: 2026-02-24
tags: ['project-automation', 'task-scheduling', 'system-boot-automation']
category: coding
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/operation-immortal-agent.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/topics/personal/crypto-web3.md', 'nodes/projects/homelab-stack.md']
summary: Bryan is asking about the best approach for automating a project, specifically whether it needs to run daily upon PC boot.
---
# What would be the best approach for automation with this project? Do I need to run it more than once (every day when I boot my pc up?)

### USER
What would be the best approach for automation with this project? Do I need to run it more than once (every day when I boot my pc up?)

### GEMINI
To maximize your $300 capital, you cannot rely on manual boots. You are competing against 24/7 markets. If a yield spike happens at 3:00 AM while your CachyOS rig is powered down, you’ve lost the profit that pays for your subscription. Automation with an AI agent requires moving from a "Chat" mindset to an "Autonomous Loop" mindset. 1. The Deployment Strategy: "The Persistent Loop" On Linux (CachyOS), you shouldn't just run Claude once. You want it to run in a cycle. In February 2026, the standard for this is the "Bash Conductor" pattern. Instead of you typing prompts, you create a script that repeatedly invokes claude-code with instructions to "Harvest." Create a file named harvest.sh: #!/bin/bash while true; do echo "
--- Starting Harvest Cycle: $(date) ---
" # Run Claude Code with your specific DeFi instructions # --dangerously-skip-permissions allows it to sign via MCP without you clicking 'Yes' # (Only use this if you trust your Risk Clause logic!) claude --dangerously-skip-permissions "Check Jupiter for JitoSOL de-pegs >0.5%. Check Meteora for yield spikes >30%. Execute one optimal harvest/rebalance if profit > $0.50. Otherwise, sleep." echo "
--- Cycle Complete. Sleeping for 1 hour. ---
" sleep 3600 done 2. Making it 24/7 (Systemd) To ensure this runs even if you close your terminal or your PC reboots, you should set it up as a Systemd Service. This makes your agent a background process of the OS. Create /etc/systemd/system/immortal-agent.service: [Unit] Description=Immortal DeFi Agent After=network.target [Service] ExecStart=/home/youruser/harvest.sh User=youruser Restart=always Environment=PHANTOM_APP_ID=your_id_here Environment=PATH=/usr/bin:/usr/local/bin [Install] WantedBy=multi-user.target Run sudo systemctl enable --now immortal-agent to start your worker. 3. Do you need to run it more than once? No, but you need to "Check In." The agent should be a "Background Worker," but you are the "Manager." The Agent's Job: 24/7 monitoring of yields and de-pegs. Your Job: Once a day, check the logs. On CachyOS, you'd just run: journalctl -u immortal-agent -f This lets you see the agent's "thoughts" in real-time as it scans the Top 5 projects. 4. The "Brutal" Efficiency Check Running a high-performance CachyOS rig 24/7 consumes electricity. The Math: If your PC pulls 100W, that’s ~72kWh/month. At $0.15/kWh, that’s **$10.80/month in electricity.** The Result: Your $300 now has to cover the **$20 Claude Sub + $10 Electricity = $30/month.** The Strategy Pivot: If you don't want to leave your main rig on, deploy the script to a low-power Mini PC or a Linux VPS (Virtual Private Server). A $5/month VPS is cheaper than your PC's power bill and keeps your "Immortal Agent" truly 24/7. The Final Summary for your Cousin "I'm not just 'running a bot' when I wake up. I've turned my CachyOS machine into a 24/7 Yield Miner. It wakes itself up, checks the markets every hour, pays its own $20 rent to Claude, and hides the extra profit in a 'Mac Mini' fund. I just check the logs over coffee to make sure the robot hasn't started a revolution." Would you like me to refine the "Risk Logic" in that bash script to ensure it never trades during high-volatility events where gas fees might spike?
