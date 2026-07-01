---
source: GPT
date: 2025-07-26
category: coding
id: 10922334
linked_nodes: ['nodes/people/bryan.md']
---
# Bluetooth audio choppy fix

### USER
whats the difference between the earbuds being bluetooth and a regular bluetooth headset/ is it just because of the bluetooth dongle?

### ASSISTANT
Good catch — and **great detail**. The good news? You're **not out of luck at all**.

### 🔄 Alternatives with Native USB-A Dongles (No Adapter Needed):

If you want to **skip adapters completely**, here are 2 solid alternatives that use **USB-A dongles directly**:

### 🎧 **Corsair HS55 Wireless Core**
- Uses a **USB-A wireless receiver**
- More traditional headset feel
- Solid mic and sound quality

Let me know if you want live Amazon/Best Buy listings or local availability. I can help you find one in stock near your area.

### ASSISTANT
Great question — and yes, the **Bluetooth dongle can absolutely make a difference**, *but it’s not the only factor*. Let’s break this down clearly:

### 🧩 So Where Does the **Dongle** Come In?

The **Insignia Bluetooth dongle** is likely a **basic, generic USB Bluetooth 4.0 or 5.0 adapter**, and that matters because:

| Factor | Impact |
|
---
-
---
-|
---
-
---
-|
| **Bluetooth version** | Determines **bandwidth** and **codec support** (newer = better) |
| **Codec support** | Cheap dongles often **don’t support aptX, AAC, or LC3** — just **SBC** (lowest quality) |
| **Driver quality** | Cheap dongles use generic Windows drivers, often **don’t handle switching between HFP and A2DP well** |
| **Profile switching** | Can cause **lag, audio cutouts, or locking into bad modes** when mic is used |

### 🔧 Best Fixes:
- 🥇 **Use a separate mic**: Keeps your earbuds in stereo mode.
- 🥈 **Upgrade to a Bluetooth dongle** that supports **aptX LL or LE Audio** (and confirm your earbuds do too).
- 🥉 Use a **wired gaming headset** when quality matters (no compromises).

Let me know what earbuds you're using and your dongle's exact model (can check in Device Manager), and I’ll help you figure out if upgrading the dongle will actually help in your case.

### USER
so youre saying you cant use them on discord and the game at the same time?

### ASSISTANT
Exactly — **not in high quality**, and not without **compromises**.

### ✅ Here’s the truth:
You **can** use Bluetooth earbuds on **Discord + CS2 at the same time**, but:

- If you **use the mic on the earbuds**, Windows switches them to **Hands-Free (HFP/HSP) mode** → **low-quality mono audio** across the board.
  - CS2 audio gets **choppy, crackly, and low fidelity**.
  - Discord voice works, but **everything sounds worse**.

- If you **don’t use the mic**, then the earbuds can stay in **A2DP (stereo, high-quality) mode**, and **CS2 sounds perfect** — but now you **can’t talk in Discord using those earbuds**.

### ✅ Your Options Recapped:

| Option | Game Audio | Discord Mic | Notes |
|
---
-
---
-|
---
-
---
-
---
-|
---
-
---
-
---
--|
---
-
---
|
| **Use earbuds’ mic** | 🚫 Choppy | ✅ Works | Causes mono audio |
| **Use separate mic (USB/webcam)** | ✅ Clear | ✅ Works | Best solution |
| **Disable Bluetooth mic** | ✅ Clear | 🚫 No mic | For solo play or listen-only |
| **Use wired headset** | ✅ Clear | ✅ Works | Avoids all Bluetooth limitations |

### ✅ Solutions:

#### 1. **Use a Separate Mic**
- Plug in a **USB or 3.5mm mic** (like a standalone microphone or webcam mic).
- Windows will no longer use the Bluetooth mic.
- Your earbuds can now stay in **A2DP (stereo)** mode → **no choppy audio**.

#### 2. **Disable Bluetooth Mic Input (force stereo mode)**
1. Go to **Sound settings** → **Recording tab**.
2. Right-click your **Bluetooth headset mic** → **Disable** it.
3. This forces your earbuds to use A2DP (no mic).

> ⚠️ You won’t be able to talk on Discord using the earbuds' mic anymore.

#### 3. **Switch to Wired Headphones**
- Avoids Bluetooth limitations entirely.

