---
category: streaming
date: 2026-01-08
id: 366587
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/streaming-rig.md']
linked_projects: []
resolution: partial
sentiment: building
source: GEMINI
summary: Bryan wants to enhance the 3D appearance of a coin-like object in a video
  while preserving the existing art style.
tags:
- video-editing
- 3d-effect
- image-manipulation
---
# make the object in this video look more like a coin while maintaining the art/characters that are within the image. do not change anything about the way it looks in that regard, only focus on making the object look more 3 dimensional

### USER
make the object in this video look more like a coin while maintaining the art/characters that are within the image. do not change anything about the way it looks in that regard, only focus on making the object look more 3 dimensional

### GEMINI
I cannot edit this video file directly to render new 3D geometry. I am an AI, not a post-production studio or a 3D rendering engine. However, acting as your technical advisor, I will expose exactly why your current attempt fails to look like a coin and give you the specific workflow to fix it. The Problem: You Are Faking 3D Right now, you are rotating a 2D plane (or a cylinder with near-zero height) in 3D space. It doesn't look like a coin; it looks like a rotating cardboard coaster or a POG. To achieve the "coin" look without losing the artwork, you need to stop treating this as an image and start treating it as a physical object. You are missing three critical components: Geometric Depth (Extrusion): Coins have a specific thickness. Materiality (Specular/Metallic): Coins interact with light; they don't just display color. Topography (Bump/Normal Maps): Real coins are stamped. The art shouldn't just be printed on; it should be embossed into the surface. The Execution Plan To fix this, you need to use a 3D tool like Blender (free) or After Effects (with Element 3D). Here is the prioritized workflow to make this a tangible object. 1. Fix the Geometry (The "Third Dimension") Extrude the Cylinder: You need to increase the depth (Z-axis). A standard coin is not a wafer. Give it visible thickness. Bevel the Edges: Sharp 90-degree angles look like computer graphics. Real coins have slightly rounded or chamfered edges. Add a small bevel modifier to catch the light on the rim. Separate the Faces: The meme art goes on the top and bottom faces (Caps). The side (the Rim) needs to be a separate material—usually a ridged metal texture or a smooth, high-polish gold/silver. Do not wrap the meme faces around the side; it looks amateurish. 2. Fix the Material (The "Coin" Look) The art is currently completely matte (flat). Keep the Art: Map your meme image to the Base Color (Albedo). Make it Metallic: Turn the "Metallic" value up to 1.0. Adjust Roughness: Turn the "Roughness" down (around 0.2 - 0.3). This allows the environment to reflect off the surface. Lighting: You need an HDRI environment or point lights in your scene. A coin only looks like a coin if light glints off it as it spins. 3. Advanced Polish: The "Stamped" Effect If you want to stop looking like a cheap sticker on a token, you need Normal Mapping. Take your source image into Photoshop or an online Normal Map generator. Convert the meme art into a purple/blue Normal Map (or a black and white Height Map). Apply this to the "Normal" or "Displacement" slot of your 3D material. Result: The light will catch the edges of the Illuminati triangle and the text, making it look like the characters are stamped out of the metal. Summary of Changes FeatureCurrent State (The "POG")Desired State (The Coin)ThicknessPaper-thinExtruded cylinder with substantial weightEdgeNon-existent or texturedMetallic, possibly ridged/reededSurfaceFlat ImageMetallic shader with roughness variationTexturePrinted inkEmbossed relief (via Normal Map) Next Step Do you have the original static image file of the meme art? If you upload that, I can guide you on how to generate the specific "Normal Map" to make the characters pop out like real metalwork.

### GEMINI
I couldn't do that because I'm getting a lot of requests right now. Please try again later.
