---
source: GPT
date: 2025-10-23
category: ai-tools
id: 40951358
linked_nodes: ['nodes/people/bryan.md']
---
# Repartition USB for BIOS

### ASSISTANT
Great—thanks for the detail. You’ve already done the hard part by cleaning the drive. For your entity["motherboard_model", "ASUS PRIME Z690-P WiFi", 0] (or the D4 variant) and BIOS update approach, here’s how to pick the *correct format* and setup so it works reliably:

### 🎯 How to format it accordingly  
Since you have a large (128 GB) drive, Windows’ built-in “Format” GUI may not give FAT32 as an option (Windows often limits FAT32 to ≤32 GB). Here’s how to do it:

**Option A – Using DiskPart (continued from your cleaning)**  
1. After your `clean` step in DiskPart, execute:  
   ```
   create partition primary
   format fs=fat32 quick
   assign
   exit
   ```
   This will format the whole drive as FAT32.  
2. Copy the renamed BIOS file (for your board) to the root of the drive.

**Option B – Use a third‐party tool**  
If DiskPart refuses FAT32 on 128 GB (sometimes happens), you can use tools like Rufus or “Fat32format” to force‐format a large drive as FAT32.

If you like, I can check the exact FAQ section for the PRIME Z690-P WiFi (or D4 version) on ASUS’s site and pull the exact formatting requirement for *that model* just to be sure. Would you like me to do that?

### USER
so for the thumbdrive i have 4.42 gb RAW, 13mb healthy and 112.13 gb unallocated

### USER
so i did everything up to the clean step and it went through. DiskPart succeeded in cleaning the disk. what i want to ensure before we get into step 6 is the proper format for the drive. the motherboard i'm running is the asus prime z690-p wifi. i have the bios file (Version 3801; released 2025/05/29; SHA-256 ：6E3550F3EC97F181EEC2CFEFA70CC637C073B760D1A237AB30BD661CCBEE420F )

### ASSISTANT
Perfect — you’re in the home stretch.  
Since you’ve got the **ASUS PRIME Z690-P WIFI (DDR5)** board, here’s your exact, no-guesswork walkthrough to safely update your BIOS.  

### 🧩 What You Should Have Ready
✅ Your USB drive:
- Formatted as **FAT32 / MBR** (you’ve already done this 👍)  
- Contains only one file: the renamed **`.CAP`** BIOS file (for example: `PRIMEZ690PWIFI.CAP`)  
- Plugged into a **rear USB 2.0 port** on the motherboard (these are the most reliable for updates).

✅ Your system:
- Plugged into stable power — don’t turn it off mid-update.  
- Ideally at **default/stock settings** (no overclocking active).

### 🧰 Optional: Post-Update Steps
After a successful update:
1. Go into BIOS → press **F5** to load “Optimized Defaults.”  
2. Press **F10** to save and reboot.  
3. Back in Windows, confirm your BIOS version:  
   - Press `Win + R`, type `msinfo32`, and check **BIOS Version/Date**.  

If you’d like, I can double-check what your **renamed file should be called exactly** (the one ASUS EZ Flash expects). Want me to verify that for the *PRIME Z690-P WIFI (DDR5)* model from the official ASUS download page?

### USER
when i ran the create partition primary command it pulled up the format menu and only allows 116gb, and only gives me the options for exFAT and NTFS

### ASSISTANT
Hey there! How's it going? What's on your mind today?{'asset_pointer': 'sediment://file_000000003df861f6bcdd77eb995d371b', 'content_type': 'audio_asset_pointer', 'expiry_datetime': '2026-04-21T16:56:31.114377+00:00', 'format': 'wav', 'metadata': {'end': 3.3, 'end_timestamp': None, 'interruptions': None, 'original_audio_source': None, 'pretokenized_vq': None, 'start': 0.0, 'start_timestamp': None, 'transcription': None, 'word_transcription': None}, 'size_bytes': 158478, 'tool_audio_direction': None}

