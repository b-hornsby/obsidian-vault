---
source: CLAUDE
date: 2025-12-02
category: coding
id: 24353316
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/flappy-meme-bird.md']
---
# Reviewing plan.md for flappy bird project

### HUMAN
i need you to look over my plan.md carefully to ensure that i didnt miss out on any details before i plug that into windsurf and get to work on the dank meme flappy bird project. so far i have that pasted and i created another .md file that i want to serve as a way for the different models to know what's changed, what time, etc. this is the plan.md:

### ASSISTANT
I've reviewed your plan.md thoroughly, and it's impressively comprehensive! Here are some observations and suggestions:

## ✅ Strengths
- Excellent phase breakdown with clear DoD criteria
- Thorough technical specifications
- Good mobile-first thinking
- Detailed UI/UX flow
- Smart use of LocalStorage (avoiding the common browser storage pitfall)

## 🔍 Potential Gaps & Suggestions

### 1. **Critical: Browser Storage Restriction**
Your plan correctly uses LocalStorage, but you should add a note that **localStorage won't work in Claude artifacts**. Since you're using Windsurf, this is fine, but worth documenting.

### 2. **Missing: Obstacle Generation Logic**
- How far apart should pipes spawn? (e.g., every 200px, random 150-250px?)
- Minimum/maximum gap heights?
- Should gap position vary vertically?
- Object pooling details for performance

### 3. **Coin Spawn Logic Underspecified**
- What % of obstacles should have coins? (e.g., 60% regular, 20% risky?)
- Exact positioning rules for "safe" vs "risky"
- Should coins spawn every X obstacles or randomly?

### 4. **Character Differences**
- Are characters purely cosmetic, or do they have different hitboxes/abilities?
- If cosmetic, state this explicitly to avoid scope creep

### 5. **Game Constants/Configuration**
Consider adding a "Game Constants" section:
```javascript
// Suggested addition to plan
GAME_CONFIG = {
  GRAVITY: 800,
  FLAP_VELOCITY: -350,
  OBSTACLE_SPEED_START: 200,
  OBSTACLE_SPACING: 250,
  GAP_SIZE_MIN: 120,
  GAP_SIZE_MAX: 180,
  SCORE_FOR_DIFFICULTY_INCREASE: 10
}
```

### 6. **Error Handling**
- What happens if LocalStorage is full?
- What if asset loading fails?
- Network timeout handling for audio assets?

### 7. **Input Handling Details**
- Should spacebar work on mobile browsers?
- Prevent default behavior for space (stop page scroll)?
- Multi-touch handling (ignore or use first touch only)?

### 8. **Game Over Conditions**
- Does hitting the top of the screen cause game over?
- Ceiling collision or infinite upward flight?

### 9. **Visual Polish Details**
- Screen shake intensity/duration on collision?
- Particle effects specs (color, count, lifetime)?
- Transition duration between scenes?

### 10. **Meme Selection Criteria**
You mention suggested memes but haven't finalized them. Consider:
- Avoiding controversial/offensive memes
- Ensuring visual distinctiveness when pixelated
- Balanced rarity distribution (2 common, 2 uncommon, 1 rare, 1 legendary?)

### 11. **Performance Metrics**
- Target frame rate: You mention 60 FPS but should specify minimum acceptable (45 FPS?)
- Memory budget for mobile devices?
- Asset loading timeout values?

### 12. **Version Control Strategy**
Your changelog.md idea is great! Add to plan:
- Git commit message conventions
- Branch naming strategy (feature/, bugfix/, etc.)
- When to version bump

### 13. **Debug Mode**
Consider adding:
- Debug mode toggle (keyboard shortcut?)
- Hitbox visualization
- FPS counter
- Skip to any scene for testing

### 14. **Edge Cases**
- What if player achieves score > 999? (UI overflow?)
- Maximum coins cap? (Integer overflow at ~2 billion)
- Rapid restart spam (memory leaks?)

### 15. **Shop UX Details**
- Character preview animation in shop?
- "Are you sure?" dialog for purchases over 200 coins?
- "Not enough coins" feedback (shake animation, sound?)

