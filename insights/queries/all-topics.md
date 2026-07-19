---
tags: [query, dashboard, topics]
---

# All Topics — Query View

> All topic entity pages with conversation counts and linked files. [[insights/goals/goals-overall|Goals Overview]] and [[nodes/projects/second-brain-vault|Second Brain Vault]] consume the same underlying data.

## Topic Pages

```dataview
TABLE
  aliases AS "Aliases",
  tags AS "Tags"
FROM "nodes/topics"
WHERE type = "topic"
SORT file.name ASC
```

## Conversations by Category

> Category is the primary topic classification on each conversation file.

```dataview
TABLE length(rows) AS "Conversations"
FROM "processed"
WHERE category
GROUP BY category AS "Category"
SORT Conversations DESC
```

## Conversations by Topic (via linked_nodes)

> Topics linked through the `linked_nodes` frontmatter field.

```dataview
TABLE length(rows) AS "Conversations"
FROM "processed"
FLATTEN linked_nodes AS ln
WHERE contains(ln, "nodes/topics/")
GROUP BY ln AS "Topic"
SORT Conversations DESC
```

## Topic Map of Contents

```dataview
TABLE
  file.inlinks AS "Inlinks",
  file.outlinks AS "Outlinks"
FROM "nodes/topics"
WHERE type = "topic"
SORT file.name ASC
```
