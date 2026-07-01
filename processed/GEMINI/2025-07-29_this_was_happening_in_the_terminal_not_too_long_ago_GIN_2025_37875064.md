---
category: ai-tools
date: 2025-07-29
id: 209260
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: stuck
source: GEMINI
summary: Bryan is sharing Ollama terminal logs showing repeated 400 errors on POST
  /api/show requests to diagnose the connection issue.
tags:
- ollama
- api-errors
- 400-status
- terminal-logs
---
# this was happening in the terminal not too long ago? [GIN] 2025/07/29 - 15:49:14 | 400 |       525.4µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:14 | 200 |     10.2208ms |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:17 | 400 |      1.5943ms |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:17 | 200 |      1.1451ms |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:20 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:20 | 200 |       504.5µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:23 | 400 |       504.1µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:23 | 200 |       517.3µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:26 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:26 | 200 |       505.8µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:29 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:29 | 200 |       775.9µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:32 | 400 |       702.4µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:32 | 200 |       593.3µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:35 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:35 | 200 |       596.1µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:38 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:38 | 200 |       735.2µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:41 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:41 | 200 |       731.2µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:47 | 400 |       996.8µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:47 | 200 |       504.7µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:50 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:50 | 200 |       503.5µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:53 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:53 | 200 |       550.6µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:56 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:56 | 200 |       778.6µs |       127.0.0.1 | GET      "/api/tags"

### USER
this was happening in the terminal not too long ago? [GIN] 2025/07/29 - 15:49:14 | 400 |       525.4µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:14 | 200 |     10.2208ms |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:17 | 400 |      1.5943ms |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:17 | 200 |      1.1451ms |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:20 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:20 | 200 |       504.5µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:23 | 400 |       504.1µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:23 | 200 |       517.3µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:26 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:26 | 200 |       505.8µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:29 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:29 | 200 |       775.9µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:32 | 400 |       702.4µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:32 | 200 |       593.3µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:35 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:35 | 200 |       596.1µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:38 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:38 | 200 |       735.2µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:41 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:41 | 200 |       731.2µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:47 | 400 |       996.8µs |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:47 | 200 |       504.7µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:50 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:50 | 200 |       503.5µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:53 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:53 | 200 |       550.6µs |       127.0.0.1 | GET      "/api/tags"
[GIN] 2025/07/29 - 15:49:56 | 400 |            0s |       127.0.0.1 | POST     "/api/show"
[GIN] 2025/07/29 - 15:49:56 | 200 |       778.6µs |       127.0.0.1 | GET      "/api/tags"

### GEMINI
That output from your terminal is the Ollama server logs running from your ollama serve command. This is exactly what we want to see! Let's break down what those lines mean: [GIN]: This is the logging prefix from the Gin web framework, which Ollama uses for its API server. 2025/07/29 - 15:49:14: Timestamp of the API request. 400 | ... | POST "/api/show": This indicates a request to the /api/show endpoint. A 400 status code means "Bad Request". This typically happens if the request body is malformed or missing required parameters. 200 | ... | GET "/api/tags": This indicates a request to the /api/tags endpoint. A 200 status code means "OK" or "Success". This endpoint is used to list the models that Ollama currently has available (like llama3.1:8b-instruct-q4_K_M). What this tells us: Ollama is definitely running and responsive. The server is alive and receiving requests. Something is repeatedly trying to POST to /api/show and failing (400 Bad Request). This could be continue.dev attempting to show a model, but sending an incorrect request, or it could be another application. Something is repeatedly successfully GETting /api/tags. This is a good sign, as continue.dev would typically call /api/tags to discover available models. The presence of these logs confirms that your ollama serve command is working as intended in your terminal. However, the core problem remains that continue.dev is not reflecting this connection in VS Code (no output channel, no models in sidebar). This output doesn't solve the VS Code side of the problem, but it confirms that Ollama itself is operational. Since the Ollama server is running and responding, and continue.dev still isn't working in VS Code after all our troubleshooting, the issue is almost certainly with the continue.dev extension's integration into your VS Code environment. As previously discussed, the next step is to file a detailed bug report on the continue.dev GitHub page. This log output will be valuable information to include in that report.
