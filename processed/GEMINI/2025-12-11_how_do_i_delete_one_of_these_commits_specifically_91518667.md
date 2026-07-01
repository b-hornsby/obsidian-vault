---
category: coding
date: 2025-12-11
id: 790344
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: partial
sentiment: curious
source: GEMINI
summary: Bryan is asking how to delete a specific commit from his Git history.
tags:
- git-delete-commit
- commit-history
- version-control
- code-cleanup
---
# how do i delete one of these commits specifically? 

### USER
how do i delete one of these commits specifically? 

### GEMINI
This is where you graduate from a beginner using basic add/commit to a strategic developer managing history. Your intention is to use a surgical tool to rewrite history, which is inherently dangerous and must be done with complete awareness of the consequences. The correct tool is Interactive Rebase (git rebase -i), and it should be treated like a high-powered, non-reversible editor for your commit history. The Critical Risk: Rewriting History Any action that removes a commit (except for git revert) will change the SHA-1 hash of the commit you delete, and the SHA-1 hash of every single commit that came after it. Local Consequence: You need to be ready to resolve conflicts when Git reapplies the subsequent commits. Remote Consequence: If the deleted commit was already pushed, you will need to use git push --force (or the safer git push --force-with-lease), which overwrites the remote history. If anyone else has pulled those commits, their repository will be out of sync, and they will face major problems. Do not do this on a shared branch. The Precise, Surgical Solution Assuming the commit you want to delete is not the last one and the branch is local or private: Step 1: Identify the Parent Commit You must start the interactive rebase from the commit immediately before the first commit you want to modify or delete. Run git log --oneline to see your history. Find the SHA-1 hash of the commit that is one step older than the commit you want to delete. Let's say your history looks like this, and you want to delete B: E - Last Commit (HEAD) D - Commit D C - Commit C B - Commit B (The one to delete) A - Commit A (The Parent Commit) You need the hash of A. (Or, if B is the 5th last commit, you could use HEAD~6). Step 2: Start the Interactive Rebase Start the rebase using the hash of the parent commit (A). git rebase -i <SHA-of-Commit-A> Git will open a text editor (like Vim or Nano) showing a list of commits starting from B up to the latest commit (E). Step 3: Edit the Commit List In the editor, you will see a list of lines, one for each commit, all starting with pick: pick <SHA-B> Commit B (The one to delete) pick <SHA-C> Commit C pick <SHA-D> Commit D pick <SHA-E> Last Commit (HEAD) # Rebase <SHA-A>.. onto <SHA-A> (4 commands) # ... instructions ... # Commands: # p, pick = use commit # r, reword = use commit, but edit the commit message # e, edit = use commit, but stop for amending # s, squash = use commit, but meld into previous commit # f, fixup = like "squash", but discard this commit's log message # d, drop = remove the commit # ... # If you remove a line here THAT COMMIT WILL BE LOST. To delete Commit B: Change the word pick to drop on the line for Commit B, OR simply delete the entire line. Save and close the file. Step 4: Complete the Rebase Git will now attempt to reapply commits C, D, and E without ever applying B. If Git encounters conflicts, you must resolve them, then run git rebase --continue. If the rebase finishes successfully, run git log --oneline to confirm that B is gone and the SHA-1 hashes of C, D, and E have changed. Step 5: Force Push (If necessary) If this branch was already pushed to a remote repository (like GitHub), you must overwrite the remote history: git push --force-with-lease The Safer Alternative: git revert If the commit is already public or shared, do not rewrite history. Instead, create a new commit that undoes the changes introduced by the target commit. git revert <SHA-of-Commit-B> This creates a new commit (let's call it F) that contains the inverse of B's changes. Commit B is still in the history, but its effects are canceled out, preserving the integrity of the shared timeline. Are you operating on a private branch where force-pushing is acceptable, or is this a shared branch that requires a safer, non-history-rewriting approach? To learn more about how interactive rebase can simplify and clean up your commit history, you can watch this video: Delete commits and edit commits with git rebase. Crazy simple and useful.


## Related

### Projects

- [[nodes/projects/homelab-stack|Homelab Stack]]

### Topics

- [[nodes/topics/tech/coding|Coding]]
- [[nodes/topics/tech/ai-tools|Ai Tools]]
- [[nodes/topics/personal/streaming|Streaming]]
