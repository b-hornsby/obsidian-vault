---
category: streaming
date: 2025-10-13
id: 329365
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GPT
summary: Bryan was trying to fix his Tikfinity goal overlay (used as a DS3 death counter)
  so it persists across stream sessions instead of resetting.
tags:
- tikfinity
- goal-overlay
- obs-persistence
- death-counter
- streaming-overlay
---
# Goal overlay persistence fix

### USER
how do i get my goal overlay (using it as my death counter for ds3) to keep track of my last deaths? it keeps restarting after i start up a new stream

### USER
this shouldn't be that complicated i'm using tikfinity for a custom goal rather than the ones built into tiktok studio

### ASSISTANT
Perfect — that’s actually ideal 👌  
The **TikFinity desktop app** gives you full access to local settings, including the “save variables” feature we need to make your death counter persist between sessions.  

Let’s go step-by-step with **exact clicks** inside the **TikFinity desktop app** so your DS3 death counter never resets again:

### 💾 Step 2: Enable Variable Saving and Loading
Now we’ll make sure TikFinity remembers that variable between sessions.

1. At the **top-right corner** of the Variables screen, click the **gear icon ⚙️ (Settings)**.  
   *(If you don’t see it, make sure you’re in the Variables tab.)*

2. Enable the following options:
   - ✅ **“Save variables to file on exit”**  
   - ✅ **“Load variables from file on startup”**

3. Click **Save/Close** (if required).

This tells TikFinity to automatically store all variable values (like your death counter) in a JSON file when you close the app, and reload them when you open it again.

### 🔢 Step 4: Tie the Variable to Your Goal Overlay
Now, make sure your on-screen goal is using the same variable.

1. Go to **Overlays → Your Goal Overlay.**
2. Under **Goal Type**, select **“Custom Variable.”**
3. Choose your variable (e.g. `deathCount`).
4. (Optional) Set the goal max value (e.g. if you want to reach 100 deaths).

Now your overlay will pull that number directly from the saved variable — meaning it’ll stay at the same number even after restarting TikFinity or OBS.

## ✅ Final Result
When you reopen TikFinity, it’ll:
- Auto-load your last saved death count.
- Keep your overlay in sync with it.
- Let you keep tracking across multiple streams.

So you’ll never lose your death tally again 🔥

## 🧩 The Issue
Most goal overlays (like “Follower Goal,” “Donation Goal,” or “Custom Goal”) **reset** every time you restart the stream because:
- They’re **tied to the current session**, not stored globally.
- The counter’s value isn’t being saved anywhere locally or online.

### **Option 2: Use StreamElements (with Persistent Custom Widget)**
If your overlay is hosted through **StreamElements**, here’s how to make it remember:

1. Go to your overlay editor.
2. Add a **Custom Widget**.
3. Edit the code to store and retrieve the death count using their **Persistent Storage API**:

```js
// Example snippet for StreamElements custom widget
let deaths = SE_API.store.get('ds3_deaths') || 0;

window.addEventListener('onEventReceived', (obj) => {
    if (obj.detail.listener === 'widget-button') {
        if (obj.detail.event.field === 'death') {
            deaths++;
            SE_API.store.set('ds3_deaths', deaths);
            updateDisplay();
        }
    }
});

function updateDisplay() {
    document.getElementById('deathCount').innerText = deaths;
}
```

That uses **SE_API.store** to keep the value even after you end a stream or refresh the overlay.

## 🧭 TL;DR (Best Approach)
If you’re using **OBS directly** →  
🟢 **Use a text file counter** and link it to a text source in OBS.

If you’re using **StreamElements / web overlay** →  
🟢 Add a **custom widget** and use `SE_API.store` to make it persistent.

## 🧩 QUICK FIX — TikFinity Custom Goal Keeps Resetting

### 🔹 Step 1: Open TikFinity
Launch the **TikFinity desktop app** like you normally do before your stream.

### 🔹 Step 3: Turn On Save/Load
In the **top-right corner of that page**, click the **⚙️ gear icon** (Settings).

Then make sure these two options are **enabled**:
- ✅ **Save variables to file on exit**  
- ✅ **Load variables from file on startup**

That’s it.  

TikFinity will now automatically save the value of every variable — including your custom goal — when you close the app, and reload it next time you start it up.

### 🔹 Step 5: Test It
1. Increase your counter manually or via your command/hotkey.  
2. Close TikFinity completely.  
3. Reopen TikFinity → go to **Variables** → you should see the same number still there.  
4. Open your overlay URL → it should show the same number too.

If it does — done. 🎯

Do you want me to show how to set up a **hotkey** (so you can press one button to add +1 death instantly)? It takes less than a minute and makes it feel way smoother while streaming.

### USER
for extra clarity i'm using tikfinity for the goal overlay

### ASSISTANT
Perfect — that clears it up completely 👌  

So you’re using **TikFinity** for your stream overlay (like follower/sub goals or counters) — and your **death counter** keeps resetting each time you restart your stream.  

Let’s break down **why that happens** and how to make it **save your last total** instead of resetting every time.

## ✅ Fix: Make Your Death Counter Persistent

Here are **three ways** to make your DS3 death counter **remember your last value** between streams:

### **Option 2: Use a Persistent Goal (Custom Overlay Variable)**
If you’re using a **Goal Overlay** tied to a specific variable:
1. Go to your **Goal overlay settings**.
2. Make sure it’s **not tied to session-only data** (like followers or donations).
3. Set its **“Goal type”** to **Custom Variable**.
4. Use a variable you control (e.g. `deathCount`).
5. Then in your TikFinity **Actions** or **Commands**, increment it like:
   ```
   Variable: deathCount
   Operation: Add
   Value: 1
   ```
   Every time you die, you press your hotkey or trigger your command.

If “Save variables to file” is turned on (Option 1), your counter will automatically persist between streams.

## 🧠 Bonus Tip: Auto-Increment with Hotkey
You can set up a **hotkey** or **command button** that adds +1 to your death counter automatically.

- Go to **Actions → New Action**
- Add a **Modify Variable** action:
  - Select `deathCount`
  - Operation: `Add`
  - Value: `1`
- Then go to **Hotkeys** → Assign a keyboard key (e.g. `F1`) to that action.

Now you can press `F1` every time you die, and TikFinity + OBS overlay will update instantly.

Would you like me to walk you through **exactly where to click in TikFinity’s UI** (step-by-step with menu names) to set up the saved variable and goal overlay together? That’ll make it 100% plug-and-play.