---
id: 523869
source: CLAUDE
date: 2026-04-05
tags: ['obs-overlay', 'now-playing', 'streaming-tools', 'pixelchat', 'lastfm']
category: streaming
sentiment: exploratory
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is searching for an alternative to 6labs for a 'now playing' overlay in OBS, seeking a tool similar to PixelChat but without the slow Last.fm scrobbling issues.
---
# OBS now playing overlay alternative

### HUMAN
i need a now playing overlay for my obs but 6labs sucks now

### ASSISTANT
```
This block is not supported on your current device yet.
```

Let me ask a couple quick things before I build this out:
```
This block is not supported on your current device yet.
```

### HUMAN
[User dismissed — do not proceed, wait for next instruction]

### ASSISTANT
No worries, just let me know when you're ready or if you want to give me the details another way!

### HUMAN
i just need to know if anything like that exists already

### ASSISTANT
Yeah, a few solid options:

**NOWTHEN** (nowthen.app) — pretty popular OBS now-playing overlay, free tier available, works with Spotify.

**Castbox / Song Ticker** — some streamers use browser source overlays tied to Last.fm scrobbling.

**Spotify OBS Plugin** — there's a community plugin that reads your Spotify playback directly into OBS as a browser source, no third party needed.

**Last.fm + custom HTML** — Last.fm has a free API, you point a local HTML file at it and add it as a browser source in OBS. Full control, no subscriptions.

**NowPlaying.io** — another 6 Labs competitor, cleaner UI, free plan exists.

**Replug** — more streamer-toolkit focused but has a now playing widget.

Honestly if you're on Spotify and want zero BS, the custom HTML + Last.fm API route gives you the most control and it's what a lot of people land on after getting fed up with the hosted services. I can build you one right now — you'd just drop the HTML file in as a browser source and you're done. Want that instead?

### HUMAN
i used to use pixelchat but the last.fm aspect is slow because of how scrobbling works

### ASSISTANT
Yeah that's the inherent problem with Last.fm — it scrobbles after like 50% of the track is played, so your overlay is always behind. Not great.

If you're on **Spotify**, the Spotify Web API gives you real-time currently playing data — no scrobbling delay at all. You poll it every few seconds and it's basically instant.

The catch is you need to set up a Spotify app in their developer dashboard to get a client ID/secret, but it's free and takes maybe 5 minutes. Then I can build you a self-hosted HTML overlay that:

- Polls Spotify every 3-5 seconds
- Shows track, artist, album art
- Styles it however you want
- Drops straight into OBS as a browser source

You'd run a tiny local server (or I can make it fully client-side with token auth). Want to go that route?

### HUMAN
is there any tool out there that already does that like pixelchat?

### ASSISTANT
```
This block is not supported on your current device yet.
```

Yeah there are a few good ones:

**nowplaying.site** — direct Spotify connect, no Last.fm, works with OBS/Streamlabs. Probably the closest to what you're used to with PixelChat.

**nowplayingobs.com** — Spotify-specific, bills itself as privacy-friendly, smooth updates.

**Sound Alerts** — has a built-in Spotify Now Playing widget that connects directly, fully customizable, and works as a browser source in OBS. You may already have Sound Alerts if you use it for alerts.

**Music on Stream** — Chrome extension that reads directly from Spotify web/desktop, YouTube Music, SoundCloud, Deezer and more — no scrobbling involved, real-time. This one's pretty slick because it reads from the player directly.

The Chrome extension one is probably worth looking at since it sidesteps any API auth setup and just reads what's playing in your browser. Any of those sound worth trying?
