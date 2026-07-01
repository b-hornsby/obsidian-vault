---
id: 066132
source: GROK
date: 2025-08-08
tags: ['openai', 'quantized-models', 'open-source-llm']
category: ai-tools
sentiment: curious
resolution: partial
linked_projects: []
linked_nodes: ['nodes/people/bryan.md', 'nodes/projects/operation-immortal-agent.md']
summary: Bryan was asking whether OpenAI plans to release quantized versions of their new open models.
---
# OpenAI Quantized Models Overview

### HUMAN
Are there plans for quantized versions of the new open model open ai models?

### ASSISTANT
OpenAI has already released two open-weight models, gpt-oss-120b and gpt-oss-20b, which are natively quantized using the MXFP4 format for efficient deployment. Specifically, the Mixture of Experts (MoE) weights in these models are quantized to 4-bit precision, allowing gpt-oss-120b to run on a single H100 GPU and gpt-oss-20b to operate within 16GB of memory, suitable for consumer hardware like laptops.[](https://openai.com/index/introducing-gpt-oss/)[](https://huggingface.co/blog/welcome-openai-gpt-oss)[](https://github.com/openai/gpt-oss)

There is no direct information from the provided sources about plans for additional quantized versions (e.g., different quantization levels like GPTQ or AWQ) beyond the existing MXFP4 quantization. However, posts on X indicate interest from the community in further quantized versions, such as a 4-bit GPTQ or AWQ version of gpt-oss-120b, suggesting potential demand but no confirmed plans from OpenAI. OpenAI’s focus on native MXFP4 quantization and their permissive Apache 2.0 license suggests they are prioritizing efficient, accessible models for developers, which could imply future quantization efforts if demand grows, but no specific announcements have been made.[](https://www.technologyreview.com/2025/08/05/1121092/openai-has-finally-released-open-weight-language-models/)[](https://www.cnbc.com/2025/08/05/openai-open-weight-meta-mistral-deepseek-ai.html)

For the most current details, you can check OpenAI’s official blog or Hugging Face for updates on model releases. If you’re interested in community-driven quantization efforts, platforms like Hugging Face or GitHub may host user-contributed quantized versions in the future.[](https://x.com/OpenAI/status/1952783301212856704)[](https://github.com/openai/gpt-oss)
