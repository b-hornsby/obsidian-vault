---
id: 845978
source: GEMINI
date: 2025-07-05
tags: ['ai-tools', 'module', 'llm', 'ai', 'gemini', 'model', 'oobabooga', 'rag']
category: ai-tools
sentiment: building
resolution: resolved
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md', 'nodes/topics/tech/ai-tools.md']
---
# You: my wifi drops frequently
AI: Thinking...
/home/bryan_/helpdesk_ai_rag/rag_chat.py:76: LangChainDeprecationWarning: The method `Chain.__call__` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.
  response = qa_chain({"query": query})
Traceback (most recent call last):
  File "/home/bryan_/helpdesk_ai_rag/rag_chat.py", line 88, in <module>
    main()
    ~~~~^^
  File "/home/bryan_/helpdesk_ai_rag/rag_chat.py", line 76, in main
    response = qa_chain({"query": query})
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 386, in __call__
    return self.invoke(
           ~~~~~~~~~~~^
        inputs,
        ^^^^^^^
    ...<2 lines>...
        include_run_info=include_run_info,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 167, in invoke
    raise e
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 157, in invoke
    self._call(inputs, run_manager=run_manager)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/retrieval_qa/base.py", line 154, in _call
    answer = self.combine_documents_chain.run(
        input_documents=docs, question=question, callbacks=_run_manager.get_child()
    )
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 608, in run
    return self(kwargs, callbacks=callbacks, tags=tags, metadata=metadata)[
           ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 386, in __call__
    return self.invoke(
           ~~~~~~~~~~~^
        inputs,
        ^^^^^^^
    ...<2 lines>...
        include_run_info=include_run_info,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 167, in invoke
    raise e
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 157, in invoke
    self._call(inputs, run_manager=run_manager)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/combine_documents/base.py", line 138, in _call
    output, extra_return_dict = self.combine_docs(
                                ~~~~~~~~~~~~~~~~~^
        docs, callbacks=_run_manager.get_child(), **other_keys
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/combine_documents/stuff.py", line 259, in combine_docs
    return self.llm_chain.predict(callbacks=callbacks, **inputs), {}
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/llm.py", line 319, in predict
    return self(kwargs, callbacks=callbacks)[self.output_key]
           ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 386, in __call__
    return self.invoke(
           ~~~~~~~~~~~^
        inputs,
        ^^^^^^^
    ...<2 lines>...
        include_run_info=include_run_info,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 167, in invoke
    raise e
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 157, in invoke
    self._call(inputs, run_manager=run_manager)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/llm.py", line 127, in _call
    response = self.generate([inputs], run_manager=run_manager)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/llm.py", line 139, in generate
    return self.llm.generate_prompt(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        prompts,
        ^^^^^^^^
    ...<2 lines>...
        **self.llm_kwargs,
        ^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/language_models/llms.py", line 766, in generate_prompt
    return self.generate(prompt_strings, stop=stop, callbacks=callbacks, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/language_models/llms.py", line 973, in generate
    return self._generate_helper(
           ~~~~~~~~~~~~~~~~~~~~~^
        prompts,
        ^^^^^^^^
    ...<3 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/language_models/llms.py", line 792, in _generate_helper
    self._generate(
    ~~~~~~~~~~~~~~^
        prompts,
        ^^^^^^^^
    ...<3 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_community/llms/openai.py", line 463, in _generate
    response = completion_with_retry(
        self, prompt=_prompts, run_manager=run_manager, **params
    )
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_community/llms/openai.py", line 121, in completion_with_retry
    return llm.client.create(**kwargs)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/_utils/_utils.py", line 287, in wrapper
    return func(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/resources/completions.py", line 541, in create
    return self._post(
           ~~~~~~~~~~^
        "/completions",
        ^^^^^^^^^^^^^^^
    ...<30 lines>...
        stream_cls=Stream[Completion],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/_base_client.py", line 1249, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/_base_client.py", line 1037, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Internal Server Error
(base) bryan_@DESKTOP-NG2I0P2:~/helpdesk_ai_rag$

### USER
You: my wifi drops frequently
AI: Thinking...
/home/bryan_/helpdesk_ai_rag/rag_chat.py:76: LangChainDeprecationWarning: The method `Chain.__call__` was deprecated in langchain 0.1.0 and will be removed in 1.0. Use :meth:`~invoke` instead.
  response = qa_chain({"query": query})
Traceback (most recent call last):
  File "/home/bryan_/helpdesk_ai_rag/rag_chat.py", line 88, in <module>
    main()
    ~~~~^^
  File "/home/bryan_/helpdesk_ai_rag/rag_chat.py", line 76, in main
    response = qa_chain({"query": query})
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 386, in __call__
    return self.invoke(
           ~~~~~~~~~~~^
        inputs,
        ^^^^^^^
    ...<2 lines>...
        include_run_info=include_run_info,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 167, in invoke
    raise e
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 157, in invoke
    self._call(inputs, run_manager=run_manager)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/retrieval_qa/base.py", line 154, in _call
    answer = self.combine_documents_chain.run(
        input_documents=docs, question=question, callbacks=_run_manager.get_child()
    )
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 608, in run
    return self(kwargs, callbacks=callbacks, tags=tags, metadata=metadata)[
           ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 386, in __call__
    return self.invoke(
           ~~~~~~~~~~~^
        inputs,
        ^^^^^^^
    ...<2 lines>...
        include_run_info=include_run_info,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 167, in invoke
    raise e
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 157, in invoke
    self._call(inputs, run_manager=run_manager)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/combine_documents/base.py", line 138, in _call
    output, extra_return_dict = self.combine_docs(
                                ~~~~~~~~~~~~~~~~~^
        docs, callbacks=_run_manager.get_child(), **other_keys
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/combine_documents/stuff.py", line 259, in combine_docs
    return self.llm_chain.predict(callbacks=callbacks, **inputs), {}
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/llm.py", line 319, in predict
    return self(kwargs, callbacks=callbacks)[self.output_key]
           ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/_api/deprecation.py", line 189, in warning_emitting_wrapper
    return wrapped(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 386, in __call__
    return self.invoke(
           ~~~~~~~~~~~^
        inputs,
        ^^^^^^^
    ...<2 lines>...
        include_run_info=include_run_info,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 167, in invoke
    raise e
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/base.py", line 157, in invoke
    self._call(inputs, run_manager=run_manager)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/llm.py", line 127, in _call
    response = self.generate([inputs], run_manager=run_manager)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain/chains/llm.py", line 139, in generate
    return self.llm.generate_prompt(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        prompts,
        ^^^^^^^^
    ...<2 lines>...
        **self.llm_kwargs,
        ^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/language_models/llms.py", line 766, in generate_prompt
    return self.generate(prompt_strings, stop=stop, callbacks=callbacks, **kwargs)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/language_models/llms.py", line 973, in generate
    return self._generate_helper(
           ~~~~~~~~~~~~~~~~~~~~~^
        prompts,
        ^^^^^^^^
    ...<3 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_core/language_models/llms.py", line 792, in _generate_helper
    self._generate(
    ~~~~~~~~~~~~~~^
        prompts,
        ^^^^^^^^
    ...<3 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_community/llms/openai.py", line 463, in _generate
    response = completion_with_retry(
        self, prompt=_prompts, run_manager=run_manager, **params
    )
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/langchain_community/llms/openai.py", line 121, in completion_with_retry
    return llm.client.create(**kwargs)
           ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/_utils/_utils.py", line 287, in wrapper
    return func(*args, **kwargs)
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/resources/completions.py", line 541, in create
    return self._post(
           ~~~~~~~~~~^
        "/completions",
        ^^^^^^^^^^^^^^^
    ...<30 lines>...
        stream_cls=Stream[Completion],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/_base_client.py", line 1249, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/bryan_/miniconda3/lib/python3.13/site-packages/openai/_base_client.py", line 1037, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Internal Server Error
(base) bryan_@DESKTOP-NG2I0P2:~/helpdesk_ai_rag$

### GEMINI
Okay, we're very, very close! This is a fantastic step to get this error, as it means your rag_chat.py script successfully: Loaded the embedding model. Loaded your ChromaDB knowledge base. Set up the retriever. Successfully connected to your Oobabooga API! (If it hadn't, you'd see a connection error, not an Internal Server Error). Sent your question ("my wifi drops frequently") to the Oobabooga API along with the retrieved context. The error openai.InternalServerError: Internal Server Error is coming from Oobabooga itself, not from your rag_chat.py script. This usually means Oobabooga's model hit a snag when trying to process the prompt sent to it. Common reasons for this specific type of Internal Server Error from Oobabooga when using LangChain: Model Configuration Issues in Oobabooga: Context Window / Max Tokens: The prompt (your question + the retrieved documents) might be too long for the model's context window. GGUF models often have a specific n_ctx (context size) they can handle. If the combined prompt exceeds this, the model can error out. Output Tokens: If the model is trying to generate a very long answer, it might hit a limit. GPU/CPU memory limits: The model might be trying to allocate more memory than available. Oobabooga API model parameter: Sometimes, the OpenAI client expects a model parameter that Oobabooga isn't configured to receive or explicitly ignores, which can cause an internal parsing error. However, we're not explicitly sending one in this OpenAI setup, so it's less likely the direct cause here unless Oobabooga's API itself is misinterpreting the request. Let's start by trying a couple of common fixes, focusing on Oobabooga's side and the size of the prompt. Troubleshooting openai.InternalServerError Step 1: Adjust CHUNK_SIZE in create_db.py (Reducing Prompt Size) Your documents are likely well-populated now, and the combined text of 3 chunks (k=3) plus your prompt might be too large for the LLM's context window. Let's make the chunks smaller. Switch to your first terminal (where rag_chat.py is located, ~/helpdesk_ai_rag$). Open create_db.py for editing: nano create_db.py Find these lines: # Size of each text chunk (adjust based on your document length) CHUNK_SIZE = 500 Change CHUNK_SIZE from 500 to 250: # Size of each text chunk (adjust based on your document length) CHUNK_SIZE = 250 Save and Exit nano (Ctrl + X, then Y, then Enter). Step 2: Re-create the Vector Database Since you changed the CHUNK_SIZE, you must rebuild your chroma_db for the changes to take effect. In the first terminal (still in ~/helpdesk_ai_rag$), run create_db.py again: python create_db.py This will re-process all your documents into smaller chunks and overwrite the existing chroma_db. Wait for it to complete fully. You should see the usual success messages. Step 3: Adjust k (Number of Retrieved Documents) in rag_chat.py While we're at it, let's also reduce the number of documents retrieved in rag_chat.py to further ensure the prompt fits. Still in the first terminal, open rag_chat.py for editing: nano rag_chat.py Find this line: retriever = db.as_retriever(search_kwargs={"k": 3}) # k=3 means retrieve top 3 most similar documents Change k from 3 to 1 or 2 (let's try 1 for now, to be safe): retriever = db.as_retriever(search_kwargs={"k": 1}) # k=3 means retrieve top 3 most similar documents This tells the "Librarian" to only fetch the single most relevant chunk. Save and Exit nano (Ctrl + X, then Y, then Enter). Step 4: Re-run rag_chat.py Now, with smaller chunks and fewer retrieved documents, try your question again. In the first terminal (still in ~/helpdesk_ai_rag$), run rag_chat.py again: python rag_chat.py Once it loads, try your question: my wifi drops frequently Please perform these steps, and paste the entire output from your terminal after asking the question. Hopefully, this resolves the Internal Server Error!