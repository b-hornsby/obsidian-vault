---
id: 675296
source: GEMINI
date: 2025-08-21
tags: ['discord', 'bot-permissions', 'channel-management', 'server-config']
category: coding
sentiment: building
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan is asking about Discord server permissions needed to restrict a channel so only his bot can post in it.
---
# what permissions do i need to change in my discord server to allow the bot that i have set up to be the only one posting in that channel?

### USER
what permissions do i need to change in my discord server to allow the bot that i have set up to be the only one posting in that channel?

### GEMINI
Based on the images provided, here are the permissions you need to change in your Discord server to allow a bot to be the only one posting in a channel: 1. For the Channel's permissions: Remove the "Send Messages" permission for all roles, including @everyone. This will prevent anyone other than the bot from typing and sending messages in the channel. 2. For the Bot's specific role: Ensure the bot's role has the "Send Messages" permission enabled. This is crucial for the bot to be able to post in the channel. 3. Other permissions you may want to disable for non-bot roles: Send Messages in Threads: If you want to keep the channel completely free of user-generated content, you should also disable this. Embed Links: Disabling this will prevent users from posting links that create rich embeds. Attach Files: Disabling this will prevent users from uploading images, videos, or other files. Add Reactions: Disabling this will prevent users from adding emoji reactions to messages. Use External Emoji/Stickers: Disabling these will prevent users from using emojis or stickers from other servers. Mention @everyone, @here, and All Roles: Disabling this prevents users from spamming mentions. By disabling the "Send Messages" permission for everyone and keeping it enabled only for the bot's role, you will achieve the desired effect of having a bot-only posting channel.
