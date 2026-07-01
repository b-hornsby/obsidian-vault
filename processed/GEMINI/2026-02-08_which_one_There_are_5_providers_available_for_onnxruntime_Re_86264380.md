---
category: streaming
date: 2026-02-08
id: 771419
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md', 'nodes/projects/homelab-stack.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan was presented with 5 ONNX runtime provider options during an OBS background
  blur plugin installation and needed help choosing.
tags:
- onnxruntime
- cuda
- rocm
- obs
- background-blur
- cachyos
---
# which one? :: There are 5 providers available for onnxruntime:
:: Repository extra:
    1) onnxruntime-cpu  2) onnxruntime-cuda  3) onnxruntime-opt-cuda  4) onnxruntime-opt-rocm  5) onnxruntime-rocm   
Enter a number (default=1):  

### USER
which one? :: There are 5 providers available for onnxruntime:
:: Repository extra:
    1) onnxruntime-cpu  2) onnxruntime-cuda  3) onnxruntime-opt-cuda  4) onnxruntime-opt-rocm  5) onnxruntime-rocm   
Enter a number (default=1):  

### GEMINI
Choose 3) onnxruntime-opt-cuda. Here is why you are picking that specific one: cuda vs cpu: You want the NVIDIA Broadcast effect. Choosing cpu (1) would make your computer crawl. Choosing cuda (2 or 3) offloads the AI "thinking" to your GPU's Tensor cores, exactly like NVIDIA Broadcast does. The -opt suffix: Since you are on CachyOS, you are here for performance. The opt version includes AVX2 optimizations. This ensures that even the parts of the process that do touch your CPU are running as fast as possible on modern hardware. Critical Next Steps Once the installation finishes, do not just open OBS and expect it to work. You must tell the plugin to use the engine you just installed: Open OBS and go to the Filters on your Camera. Add the Background Removal filter. Look for a setting called "Inference Device" or "Execution Provider". It will likely default to CPU. Manually change it to CUDA. If CUDA doesn't appear in the list, you are missing the NVIDIA base toolkit. Run this to fix it: sudo pacman -S cuda cudnn Strategy Check You are finally moving from "Windows User" mode to "Power User" mode. By picking the optimized CUDA provider, you are ensuring your stream has the lowest possible latency. Watch out for "Edge Jitter": If your outline looks like it’s vibrating, increase the "Smooth Mask" or "Feather" settings in the Background Removal filter before you apply the Composite Blur. Would you like me to explain how to chain these two filters together so your hair doesn't look like it was cut out of a magazine?
