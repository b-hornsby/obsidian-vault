---
source: GPT
date: 2025-07-15
category: general
id: 50465550
linked_nodes: ['nodes/people/bryan.md']
---
# Check CrewAI Version

### ASSISTANT
To check your **CrewAI version** in **Cursor** (or any terminal inside your project environment), do the following:

#### 🧠 Option 2: Using Python
Alternatively, run this in a Python shell or script:

```python
import crewai
print(crewai.__version__)
```

> You can run this in a file or directly in the Python REPL with `python3`.
---
### ⚠️ If You Get an Error:
If CrewAI isn't found, it's likely not installed in your current environment. You can install it with:

```bash
pip install crewai
```

Or update it:

```bash
pip install --upgrade crewai
```

Let me know if you want help checking which environments are active in Cursor or WSL2 — I can walk you through that too.