### ASSISTANT
Absolutely! One of the easiest ways is to use Windows Disk Management. You can plug in your thumb drive, then right-click on the Start menu and choose "Disk Management." From there, you can find your drive, delete any existing partitions, and then create a new partition that uses the full capacity. You can format it as FAT32 or NTFS,{'asset_pointer': 'sediment://file_00000000de4c61f6b78dfc44d4ba086d', 'content_type': 'audio_asset_pointer', 'expiry_datetime': '2026-04-21T16:58:43.781683+00:00', 'format': 'wav', 'metadata': {'end': 19.0, 'end_timestamp': None, 'interruptions': None, 'original_audio_source': None, 'pretokenized_vq': None, 'start': 0.0, 'start_timestamp': None, 'transcription': None, 'word_transcription': None}, 'size_bytes': 912078, 'tool_audio_direction': None}

### USER
So I'm looking to update my BIOS, and I have a thumb drive to put the file on, but for whatever reason, it's supposed to be a... give me one second... it's supposed to be... I don't know what size this is supposed to be. Oh, it's supposed to be 128 gigs, and it says that it only had four gigs when I tried to format it, and it didn't work because there's something blocking it. So I need to repartition it so I have the full thing, and then start from there, and then I want to update my BIOS from that point.{'audio_asset_pointer': {'asset_pointer': 'sediment://file_00000000462861f68972a46596d35064', 'content_type': 'audio_asset_pointer', 'expiry_datetime': '2026-04-21T16:58:11.376123+00:00', 'format': 'wav', 'metadata': {'end': 36.58, 'end_timestamp': None, 'interruptions': None, 'original_audio_source': None, 'pretokenized_vq': None, 'start': 0.0, 'start_timestamp': None, 'transcription': None, 'word_transcription': None}, 'size_bytes': 1755918, 'tool_audio_direction': None}, 'audio_start_timestamp': 81.26908616899891, 'content_type': 'real_time_user_audio_video_asset_pointer', 'expiry_datetime': '2026-04-21T16:58:11.376123+00:00', 'frames_asset_pointers': [], 'video_container_asset_pointer': None}

### USER
so from having the .cap file in the usb root and everything being renamed, what do i need to do next to update my bios? again i'm rocking the PRIME Z690-P WIFI motherboard (DDR5)

### USER
so i did the rufus steps and now my drive has two files in it. it has an autorun ICO file and then another autorun file that the type is specified as a setup info file?

### USER
to clarify this is a 128gb thumb drive. it won't let me delete any of those partitions i mentioned earlier either

### ASSISTANT
Ah — perfect, that actually explains exactly what’s going on. 👍  

Here’s what’s happening:  
- **4.42 GB RAW** → This is an old or corrupted partition. “RAW” means it’s not formatted properly.  
- **13 MB Healthy** → Likely a leftover EFI or system partition (tiny and useless in your case).  
- **112.13 GB Unallocated** → That’s the actual free space of your drive that’s not being used yet.

Let’s fix it so your thumb drive becomes one clean, usable volume:  

### 🧑‍💻 Option 2: If Disk Management won’t delete partitions  
Run **DiskPart** (Windows built-in tool):

1. Press `Win + R`, type `cmd`, right-click → **Run as Administrator**.  
2. Enter these commands carefully:  
   ```bash
   diskpart
   list disk
   select disk X       # replace X with the number of your USB drive
   clean
   create partition primary
   format fs=exfat quick
   assign
   exit
   ```
   ⚠️ **Double-check** you selected the correct disk before typing `clean` — it erases everything on that drive.

### 🧨 Step-by-Step: Fully Reset the 128GB Thumb Drive Using DiskPart

