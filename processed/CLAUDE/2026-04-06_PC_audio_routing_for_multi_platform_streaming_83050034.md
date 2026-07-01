---
id: 093880
source: CLAUDE
date: 2026-04-06
tags: ['audio-routing', 'multistreaming', 'tiktok-live-studio', 'obs-studio', 'voicemeeter-banana', 'virtual-cables']
category: streaming
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is struggling to properly route his PC audio for multistreaming on TikTok and Twitter using OBS Studio, VoiceMeeter Banana, and virtual cables, specifically ensuring his mic settings in OBS are transmitted to TikTok Live Studio.
---
# PC audio routing for multi-platform streaming

### HUMAN
help me properly route my pc audio so that i can multi stream on tiktok and twitter (when i get the premium sub). i already have aitum multistream and aitum vertical installed as well as voicemeter banana with cables a+b as well. i simply want to ensure that since i am using the vertical virtual camera to stream my vertical obs setup to tiktok live studio my audio from obs come through on tiktok as well (especially my mic settings in obs).

### ASSISTANT
```
This block is not supported on your current device yet.
```

Here's the thing with TikTok Live Studio specifically — it's its own separate app that captures audio differently than OBS. The core challenge is that your Aitum Vertical plugin sends a *virtual camera* feed to TikTok Live Studio, but there's no built-in "virtual mic" handoff the same way. You need to route audio so TikTok Live Studio is listening to the same mixed output your OBS is working with.

Here's a clean diagram of how everything should flow, then I'll walk you through the exact settings.
```
This block is not supported on your current device yet.
```

Here's how to set each piece up:

**VoiceMeeter Banana**

This is your central hub. Everything routes through here first. Your mic goes into a hardware input strip (H1 or H2). Your desktop audio should be set as the A1 output device in Windows Sound settings (set VoiceMeeter Input as your default playback device). On each input strip, enable both B1 and B2 outputs — this sends your full mix to both virtual cables simultaneously.

**Cable A → OBS**

In OBS, add an Audio Input Capture source and point it at `VoiceMeeter Output (Cable A)`. This is what OBS "hears" as your mic/mix. Apply all your OBS mic filters here — noise suppression, compression, EQ, etc. Set audio monitoring to "Monitor Off" since VoiceMeeter is already handling the mix; you don't want doubling.

**Cable B → TikTok Live Studio**

In TikTok Live Studio's audio settings, set the microphone input to `VoiceMeeter Aux Output (Cable B)`. Since both B1 and B2 are getting the same mixed signal from VoiceMeeter, TikTok Live Studio will hear the exact same audio mix — including everything you've set up in OBS's audio chain — without OBS being in the loop at all.

**Aitum Vertical (video side)**

In TikTok Live Studio, set the camera source to the Aitum Vertical virtual camera. This handles the vertical video. Audio and video are independent here — TikTok Live Studio takes video from the virtual camera and audio from Cable B, and they go out together in the stream.

**One thing to double-check:** In VoiceMeeter, make sure your mic strip has B1 *and* B2 both lit up (not just B1). If B2 is off, Cable B gets no signal and TikTok Live Studio will be silent.

When you add Twitter via Aitum Multistream, that stream pulls directly from OBS's encoder output so no extra audio config needed there — it just works off what OBS is already encoding.

### HUMAN
okay so for more context my audio is all messed up now in obs. what should my desktop audio source be and what should my mic source be before i move on to the vb side of things

### ASSISTANT
Good call getting OBS sorted first before touching VoiceMeeter. Let's figure out exactly where you're at.

What does your current OBS audio setup look like? Specifically:
```
This block is not supported on your current device yet.
```

### HUMAN
Q: What do you currently have set as your Desktop Audio device in OBS settings?
A: cable a input (vb audio virtual cable a)

Q: What's your mic showing up as in OBS right now?
A: microphone (yeti stereo microphone)

### ASSISTANT
Okay that explains the mess. Right now you've got it backwards from what you want. Here's the fix:

**Desktop Audio** → set this to `VoiceMeeter Input` (this captures whatever VoiceMeeter is mixing and sending out — your game audio, music, etc.)

**Mic/Auxiliary Audio** → keep your Yeti here for now, but this is temporary. Eventually the Yeti will plug into VoiceMeeter directly and OBS will listen to Cable A instead. But don't touch VoiceMeeter yet — get OBS reading correctly first.

The reason Cable A as desktop audio is wrong: Cable A is meant to be an *output* from VoiceMeeter that OBS listens to for the full mix. You had it set as the thing OBS thinks is your desktop sound, which means OBS was trying to capture VoiceMeeter's output bus as if it were your speakers — circular and messy.

So in OBS go to **Settings → Audio** and make these two changes:

- **Desktop Audio** → `VoiceMeeter Input`
- **Mic/Auxiliary Audio** → `Microphone (Yeti Stereo Microphone)` (leave as is)

Once you've done that, do you have audio showing up on both meters in the OBS mixer? That'll tell us if the signal flow is clean before we move to VoiceMeeter.

### HUMAN
these are my options for desktop audio

### ASSISTANT
You've got a lot of VB-Audio stuff installed — looks like you have both the standard VoiceMeeter Banana cables *and* the VAIO virtual devices. That's why it's cluttered.

For **Desktop Audio** you want **`Voicemeeter Input (VB-Audio Voicemeeter VAIO)`** — that's the main one. Ignore all the "In 2/3/4/5" and VAIO3 variants, those are extra VAIO channels you don't need for this setup.

