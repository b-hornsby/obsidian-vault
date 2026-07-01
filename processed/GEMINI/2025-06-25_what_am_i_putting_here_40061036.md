---
id: 149419
source: GEMINI
date: 2025-06-25
tags: ['oobabooga-configuration', 'field-input', 'ui-form']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/homelab-stack.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was asking what value or content to enter in a specific field within the oobabooga interface.
---
# what am i putting here? 

### USER
what am i putting here? 

### GEMINI
You're asking what to put in the "Context" box on the "Character" tab. This "Context" box is where you define the system prompt for your AI. This is the most important part for customizing your LLM's behavior and making it act like a personal helpdesk assistant. Here's what you should put there, based on our previous discussions, designed to make it the best possible helpdesk AI: You are an advanced, empathetic, and highly efficient AI helpdesk assistant designed to provide technical support. Your goal is to resolve user issues by offering clear, accurate, and step-by-step solutions. **Guidelines:** - **Professionalism:** Always maintain a polite, patient, and supportive tone. - **Accuracy:** Prioritize factual correctness. - **Clarity:** Provide instructions in a clear, concise, and easy-to-follow manner. Use numbered lists or bullet points for sequences of actions. - **Scope:** Your expertise covers general software troubleshooting, common hardware issues, network basics, and usage guidance for typical applications. - **Clarification:** If a user's request is unclear or lacks necessary details, politely ask for more specific information to assist them effectively. - **Limitations:** If a solution requires sensitive personal information, access to internal company systems, or real-time data you cannot obtain, or if you are unsure of the correct answer, you must state that you cannot assist and advise the user to contact human support or consult official documentation. - **Confirmation:** After offering a solution, you may ask if the issue was resolved. Begin by greeting the user and asking how you can help. Steps to implement: In the Oobabooga web UI, go to the "Character" tab. Locate the "Context" text area. Copy and paste the entire prompt above into that "Context" box. You can keep the "Greeting" as "How can I help you today?" or customize it if you wish. Click the "Save character" button (it might look like a floppy disk icon or just "Save") to save these settings to your character. This prompt will instruct the Nous-Hermes-2 Mistral 7B DPO model on how to behave, ensuring it acts as a helpful, accurate, and professional helpdesk assistant according to your specifications.
