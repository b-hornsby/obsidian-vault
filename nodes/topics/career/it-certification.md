---
type: topic
status: reference
priority: P3
tags: [topic, career, certification, archived]
aliases: [IT Certification, CompTIA, Certs]
---

# IT Certification

*Decision record and knowledge baseline. Certifications paused while real IT experience is built on the job.*

My certification journey is a story of strategic pivots and honest self-assessment. I went from building an entry-level help desk resume, through intensive CompTIA A+ and Network+ study, to a pivotal moment where I questioned whether the certs were even worth pursuing — and ultimately shifted focus to a project-based strategy for breaking into tech.

---

## The arc

My formal IT training started with Tiffin University's IT Helpdesk Administrator program, which I completed in May 2025. It covered hardware troubleshooting, networking fundamentals, OS support, ticketing systems, and security — all aligned with CompTIA A+ and Network+ objectives. I earned the certificate. It was a genuine milestone: structured, university-level IT training pursued while working full-time in a warehouse.

But the certification exams were a different story. My practice test scores hovered around 52-60%, well below the 80% passing threshold. The exams tested rote knowledge of ports, protocols, and vendor-specific details that felt disconnected from the hands-on skills I was actually developing in my homelab.

---

## The pivot

In May 2025, I had a breakthrough conversation with GPT that changed my trajectory. I asked directly: "Should I stop chasing CompTIA certs and instead leverage my completed program plus build practical projects to break into tech?"

The advice was blunt and practical — pivot now. Stop burning time on exams where you're scoring 55%. Instead, build 2-3 real IT projects (home labs, ticketing systems, network diagnostics), document them publicly on LinkedIn and GitHub, and apply strategically.

I didn't quit the certs out of laziness. I made a calculated decision that execution mattered more than credentials in 2025's market, where AI and automation were rapidly changing what employers valued. The certs can always come later as a resume boost, not a blocker.

---

## What I actually know

Despite the exam struggles, the certification conversations reveal genuine knowledge:

- **Networking fundamentals:** I understand TCP/IP, subnetting, DNS, DHCP, and the OSI model well enough to troubleshoot real problems in my homelab.
- **Hardware:** I've built and maintained my own PC and understand component compatibility, thermal management, and power requirements.
- **Operating systems:** Proficient with Windows, Linux (CachyOS/Arch), dual-boot configuration, bootloaders, and secure boot.
- **Troubleshooting methodology:** I approach problems methodically — isolate variables, test hypotheses, document findings.

---

## The gaps

- **No certifications completed.** Despite Tiffin University training, no CompTIA certs awarded as of early 2026.
- **Exam-specific knowledge gaps remain** in rote memorization details.
- **Professional experience now on the job.** Endpoint provisioning, Entra ID, Freshservice, IT Glue, NinjaOne — these are now daily practice, not gaps.

---

## What I need to do

1. **Pause formal exam commitment** until a target path is specific.
2. **Convert study time into daily IT task notes** — provisioning, user management, ticketing, monitoring.
3. **Keep homelab practice targeted to job domains** — deployment, scripting, documentation.

---

## Key Conversations

- [[processed/GPT/2025-04-29_Brutal_Truth_for_Growth_10343908.md|Brutal truth for growth]] — "I don't want comfort. I don't want sugarcoating"
- [[processed/GEMINI/2025-04-07_For_me_theres_just_a_lot_of_acronyms_and_way_too_many_number_33195580.md|Network+ study]] — "for me there's just a lot of acronyms and way too many numbers to remember"
- [[processed/GEMINI/2025-10-26_lets_work_through_this_quick_fix_solutions_name_idea_for_my__72290278.md|Business name brainstorm]] — "i think i'm cooking up something"

---

## Related

- [[nodes/people/bryan.md|Bryan]] — the person using this as decision record
- [[nodes/topics/career.md|Career]] — current IT role and forward growth paths
- [[nodes/projects/job-search.md|Job Search]] — archived transition record
- [[nodes/projects/resume.md|Resume]] — pre-employment iteration history
- [[nodes/projects/homelab-stack.md|Homelab]] — job-relevant infrastructure practice
- [[nodes/topics/thinking-patterns.md|Thinking Patterns]] — the planning-vs-shipping tension
- [[nodes/topics/tech/it-tooling.md|IT Tooling]] — daily Freshservice / Entra / IT Glue / NinjaOne notes

---

## All Conversations

```dataview
TABLE title AS "Title", date AS "Date", source AS "Source"
FROM "processed"
WHERE contains(tags, "it-certification")
SORT date DESC
LIMIT 50
```
