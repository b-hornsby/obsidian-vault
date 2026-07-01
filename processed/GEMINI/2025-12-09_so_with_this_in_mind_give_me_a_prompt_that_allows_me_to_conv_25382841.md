---
id: 087900
source: GEMINI
date: 2025-12-09
tags: ['windsurf', 'prompt-engineering', 'claude', 'game-physics']
category: coding
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/flappy-meme-bird.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/flappy-meme-bird.md', 'nodes/topics/tech/coding.md']
summary: Bryan wanted a prompt to convey his game physics requirements to Claude in Windsurf.
---
# so with this in mind, give me a prompt that allows me to convey this to claude in windsurf please 

### USER
so with this in mind, give me a prompt that allows me to convey this to claude in windsurf please 

### GEMINI
That's an interesting redirection. You want a prompt that uses the detailed, physics-based implementation strategy we just developed, framed as a request to another AI, Claude, operating within a context I don't fully understand ("windsurf"). Your goal is to convey the specific, non-obvious requirement for time-based physics ($\Delta t$) and the critical tuning ratios for a faithful remake. Here is a focused, high-detail prompt designed to bypass vague "how-to" answers and force Claude to engage with the technical strategy we established. 📝 Prompt to Convey to Claude "I am building a faithful remake of Flappy Bird using HTML5 Canvas and JavaScript. I need to ensure the physics are frame-rate independent to replicate the original's difficult 'feel.' Do not give me simple pixel-per-frame values. My current understanding is that success depends on a time-based physics loop using requestAnimationFrame and calculating Delta Time ($\Delta t$, in seconds) for all movements. Challenge/Request: Provide the complete, time-based $\Delta t$ implementation strategy, focusing only on the following three critical components. Specify realistic pixel/second$^2$ or pixel/second values for the constants. Bird Physics (The Ratio): What is the optimal starting ratio between Gravity ($g$) (pixels/sec$^2$) and Impulse ($I$) (pixels/sec)? Provide values for both $g$ and $I$ that result in the rapid fall/twitchy jump required for the classic difficulty. Pipe Movement: What is a suitable starting value for the constant horizontal speed ($v_x$) in pixels/second? Ensure the pipe movement is also strictly $\Delta t$ based. Gap/Rhythm: Detail the recommended ratio for Gap Height ($G_{\text{gap}}$) relative to the bird's height, and the typical horizontal distance (in pixels) between pipe pairs to maintain the high-pressure rhythm. Frame your response as a detailed, ready-to-implement code strategy." Why this prompt works: It clearly states the technology (HTML5 Canvas/JS). It exposes the critical constraint (frame-rate independence via $\Delta t$). It explicitly forbids low-value answers (no simple pixel/frame values). It forces focus on the strategic ratios we identified ($I/g$, $G_{\text{gap}}/\text{Bird Height}$). It demands specific time-based units (pixels/sec and pixels/sec$^2$).
