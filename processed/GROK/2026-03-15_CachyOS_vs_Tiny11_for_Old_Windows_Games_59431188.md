---
id: 917260
source: GROK
date: 2026-03-15
tags: ['cachyos', 'tiny11', 'dual-boot', 'windows-gaming-on-linux', 'fortnite', 'rocket-league']
category: homelab
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/homelab-stack.md']
summary: Bryan was deciding whether to keep CachyOS or switch to Tiny11 for playing Windows-exclusive games like Fortnite and Rocket League, and exploring dual-boot options.
---
# CachyOS vs Tiny11 for Old Windows Games

### HUMAN
Really missing some of the windows games I used to play. Worth keeping cachyos or should I switch to tiny 11?

### ASSISTANT
It really depends on what specific old Windows games you're missing and how much hassle you're willing to tolerate for potentially better performance or a lighter system.

**CachyOS (Arch-based Linux, performance-optimized)** is actually surprisingly strong for older Windows games in 2026. Many users report that classics run **better** on it than modern Windows due to Proton/Wine compatibility layers handling legacy quirks more cleanly—no weird compatibility mode conflicts, no forced updates breaking things, and often smoother behavior. CachyOS ships with Proton-CachyOS (a tuned fork with extra patches for gaming), Wine tweaks, and gaming meta packages that make setup straightforward via Steam + Lutris/Bottles for non-Steam titles.

- Older DirectX 9/older titles frequently hit Gold/Platinum on ProtonDB (near-perfect or better-than-Windows).
- Some people specifically say old Windows games feel "actually better" on CachyOS because Windows itself has accumulated compatibility baggage over time.
- Performance can match or beat Windows in CPU-bound/older scenarios, with snappier system feel overall (especially if your hardware isn't bleeding-edge Nvidia).
- Downsides: If any of your games have kernel-level anti-cheat (rare for truly old titles), they won't work. Setup might need tweaks for edge cases (Proton version, launch options, or Gamescope for some).

**Tiny11** (stripped-down, debloated Windows 11) gives you native Windows compatibility with almost zero effort. Your old games will just work exactly like they used to—no layers, no Proton tinkering. It's lightweight (can run on very low RAM/disk compared to stock Win11), skips bloat/telemetry/Microsoft account nonsense, and bypasses Win11 hardware checks, so it's great if you're on older hardware and just want "Windows but less annoying."

- Perfect for 100% compatibility, especially if games rely on very specific Windows APIs, old DRM, or non-Steam launchers that hate Wine.
- Gaming performance is native, so no translation overhead (though for old games, that overhead is tiny anyway on Linux).
- Downsides: Still Windows underneath—so ads/telemetry can creep back with updates, forced features might return, and it's not as snappy/system-optimized as a tuned Linux distro like CachyOS. Security/support is unofficial (modified ISO).

**Quick recommendation**:
- If the games are **mostly Steam-based old titles** (or run well via Lutris/Wine), stick with **CachyOS**. You'll likely get a nicer experience overall—faster OS, better for retro gaming quirks, no Windows telemetry/ads, and community reports often favor Linux for pre-2010s stuff.
- If you have a few stubborn games that refuse to cooperate on Proton (check ProtonDB for your exact titles), or you just want zero friction and native everything, switch to **Tiny11**. It's the safer "set it and forget it" path for pure old-Windows nostalgia.

What games are you specifically missing? Titles like old-school stuff (e.g., Diablo II, Half-Life, Age of Empires, etc.) almost always run flawlessly on modern Proton setups. If you name a couple, I can give a more targeted take. Either way, both are solid choices in 2026—Linux gaming has come a long way, but native Windows still wins on raw plug-and-play for some legacy edge cases.

### HUMAN
Primarily Fortnite, rocket league, etc is what I’m referring to but I’m loving cachy otherwise

### ASSISTANT
Fortnite and Rocket League are both competitive multiplayer titles with anti-cheat systems, which makes them trickier on Linux than single-player or older games.

**Fortnite** (Epic Games launcher, kernel-level Easy Anti-Cheat):  
Unfortunately, it doesn't run natively or reliably via Proton/Wine on Linux in 2026. Epic has not enabled full kernel-level anti-cheat support for their own game on Proton/Linux (despite EAC technically supporting it for other devs). Community reports and checks (including ProtonDB searches) show it's effectively blocked or unplayable online—many sources confirm you can't play it directly on Linux without workarounds like cloud gaming (GeForce Now, Xbox Cloud, etc.). If Fortnite is a must-play game for you (especially with friends or competitively), this is the big blocker.

**Rocket League** (now Epic-owned, but Steam-available):  
This one is much better news! It runs great on Linux via Proton. The native Linux build was dropped years ago, but the Windows version through Proton works perfectly—including online multiplayer. Recent updates (as of early 2026) added Easy Anti-Cheat, but Psyonix explicitly confirmed it would still support Linux/Proton/Steam Deck without breaking it. ProtonDB reports consistently show it as Gold/Platinum rated: "just works," excellent performance (often better than Windows due to lower overhead), no major issues with multiplayer. Use GE-Proton or Proton-CachyOS for the smoothest experience—many users say it feels snappier on tuned Arch distros like CachyOS.

Since you're already loving CachyOS otherwise (great choice for performance—optimized kernel, scheduler tweaks, etc.), and Rocket League is your other main one, I'd lean toward **sticking with CachyOS** for now.

- Rocket League: Zero drama, native-feeling multiplayer.
- Fortnite: The pain point— you'd need to dual-boot Windows (or Tiny11) just for it, or stream via cloud services (which works surprisingly well if your internet is solid in Akron—low latency to NA East servers).

If Fortnite is the primary game you're missing and you play it a lot, Tiny11 would give you seamless native access to both (plus any other Epic/Steam stuff) with a super-light Windows install—no bloat, no forced updates nagging you. But if Rocket League is more frequent and Fortnite is occasional (or you're okay streaming it), CachyOS keeps delivering the snappy, ad-free, customizable experience you're enjoying.

