---
id: 197383
source: GEMINI
date: 2025-09-25
tags: ['obs-studio', 'scene-creation', 'grouping-sources']
category: streaming
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/streaming-rig.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
summary: Bryan is asking if it's normal for a scene to be created when grouping sources in OBS.
---
# is it normal for a scene to be created if i make a group in my sources for a scene? 

### USER
is it normal for a scene to be created if i make a group in my sources for a scene? 

### GEMINI
That's an insightful question about OBS terminology! No, it is not normal for a "Group" in your Sources list to automatically create an entirely new "Scene" in your Scenes list. A Group is purely an organizational tool within a single Scene. They are two distinct things in OBS: FeatureLocationPurposeSceneThe main list (Scenes Panel)This is the entire screen or layout that your viewers see (e.g., "Starting Soon," "Gameplay," "Be Right Back"). You switch between these.GroupThe list inside a Scene (Sources Panel)This is a "folder" that lives inside a Scene. It lets you select, move, resize, or apply filters to multiple Sources (images, text, game capture) at the same time. How a Group Can "Act" Like a Scene While creating a Group doesn't make a new Scene, you might be thinking of a very common and powerful OBS technique called Scene Nesting (or putting a "Scene as a Source"): You create a new, separate Scene (e.g., "Webcam & Border"). You put your Webcam Source and a Border Image Source inside that new Scene. In your main "Gameplay" Scene, you add a Source and choose Scene, then select "Webcam & Border." In this scenario: The new scene you created ("Webcam & Border") now appears as a single item in your Sources list in the "Gameplay" scene. Any time you edit the webcam's position or border in the "Webcam & Border" scene, it instantly updates in all other scenes where you nested it. This is a great organizational tip, but it still requires you to manually create the new Scene first. If your OBS is spontaneously creating new entries in the Scenes list just by making a Group in the Sources list, that would indicate unusual behavior, possibly from a very old plugin or some form of corruption in your profile.
