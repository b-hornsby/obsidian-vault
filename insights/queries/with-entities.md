---
tags: [query, dashboard, entities, linked-nodes]
---

# Conversations with Entity Links

> All conversations that have meaningful `linked_nodes` references to entity pages.

## All Entity-Linked Conversations

> Files where `linked_nodes` is non-empty and contains entity references.

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  linked_nodes AS "Linked Entities",
  date AS "Date"
FROM "processed"
WHERE linked_nodes AND length(linked_nodes) > 0
SORT date DESC
LIMIT 50
```

## By Entity — Conversation Counts

> How many conversations link to each entity page.

```dataview
TABLE length(rows) AS "Conversations"
FROM "processed"
FLATTEN linked_nodes AS ln
WHERE ln
GROUP BY ln AS "Entity"
SORT Conversations DESC
```

## People Mentions

> Conversations linked to person entity pages.

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  date AS "Date",
  summary AS "Summary"
FROM "processed"
FLATTEN linked_nodes AS ln
WHERE contains(ln, "nodes/people/")
GROUP BY ln AS "Person"
SORT file.name ASC
```

## Project Mentions

> Conversations linked to project entity pages.

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  date AS "Date"
FROM "processed"
FLATTEN linked_nodes AS ln
WHERE contains(ln, "nodes/projects/")
GROUP BY ln AS "Project"
SORT file.name ASC
```

## Topic Mentions

> Conversations linked to topic entity pages.

```dataview
TABLE
  file.name AS "File",
  category AS "Category",
  date AS "Date"
FROM "processed"
FLATTEN linked_nodes AS ln
WHERE contains(ln, "nodes/topics/")
GROUP BY ln AS "Topic"
SORT file.name ASC
```

## Entity Link Coverage

> Overview of how well-connected the vault is.

```dataview
TABLE length(rows) AS "Files"
FROM "processed"
WHERE linked_nodes
GROUP BY length(linked_nodes) AS "Link Count"
SORT Files DESC
```
