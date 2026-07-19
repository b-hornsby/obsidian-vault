---
tags: [query, dashboard, tags]
---

# All Tags — Frequency Dashboard

> Tag frequency across all 3,080 conversation files. Sorted by count descending. Used by [[nodes/topics/thinking-patterns|Thinking Patterns]] for trend checks.

```dataview
TABLE length(rows) AS "Count"
FROM "processed"
FLATTEN tags AS tag
GROUP BY tag
SORT Count DESC
```

## Top Tags at a Glance

| Tag | Count |
|-----|-------|
| cachyos | 268 |
| gemini | 260 |
| ai | 223 |
| troubleshooting | 164 |
| local-llm | 146 |
| oobabooga | 142 |
| coding | 131 |
| model | 121 |
| go | 104 |
| steam-deck | 102 |
| python | 92 |
| obs-studio | 91 |
| ollama | 88 |
| image-editing | 88 |
| ai-tools | 85 |
| linux | 78 |
| rag | 76 |
| image-generation | 69 |
| text-generation | 65 |
| cursor-ide | 64 |
| character-design | 60 |
| homelab | 50 |
| text-generation-webui | 48 |
| llm | 42 |
| wsl2 | 40 |
| kde | 40 |
| nordvpn | 40 |
| obs | 39 |
| agent | 36 |
| ide | 35 |
| llama.cpp | 35 |
| error | 35 |
| continue.dev | 34 |
| git | 33 |
| version-control | 32 |
| package-management | 32 |
| streaming | 32 |
| blue-yeti | 32 |
| solana | 30 |

## By Category

```dataview
TABLE length(rows) AS "Files"
FROM "processed"
FLATTEN tags AS tag
GROUP BY file.category AS Category
SORT Files DESC
```
