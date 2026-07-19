---
tags: [query, dashboard, projects]
---

# All Projects — Query View

> All project entity pages with status, first/last seen dates, and linked conversation counts. [[insights/goals/goals-overall|Goals Overview]] maps these to quarterly targets.

## Project Pages

```dataview
TABLE
  status AS "Status",
  first_seen AS "First Seen",
  last_seen AS "Last Seen",
  tags AS "Tags"
FROM "nodes/projects"
WHERE type = "project"
SORT last_seen DESC
```

## Projects by Conversation Count

> Number of conversations linking to each project via `linked_nodes`.

```dataview
TABLE length(rows) AS "Conversations"
FROM "processed"
FLATTEN linked_nodes AS ln
WHERE contains(ln, "nodes/projects/")
GROUP BY ln AS "Project Link"
SORT Conversations DESC
```

## Project Entity Pages

```dataview
LIST
FROM "nodes/projects"
WHERE type = "project"
SORT file.name ASC
```
