---
tags: [query, dashboard, recent, activity]
---

# Recently Modified — Last 20 Files

> The 20 most recently modified conversation files in the vault.

## Last 20 Modified

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  date AS "Date",
  source AS "Source",
  summary AS "Summary"
FROM "processed"
SORT file.mtime DESC
LIMIT 20
```

## Last 20 by Date (Frontmatter)

> Most recent by the `date` frontmatter field (may differ from file modification time).

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  date AS "Date",
  source AS "Source",
  summary AS "Summary"
FROM "processed"
WHERE date
SORT date DESC
LIMIT 20
```

## Recent by Source

> Breakdown of the 20 most recent files by their source (AI platform).

```dataview
TABLE length(rows) AS "Count"
FROM "processed"
SORT file.mtime DESC
LIMIT 20
GROUP BY source AS "Source"
SORT Count DESC
```

## Recent Activity by Category

> Category distribution of the 20 most recently modified files.

```dataview
TABLE length(rows) AS "Count"
FROM "processed"
SORT file.mtime DESC
LIMIT 20
GROUP BY category AS "Category"
SORT Count DESC
```
