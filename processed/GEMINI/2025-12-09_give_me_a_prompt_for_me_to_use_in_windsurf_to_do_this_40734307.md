---
id: 771842
source: GEMINI
date: 2025-12-09
tags: ['windsurf', 'prompt-engineering', 'game-development', 'ai-coding']
category: coding
sentiment: building
resolution: partial
linked_projects: ['nodes/projects/flappy-meme-bird.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/flappy-meme-bird.md', 'nodes/topics/tech/coding.md']
summary: Bryan wanted a well-crafted prompt to use in Windsurf for implementing a game feature.
---
# give me a prompt for me to use in windsurf to do this 

### USER
give me a prompt for me to use in windsurf to do this 

### GEMINI
That's an interesting redirection. You want a prompt that uses the detailed, physics-based implementation strategy we just developed, framed as a request to another AI, Claude, operating within a context I don't fully understand ("windsurf"). Your goal is to convey the specific, non-obvious requirement for time-based physics ($\Delta t$) and the critical tuning ratios for a faithful remake. Here is a focused, high-detail prompt designed to bypass vague "how-to" answers and force Claude to engage with the technical strategy we established. 📝 Prompt to Convey to Claude "I am building a faithful remake of Flappy Bird using HTML5 Canvas and JavaScript. I need to ensure the physics are frame-rate independent to replicate the original's difficult 'feel.' Do not give me simple pixel-per-frame values. My current understanding is that success depends on a time-based physics loop using requestAnimationFrame and calculating Delta Time ($\Delta t$, in seconds) for all movements. Challenge/Request: Provide the complete, time-based $\Delta t$ implementation strategy, focusing only on the following three critical components. Specify realistic pixel/second$^2$ or pixel/second values for the constants. Bird Physics (The Ratio): What is the optimal starting ratio between Gravity ($g$) (pixels/sec$^2$) and Impulse ($I$) (pixels/sec)? Provide values for both $g$ and $I$ that result in the rapid fall/twitchy jump required for the classic difficulty. Pipe Movement: What is a suitable starting value for the constant horizontal speed ($v_x$) in pixels/second? Ensure the pipe movement is also strictly $\Delta t$ based. Gap/Rhythm: Detail the recommended ratio for Gap Height ($G_{\text{gap}}$) relative to the bird's height, and the typical horizontal distance (in pixels) between pipe pairs to maintain the high-pressure rhythm. Frame your response as a detailed, ready-to-implement code strategy."
