---
category: coding
date: 2025-06-23
id: 571872
linked_nodes: ['nodes/people/bryan.md', 'nodes/topics/tech/coding.md']
linked_projects:
- homelab-stack
resolution: unresolved
sentiment: stuck
source: GEMINI
summary: The user encountered a git pull --ff-only failure due to diverging branches
  in their text-generation-webui repository and needs to decide between merge or rebase.
tags:
- git
- version-control
- diverging-branches
- fast-forward
- text-generation-webui
---
# (.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git pull --ff-only
hint: Diverging branches can't be fast-forwarded, you need to either:
hint:
hint:   git merge --no-ff
hint:
hint: or:
hint:
hint:   git rebase
hint:
hint: Disable this message with "git config advice.diverging false"
fatal: Not possible to fast-forward, aborting.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### USER
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ git pull --ff-only
hint: Diverging branches can't be fast-forwarded, you need to either:
hint:
hint:   git merge --no-ff
hint:
hint: or:
hint:
hint:   git rebase
hint:
hint: Disable this message with "git config advice.diverging false"
fatal: Not possible to fast-forward, aborting.
(.venv) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$

### GEMINI
Okay, Bryan, this message means that Git found differences between your local version of the Oobabooga code and the official repository's code that it can't simply "fast-forward" through. This usually happens if there are uncommitted changes on your local machine, or if your local branch history has diverged from the remote's history in a way that requires a more explicit command. Since your primary goal is just to update Oobabooga and get the latest features (including the RAG extensions), and you're not planning to keep any personal code changes within Oobabooga's core files, the safest and most reliable way to fix this is to reset your local repository to match the official one. Important Reassurance: This process will NOT affect your user_data/models folder. It will NOT affect your characters folder. It will NOT affect your data_sources folder (with your .txt files). It will discard any uncommitted changes to Oobabooga's core code files (like server.py itself or other files in the main text-generation-webui directory). For most users, these kinds of changes are unintentional or not important. Here are the commands to get your local Oobabooga code in sync: Fetch the latest changes from the remote without merging: git fetch origin main Press Enter. This downloads the latest state of the official repository's main branch to your local machine, but doesn't apply it yet. Reset your local branch to exactly match the remote's main branch: git reset --hard origin/main Press Enter. You'll get a message like HEAD is now at <commit-hash> ... This command forcefully overwrites your local Oobabooga code with the latest official version. Now, try git pull again (it should work cleanly this time, but it's good practice): git pull Press Enter. This should now result in "Already up to date." or a fast-forward merge, as your local branch is now aligned with the remote. Update Python dependencies: pip install -r requirements.txt --upgrade Press Enter. This will ensure all necessary Python libraries are correct for the updated code. Restart Oobabooga: Once the pip install command finishes, start Oobabooga manually again: python3 server.py --model-dir "user_data/models" --gpu-layers -1 --loader llama.cpp Press Enter. After it fully loads, check the "Settings" tab again (or look for a new "Extensions" tab if it appears on the left). You should now see the dedicated RAG extensions in the list!