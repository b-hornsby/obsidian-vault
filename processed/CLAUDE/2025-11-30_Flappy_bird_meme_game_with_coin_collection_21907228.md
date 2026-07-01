---
category: coding
date: 2025-11-30
id: 293517
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/flappy-meme-bird.md', 'nodes/topics/tech/coding.md']
linked_projects:
- flappy-meme-bird
resolution: partial
sentiment: executing
source: CLAUDE
summary: Bryan wanted to know how to start the Dank Flappy Bird project in Windsurf,
  ensure the model references plan.md and project_changes.md, and set up timestamped
  change documentation.
tags:
- flappy-bird
- windsurf
- project-setup
- vite
- phaser
- changelog
---
## Alright, let's recap everything before I create your plan.md:

**PROJECT OVERVIEW:**
- **Name:** Flappy Dank (or whatever you want to call it!)
- **Platform:** Web-based (desktop + mobile)
- **Tech Stack:** Phaser 3 + Vite
- **Art Style:** Pixelated/8-bit memes with meme collage background

**CORE GAMEPLAY:**
- Flappy Bird mechanics with Dank Meme as player
- Click/tap to flap, gravity pulls down
- Progressive difficulty (speed increases every 10 points, then caps)
- Coins: +1 (safe spots), +5 (risky spots)
- Persistent coin wallet across runs

**CHARACTERS & ECONOMY:**
- 5-6 unlockable memes with rarity tiers
- Progressive pricing: 50 → 100 → 200 → etc.
- One expensive final unlock (500+ coins)
- Start with only Dank Meme unlocked

**UI/SCREENS:**
- Main Menu → Character Shop → Gameplay → Game Over
- Top 5 local leaderboard
- Pause functionality
- Settings for sound on/off
- Simple transitions (fades/slides)

**AUDIO:**
- Essential sound effects (flap, coin, death, UI)
- Background music deferred to later

**MOBILE:**
- Portrait mode
- Full browser window
- Touch controls

**Does this capture everything correctly?** Any last changes before I generate the plan.md file for Windsurf?

### HUMAN
just name it dank flappy bird and we're all good that sounds great

### ASSISTANT
Perfect! Let me create your comprehensive plan.md file for Windsurf.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've created a comprehensive plan.md file for your Dank Flappy Bird project. 

This plan includes:

✅ **Complete technical specifications** - Tech stack, architecture, and implementation details
✅ **Detailed feature breakdown** - Every system from coins to character unlocks
✅ **8 development phases** - From MVP to polish, with clear milestones
✅ **UI/UX flow** - All screens mapped out with functionality
✅ **Asset lists** - Everything you need to source or create
✅ **Testing checklist** - Comprehensive QA coverage
✅ **Project structure** - Recommended folder organization
✅ **Quick start guide** - Get coding today

The plan is organized so you can:
1. **Reference it in Windsurf** as you build each feature
2. **Track progress** by checking off tasks in each phase
3. **Stay focused** on the MVP without feature creep
4. **Scale up** with the "Future Enhancements" section later

You can copy this into your project as `plan.md` and start with Phase 1 to get a playable prototype running quickly. Good luck with the build! 🎮🔥

### HUMAN
okay so i pasted this into a plan.md so windsurf knows whats up. i also added a project_changes.md so that way the model doesn't get lost in what's been changed or not, limiting as much hallucination as possible. given those two facts, how do i start this project and how do i make sure the model references both when building this out?

### ASSISTANT
Great thinking with the `project_changes.md` file! That's a smart way to track progress and reduce hallucination. Let me walk you through the setup:

## 1. Initial Project Setup

First, let's get your project initialized:

```bash
# Create the project
npm create vite@latest dank-flappy-bird -- --template vanilla

# Navigate into it
cd dank-flappy-bird

# Install Phaser
npm install phaser

# Start dev server to test
npm run dev
```

## 2. Structure Your Documentation

Your project root should look like this:

