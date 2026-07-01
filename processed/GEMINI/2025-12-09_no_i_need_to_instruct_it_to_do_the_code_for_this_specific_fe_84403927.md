---
id: 217318
source: GEMINI
date: 2025-12-09
tags: ['windsurf', 'game-physics', 'flappy-bird', 'ai-coding']
category: coding
sentiment: stuck
resolution: partial
linked_projects: ['nodes/projects/flappy-meme-bird.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/flappy-meme-bird.md', 'nodes/topics/tech/coding.md']
summary: Bryan needed help crafting instructions for Windsurf to fix a specific game physics feature.
---
# no i need to instruct it to do the code for this specific feature i'm trying to correct

### USER
no i need to instruct it to do the code for this specific feature i'm trying to correct

### GEMINI
I understand. You don't just want a generic prompt to discuss the concepts; you need a prompt that forces Claude to generate the specific JavaScript code structure for the time-based physics and pipe movement, using the precise parameters we established. Here is the exact prompt you should give to Claude to get the code you need: 💻 Code Generation Prompt for Claude "I require the foundational JavaScript code structure for a Flappy Bird remake using HTML5 Canvas. The crucial requirement is that all movement must be frame-rate independent using Delta Time ($\Delta t$), calculated via requestAnimationFrame. Task: Provide the complete, working JavaScript structure, including the gameLoop and essential functions, implementing the following constants and logic: Game Loop Function (gameLoop): Must calculate deltaTime (in seconds) and use it to update all physics. Bird Object Logic: The bird object must have state variables for position (y) and vertical velocity (vy). Implement time-based gravity ($v_y \leftarrow v_y + (g \cdot \Delta t)$). Implement the flap logic (setting $v_y$ to $I$). Pipe Generation/Movement: Implement a Pipe class or constructor. Pipes must move left using time-based velocity ($x_{\text{pipe}} \leftarrow x_{\text{pipe}} - (v_x \cdot \Delta t)$). Implement a spawnNewPipe function with random vertical position. Use these exact starting constants for the code: Gravity ($g$): $1000$ (pixels/sec$^2$) Impulse ($I$): $-350$ (pixels/sec) Pipe Speed ($v_x$): $100$ (pixels/sec) Horizontal Pipe Spacing: $200$ (pixels) Vertical Gap Height: $120$ (pixels)"