Quick tips if staying on Cachy:
- For Rocket League: Install via Steam, force Proton Experimental or GE-Proton in properties. Add launch options if needed (rarely required).
- For Fortnite: Try Heroic Games Launcher (flatpak or AUR) to manage Epic library—some report partial success offline/single-player modes, but online is a no-go without cloud.

How often do you play each? If Fortnite dominates, dual-boot might be worth it (CachyOS plays nice with Windows partitions). Otherwise, enjoy the penguin life—Linux gaming in 2026 is killer for most titles! 🐧

### HUMAN
Overall?

### ASSISTANT
Overall, **stick with CachyOS**—it's the better choice for you right now, especially since you're already loving it and Fortnite isn't fully playable on Linux anyway.

Here's the breakdown based on the current 2026 status:

- **Rocket League**: Runs excellently on Linux via Proton. Psyonix explicitly confirmed that even after adding Easy Anti-Cheat (EAC) in early 2026, Proton/Linux/Steam Deck support remains intact. ProtonDB and community reports show it's Gold/Platinum—smooth multiplayer, often better performance than Windows due to lower overhead. On CachyOS specifically, use Proton-CachyOS (their tuned fork) or GE-Proton for the best results. Some users hit snags with Heroic Launcher setups (low FPS/input lag in isolated cases), but switching to Steam + Proton fixes it for most. If you're getting issues, force Proton Experimental/GE in Steam properties and tweak launch options if needed—it's very reliable.

- **Fortnite**: Still a hard no for native/online play on Linux. Epic deliberately blocks it (despite EAC technically supporting Linux for other games)—they haven't enabled full kernel-level support for Fortnite itself, and there's active detection to prevent Proton/Wine runs on official servers. Recent sources (ProtonDB, Reddit, GamingOnLinux) confirm it's unplayable directly: crashes, bans, or outright refusal to launch multiplayer. Workarounds like private servers (EZFN for old seasons) exist but aren't the real Fortnite experience. Cloud streaming (GeForce Now, Xbox Cloud) works well as an alternative if your internet in Akron is decent—low-latency to NA East, no install hassle.