```
dank-flappy-bird/
├── plan.md                    ← Your master plan (already created)
├── project_changes.md         ← Track what's been implemented
├── README.md                  ← Basic project info
├── package.json
├── src/
├── public/
└── ... (other files)
```

## 3. Set Up `project_changes.md` Template

Here's a template structure I recommend:

```markdown
# Project Changes Log

**Last Updated:** [Date]

## ✅ Completed

### Phase 1: Core Gameplay (MVP)
- [ ] Set up Vite + Phaser 3 project
- [ ] Implement player physics
- [ ] Create obstacle spawning system
- ...

### Phase 2: Coin System
- [ ] Not started yet

## 📝 Implementation Notes

### [Date] - Project Initialization
- Created Vite project with vanilla template
- Installed Phaser 3
- Set up basic folder structure

## 🔄 Next Steps

1. Create basic game scene
2. Implement player sprite
3. Add flap mechanics
```

## 4. How to Make Windsurf Reference Both Files

When working with Windsurf's AI, you need to **explicitly prompt it** to check these files. Here are strategies:

### Strategy A: Direct File References in Prompts

```
"Look at plan.md Phase 1 and project_changes.md. 
I want to start implementing the player physics. 
Update project_changes.md as we go."
```

### Strategy B: Create a `.windsurfrules` File (Recommended)

Create a `.windsurfrules` file in your project root:

```markdown
# Windsurf Rules for Dank Flappy Bird

## Required File References
Before implementing any feature, ALWAYS:
1. Check `plan.md` for the specification
2. Check `project_changes.md` for what's already done
3. Update `project_changes.md` after making changes

## Workflow
1. User requests a feature
2. Reference the relevant section in `plan.md`
3. Check `project_changes.md` to see current state
4. Implement the feature
5. Update `project_changes.md` with:
   - What was changed
   - Files modified
   - Any deviations from plan.md
   - Next logical step

## Code Standards
- Follow the project structure defined in plan.md
- Use ESM imports
- Comment complex logic
- Keep scenes modular

## Important Context
- This is a Phaser 3 web game
- Target: Desktop + Mobile (portrait)
- No localStorage for game state (use LocalStorage for save data only)
```

### Strategy C: Pinning Files in Windsurf

In Windsurf, you can **pin files** to context:
1. Right-click on `plan.md` → "Add to Chat Context" (or pin icon)
2. Right-click on `project_changes.md` → "Add to Chat Context"
3. These files will stay in the AI's context for all messages

### Strategy D: Start Each Session With Context

Begin each coding session with:

```
"Review plan.md and project_changes.md. 
What's the next task in Phase 1 that hasn't been completed yet?"
```

## 5. Recommended First Prompt

Here's what I'd say to Windsurf right now:

```
"I have plan.md with our full game spec and project_changes.md 
to track progress. 

Let's start Phase 1 of plan.md. First task is 'Set up Vite + 
Phaser 3 project'. 

I've already run:
- npm create vite@latest dank-flappy-bird -- --template vanilla
- npm install phaser

Now help me:
1. Set up the basic Phaser config in src/main.js
2. Create src/config.js with game settings for mobile portrait mode
3. Create a basic BootScene just to test

### HUMAN
i mean what do i need to tell windsurf to get this started sorry i should have clarified

### ASSISTANT
Ah gotcha! Here's exactly what to tell Windsurf to kick things off:

That should get Windsurf to:
- Read both your documentation files
- Understand the context
- Start building according to your plan
- Track changes as it goes

Let me know how it responds and if you need to adjust the prompt!

### HUMAN
other thing i would like it to add is time stamps for each change and document it in project_changes.md. i haven't done anything to the environment yet, not even this step: I've already created the project with: - npm create vite@latest dank-flappy-bird -- --template vanilla - npm install phaser

### ASSISTANT
Perfect! Here's the updated prompt with timestamps included and starting from scratch:

This will have Windsurf:
- Start completely from scratch
- Add timestamps to every change in `project_changes.md`
- Guide you through the setup process
- Track everything as you build


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]