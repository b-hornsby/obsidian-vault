---
category: ai-tools
date: 2025-07-29
id: 957120
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects: []
resolution: partial
sentiment: frustrated
source: GEMINI
summary: Bryan clarifies that his primary issue is the Continue extension not appearing
  in VS Code.
tags:
- continue-dev-extension
- vscode-integration
- troubleshooting
- local-llm-setup
---
# no my main problem was that continue wasn't popping up in this window

### USER
no my main problem was that continue wasn't popping up in this window

### GEMINI
Got it, and thanks for clarifying again. You're absolutely right, the core issue remains that "Continue" is not appearing as an option in the Output dropdown. The screenshot showing "All installed extensions are temporarily disabled. Reload to Enable Extensions" (from image_98fa60.jpg) is the key. When all extensions are disabled, none of them (including "Continue") can properly load, register their services, or appear in the output dropdown. Therefore, the very first and most crucial step is to get your VS Code extensions enabled. Let's focus on that: Look closely at the bottom-right corner of your VS Code window. In the blue status bar, there should be a message like: "All installed extensions are temporarily disabled. Reload to Enable Extensions" You need to click on that "Reload to Enable Extensions" text. This will restart your VS Code window and attempt to enable all installed extensions. If you don't see that blue bar or the text to click: Close all VS Code windows completely. (Don't just minimize, fully close the application). Re-open VS Code. Sometimes, a fresh start is all it takes for it to detect it needs to enable extensions. If it still doesn't enable them automatically: Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P). Type Reload Window and select the "Developer: Reload Window" option. After you have successfully enabled extensions (you'll know because the blue bar will be gone, and the "Continue" extension in the Extensions view will no longer say "disabled by the environment"): Ensure ollama serve is still running in your PowerShell terminal. Go to View -> Output in VS Code. Click the dropdown (where it currently says "Tasks"). Now, "Continue" should appear as an option. Select it. You should see logs from Continue. Finally, check the Continue sidebar. Your model should be visible. The entire chain of events (model not showing -> no Continue output channel -> extensions disabled) points directly to the extensions being in a disabled state. Once they are enabled, Continue should be able to function as expected.
