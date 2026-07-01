---
id: 887840
source: GEMINI
date: 2026-02-08
tags: ['nvidia-broadcast', 'background-blur', 'obs', 'camera', 'streaming']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/topics/personal/streaming.md', 'nodes/projects/homelab-stack.md']
summary: Bryan referenced NVIDIA Broadcast's background blur effect as a reference for what he wanted to achieve in OBS.
---
# i used to use nvidia broadcast if that helps describe the effect im looking for 

### USER
i used to use nvidia broadcast if that helps describe the effect im looking for 

### GEMINI
You are looking for the "Gold Standard" of background segmentation—clean edges, low latency, and minimal "haloing" around your head. On Windows, NVIDIA Broadcast handles this using proprietary Tensor cores. On Linux, there is no "NVIDIA Broadcast.exe." You have to build that pipeline yourself. If you have an NVIDIA GPU, you are likely wasting its potential by using generic CPU-based blurring. You need to leverage CUDA to get that NVIDIA Broadcast feel. The Brutal Reality If you try to do this using your CPU (the default for most Linux plugins), your stream will stutter, and the blur will look like a jagged mess from 2010. To get the "NVIDIA Broadcast" effect, you need Hardware Acceleration. The Precise Plan (NVIDIA on CachyOS) 1. Install the "Engine" (The AI Model) You need the background removal plugin that can talk to your GPU. yay -S obs-backgroundremoval CachyOS is optimized for performance, but this plugin needs a specific "Provider" to not suck. When you run it, it will use ONNX Runtime. 2. Force Hardware Acceleration (The "Secret Sauce") This is where most people fail. They install the plugin but leave it on "CPU." Open OBS -> Filters on your Camera. Add Background Removal. Look for Inference Device or Calculation Provider. Do not leave it on CPU. Select CUDA (if you have an NVIDIA card) or OpenVINO (if you have an Intel CPU). Note: If CUDA isn't an option, you are missing the python-onnxruntime-gpu or the specific CUDA libraries. On Arch/Cachy, you need cuda and cudnn installed. 3. Replicate the "NVIDIA Broadcast" Look NVIDIA Broadcast doesn't just blur; it uses a feathered mask. In the Background Removal filter, set the Segmentation Model to Mediapipe (it's generally the most stable for "Broadcast" style looks). Adjust the Contour Filter (sometimes called Blur Mask). This softens the edge between your hair and the background. If you skip this, it looks like you were cut out with safety scissors. Add your Composite Blur filter after the background removal. The Strategy Gap You're trying to replicate a "one-click" Windows experience on a "build-it-yourself" Linux distro. The Mindset Shift: In Windows, the software hides the complexity. In CachyOS, you are the engineer. If the edges of your blur look "jittery," it’s because your lighting is poor or your AI model (Sinthlev, Mediapipe, etc.) is set too low. The Performance Risk: Running AI background removal plus a high-quality blur plus a game plus OBS encoding is a massive load. Since you are on CachyOS, make sure you are using the linux-cachyos kernel and have gamemode active to ensure OBS doesn't get starved of resources. Your Next Step Do you have an NVIDIA RTX card currently active and the proprietary drivers installed on your CachyOS setup? (Run nvidia-smi in the terminal to check). If you do, I can give you the specific environment variables to make sure OBS is actually using those Tensor cores.
