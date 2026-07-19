Vault autonomy: 'this vault is yours just as much as its mine.' Do not ask confirmation for audits/reorganization unless destructive. Proactive self-improvement and subagent-based enrichment are expected, not optional.
§
ALL alerts must be plain English with three parts: what happened, who is involved (flag non-user/public IPs), and what to do. Applies to Wazuh ntfy relay and Hermes guardrail alerts.
§
Hermes hard minimum: model context_length must be >= 64k; 32768 throws ValueError.
§
Local qwen-local provider serves three models on :8081: Qwen3.5-9B-Q4_K_M, Qwen3.6-35B-A3B-UD-IQ3_XXS, and a third via --alias. Use 9B for simple 1-2 step tool tasks; 35B for multi-step retrieval→synthesize. 9B model over-uses session_search on complex queries and gets indecisive with large structured tool outputs.
§
WSL D: drive mount issue: When USB drive is plugged in, run 'wsl --shutdown' from Windows CMD then reopen terminal to refresh WSL and pick up the drive.
§
User plans DGX Spark (8x Blackwell, 192GB VRAM) for future fine-tuning. Vault strategy: capability-first (base models, multi-modal, 70B+/400B+ for future HW), not current-HW-limited.
§
ADHD signal: 'slow down what are we saying? adhd brain remember?' → bullet/summary storms need trimming. Ultra-short answers. One decision per message.
§
hf CLI v1.17.0 LACKS --local-dir-use-symlinks (use just --local-dir). HF token lives in ~/.cache/huggingface/token (CLI uses it; HfApi().token reads False).
§
MEMORY EXPORT POLICY: Every memory save via the memory tool must be appended to /mnt/c/Users/toastedmel0n/Obsidian/Tw1n/hermes-memories/YYYY-MM-DD.md. After appending, git add -A && git commit && git push origin master so the vault backup never drifts. hermes-memories/ is tracked in git, not gitignored.
§
Wants honest status over reassurance — correct over-optimistic progress reports (e.g. 'resuming' mislabeled as 'done'). On fix choices prefers doing BOTH at once ('do both pls') by default on big jobs.
§
Ecto pet scale set to 0.7. `hermes pets scale` is global usage, not per-slug.
§
User asked "you dig the ecto pet we made?" — I had no session context for this yet; need to search.