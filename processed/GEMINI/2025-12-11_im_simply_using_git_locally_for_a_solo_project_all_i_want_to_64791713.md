---
category: coding
date: 2025-12-11
id: 599109
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: exploratory
source: GEMINI
summary: Bryan clarifies that he's using Git locally for a solo project and wants
  to delete a commit.
tags:
- git-delete-commit
- local-repository
- version-control
- solo-project
---
# im simply using git locally for a solo project. all i want to do is delete one of them 

### USER
im simply using git locally for a solo project. all i want to do is delete one of them 

### GEMINI
This is the critical detail: solo and local. Because you are working alone and have not pushed this history to a shared server, you have the clearance to use the surgical method to rewrite history without worrying about causing chaos for others. The tool is Interactive Rebase (git rebase -i). It is the non-destructive way to perform a destructive action, giving you a chance to review and confirm the change before it's final. Here is the precise, step-by-step plan to simply delete that single commit. The Precise Plan: Deleting a Local Commit Step 1: Identify the Parent Commit You cannot tell Git to delete Commit B directly. You must tell Git to start rewriting the history from the commit immediately before B. Run the command to view your history: git log --oneline Locate the commit you want to delete (let's call it B). Copy the short SHA-1 hash of the commit that comes before it (the parent commit, let's call it A). Example: If your history looks like this and you want to delete c8230f8: 25d8b74 (HEAD) FEAT: Final UI polish 77c5f2b FIX: Auth error handling c8230f8 WIP: Half-finished experimental change <
--- COMMIT TO DELETE (B) 1e9a301 FEAT: Initial user signup (A) <
--- PARENT SHA TO USE You need the hash 1e9a301. Step 2: Start the Interactive Rebase Start the history editor using the hash of the Parent Commit (A): # Replace <SHA-A> with the parent hash you copied (e.g., 1e9a301) git rebase -i <SHA-A> A text editor will open, showing you a list of commits starting from B to the present. Step 3: Execute the Deletion (drop) In the text file: Find the line for the commit you want to delete (c8230f8 in the example). Change the word pick at the beginning of that line to drop (or simply delete the entire line). The Editor Content Should Look Like This (After Editing): drop c8230f8 WIP: Half-finished experimental change pick 77c5f2b FIX: Auth error handling pick 25d8b74 FEAT: Final UI polish Save the file and close the editor. Step 4: Confirm the History Git will now attempt to reapply the remaining commits. Once finished, run git log --oneline again. You will see that the commit is gone, and the SHAs of all subsequent commits (77c5f2b and 25d8b74) have changed. The history is now clean. The Blunt Reminder You are using a powerful tool to clean up history, but this only fixes a symptom. The need to frequently delete a commit means you are still committing work that is not yet ready. The better habit is: If you have an experimental change you might delete, use git stash instead of git commit until you are sure you want to keep the work. Stashing is non-committal and non-destructive. Now, proceed with the rebase. Do you have the parent hash ready?


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
