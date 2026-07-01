---
category: coding
date: 2025-11-24
id: 771268
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: building
source: CLAUDE
summary: Bryan wanted help creating a plan.md for a crypto project meme generator
  with movable/resizable text, social sharing, and downloadable memes using React.
tags:
- meme-generator
- windsurf
- crypto-project
- plan-md
- react
- imgflip
---
# Creating a project plan for Windsurf

### HUMAN
working on a coding project and i need help with a plan.md that i can feed into windsurf before i get started. think you can help me with that?

### ASSISTANT
Absolutely! I'd be happy to help you create a plan.md file for Windsurf. To make sure I create the most useful plan for you, could you tell me a bit about your project?

For example:
- What are you building? (e.g., web app, CLI tool, API, mobile app)
- What's the main functionality or problem it solves?
- What tech stack are you planning to use? (languages, frameworks, databases, etc.)
- Are there any specific features or requirements you already have in mind?
- What's the scope? (MVP, full-featured app, prototype, etc.)

The more details you share, the better I can structure a comprehensive plan.md that will help guide your development process!

### HUMAN
so i'm working on something for a crypto project i'm a part of. they already have a site (dankmemesonsol.net) so i'm assuming what i'd be making is a web page that they can link to through the project website? not really sure how that works but the plan is to make a meme generator that users can add their own captions to. the text should be able to be moved/resized and any color should be able to be used for the text. the meme templates can be scraped for maximum templates

### ASSISTANT
```
This block is not supported on your current device yet.
```

Got it! So you're building a meme generator web app for a crypto project. Let me create a comprehensive plan.md for you. A few quick questions to make this plan perfect:

1. **Meme template scraping** - Where would you like to scrape templates from? (e.g., Imgflip, popular meme sites, or do you want to pull specific memes related to the crypto project?)

2. **Hosting/Integration** - Should this be:
   - A standalone single-page application they can host anywhere and link to?
   - Something that could be embedded into their existing site?

3. **Features priority** - Beyond the core functionality (add captions, move/resize text, change colors), would you also want:
   - Download/save memes?
   - Share directly to social media?
   - Upload custom images as templates?
   - Multiple text boxes?

4. **Tech preferences** - Any preference on framework? (React is probably easiest for this, but I can plan for vanilla JS, Vue, etc.)

I can create a solid plan with sensible defaults if you'd rather just get started, but these details would help me tailor it better to your needs!

### HUMAN
i was thinking of using imgflip or giphy for templates. i'm assuming it should be something embedded into their existing site? feature priority wise i want Download/save memes, Share directly to social media and Multiple text boxes. react should be good here as well

### ASSISTANT
Perfect! I've got everything I need. Let me create a comprehensive plan.md for your meme generator project.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've created a comprehensive plan.md for your crypto meme generator project. This plan includes:

**Key highlights:**
- Complete technical stack with React, fabric.js for canvas manipulation, and integrations with both Imgflip and Giphy APIs
- Detailed component architecture showing how to structure your code
- 5-phase implementation plan (roughly 4-5 weeks total)
- All your requested features: multiple text boxes, draggable/resizable text, color customization, download, and social sharing
- Embedding strategies for integration with dankmemesonsol.net
- Performance optimization tips and testing strategies

The plan is designed to be fed directly into Windsurf and gives you a clear roadmap from setup through deployment. Each phase has actionable checkboxes you can work through.

A few things you'll need to do before starting:
1. Get a free Giphy API key from developers.giphy.com (takes 5 mins)
2. Decide between Vercel or Netlify for hosting (both have great free tiers)
3. Coordinate with the dankmemesonsol.net team on how they want to embed it

Feel free to ask if you want me to adjust any part of the plan or dive deeper into any specific section!
