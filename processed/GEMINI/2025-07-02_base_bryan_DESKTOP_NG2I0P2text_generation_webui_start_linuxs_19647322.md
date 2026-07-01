---
id: 045727
source: GEMINI
date: 2025-07-02
tags: ['ai-tools', 'llm', 'ai', 'agent', 'gemini', 'model', 'oobabooga', 'rag']
category: ai-tools
sentiment: executing
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# (base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
18:50:20-374063 INFO     Starting Text generation web UI
18:50:20-375944 INFO     Loading settings from "user_data/settings.yaml"
18:50:20-377676 INFO     Loading the extension "openai"
18:50:20-457467 INFO     OpenAI-compatible API URL:

                         http://127.0.0.1:5000


Running on local URL:  http://127.0.0.1:7860

### USER
(base) bryan_@DESKTOP-NG2I0P2:~/text-generation-webui$ ./start_linux.sh
18:50:20-374063 INFO     Starting Text generation web UI
18:50:20-375944 INFO     Loading settings from "user_data/settings.yaml"
18:50:20-377676 INFO     Loading the extension "openai"
18:50:20-457467 INFO     OpenAI-compatible API URL:

                         http://127.0.0.1:5000


Running on local URL:  http://127.0.0.1:7860

### GEMINI
Fantastic! Success! That's exactly what we wanted to see: 18:50:20-457467 INFO OpenAI-compatible API URL: http://127.0.0.1:5000 This means your Oobabooga text-generation-webui is now running with its API enabled, listening on http://127.0.0.1:5000. This is the crucial foundation for integrating our RAG pipeline. Now that we have the Oobabooga API confirmed and running, we can move on to setting up the components necessary for Agentic RAG. Phase 2: Setting up RAG Components (Vector Database & Embedding Model) For Agentic RAG, we need a way to efficiently store and search your helpdesk knowledge base. This involves two main parts: Creating Embeddings: Turning your plain text documents into numerical "vectors" that computers can understand and compare for similarity. Storing Embeddings: Putting these vectors into a special database optimized for fast similarity searches (a "vector database"). We'll use Sentence Transformers for creating embeddings and ChromaDB as our vector database. These are excellent, easy-to-use choices for local LLM projects. Step 1: Install Necessary Python Libraries We'll need to install the Python libraries for ChromaDB, Sentence Transformers, and LangChain (our orchestration framework). Why these? sentence-transformers: This library provides pre-trained "embedding models." Think of an embedding model as a highly skilled artist who can take any piece of text (like a helpdesk article) and draw a unique "picture" of its meaning using numbers. Texts with similar meanings will have "pictures" that look very similar. chromadb: This is our "vector database." Imagine a massive library where every book (or document) has a barcode that represents its "meaning picture." ChromaDB is like a super-efficient librarian who can take a new "meaning picture" (from your question) and instantly find all the books whose "meaning pictures" are most similar to it. It's designed for speed when comparing these numerical "pictures." langchain: This is our "orchestration framework." This is the smart manager that ties everything together. It will take your user's question, send it to the embedding model, use that embedding to search ChromaDB for relevant documents, take those documents, and then combine them with your original question to send to Oobabooga's Nous-Hermes model for a final, informed answer. It handles the "agentic" part by managing the flow of information and deciding what steps to take. Open a NEW Ubuntu WSL terminal window. Important: Keep your Oobabooga terminal window running in the background. We need Oobabooga to stay active with its API enabled. To open a new window, click the Windows Start button, type "Ubuntu", and click on the Ubuntu app. Navigate to a suitable directory. We don't want to install these directly inside the text-generation-webui folder to keep things separate. A good place would be your home directory or a new folder specifically for your RAG project. Let's create a new folder: mkdir ~/helpdesk_ai_rag cd ~/helpdesk_ai_rag Activate your Oobabooga's Conda environment. Oobabooga uses conda to manage its Python environment. This ensures that the libraries we install are compatible with your existing Python setup. Your start_linux.sh script already activates an environment, likely named textgen or similar. You can find the exact name by looking at the lines around conda activate in your start_linux.sh script, or often it's the base environment if you haven't explicitly created one. Based on your prompt, it looks like your terminal starts with (base), which indicates your base conda environment is active. We'll proceed with that. If it said something else, like (textgen), you'd activate that instead. If your prompt shows (base), you're already in the right environment. If not, activate the base environment: conda activate base (You should see (base) appear at the beginning of your terminal prompt once it's active.) Install the libraries. Now, run the following command to install everything: pip install langchain chromadb sentence-transformers unstructured "unstructured[pdf]" pypdf openai unstructured and pypdf: These are helpers for loading data, especially from PDF files, which are common for helpdesk documents. openai: Even though we're using Oobabooga, LangChain often uses the openai library to communicate with OpenAI-compatible APIs (like Oobabooga's API). This command might take a few minutes as it downloads and installs many packages. You'll see a lot of text scrolling by. Please run these commands in your new Ubuntu terminal window. Once the installation is complete, please let me know if there were any errors during the pip install step. If there were errors, please paste them here.