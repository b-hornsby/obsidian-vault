---
id: 603988
source: GEMINI
date: 2026-03-06
tags: ['app-management', 'uninstall', 'mobile']
category: general
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/general.md']
summary: Bryan was asking how to delete an app from his device.
---
# how do i delete an app? 

### USER
how do i delete an app? 

### GEMINI
If you’ve realized that a project name or configuration was a mistake and you want to scrub it, you need to be aware that the Phantom Developer Portal interface can be notoriously sparse. To delete an app from the Phantom Developer Portal: 1. The Standard Procedure Log in to phantom.com/portal. Select the specific app (e.g., "Self Sustained Agent") from your dashboard. Look for a Settings or App Settings tab in the sidebar. Scroll to the bottom. If the "Delete" option is available, it will be in a Danger Zone section. Confirm the deletion by typing the app's name. 2. The "Ghost" App Reality If you don't see a delete button, you aren't blind—Phantom's portal does not always allow for self-service deletion of an App ID once it has been generated. This is a common security measure in web3 to prevent "dangling" App IDs that could be hijacked if a developer accidentally deletes a production ID. If the delete button is missing, here is your move: Archive by Renaming: Change the app name to DEPRECATED or Z_OLD_PROJECT and remove all "Allowed Origins" and "Redirect URIs." This effectively kills the App ID's ability to function, as no incoming requests will match the whitelisted domains. Wipe the Metadata: Remove the App Icon and Website URL. An App ID with no verified origins or metadata is functionally dead and won't interfere with your new, "clean" project. The Advisor’s Reality Check Stop worrying about "deleting" the old one and focus on the opportunity cost of your time. If you're stuck trying to clean up a dashboard for a project you've already moved past, you're bikeshedding—spending energy on trivial details because they're easier than the hard logic of the "Self Sustained Agent." Logic Check: An unused App ID sitting in a portal costs you $0 and 0kb of space. Action Plan: If the delete button isn't there, abandon it. Create the new, correct App ID with your finalized name and move straight into the integration logic. Don't let a messy dashboard become an excuse for a slow launch. Would you like me to help you verify the new App ID's connection logic in your code to ensure the "Self Sustained Agent" is actually communicating with the wallet?