Avoid the `Speakers (Yeti Stereo Microphone)` that's currently selected — that's OBS trying to use your Yeti as a playback device which makes no sense for desktop audio.

So to confirm your two settings in OBS Audio:

- **Desktop Audio** → `Voicemeeter Input (VB-Audio Voicemeeter VAIO)`
- **Mic/Aux** → your Yeti (direct, as it already is)

Once you set that, do you see signal on the Desktop Audio meter in OBS when you play something — like a YouTube video or your game?

### HUMAN
* `Voicemeeter Input (VB-Audio Voicemeeter VAIO) doesnt exist on that list `

### ASSISTANT
You're right, my bad — looking at your screenshot again the exact options you have are:

- `Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)`
- `Voicemeeter VAIO3 Input (VB-Audio Voicemeeter VAIO)`
- `Voicemeeter In 1-5 (VB-Audio Voicemeeter VAIO)`

The standard `Voicemeeter Input` not being there is a bit odd. This might be because you have **VoiceMeeter VAIO** (the more advanced version) installed rather than standard Banana, which renames the primary input.

Try **`Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)`** for desktop audio — that's most likely your primary mix bus in this setup.

But before we guess further — can you open VoiceMeeter and screenshot what it looks like? Specifically I want to see:

- How many hardware input strips you have
- What your A1/A2 output is set to
- Whether you see B1/B2 buttons on the strips

That'll tell us exactly which output bus to point OBS at so we're not just trying options blind.

### HUMAN
so what do i need to do?

### ASSISTANT
I still need to see your VoiceMeeter to give you the right answer — without knowing how it's configured I'd just be guessing which bus to point OBS at and we'd go in circles.

Can you screenshot your VoiceMeeter Banana window and drop it here?

### ASSISTANT
Okay this is super helpful. A few things jump out immediately:

**The big issue:** Stereo Input 1 is set to `CABLE-A Output (VB-Audio V...)` — that's your physical Cable A plugged into VoiceMeeter as an input. That's backwards and is likely the root of your loop/mess. Cable A should be an *output destination*, not something feeding into VoiceMeeter.

**What you actually have:**
- Stereo Inputs 2 and 3 are empty — your Yeti isn't plugged into VoiceMeeter at all yet
- Your Virtual Inputs (VoiceMeeter Input + VoiceMeeter AUX Input) are there and working
- Hardware Out A1/A2/A3 — we need to see what A1 is set to (your actual playback device like your headphones/speakers)
- None of your input strips have B1 or B2 lit up — meaning nothing is being routed to your virtual cables right now

**Here's what to fix in VoiceMeeter first:**

1. **Stereo Input 1** — click the device name and change it from Cable-A to your **Yeti** (`Microphone (Yeti Stereo Microphone)`)
2. **A1 output** — click A1 at the top right and make sure it's set to your actual headphones or speakers (your FiiO DAC-E10 or whichever you monitor with)
3. **On every input strip** — enable **B1** so the signal routes to VoiceMeeter's virtual output bus, which is what OBS will listen to

Can you click that A1 button in the top right to show what output device it's currently assigned to?

### HUMAN
yeah my a1 is current on my fiio dac

### ASSISTANT
Perfect, that's correct — your FiiO is your monitoring device so A1 is exactly right.

Now let's get everything routed properly. Here's what to do step by step:

**Step 1 — Fix Stereo Input 1 (your Yeti)**
Click the `CABLE-A Output` label under Stereo Input 1 and change it to `Microphone (Yeti Stereo Microphone)`. Your Yeti needs to be a hardware input into VoiceMeeter, not Cable A.

**Step 2 — Route your inputs to B1**
On Stereo Input 1 (Yeti), click **B1** to light it up. This sends your mic into the virtual output bus that OBS will read from.

For desktop audio, your apps need to be playing back *through* VoiceMeeter. Go to **Windows Sound settings → Playback** and set `VoiceMeeter Input (VB-Audio Voicemeeter VAIO)` as your **default playback device**. That way your game/browser audio flows into VoiceMeeter automatically via the Virtual Input strip, and you route that to B1 as well.

**Step 3 — Back in OBS**
- **Desktop Audio** → `CABLE-B Output (VB-Audio Virtual Cable B)` — actually scratch that, with your setup the cleaner pick is `Voicemeeter AUX Input` or we use B1's output. 

Actually before I give you the final OBS device — what do you want OBS to capture? Just your mic, or your mic *and* desktop audio mixed together in one track?

### HUMAN
VoiceMeeter Input (VB-Audio Voicemeeter VAIO) doesnt exist remember

### ASSISTANT
You're right, my bad again. Looking at your VoiceMeeter screenshot, your virtual inputs are labeled:

- `Voicemeeter Input` (the left virtual input strip)
- `Voicemeeter AUX I` (the right virtual input strip)

So in **Windows Sound Settings → Playback**, look for whichever of these shows up as a playback device — it'll likely appear as one of the options you already saw in OBS. Based on your OBS dropdown it would be either:

- `Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)`
- `Voicemeeter VAIO3 Input (VB-Audio Voicemeeter VAIO)`

Can you screenshot your **Windows Sound Settings → Playback tab** (or right-click the speaker icon → Sound Settings → scroll to output devices)? That'll show us exactly what VoiceMeeter is exposing as a playback device on your system so we stop guessing at names.

Also still need your answer on the routing question — do you want OBS to capture your **mic only**, or **mic + desktop audio mixed**?