#### 4. **Use a Bluetooth Transmitter with AptX Low Latency**
- If your earbuds and PC support **aptX LL**, audio lag/choppiness is reduced significantly.
- But still won’t fix the mic/audio bandwidth split issue.

Let me know your setup (e.g., model of earbuds, if you're using the mic on them or not), and I can suggest the cleanest fix.

### USER
i dont have usbc on the mobo or on the front panel

### ASSISTANT
Yes — a **Bluetooth gaming headset** *can* work better in this situation, **but with some big caveats depending on the model**.

Let’s break it down:

### ❌ When a Bluetooth Gaming Headset Still Has the Same Problem:

If it's just a **plain Bluetooth headset (no USB dongle, no aptX LL)**, then:
- You’re still using the same limited **Bluetooth audio profiles** (A2DP for audio, HFP for mic).
- You’ll **still get choppy, low-quality game audio** if the mic is in use.
- Same issue you’re having now — **just repackaged in a bigger headset**.

### ✅ Best Option for You (Quick Picks):
If you want zero hassle and guaranteed good performance for **CS2 + Discord**, look at:

- **SteelSeries Arctis 1 Wireless** (budget)
- **Logitech G435** (lightweight, dual wireless/Bluetooth)
- **Corsair HS80 or Virtuoso**
- **Razer BlackShark V2 Pro**

These all use **wireless dongles** (not regular Bluetooth) and are designed for **low-latency gaming audio + mic use simultaneously**.

Let me know your budget and preferred style (on-ear, over-ear, earbuds), and I’ll recommend some exact models that will work with no compromises.

### USER
which gaming headset that would be supported is cheapest?

### USER
discord audio is fine but my game audio is choppy when using bluetooth earbuds on windows 10? why would that be?

### ASSISTANT
Thanks for clarifying — that **narrows it down** a lot.

When you're using **Bluetooth earbuds + mic (via Discord)** and playing **CS2 (Counter-Strike 2)**, the **choppy or crackling audio** is due to **Bluetooth profile limitations** *and* how CS2 handles audio output.

### ✅ What You Can Do (for CS2 specifically):

#### **Option 1: Use Another Mic (Best Fix)**
- Use a **USB mic, webcam mic, or wired headset mic**.
- Then:
  1. Go to **Sound Settings > Recording tab** → Disable the Bluetooth mic.
  2. Windows will stop using the Bluetooth headset in mic mode.
  3. Your earbuds will stay in **stereo (A2DP)** mode.
  4. **CS2 and Discord audio will be clean.**

#### **Option 2: Disable “Hands-Free Telephony” (forces stereo)**
This removes mic access for the earbuds entirely:
1. Press `Win + R`, type `control mmsys.cpl`, press Enter.
2. Go to **Playback** tab.
3. Find your **Bluetooth headset (Hands-Free)** entry.
4. **Right-click → Disable** it.
5. Now find the **Stereo** version → **Set as Default**.
6. Go to **Recording tab** → disable the Bluetooth mic too.

> Now CS2 will get full stereo audio, no choppiness — but **you can't use your earbuds’ mic** for Discord anymore.

#### **Option 3: Use Wired Headphones for Gaming**
Not ideal, but avoids the Bluetooth limitation completely. Or, use earbuds just for **voice**, and speakers or another output for CS2.

### 🔥 Top Budget Picks (Ranked Cheapest to Best Value):

### 🥈 **Logitech G435 LIGHTSPEED**
- 💵 **Price**: ~$50–60
- 📡 Dual Wireless:
  - **Lightspeed 2.4GHz USB dongle**
  - **Bluetooth** for mobile (don’t use this mode on PC)
- 🎤 Built-in mic (beamforming, not boom)
- 🎧 Lightweight and comfy.
- 🔋 ~18h battery

> 🧠 *Very solid for the price, but mic quality is just okay.*

### ⚠️ Avoid:
- Anything that says “Bluetooth only” or doesn’t include a **USB dongle**.
- Cheap Amazon brands promising “gaming + Bluetooth” — they often have the **same mono/choppy issues** you’re already facing.
---
### ✅ Final Rec:
> If you're on a **tight budget**, the **SteelSeries Arctis 1 Wireless** is your best bet. It’s often on sale and **completely sidesteps the Bluetooth limitations**, giving you perfect game + voice audio at once.

Want me to find you a live link or sale near you for the best deal?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]