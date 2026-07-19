---
generated: 2026-04-29
files_scanned: 3400
date_range: 2023-11-05 to 2026-04-09
---

# Blind Spot Detection — April 2026

---

## Pattern A — The Loop

Topics or questions Bryan has returned to 3+ times without apparent resolution.

### LOOP DETECTED: Local LLM Setup & GPU Optimization
First asked: 2025-11-17
Times returned: 10+
Last seen: 2026-04-02
What he keeps asking: Which model runs best on RTX 3070, whether to use Ollama vs LM Studio vs local alternatives, CUDA version conflicts, 35B model performance on 8GB VRAM, DDR5 RAM impact.
What's likely missing: He hasn't committed to a single working local stack. The 3070 has been "enough" since November 2025, but he keeps treating it like a bottleneck that needs solving.
Suggested resolution path: Pick one stack (Ollama + a single quantized 7B/13B model), document the exact working config in one note, and stop optimizing until a project actually hits a performance wall.

### LOOP DETECTED: Python Beginner Fundamentals
First asked: 2025-02-21
Times returned: 15+
Last seen: 2025-04-26 ([[processed/GEMINI/2025-04-26_so_at_first_this_started_as_a_solana_price_tracking_project__32861723.md]])
What he keeps asking: What is a dictionary vs list vs tuple, why some functions end in `()`, how `csv` works, basic syntax questions that a single structured course would cover in Module 1.
What's likely missing: He's using LLMs as a replacement for foundational learning instead of a supplement. Ad-hoc Q&A creates Swiss Cheese knowledge — gaps he keeps falling through.
Suggested resolution path: Pick one Python course (free or paid), work through it sequentially for 30 days without asking LLMs to explain concepts the course already covers. Use LLMs for debugging, not curriculum.

### LOOP DETECTED: AI Coding Tool Selection (Cursor vs Windsurf vs Copilot vs Claude Code)
First asked: 2025-09-23
Times returned: 25+
Last seen: 2026-03-02
What he keeps asking: Which is cheapest, which has the best free tier, which is most intuitive, should he switch from one to another, how does Claude Code compare.
What's likely missing: Decision paralysis disguised as research. No tool comparison has resulted in a shipped project. The tool is not the blocker.
Suggested resolution path: Commit to one tool for 90 days. No exceptions. Set a calendar reminder. If a project isn't shipping, the IDE isn't the reason.

### LOOP DETECTED: LinkedIn Profile & Career Positioning
First asked: 2025-05-31
Times returned: 12+
Last seen: 2026-04-01 ([[processed/CLAUDE/2026-04-01_Writing_a_cover_letter_95600404.md]])
What he keeps asking: What job title to use beyond warehousing, how often to post AI solution content, how to optimize his profile for career transition, what tone to strike.
What's likely missing: He's optimizing presentation without building portfolio projects that justify the narrative. A LinkedIn title can't substitute for shipped work.
Suggested resolution path: Build and ship 2 public projects before touching LinkedIn again. The profile is downstream of the work.

---

## Pattern B — Stated vs. Actual

Comparing goals in [[goals-overall]] against actual conversation time allocation.

### STATED GOAL: Operation Immortal Agent — "The most serious thing I've built... it needs to keep moving"
ACTUAL TIME SPENT: ~25 conversations over 3 days (Feb 24-26, 2026), then 3-4 tangential mentions in March, then silence. The last explicit reference was March 24, where he stated "This isn't for my immortal agent project."
DELTA: Intense sprint followed by abandonment. The project lives in planning documents, not commits.
QUESTION TO CONSIDER: Is the $300 seed fund real, or is the planning itself the gratification?

### STATED GOAL: IT as a bridge — "Tiffin cert and job applications are real and practical"
ACTUAL TIME SPENT: 5-6 conversations about CompTIA A+ / Network+ in April-June 2025, then essentially dropped. One cover letter written in April 2026. Minimal evidence of consistent job application activity.
DELTA: Career energy shifted to LinkedIn branding, AI tool tinkering, and crypto trading questions — not cert completion or applications.
QUESTION TO CONSIDER: Is the IT bridge being built, or is "preparing to transition" more comfortable than actually transitioning?

### STATED GOAL: Privatized AI solutions — "Be the person who actually implements this stuff for them"
ACTUAL TIME SPENT: ~449 conversations reference local LLM / helpdesk AI / oobabooga setup (June-July 2025), but almost none about pricing, client acquisition, contracts, or actual business development. No customer conversations. No service packages defined.
DELTA: Building the lab, not the business. The homelab is the project, not the delivery mechanism.
QUESTION TO CONSIDER: Who is the first customer? If there isn't one, this is a hobby with business aesthetics.