Since Fortnite is blocked regardless of distro (Tiny11/Windows wouldn't change that on Linux side, but switching to Tiny11 would let you play it natively), and Rocket League thrives on CachyOS, there's no strong reason to abandon what you enjoy about the OS: snappy performance, no bloat/telemetry, optimized kernel/scheduler for gaming, and that penguin vibe 🐧.

**Best path forward on CachyOS**:
- Keep Rocket League on Steam with Proton-CachyOS enabled (install via CachyOS Hello gaming meta if not already).
- For Fortnite: Stream via GeForce Now (free tier available, or paid for better queues/resolution) or Xbox Cloud if you have Game Pass. It's surprisingly solid for battle royale on good connections.
- If Fortnite becomes a daily must-have and streaming doesn't cut it, consider a simple dual-boot setup (CachyOS + Tiny11/Windows on separate partitions). GRUB handles it easily, and you reboot only when needed—many Linux gamers do this for 1-2 stubborn titles.

CachyOS gives you the superior daily driver experience for most things (including your other old Windows nostalgia games via Proton), while the one big miss (Fortnite) has the same limitation everywhere outside native Windows. Enjoy the setup you're happy with—Linux gaming keeps getting stronger, and you're already in a great spot! If Rocket League feels off or you want specific tweaks, drop details and I can help refine. 🚀

### HUMAN
On one drive? I know they don’t play well together?

### ASSISTANT
Yeah, you're spot on—**Microsoft OneDrive** and **Linux** (including CachyOS) don't "play well together" in the same seamless, native way they do on Windows. There's no official Microsoft client for Linux, so you rely on third-party open-source tools, which can be solid but come with quirks, especially if you're expecting full two-way sync, tray icons, or zero-maintenance behavior like on Windows.

In 2026, the situation is pretty good overall thanks to community efforts, but it's not perfect:

- The most popular and actively maintained option is the **abraunegg/onedrive** client (often just called "onedrive" in repos/AUR). It's free, open-source, supports personal, business, and SharePoint accounts, and handles two-way sync reliably for most users. On Arch-based distros like CachyOS, you can install it from the AUR (e.g., `onedrive-abraunegg` package) or build from GitHub. Many CachyOS users on the forum and Reddit report success with it—tray icons work after adding deps like `qt5-svg`, and sync is stable once configured (e.g., via `onedrive --monitor` for background running). There are occasional bugs like case-insensitive filename conflicts or resume-from-sleep issues (especially with mounts), but updates keep fixing them.

- Another strong contender is **onedriver** (from AUR: `onedriver`), which mounts OneDrive as a native filesystem (FUSE-based)—great for Dolphin/Nautilus integration without full sync overhead. It has a nice GUI for setup and auto-mounting. Users say it's snappier for browsing large folders, though sync might feel less "automatic" than abraunegg's.

- For KDE users on CachyOS (assuming Plasma since it's common), there's also **gvfs-onedrive** in the repos for built-in GNOME-style integration (might need tweaks for full KDE Dolphin support).

No major gaming/Proton conflicts show up in reports—OneDrive sync doesn't interfere with Steam/Proton games unless you're storing game files/saves directly in a synced folder (which can cause lockups or slow performance if files are large/changing often). Just exclude game folders from sync if needed (easy in config files).

**Quick setup tips for CachyOS**:
1. Install via AUR helper (e.g., `yay -S onedrive-abraunegg` or `onedriver`).
2. Run `onedrive` once to auth (it opens a browser for Microsoft login).
3. Configure sync (e.g., `onedrive --synchronize --resync` first time, then `--monitor` for background).
4. For tray/icon: Install any missing deps like `qt5-svg` and restart.
5. If issues: Check the GitHub repo for config tweaks (skip certain folders, selective sync).

If you just need occasional access (not constant sync), browser works fine, or use rclone for mounting (but that's more manual).

Bottom line: It works well enough for daily use on CachyOS (better than ever in 2026), but expect a bit more setup and occasional hiccups compared to Windows native. If OneDrive is critical (e.g., work/school files) and the third-party client frustrates you, that's a valid reason to consider Tiny11 or dual-boot for zero friction. But since you're loving Cachy otherwise and gaming (Rocket League) is smooth, try the abraunegg client first—most folks stick with it happily.

What exactly are you trying to do with OneDrive (full sync, just access files, game saves, etc.)? That'll help narrow the best tool. 🐧

### HUMAN
No I’m saying should I dual boot on the one 2tb that I have or what?

### ASSISTANT
Yes, **dual-booting CachyOS and Tiny11 (or any stripped Windows 11) on your single 2TB drive is totally doable** and a common setup for folks in your position—wanting to keep CachyOS as the main daily driver while having native Windows access for Fortnite (and anything else stubborn).

It's not without risks or annoyances, but on a modern UEFI system with a large 2TB SSD like yours, it's manageable and often reliable if done carefully. Many CachyOS/Arch users run this way successfully in 2026.

### Pros of Dual-Booting on One Drive
- Keeps everything on your existing hardware—no extra SSD needed.
- GRUB (CachyOS's bootloader) can detect and add Windows entries automatically (or with a quick fix like `os-prober` + `grub-mkconfig`).
- Fast switching: Reboot → GRUB menu → pick OS (usually 5-10 seconds).
- Shared access to files: Create a large NTFS partition for games, documents, OneDrive-synced stuff—both OSes read/write it easily (Linux handles NTFS well via ntfs-3g).
- Space efficiency: Shrink your current Windows partition (if any) to free ~200-500GB for CachyOS (plenty for root + home + games), leaving the rest for shared storage.

### Cons and Common Issues (Why People Warn Against It)
- **Windows updates can overwrite GRUB**: Windows loves to "repair" the EFI partition and replace the bootloader with its own. This happens semi-randomly after big updates/feature drops. Fixable by booting a CachyOS live USB → chroot → reinstall GRUB, but it's a hassle (happens to ~20-30% of dual-booters per forums/Reddit).
- **Time sync weirdness**: Windows uses local time, Linux uses UTC → clock jumps when switching. Fix: In CachyOS, run `timedatectl set-local-rtc 1 --adjust-system-clock` (or vice versa in Windows registry tweak).
- **Partitioning risks**: Shrinking NTFS from Windows is safe-ish, but always back up first. If you mess up, data loss possible.
- **Secure Boot/BitLocker**: If your current Windows has BitLocker on, disable it first (painful). Secure Boot usually needs off for Linux install, but can re-enable later with tweaks.
- **Rare boot loops** or GRUB not detecting Windows after updates—fixed with live USB tools.

Overall, community consensus (CachyOS forums, Arch Wiki, Reddit r/cachyos) is: It's fine on one drive if you're okay troubleshooting occasionally, but **separate drives** is "safer" for zero bootloader conflicts. Since you only have one 2TB drive, go for it—many do and stick with it.

### Recommended Steps for Your Setup (Safest Order)
1. **Backup everything important** (external drive, cloud, etc.). Fortnite saves are cloud-based anyway.
2. **In current Windows** (or install Tiny11 first if you're not on Windows yet):
   - Shrink your main partition to free space (e.g., via Disk Management: right-click C: → Shrink Volume → aim for 300-600GB free unallocated for CachyOS).
   - Disable **Fast Startup** (Power Options → "Choose what the power buttons do" → uncheck "Turn on fast startup").
   - Disable **Secure Boot** in BIOS/UEFI if enabled.
   - If BitLocker: Turn it off.
   - Create a Tiny11 install USB if switching to it (use Rufus + Tiny11 ISO).
3. **Install/keep Tiny11 on its partition** first (recommended—Windows bootloader is picky).
   - If already on Windows: Just shrink as above.
   - Boot Tiny11 installer from USB → custom install → select the existing partition or create new one in unallocated space.
4. **Install CachyOS in the free space**:
   - Boot CachyOS ISO USB.
   - Use the installer (Calamares or manual)—choose "Install alongside" if available, or manual partitioning:
     - Reuse/share the existing EFI partition (~100-500MB FAT32, usually /dev/nvme0n1p1 or similar—mount it as /boot/efi).
     - Create new partitions in free space: e.g., 50-100GB for root (/), rest for /home or BTRFS subvolumes (CachyOS loves BTRFS snapshots).
   - Proceed with install—GRUB should detect Windows automatically.
5. **Post-install fixes** (common):
   - Boot into CachyOS → terminal: `sudo pacman -Syu os-prober`, then `sudo grub-mkconfig -o /boot/grub/grub.cfg` to add Windows entry if missing.
   - For OneDrive: Install `onedrive-abraunegg` from AUR as before—sync works across both OSes if on shared NTFS.
   - Test Fortnite in Windows (native, no issues).
   - Rocket League stays in CachyOS (Proton perfection).

If GRUB gets overwritten later: Boot CachyOS live USB → mount partitions → chroot → reinstall GRUB (CachyOS wiki has exact commands—quick 5-10 min fix).

**Bottom line recommendation**: Yes, dual-boot on your one 2TB drive—it's worth it for seamless Fortnite access without ditching CachyOS entirely. The occasional bootloader hiccup is annoying but fixable, and you'll keep enjoying the snappy Cachy experience most of the time. If it frustrates you long-term, add a cheap second SSD later (easiest fix).

If you're nervous about partitioning or need step-by-step for your exact disk layout (e.g., share `lsblk` output from live USB), drop details—I can guide more precisely. You've got this! 🐧 + 🪟

### HUMAN
Could I use a separate regular ssd just for tiny11 and then use my remaining space on the 2tb for whatever windows games?

### ASSISTANT
Yes, **using a separate regular SSD just for Tiny11 (or any lightweight Windows 11 install) while keeping your 2TB drive mostly for shared Windows games (and your CachyOS install) is an excellent setup**—actually one of the **best and most recommended ways** to handle dual-booting in 2026, especially for gaming.

This approach gives you the advantages of separation without the bootloader headaches of cramming everything onto one drive.

### Why This Setup Wins
- **Tiny11 on its own SSD** (e.g., a cheap 500GB–1TB SATA or NVMe SSD):  
  Windows gets its own dedicated EFI partition and full control over its boot process. No risk of Windows updates nuking GRUB (CachyOS's bootloader) or vice versa. Installs are cleaner, and troubleshooting is isolated—if something breaks in Windows, it doesn't touch CachyOS.

- **Your 2TB drive** for games + CachyOS:  
  - Install/keep CachyOS on part of the 2TB (e.g., shrink existing partitions if needed, or use free space—aim for 100–300GB for root/home + BTRFS snapshots).  
  - Use the remaining bulk of the 2TB (e.g., 1.5TB+) as a large **shared NTFS partition** for games, Steam library, Epic stuff, documents, OneDrive sync folder, etc.  
  Both OSes can read/write NTFS reliably (Linux via ntfs-3g or the built-in kernel driver—very stable now). Steam even has official guidance for shared NTFS libraries in dual-boot scenarios (Proton works great on them for Rocket League, etc.).

- **Boot process**:  
  - CachyOS's GRUB (or Limine in newer installs) can detect and add a Windows entry from the separate SSD automatically (run `sudo limine-scan` or `os-prober` + `grub-mkconfig` if needed).  
  - Many users prefer **BIOS boot menu** (F11/F12/Del key at startup) to pick drives directly—no GRUB conflicts at all.  
  - rEFInd (installable on CachyOS) is another clean GUI boot manager that scans both drives safely.

### Advantages Over Single-Drive Dual-Boot
- Much lower risk of bootloader overwrites (Windows is infamous for this during updates).
- Easier recovery: If one OS bricks, boot the other or live USB without issues.
- Better organization: Games on the big/fast 2TB (probably your NVMe), OSes isolated.
- Performance: No contention—Windows doesn't touch CachyOS files, and vice versa.
- Shared storage is seamless for Fortnite (native in Windows), Rocket League (Proton in CachyOS—same library folder works if you set it up in Steam).

### Potential Minor Downsides
- Need to buy/add the extra SSD (but SATA 1TB SSDs are ~$40–60 in 2026—super cheap).
- Boot selection might require hitting a key (BIOS menu) instead of auto-GRUB, but it's quick and reliable.
- If using NTFS for games: Rare edge-case performance hit on Linux (e.g., metadata ops slower than ext4/BTRFS), but for gaming it's negligible—thousands of dual-booters do this daily with no complaints. Exclude Proton prefix folders from heavy NTFS if paranoid.
- OneDrive sync: Still use the abraunegg client in CachyOS—point it to the shared NTFS folder.

### Quick Setup Outline
1. **Add the separate SSD** → Connect it (SATA or M.2 slot).
2. **Install Tiny11 on the new SSD**:
   - Boot Tiny11 USB → Custom install → Select the new SSD entirely (it'll create its own EFI + main partition).
   - Disable Fast Startup, Secure Boot if needed during setup.
3. **In CachyOS (or install it next if not already)**:
   - Partition your 2TB as needed (e.g., via GParted live or installer): Keep CachyOS partitions, create/expand a big NTFS one (label it "Games" or whatever).
   - Mount the NTFS in CachyOS (auto via fstab or Dolphin).
   - For Steam: Add the NTFS folder as a library in both OSes—games install once, play from either (Proton for Linux side).
4. **Boot config**:
   - After both installed, boot CachyOS → Update GRUB/Limine to detect Windows on the other drive.
   - Or just use BIOS boot menu to choose SSD (easiest, no conflicts).
5. **Test**: Fortnite native in Tiny11, Rocket League in CachyOS—both pulling from shared storage.

This is basically what a lot of CachyOS/Arch gamers do on forums/Reddit (separate drive for Windows to avoid drama, shared big drive for games). It's way more stable than single-drive partitioning for your use case.

If your 2TB is already full of Windows stuff, shrink the main partition from Tiny11 first to free space for CachyOS/shared NTFS. Got the exact drive layout or model (e.g., NVMe or SATA)? I can refine steps. Otherwise, this should give you the best of both worlds without compromise. 🚀🐧


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/homelab|Homelab]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
