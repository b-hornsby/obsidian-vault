---
category: coding
date: 2025-12-02
id: 698445
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md', 'nodes/projects/flappy-meme-bird.md']
linked_projects:
- flappy-meme-bird
resolution: partial
sentiment: building
source: CLAUDE
summary: Bryan wanted help creating a plan.md/PRD for a dank meme-themed Flappy Bird
  clone with unlockable meme characters, and was curious about using Next.js for the
  tech stack.
tags:
- flappy-bird
- dank-memes
- plan-md
- prd
- next-js
- html5-canvas
---
# Dank meme flappy bird game project

### HUMAN
Have an idea for a coding project and i need your help getting started. The main idea is create a flappy bird clone but instead of the bird, it should be the dank meme logo and as the user progresses gathering coins along the way, there should be unlockable memes from that era (pepe, doge, troll, Dat Boi unicycle frog, etc).  create a plan.md that serves as the prd for this project please

### ASSISTANT
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

I've created a comprehensive PRD for your Dank Memes Flappy Bird project! This plan covers:

**Key Features:**
- Classic Flappy Bird gameplay with the Dank Memes logo as the main character
- Coin collection system that persists across sessions
- 8 unlockable meme characters (Pepe, Doge, Troll Face, Dat Boi, and more) with increasing costs
- Full game state management (menu, gameplay, game over, unlock screen)

**Technical Approach:**
- HTML5 Canvas for smooth rendering
- Vanilla JavaScript (no frameworks needed for simplicity)
- LocalStorage for saving coins, unlocks, and high scores

**Development Phases:**
The plan breaks down implementation into 5 logical phases, from core mechanics to polish and deployment.

Would you like me to start building out any particular component first? I could create:
1. The basic game structure with Flappy Bird physics
2. The unlock screen UI
3. A complete playable prototype

Let me know what you'd like to tackle first!

### HUMAN
What about next.js for something like this for the tech stack? I’ve been building it out with the chosen tech stack until now I’m just curious

### ASSISTANT
Next.js would be overkill for this project, and here's why:

**Why Next.js might not be ideal:**
- **Server-side rendering** - Not needed for a game that runs entirely in the browser
- **Routing** - You don't need multiple pages/routes, just different game states in one canvas
- **Build complexity** - Adds bundling, compilation steps that slow down development for a simple game
- **Performance overhead** - React's virtual DOM diffing isn't optimized for 60 FPS canvas rendering
- **File size** - Shipping the entire React + Next.js framework for a simple game

**Where vanilla JS/HTML5 Canvas shines:**
- Direct canvas manipulation = maximum performance
- Immediate refresh during development (no build step)
- Smaller bundle size = faster load times
- Full control over the game loop without React's reconciliation
- Simpler debugging for animation/physics issues

**When Next.js WOULD make sense:**
- If you want a marketing landing page + the game
- User authentication and online leaderboards
- Server-side score validation to prevent cheating
- SEO for discoverability
- Complex UI outside the game (forums, profiles, etc.)

**Compromise option:**
You could use Next.js for the *wrapper* (landing page, leaderboards, user accounts) and embed the vanilla canvas game as a component. This gives you Next.js benefits for the app structure while keeping game performance optimal.

Since you mentioned you've already started building with your chosen tech stack - what are you using currently? I can give more specific advice based on what you've got going!

### HUMAN
This is what I’m using so far HTML5 Canvas for smooth rendering
	•	Vanilla JavaScript (no frameworks needed for simplicity)
	•	LocalStorage for saving coins, unlocks, and high scores

### ASSISTANT
Perfect! You're using exactly the right tech stack for this project. Vanilla JS + Canvas + LocalStorage is the optimal choice here for all the reasons I mentioned.

**What you have is ideal because:**
- **Maximum performance** - Direct canvas manipulation, no framework overhead
- **Fast iteration** - Just save and refresh, no build steps
- **Small footprint** - Fast loading, works great even on slower connections
- **Full control** - You own the entire game loop and rendering pipeline

**Quick tips as you continue building:**

1. **Structure your code** - Even without a framework, keep it organized:
   - Separate files for game logic, rendering, physics, UI
   - Use classes/objects for entities (Player, Pipe, Coin, etc.)
   - Keep the game loop clean and readable

2. **LocalStorage wrapper** - Create a simple storage utility:
   ```javascript
   const GameStorage = {
     saveCoins: (amount) => localStorage.setItem('coins', amount),
     getCoins: () => parseInt(localStorage.getItem('coins')) || 0,
     // etc.
   }
   ```

3. **Asset loading** - Make sure all sprites/sounds load before starting the game

4. **requestAnimationFrame** - Use this instead of setInterval for your game loop (smoother 60 FPS)

5. **Mobile considerations** - Add touch event listeners alongside click/keyboard

**Where are you at in the build right now?** Do you have the basic Flappy Bird mechanics working, or are you still setting up the foundation? I can help with specific implementation challenges if you're stuck on anything!