### STATED GOAL: Content / streaming — "Document what I'm building, share what I'm learning"
ACTUAL TIME SPENT: Heavy time on OBS setup, multistreaming to Twitter/TikTok, audio routing, now-playing overlays (April 2026). No evidence of a consistent publishing schedule, streamed builds, or documented projects in the conversation archive.
DELTA: Infrastructure without output. The rig is optimized for a show that isn't happening.
QUESTION TO CONSIDER: Is setting up the equipment more fun than being visible?

---

## Pattern C — The Drop

Projects or ideas that showed up with energy, then disappeared.

### DROPPED THREAD: Helpdesk AI Assistant (Oobabooga + Local RAG)
Active period: 2025-06-23 to 2025-07-17
Last conversation: [[processed/GEMINI/2025-07-17_can_you_explain_that_in_prompt_format_so_i_can_feed_that_to__12332395.md]]
Energy level at drop: High (449 total files reference this project; daily build sessions across GEMINI and CLAUDE; model loading, character setup, RAG integration, WSL2 debugging)
Worth revisiting? Yes — this was the closest to a real product. The local RAG + helpdesk concept directly aligns with the stated goal of privatized AI solutions. It had scope, technical depth, and a clear use case. Dropping it was a mistake.

### DROPPED THREAD: Flappy Bird Dank Meme Game
Active period: 2025-11-30 to 2025-12-10
Last conversation: [[processed/GEMINI/2025-12-10_Created_Gemini_Canvas_titled_Windsurf_Can_I_Prompt_a_Flappy__60953700.md]]
Energy level at drop: High (detailed PRD written, character roster designed, shop economy mapped, Phaser 3 stack chosen, pixel art style defined)
Worth revisiting? No — this was a learning project that served its purpose. Consciously close it and archive the plan.md.

### DROPPED THREAD: Meme Generator
Active period: 2025-11-20 to 2025-11-23
Last conversation: [[processed/GPT/2025-11-23_Meme_generator_feedback_51212497.md]]
Energy level at drop: Medium (PRD created, feedback sought from GPT)
Worth revisiting? No — unclear value proposition and no unique angle. Close it.

### DROPPED THREAD: Operation Immortal Agent
Active period: 2026-02-24 to 2026-02-26
Last conversation: [[processed/GEMINI/2026-03-24_This_isnt_for_my_immortal_agent_project_this_is_just_simply__36567605.md]] — explicitly stated it's NOT for the project
Energy level at drop: High (20+ files in 3 days, plan.md updated to v2.2, Phantom MCP integration planned, Claude Code installed specifically for this, Kamino Multiply strategy defined, $300 seed fund allocated)
Worth revisiting? Yes — but only with conditions. Fund it with real money, commit to 30 consecutive days of work, and define a "quit" criteria upfront. Otherwise consciously abandon it and stop carrying the mental weight.

### DROPPED THREAD: PC Repair Business (PCHP Solutions / Uplink)
Active period: 2025-10-24 to 2025-11-14
Last conversation: [[processed/GEMINI/2025-11-14_Im_just_going_to_Im_just_going_to_explain_it_to_you_Basicall_84703043.md]]
Energy level at drop: Medium (business names brainstormed, logo designed in GEMINI, cousin consulted, 90-day agile plan created, productized services listed)
Worth revisiting? Maybe — but only if paired with actual service delivery (e.g., 3 free repairs for portfolio), not more planning. The planning phase exceeded the selling phase by a wide margin.

### DROPPED THREAD: Blender AI Agent Workflow
Active period: 2025-09-07 to 2025-09-11
Last conversation: removed (source file missing)
Energy level at drop: High (multiple files per day, director agent setup, model downloads, Hugging Face integration attempts, Python environment troubleshooting)
Worth revisiting? No — scope was too large for current skill level. Close it and revisit in 12 months if still relevant.

---

## Pattern D — Cross-LLM Distrust

Conversations where Bryan asked the same or similar questions to multiple LLMs within short windows.

