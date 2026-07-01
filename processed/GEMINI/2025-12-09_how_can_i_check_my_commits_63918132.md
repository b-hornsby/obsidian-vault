---
id: 982268
source: GEMINI
date: 2025-12-09
tags: ['git', 'commit-history', 'version-control']
category: coding
sentiment: curious
resolution: partial
linked_projects: ['nodes/projects/flappy-meme-bird.md']
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
summary: Bryan wanted to learn how to view his git commit history.
---
# how can i check my commits? 

### USER
how can i check my commits? 

### GEMINI
The most fundamental and effective way to check your commits in Git is using the git log command. 🔍 The Basics: git log The simplest form of the command shows a reverse chronological list of all commits in the current branch: $$\text{git log}$$ This output will typically show: The SHA-1 hash (the unique commit ID). The Author (name and email). The Date (when the commit was created). The Commit Message. (Your advisor note: This is why having clean, descriptive messages is critical—it tells you the "why" of the change.) 🌟 Filtering and Formatting Your Log git log has powerful options to make the output much cleaner and more useful. OptionCommandDescriptionOne Linegit log --onelineShows one commit per line, displaying only the first part of the SHA and the subject line. (Recommended for quick scans)Specific Countgit log -n 5Shows only the last 5 commits.Graph Viewgit log --graph --oneline --decorateDisplays a visual ASCII graph of the branch structure alongside the commits.Authorgit log --author="Your Name"Shows only commits made by a specific author.Files Changedgit log --statShows which files were modified and the number of lines added/deleted for each commit.Time Periodgit log --since="2 weeks ago"Shows commits from the last two weeks. 💡 The Advisor's Recommended Command You're looking for efficiency and clarity. Use this alias to get the most useful information at a glance: $$\text{git log --graph --oneline --decorate --all}$$ --graph: Visually maps the branches and merges. --oneline: Keeps it concise. --decorate: Shows branch and tag names next to the relevant commits. --all: Shows the history of all branches, not just the current one (crucial for seeing where work is truly happening). 🧐 How to Check Uncommitted Changes Checking your commits (already saved snapshots) is one thing, but you also need to check your current work (changes that haven't been committed yet). 1. What's the Status? $$\text{git status}$$ Tells you everything about the current state: Files modified but unstaged (in the Working Directory). Files that are staged (ready to be committed). Untracked files. Which branch you are on. 2. What Exactly Changed? $$\text{git diff}$$ Shows the line-by-line differences between your Working Directory (your files now) and the Staging Area. $$\text{git diff --staged}$$ Shows the line-by-line differences between your Staging Area and the last commit (HEAD). Next Step: Which specific log output format are you finding most confusing, or do you need to check commits across multiple feature branches?
