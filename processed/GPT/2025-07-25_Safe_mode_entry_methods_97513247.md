---
source: GPT
date: 2025-07-25
category: homelab
id: 97513247
linked_nodes: ['nodes/people/bryan.md']
---
# Safe mode entry methods

### ASSISTANT
Got it — you want to boot into Safe Mode *manually* without using the forced shutdown (three consecutive forced power offs) method.

Here are a couple of manual ways that don’t rely on forced shutdowns:

### 2. Use **msconfig** to force Safe Mode next boot (if you can open Run or Task Manager)

- Press `Windows + R` to open Run  
- Type `msconfig` and hit Enter  
- Go to the **Boot** tab  
- Under **Boot options**, check **Safe boot** and select **Minimal**  
- Click OK and reboot  
- PC boots into Safe Mode  

*Remember to undo this after by unchecking Safe boot in msconfig.*

**If none of these work because your PC is too slow to do anything, then the forced shutdown method is the fallback**, but if you can get to login or desktop even briefly, **Shift + Restart** is usually the most reliable and clean manual method.

### ✅ Method: Use the **System Configuration (msconfig)** Tool

**This works even if your system is laggy but responsive enough to launch something.**

1. **Press `Ctrl + Shift + Esc`** to open **Task Manager**.
2. In Task Manager, go to **File > Run new task**.
3. Type: `msconfig` and hit Enter.
4. Go to the **Boot** tab.
5. Check the box **"Safe boot"** and choose:
   - **Minimal** for regular Safe Mode
   - **Network** for Safe Mode with internet
6. Click **Apply** and **OK**, then **Restart** when prompted.

> On next boot, you’ll be in Safe Mode automatically.

To **exit Safe Mode** later:
- Open `msconfig` again in Safe Mode.
- Uncheck **"Safe boot"** in the Boot tab.
- Apply and restart.

### 🛠 Method: Use a Bootable USB to Access Recovery

1. **Create a Windows 10/11 bootable USB** on another computer using the [Windows Media Creation Tool](https://www.microsoft.com/software-download/windows10).
2. Plug it into your affected PC and boot from USB.
3. On the Windows Setup screen, click **"Repair your computer"** (bottom left).
4. Go to:
   - **Troubleshoot > Advanced options > Startup Settings > Restart**
5. After the PC restarts, press the key for **Safe Mode (usually 4 or F4)**.

### 1. Use Windows Recovery Environment (WinRE) via Automatic Interrupt

If the normal Windows environment is basically frozen and you can’t interact:

- **Force three consecutive power-offs** during the boot process:
  - Power on the PC, as soon as Windows tries to load, hold the power button until it shuts off.
  - Repeat this 3 times.
- On the 4th boot, Windows should detect the repeated failure and boot into **Recovery Environment** automatically.

From there, you can go:

**Troubleshoot > Advanced options > Startup Settings > Restart**  
Then press **4 (Safe Mode)**.

### Why this helps:

Both methods let you get into Safe Mode *without* needing your slow, buggy Windows environment to be responsive.

### 🛠 If You *Can't* Open Anything Normally:
Use **Command Prompt** from the recovery environment:

#### 1. Try booting to Windows Recovery:
If your PC is sluggish but still loads the login screen or desktop eventually:

- Hold `Shift` and click **Restart** (from Start menu > Power button > Restart).
- This should bring you to the **Recovery Menu**.

#### 2. From Recovery Menu:
- Click: **Troubleshoot** > **Advanced Options** > **Startup Settings** > **Restart**
- Then press `4` or `F4` to boot into Safe Mode.

Let me know if you’re stuck at a specific step, and I’ll guide you through.

### USER
i want to get my pc in safe mode to fix the driver issue (pc super slow can't get into many menus/do anything). how do i do that without doing the forced shut down method? it boots up too quick for me to catch it?

### ASSISTANT
Good question! 

Booting into Safe Mode **won't directly fix the slowness or bugs** from the Windows update itself, but it *does* help by:

- Loading Windows with only essential drivers and services
- Disabling third-party programs and problematic drivers that could be causing the slowdowns or freezes

This makes Safe Mode an ideal environment to:

- Troubleshoot what’s causing the slowness (like a bad driver or software conflict)
- Run tools like **Device Manager** to uninstall or roll back faulty drivers
- Run **System Restore** to revert to a point before the update if available
- Run virus scans or cleanup tools without interference

**Safe Mode doesn’t “fix” the update itself**, but it gives you a stable, minimal environment where you *can* fix or undo things safely.
---
## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]