### Cross-LLM Cluster: Cursor vs Windsurf vs Copilot (Nov 19-25, 2025)
- [[processed/GROK/2025-11-19_AI_Coding_Tools_Comparison_Copilot_Cursor_Windsurf_58535119.md]] (GROK)
- [[processed/GROK/2025-11-24_Windsurf_vs_Copilot_Beginner_Coding_Tools_70873840.md]] (GROK)
- [[processed/GROK/2025-11-25_GitHub_Copilot_vs_Cursor_Comparison_53104226.md]] (GROK)
- [[processed/GPT/2025-11-24_Cursor_vs_Windsurf_comparison_12727549.md]] (GPT)
- [[processed/GPT/2025-11-24_Brainstorming_IDE_pros_and_cons_69734837.md]] (GPT)
- [[processed/GPT/2025-11-24_Pricing_model_comparison_17613010.md]] (GPT)
- [[processed/CLAUDE/2025-11-24_Creating_a_project_plan_for_Windsurf_26344212.md]] (CLAUDE)
- [[processed/GEMINI/2025-09-23_are_there_any_other_free_alternatives_worth_looking_at_51970815.md]] (GEMINI)
What this signals: Decision paralysis. Asking every LLM hoping one will give permission to stop researching and start building. None of them did, because the question isn't answerable by an LLM.

### Cross-LLM Cluster: Local LLM / Ollama / RTX 3070 Setup (Nov 17-18, 2025)
- [[processed/CLAUDE/2025-11-17_Ollama_server_startup_and_configuration_21643883.md]] (CLAUDE)
- [[processed/CLAUDE/2025-11-17_Open_source_LLM_for_coding_with_RTX_3070_72758463.md]] (CLAUDE)
- [[processed/CLAUDE/2025-11-18_Ollama_CUDA_compatibility_for_RTX_3070_67526640.md]] (CLAUDE)
- [[processed/GROK/2025-11-17_Open_Source_Model_for_Coding_Similarity_79651103.md]] (GROK)
- [[processed/GROK/2025-11-18_Integrating_Open_Source_AI_Coding_Models_38442136.md]] (GROK)
What this signals: Hardware insecurity. He doesn't trust that his 3070 is "enough" and keeps seeking validation. Every LLM confirmed it works. He kept asking anyway.

### Cross-LLM Cluster: Operation Immortal Agent (Feb 24-26, 2026)
- [[processed/GEMINI/2026-02-24_So_with_this_in_mind_can_you_remind_me_what_it_is_that_Im_bu_32193364.md]] (GEMINI — planning)
- [[processed/GEMINI/2026-02-26_claude_version_2159_Claude_Code_vc_projectsimmortal_agent_31442959.md]] (GEMINI — setup)
- [[processed/CLAUDE/2026-02-23_Claude_Code_terminal_vs_Cursor_integration_77770457.md]] (CLAUDE — tooling)
What this signals: He used GEMINI for architectural planning and CLAUDE for execution setup, but the project still stalled. The distrust wasn't between LLMs — it was between planning and doing. More tools won't fix a motivation gap.

### Cross-LLM Cluster: Business Name Ideas (Oct-Nov 2025)
- [[processed/GPT/2025-10-24_Business_name_and_logo_25649981.md]] (GPT)
- [[processed/GPT/2025-10-25_Business_name_feedback_25659629.md]] (GPT)
- [[processed/GPT/2025-11-07_Business_name_ideas_40059898.md]] (GPT)
- [[processed/CLAUDE/2025-11-13_Business_name_for_PC_repair_and_custom_builds_shop_37877151.md]] (CLAUDE)
What this signals: Naming is a safe form of progress. No customer, no service, no risk — just branding. Cross-LLM naming sessions are a red flag for productive procrastination.

---

## Summary

Bryan's vault shows a clear pattern: high energy, deep planning, rapid abandonment. The loops aren't knowledge gaps — they're avoidance patterns dressed up as research. The cross-LLM clusters reveal a search for external permission that no LLM can grant. The drops aren't failures; they're unclosed loops consuming mental RAM.

The honest read: He's better at starting than finishing, better at tooling than shipping, and better at infrastructure than output. The goals in [[goals-overall]] are real, but the conversation archive shows they're being pursued sideways — through setup, comparison, and optimization — rather than directly through building and delivery.

The one project that should be revived: the Helpdesk AI Assistant. It had product-market fit with his own goals, real technical progress, and a clear use case. Everything else should either ship in 30 days or be consciously closed.


## Related
- [[insights/blind-spots/2026-04-blind-spots|Blind Spots Report]]
- [[insights/blind-spots/2026-04-blind-spots|Blind Spots Report]]
