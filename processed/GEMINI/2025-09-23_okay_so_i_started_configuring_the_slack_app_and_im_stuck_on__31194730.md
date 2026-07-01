---
category: ai-tools
date: 2025-09-23
id: 560410
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- private-ai-consulting
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan was trying to configure a Slack app and got stuck on setting environment
  variables for Slack tokens.
tags:
- slack-app-config
- environment-variables
- slack-tokens
- api-setup
---
# okay so i started configuring the slack app and i'm stuck on this step: Set environment variables: To keep your tokens secure, set them as environment variables in your terminal before running your application. For example:

export SLACK_APP_TOKEN='xapp-...'
export SLACK_BOT_TOKEN='xoxb-...'

### USER
okay so i started configuring the slack app and i'm stuck on this step: Set environment variables: To keep your tokens secure, set them as environment variables in your terminal before running your application. For example:

export SLACK_APP_TOKEN='xapp-...'
export SLACK_BOT_TOKEN='xoxb-...'

### GEMINI
Setting environment variables in the terminal is a crucial step for security, as it prevents you from hardcoding sensitive information directly into your code. The exact command you use depends on your operating system and the type of shell you're using. 1. For macOS and Linux (Bash or Zsh) On most modern macOS and Linux systems, the default shell is either Bash or Zsh. The command to set a temporary environment variable for your current terminal session is export. Open your terminal. Copy and paste the following commands, replacing the placeholders with your actual tokens: export SLACK_APP_TOKEN='xapp-your-app-token-here' export SLACK_BOT_TOKEN='xoxb-your-bot-token-here' The single quotes are important if your tokens contain special characters. Press Enter after each command. Verification: You can check that the variables are set correctly by running: echo $SLACK_APP_TOKEN and echo $SLACK_BOT_TOKEN. The terminal should print your token strings. Important: These variables will only be active in the current terminal window. If you close the terminal or open a new one, you'll need to run the export commands again. For a permanent solution, you would add these lines to your shell's configuration file (like .bashrc or .zshrc). 2. For Windows (Command Prompt or PowerShell) The process is slightly different for Windows. Command Prompt (CMD) Use the set command. Open Command Prompt. Enter the following commands, replacing the placeholders with your actual tokens: set SLACK_APP_TOKEN=xapp-your-app-token-here set SLACK_BOT_TOKEN=xoxb-your-bot-token-here Verification: Check the variables with echo %SLACK_APP_TOKEN% and echo %SLACK_BOT_TOKEN%. Similar to macOS/Linux, these are temporary and will not persist if you close the window. PowerShell Use the $env: prefix. Open PowerShell. Enter the following commands, replacing the placeholders with your actual tokens: $env:SLACK_APP_TOKEN = 'xapp-your-app-token-here' $env:SLACK_BOT_TOKEN = 'xoxb-your-bot-token-here' Verification: Check the variables with echo $env:SLACK_APP_TOKEN and echo $env:SLACK_BOT_TOKEN. For a permanent solution on Windows, you would set them through the graphical interface by searching for "Edit the system environment variables" in the Start menu.
