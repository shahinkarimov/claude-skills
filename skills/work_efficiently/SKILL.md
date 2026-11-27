---
name: work_efficiently
description: Mandatory core discipline for parallel tool execution, zero roundtrip latency, batch operations, and single-turn verification.
---

# Work Efficiently Core Discipline

Execute all independent search, read, edit, and verification operations in parallel within a single turn.

## Core Rules
1. **Parallel Execution**: Never issue one tool call per turn when multiple calls can be made at once.
2. **Comprehensive Reading**: Read all relevant files and ranges in the initial turn.
3. **Chained Verification**: Chain execution and status checks with shell operators (&&, ;) for instant validation.
4. **Zero Hallucination / Zero Repetition**: Never re-read unchanged content or re-run passing tests without new edits.
