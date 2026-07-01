---
category: streaming
date: 2025-10-12
id: 705793
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was noting that TikTok Studio doesn't support reading from .txt files,
  blocking his death counter approach.
tags:
- tiktok-studio
- txt-file-reading
- death-counter
- file-io
- streaming-limitation
---
# tiktok studio doesnt let you read from .txt files 

### USER
tiktok studio doesnt let you read from .txt files 

### GEMINI
You are absolutely right. Unlike OBS Studio, TikTok Studio's built-in "Text" source does not have the option to read from a local .txt file. Since you can't use a local file, the easiest and most common workaround is to use a web-based counter service and bring it into TikTok Studio as a Link Source (which is TikTok Studio's version of a Browser Source). Here is the easiest way to add a death counter directly into TikTok Studio: Method: Use a Web-Based Counter (Browser Source) This method moves the counter functionality to a website, which you then display on your stream. Use a Stream Overlay Service to Create a Counter: Go to a streaming service that offers overlays/widgets like StreamElements (or a dedicated, simple online counter tool). Create a custom widget/overlay specifically for a counter. Most services will allow you to name it (e.g., "Deaths"). The service will give you a unique URL for this counter overlay. This URL is a web page that only displays the current number. Set Up Commands (Crucial Step): In the stream service's bot settings (e.g., StreamElements Chatbot), set up chat commands to control the counter. !death + (to increase the counter by 1) !death set 0 (to reset the counter) Add the Link Source in TikTok Studio: Open TikTok Studio. Go to your scene and click Add Source ($\mathbf{+}$). Select Link (this is the Browser/URL source). Paste the unique URL for your counter overlay from Step 1 into the link field. Control the Counter: When you die, you or a moderator simply type the chat command (e.g., !death +) into your TikTok Live chat. The command tells the web service to update the number. The Link Source in TikTok Studio immediately refreshes and displays the new, updated count on your stream. Why This is the Easiest Workaround: No local files: It completely bypasses the limitation of TikTok Studio not reading .txt files. Simple Control: You don't need a hotkey on your keyboard; you only need to type a simple command in chat (or set up a bot controller to trigger that command with a hotkey, if you want a faster, non-chat option). Highly Customizable: You can usually customize the font, color, and size of the number directly on the overlay service's website.
