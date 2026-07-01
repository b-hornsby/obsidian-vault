---
id: 412472
source: GEMINI
date: 2025-07-29
tags: ['coding', 'gemini', 'go', 'code', 'vs code', 'ide', 'cli', 'at']
category: coding
sentiment: exploratory
resolution: partial
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
---
# i cant find my appdata folder 

### USER
i cant find my appdata folder 

### GEMINI
Got it. The AppData folder is a hidden folder by default on Windows. This is a common hurdle! There are a couple of ways to access it: Method 1: Type it Directly into the Run Dialog This is usually the quickest way. Press Windows Key + R on your keyboard to open the "Run" dialog. Type %appdata% and press Enter. This will directly open the Roaming folder inside AppData. From there, you can navigate back one level to AppData if needed (though Roaming is usually where Code is located) or go into Local or Roaming as required. For VS Code user data, you'll specifically go from Roaming to Code. So the full path would be something like C:\Users\YourUsername\AppData\Roaming\Code. Method 2: Show Hidden Files in File Explorer If you prefer to browse to it directly, you'll need to enable "Show hidden files". Open File Explorer (the folder icon on your taskbar or press Windows Key + E). Navigate to This PC -> Local Disk (C:) -> Users -> YourUsername (replace with your actual username, e.g., Bryan). Once you're inside your user folder, you won't see AppData unless hidden items are shown. Windows 10/11: In the File Explorer ribbon at the top, click on the "View" tab. In the "Show/hide" group, check the box next to "Hidden items". Older Windows versions: Click on "Organize" (or "Tools") -> "Folder and search options". Go to the "View" tab. Under "Hidden files and folders," select "Show hidden files, folders, and drives". Click "Apply" and "OK." Once hidden items are shown, you should now see the AppData folder in your user directory. You can then double-click on it and navigate to Roaming -> Code. Once you've found the Code folder within AppData\Roaming, you can proceed with the "Deep Clean" steps I outlined earlier.