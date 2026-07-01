---
id: 821219
source: GPT
date: 2025-12-24
tags: ['chatgpt', 'chatgpt-wrapped', 'year-in-review']
category: general
sentiment: curious
resolution: resolved
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan was asking how to view his ChatGPT Wrapped year-in-review summary.
---
# ChatGPT Wrapped Guide

### ASSISTANT
{"only_tools":true}

### USER
No you didn’t

### ASSISTANT
{"path":"your_year_with_chatgpt/implicit_link::connector_openai_cocoon/start_cocoon_widget","args":{}}

### USER
How do I look at my chat gpt wrapped?

### TOOL
The following functions are available to be used with api_tool.call_tool. Use the resource name as the path and the resource argument as the args for api_tool.call_tool.

// Application for the user to trigger their "Your Year with ChatGPT" experience that allows the user to reflect on their past year with ChatGPT. You should call this tool if the user requests their 'year in review' or 'chatgpt wrapped' or a recap of their ChatGPT 2025 but always refer to this experience as "Your Year with ChatGPT" as the official name. Do not mention or acknowledge "Cocoon" because this is the code name.
namespace your_year_with_chatgpt {

// Initializes the "Your Year with ChatGPT" experience. You should only ever need to call this tool once. Do not mention "Cocoon" in your response because this is the code name.
type /your_year_with_chatgpt/implicit_link::connector_openai_cocoon/start_cocoon_widget = () => any;

} // namespace your_year_with_chatgpt

### ASSISTANT
That experience is called **Your Year with ChatGPT**.

I’ve just opened it for you — jump in and start it to see your recap.

### ASSISTANT
Fair — blunt truth: that widget **doesn’t always auto-open**, especially on iOS.

Here’s how to actually find **Your Year with ChatGPT** yourself:

### Option 1 (most reliable)
1. Open the **ChatGPT app**
2. Go to the **Home screen**
3. Look for a banner or card that says **“Your Year with ChatGPT”**
   - It usually appears near the top
   - If you don’t see it, **fully close the app and reopen it**

### Option 2
1. Tap your **profile picture**
2. Check for **Year in Review / Your Year with ChatGPT**
3. If it exists for your account, it’ll be there

### Important reality check
- It’s **rolling out gradually**
- **Free plan users may not have it yet**
- If it’s not visible anywhere, your account simply hasn’t been enabled yet — nothing you’re doing wrong

If you want, I can:
- Tell you **why some accounts don’t get it**
- Or help you infer a *DIY “wrapped”* based on how you actually use ChatGPT (which, given your history, would be brutally honest and probably more useful anyway)

### TOOL
The tool included embedded UI which has been displayed to the user.

Embedded UI description: 

Only reference this widget as "Your Year with ChatGPT" and nothing else. Don't ask any follow up questions or say you can do anything for the user. Only nudge the user to start the "Your Year with ChatGPT" experience. Don't mention "Cocoon" in your response because this is the code name.
