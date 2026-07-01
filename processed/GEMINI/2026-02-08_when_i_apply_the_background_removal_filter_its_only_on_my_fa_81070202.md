---
category: streaming
date: 2026-02-08
id: 219240
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was frustrated that the OBS background removal filter only applied
  to his face instead of blurring the background behind him.
tags:
- obs
- background-removal
- filter
- camera
- streaming
---
# when i apply the background removal filter its only on my face? i just want the background behind me to be blurred 

### USER
when i apply the background removal filter its only on my face? i just want the background behind me to be blurred 

### GEMINI
This is happening because you are treating the filter like a toggle switch rather than a layer. If the filter is "only on your face," one of two things is happening: Wrong Model: You have a "Face-only" model selected in the settings instead of a "Person/Body" model. Missing Layer: You are removing the background and leaving... nothing. Background removal turns everything that isn't you into transparency. If there is nothing "behind" your camera source in OBS, you just look like a floating head in a black void. To get the NVIDIA Broadcast effect, you need the "Sandwich Method." The Sandwich Method (The Pro Way) You need two versions of your camera running at the same time: one for you (sharp) and one for the room (blurry). Create the Background (The Bottom Slice): Add your Camera source to your scene. Name it "Background Blur." Apply the Composite Blur filter to this source. Crank it up until the room looks how you want. Create "You" (The Top Slice): Add your Camera source again (Right-click "Background Blur" -> Copy, then Right-click in Sources -> Paste Reference). Name this one "Me." Move "Me" so it is above "Background Blur" in your sources list. Apply the Background Removal filter to the "Me" source. The Result: * The "Me" source cuts out everything but your body. Because it’s transparent, the "Background Blur" source shows through the gaps. Presto: You are sharp, the background is blurred, and it looks exactly like NVIDIA Broadcast. Why it "only sees your face" right now Check these settings in the Background Removal filter: Segmentation Model: Change this to Mediapipe or Sinthlev. If it’s on a "Landmark" or "Face" model, it will literally only cut out your head. You want "Selfie" or "Human" models. Threshold: If this is too high, the AI is too "picky" and thinks your shoulders are part of the wall. Lower the threshold until your whole body is visible. The "One-Source" Pro Tip (Advanced) If you don't want two sources, do this on one camera source: Apply Background Removal. Set the "Mask" type to "Apply to Alpha". Apply Composite Blur after it. In Composite Blur settings, change the Effect Mask to "Alpha Channel." Wait—don't do this. It’s glitchy for beginners. Use the Sandwich Method above first. It’s easier to troubleshoot and uses less weird logic. The Advisor's Verdict You're currently frustrated because you want "magic" and you're getting "math." Stop looking for a single button. Your Priority Plan: Fix the Model: Ensure you're using a "Person" model in the Background Removal settings. Build the Sandwich: Set up the two-source stack I described above. Check the "Inference Device": Ensure it says CUDA. If you do this on your CPU, your stream will look like a slideshow. Does your "Me" layer successfully show your whole body now, or is the AI still "eating" your shoulders?
