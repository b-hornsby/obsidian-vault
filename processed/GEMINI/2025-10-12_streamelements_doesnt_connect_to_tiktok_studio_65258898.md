---
category: streaming
date: 2025-10-12
id: 897681
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects:
- streaming-rig
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan was noting that StreamElements doesn't connect to TikTok Studio and
  seeking alternatives.
tags:
- streamelements
- tiktok-studio
- integration-issues
- streaming-tools
---
# streamelements doesnt connect to tiktok studio? 

### USER
streamelements doesnt connect to tiktok studio? 

### GEMINI
That's an important clarification! You are absolutely correct: StreamElements does not have native, full integration with TikTok LIVE Studio in the same way it does with Twitch, YouTube, or OBS. However, the counter method I suggested relies on a universal feature that is available in TikTok LIVE Studio: the Link Source (or Browser Source). Here is the breakdown of why the counter works, and how to troubleshoot it if it's not showing up: 1. Why the StreamElements Counter Should Still Work The StreamElements "Bot Counter" is simply a web page that displays a number. The StreamElements platform is only used to generate the URL and process the chat command (!death). TikTok LIVE Studio's Link Source simply loads that web page (the URL) into your stream. It doesn't need to "connect" to StreamElements' platform—it just needs to display the content of the URL. The process of updating the counter is: A viewer types !death in your Twitch/YouTube chat. The StreamElements Chatbot sees the command and increases the number on the private web page (the URL). TikTok LIVE Studio's Link Source updates its display of that URL in real-time. 2. The Easiest Solution (If It's Not Working) If the counter is not showing up in TikTok LIVE Studio, here are the most common reasons and their fixes: ProblemLikely CauseSolutionBlank/Black BoxThe size of the Link Source is too small.In TikTok LIVE Studio, go to the Properties (settings) of the Link Source. Make sure the Width and Height are large enough to display the text (e.g., set to $\mathbf{500}$ Width and $\mathbf{150}$ Height to start).Doesn't UpdateThe Link Source is paused or needs to be reloaded.In TikTok LIVE Studio, select the Link Source, click the three-dot menu ($...$), and choose Refresh.Counter Doesn't ExistThe command or counter name is wrong.Go back to StreamElements. Double-check that the Counter Name in the overlay widget settings exactly matches the variable in the chat command (${count **name**}).Still BlackSome streamers report issues with TikTok's Link Source.As an alternative, stream using OBS Studio and then either use a Virtual Camera or StreamElements' SE.Live plugin to send your video feed to TikTok LIVE Studio. This bypasses the built-in browser source limitations. 3. An Even Easier Alternative: Tikfinity (Specifically for TikTok) Because StreamElements doesn't focus on TikTok natively, a platform called Tikfinity is often considered the easiest and most reliable tool for TikTok-specific alerts and counters: Tikfinity is designed to connect directly to your TikTok LIVE to pull data, and it generates custom counter URLs specifically for TikTok Studio. It offers things like gift goals and follower goals that respond directly to TikTok gifts and follows, which StreamElements cannot do. If the basic StreamElements URL is giving you trouble, switching to Tikfinity and following their setup guide would be the next easiest, dedicated TikTok solution.