1. Plug in the USB drive.  
2. Press **`Win + R`**, type `cmd`, right-click it, and choose **“Run as administrator.”**  
3. Type the following commands **one line at a time** (press Enter after each):

   ```bash
   diskpart
   list disk
   ```

   → Look carefully at the **list** — identify which one is your USB (based on size, likely around 115–119 GB).  
   Example:  
   ```
   Disk 0   476 GB
   Disk 1   128 GB
   ```
   You’d want to select the one that matches your thumb drive.

4. Once you’re sure which disk is the USB, type:
   ```bash
   select disk X
   ```
   (Replace **X** with the number of your USB drive.)

5. Now **the critical command** — this will completely wipe all partitions and hidden formatting:
   ```bash
   clean
   ```

   If this fails with a protection error, try:
   ```bash
   attributes disk clear readonly
   clean
   ```

6. Once it succeeds, create a new usable partition:
   ```bash
   create partition primary
   format fs=exfat quick
   assign
   exit
   ```

7. Open **File Explorer** — you should now see a clean, single 128GB drive again.  

Would you like me to add the steps for forcing a **FAT32** format too, just in case your BIOS update needs that?

### ASSISTANT
Perfect — you’re right at the finish line here, and this is a super common roadblock.  

Windows **doesn’t let you format drives larger than 32 GB as FAT32**, even though the BIOS itself *can* read FAT32 on larger drives. That’s why you only see **exFAT** and **NTFS** right now.  

Let’s fix that cleanly 👇  

## 🧱 Step 2: Use a FAT32 Formatter That Supports Large Drives  
You’ll now use a tool that can format >32 GB as FAT32 (Windows’ built-in one can’t).  
Here are two proven methods:

### ✅ **Option B — Use fat32format (command-line tool)**
1. Download **guiformat.exe** (the graphical version of fat32format):  
   👉 [https://ridgecrop.co.uk/index.htm?guiformat.htm](https://ridgecrop.co.uk/index.htm?guiformat.htm)  
2. Run it as Administrator.  
3. Select your USB drive letter.  
4. Choose **Allocation Unit Size = 32768 (default)**.  
5. Make sure “Quick Format” is checked.  
6. Click **Start** → it will format the full 128 GB as FAT32.  

Once that’s done, you can safely copy your BIOS file (e.g., `PRIMEZ690P.CAP`) to the root of the drive.  
Then you’re ready for **EZ Flash** inside BIOS (or **BIOS FlashBack** if your board supports it).

### 🧩 What those files are:
- **`autorun.ico`** — a small icon file Rufus drops in so that the USB drive has a custom icon in File Explorer.  
- **`autorun.inf`** — a simple text file that tells Windows, “use this icon when showing this USB.” It’s basically just metadata.  

They **don’t affect the BIOS update** in any way.  
You can **delete both** if you want the drive completely empty, or just leave them — the motherboard’s BIOS ignores them either way.  

Then you can:
- Plug it into the **rear I/O USB port** (not front panel, not USB-C).
- Boot into BIOS → open **Tool → ASUS EZ Flash 3 Utility** → pick your USB → select the `.CAP` file → update.
---
### ASSISTANT
Got it! Yeah, sometimes USB drives can get stuck with leftover partitions or hidden partitions that limit their capacity. You can try using something like Disk Management on Windows or a tool like Rufus or GParted to clear everything out and reformat it properly. Once it's clean, you should be able to use the full capacity and then proceed with your BIOS update. If you need any detailed steps, just let me know!{'asset_pointer': 'sediment://file_00000000c01061f689270b224f7d2c1d', 'content_type': 'audio_asset_pointer', 'expiry_datetime': '2026-04-21T16:58:11.376193+00:00', 'format': 'wav', 'metadata': {'end': 23.45, 'end_timestamp': None, 'interruptions': None, 'original_audio_source': None, 'pretokenized_vq': None, 'start': 0.0, 'start_timestamp': None, 'transcription': None, 'word_transcription': None}, 'size_bytes': 1125678, 'tool_audio_direction': None}


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]