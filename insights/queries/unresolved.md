---
tags: [query, dashboard, unresolved, action-items]
---

# Unresolved Loops — TODO, FIXME, Open Questions

> Conversations with unresolved or partial resolution, plus files containing TODO/FIXME markers.

## Unresolved Conversations

> Files where `resolution: unresolved` — conversations that ended without a clear answer.

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  sentiment AS "Sentiment",
  date AS "Date"
FROM "processed"
WHERE resolution = "unresolved"
SORT date DESC
```

## Partial Resolutions

> Files where `resolution: partial` — conversations that got partial answers. Top 50 most recent.

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  sentiment AS "Sentiment",
  date AS "Date",
  summary AS "Summary"
FROM "processed"
WHERE resolution = "partial"
SORT date DESC
LIMIT 50
```

## Abandoned Conversations

> Files where `resolution: abandoned`.

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  date AS "Date",
  summary AS "Summary"
FROM "processed"
WHERE resolution = "abandoned"
SORT date DESC
```

## Resolution Summary

```dataview
TABLE length(rows) AS "Count"
FROM "processed"
WHERE resolution
GROUP BY resolution AS "Resolution"
SORT Count DESC
```

## Sentiment of Unresolved Items

> What emotions are associated with unresolved conversations?

```dataview
TABLE length(rows) AS "Count"
FROM "processed"
WHERE resolution = "unresolved" AND sentiment
GROUP BY sentiment AS "Sentiment"
SORT Count DESC
```
