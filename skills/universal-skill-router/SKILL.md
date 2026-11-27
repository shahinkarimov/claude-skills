---
name: universal-skill-router
description: >-
  Master Router and Orchestrator for all 5,101+ local skills across Web, Mobile, AI Agents,
  Desktop Automation, DevOps, Security, UI/UX, Data Science, and GameDev. Automatically
  identifies, routes, and activates the exact specialized skill(s) for any user request
  from the Master Skill Catalog (skills_manifest.json). Use whenever beginning any coding,
  design, research, automation, or debugging task.
---

# Universal Skill Router & Orchestrator

This is the central routing engine for the **5,101 installed skills** located in your environment.

Because LLM context limits prevent loading all 5,100+ skills simultaneously into the system prompt, this router dynamically indexes, identifies, and activates the required skills **on-demand**.

---

## ⚡ Routing Workflow

Before starting work on any user request:

### Step 1: Detect & Query Matching Skills
Run the router query tool or check the manifest:
```bash
python skill_router.py "<task_keywords>"
```
Or read `skills_manifest.json`.

### Step 2: Read Chosen Skill(s)
Once the matching skill is identified (e.g., `frontend-dashboard-pro`, `playwright-e2e-automation`, `browser-use-open-source`, `microsoft-ufo`), use `read_file` on its `SKILL.md`:
```
read_file(Path: ".../skills/<skill-name>/SKILL.md")
```

### Step 3: Compose & Execute
- Adopt the persona, architectural rules, code standards, and verification steps prescribed in the skill.
- Combine multi-disciplinary skills when appropriate (e.g. `spec-driven-development` + `nextjs-react-performance` + `clean-code`).
- If subagents are involved, ensure the subagent's prompt instructs it to read the specific `SKILL.md`.

---

## 🛡️ Core 24 Mandatory Always-Active Skills (Enforced on Every Operation)

Regardless of the user prompt or domain, the following 24 foundational skills are **PERMANENTLY ACTIVE**:
1. `token-budget-advisor`: Real-time context budget calculation & prompt condensation.
2. `compact-conversation`: Intelligent compression of conversation history without losing critical decisions.
3. `ai-session-optimizer`: Minimizes turn roundtrips and optimizes latency.
4. `prompt-caching-strategy`: Exploits prompt prefix caching for dramatic token reduction.
5. `clean-code`: Direct, pragmatic implementation without over-engineering or AI comments.
6. `anti-slop-ui`: Enforces high-craft aesthetic standards and blocks generic AI styles.
7. `memory-safety-patterns`: Stack vs heap discipline, memory leak avoidance, safe resource release.
8. `file-system-memory`: Long-term state and memory persistence using local files rather than chat history.
9. `error-handling-patterns`: Resilient exception handling and graceful recovery protocols.
10. `verification-loop`: Mandatory compile/run/test validation before completing tasks.
11. `gateguard`: Fact-forcing gate requiring proof of interfaces before modification.
12. `zero-hallucination-coder`: Strict rule against guessing commands, imports, or file locations.
13. `code-simplification`: Complexity reduction and entropy minimization.
14. `security-best-practices`: Secret protection, credential isolation, and secure shell escaping.
15. `universal-skill-router`: Dynamic automatic dispatch to relevant domain expert skills.
16. `session-guard`: State consistency across interruptions, reboots, and agent handoffs.
17. `work_efficiently`: Parallel execution of independent tool calls in a single turn.
18. `git-safety-net`: Atomic, cleanly structured commits for easy rollback.
19. `locked-references`: Protection of user requirements, constants, and business constraints.
20. `written-gates-generation`: Clear milestones and measurable acceptance criteria.
21. `inferssd`: Memory-mapped offloading for heavy local AI and data tasks.
22. `typegpu`: Type-safe hardware execution standards.
23. `continuous-learning`: Instinct memory from user feedback & error corrections so the agent never repeats mistakes.
24. `planning-with-files`: Crash-proof persistent file-based planning and state checkpoints (TASK.md/plan.md).