## 📋 Suggested Additions

### Add a "Known Limitations" Section
```markdown
## ⚠️ Known Limitations
- No online leaderboard (local only)
- No cloud save sync across devices
- Maximum 5 high scores stored
- Audio may not autoplay on iOS Safari (requires user interaction)
```

### Add a "Browser Compatibility Matrix"
```markdown
## 🌐 Browser Support
| Browser | Version | Status |
|
---
-
---
--|
---
-
---
--|
---
-
---
-|
| Chrome  | 90+     | ✅ Full |
| Firefox | 88+     | ✅ Full |
| Safari  | 14+     | ✅ Full |
| iOS Safari | 14+ | ✅ Full |
| Chrome Android | 90+ | ✅ Full |
```

### Add "Input Priority"
```markdown
## 🎮 Input Handling Priority
1. Touch events (mobile)
2. Mouse clicks (desktop)
3. Spacebar (desktop)
4. Prevent conflicts (ignore keyboard on touch devices)
```

## 🎯 Recommended Next Steps

1. **Create a `CONSTANTS.md`** file with all numerical values
2. **Create `CHANGELOG.md`** with this structure:
```markdown
# Changelog

## [Unreleased]
### Added
### Changed
### Fixed

## [0.1.0] - YYYY-MM-DD
### Added
- Initial project setup
```

3. **Add `TESTING.md`** for detailed test cases
4. **Create `.env.example`** if you add any config values

## 🚀 You're Ready If...

You can answer these questions confidently:
- ✅ How far apart do pipes spawn?
- ✅ What's the exact flap velocity?
- ✅ Are characters cosmetic or functional?
- ✅ What's the minimum gap size?
- ✅ How many coins spawn per 10 obstacles?

If you can't answer these, add them to the plan before starting!
---
### HUMAN
so given what is currently in the plan.md and given the fact that i want changes to be documented as i go along, what needs added/changed? i already created a changelog.md file for the changes to be documented there

### ASSISTANT
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

I've created a comprehensive document with all the additions that should be inserted into your plan.md. Here's how to integrate it:

## 📝 Integration Strategy

**Option 1: Copy sections directly into plan.md**
- Each section has an "Insert after..." instruction
- Place them in the indicated locations
- Maintains your existing structure

**Option 2: Create supplementary docs**
- `CONSTANTS.md` - All the game configuration values
- `EDGE_CASES.md` - Error handling and edge cases
- `DEBUG.md` - Debug mode specifications
- Keep plan.md focused on high-level workflow

## 🎯 What This Adds

1. **Game Constants** - No more "we'll decide later" during coding
2. **Character List Finalized** - Clear hitbox/cosmetic specifications  
3. **Edge Cases** - Handles the "what if" scenarios
4. **Debug Mode** - Essential for testing/iteration
5. **Audio Priority** - Phased approach prevents audio rabbit hole
6. **Browser Compatibility** - Clear testing targets
7. **Input Handling** - Conflict resolution rules
8. **Playtesting Criteria** - Objective "done" definitions
9. **Critical Decisions** - Prevents scope creep mid-development

## 💡 Recommended Next Steps

1. **Copy sections into plan.md** where indicated
2. **Review the "Critical Decisions Made"** section - agree/disagree with locks?
3. **Adjust constants** if you have strong opinions (e.g., gravity feels better at 900?)
4. **Initialize changelog.md** with Phase 1 header ready

Your changelog.md should follow this structure:
```markdown
# Changelog
All notable changes to Dank Flappy Bird will be documented here.

## [Unreleased]

## [0.1.0] - TBD (Phase 1: Core Gameplay)
### Added
- (will be filled in as you work)

### Changed
### Fixed
```

The plan is now **99% complete** - you can confidently hand this off to Windsurf and make steady progress without decision paralysis! 🚀

### HUMAN
i'm going to delete what is in the plan.md that i pasted here earlier. can you make me a new plan.md that includes these things and also make those other files as well? (constants.md, edge_cases.md, DEBUG.md)

### ASSISTANT
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```
