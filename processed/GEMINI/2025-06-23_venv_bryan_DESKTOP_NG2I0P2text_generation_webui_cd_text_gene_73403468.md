---
category: coding
date: 2025-06-23
id: 847422
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects: []
resolution: partial
sentiment: curious
source: GEMINI
summary: The user encountered a git pull error due to divergent branches and needs
  to configure a reconciliation strategy (merge, rebase, or fast-forward only) before
  proceeding.
tags:
- git
- version-control
- divergent-branches
- pull-strategy
- cli
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git pull
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ cd ~/text-generation-webui
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git pull
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
You've hit a common Git message, Bryan! Don't worry, this doesn't mean you've messed anything up or that anything is erased. This fatal: Need to specify how to reconcile divergent branches. message appears because your local main branch (the one Oobabooga is on) has a slightly different history than the main branch on the official Oobabooga GitHub repository. This can happen for various reasons, even without you making explicit commits. Git just needs you to tell it how you want to combine these different histories. Given that you want to simply update Oobabooga and don't want to lose any of your current files or settings, the safest and most direct way to handle this for Oobabooga updates is to use the --ff-only (fast-forward only) option. This tells Git: "Only update my code if it's a simple, straightforward update that won't create complex merges." Here's what to do: Run the git pull command with the --ff-only option: git pull --ff-only Press Enter. What this does: It tries to perform a "fast-forward" merge. This is the cleanest way to update if your local branch hasn't introduced any new commits that conflict with the remote. If there are no conflicts, it will simply apply the updates from the Oobabooga repository. If there are minor uncommitted changes or conflicts that prevent a clean fast-forward, Git will tell you (it won't force a messy merge, which is what we want to avoid). We can address that if it happens, but it's less common for typical Oobabooga users who don't manually edit the core code files. After that command finishes successfully (without another "fatal" error): You should see output indicating that files have been updated. Then, you can proceed with updating the Python dependencies: pip install -r requirements.txt --upgrade Press Enter. Once both of those commands complete, you can restart Oobabooga manually and check the extensions list again.