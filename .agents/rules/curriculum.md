# Curriculum Generation & Pedagogy Rules (`curriculum`)

Whenever working on curriculum materials, lecture scripts, or pre-reads in this repository, strictly enforce the following rules:

1. **Approach & Tone**:
   - Write as an approachable senior mentor. Grade 7 reading level.
   - **Zero Jargon**: Never use academic abstractions or buzzwords without intuition. Lead with concrete everyday analogies.
   - Banned words: `leverage`, `utilize`, `robust`, `seamlessly`, `empower`, `cutting-edge`, `dive into`, `delve`.

2. **Strict Curriculum Alignment**:
   - Cross-reference `curriculum/<batch_id>.csv`.
   - Never reference, assume, or use concepts, syntax, methods, or algorithms that haven't been taught in prior completed sessions.
   - Zero forward references: never preview upcoming modules or lectures.

3. **Template Conformity**:
   - `lecture-script.md` must strictly follow Format v2 in `templates/lecture-script-template.md` (Agenda 120 min, Scenario, Problem Statement, What We Will Use, How Mermaid flow, 4 Topics each with a Quiz, Closing with outcome & summary, Launch the Feedback Poll). Code <= 10 lines.
   - `pre-read.md` must follow `templates/pre-read-template.md` (Mental Map Mermaid flow, Bloom's verbs in outcomes, intuitive concept walkthroughs, 3 Think It Through questions with hints).

4. **Directory Structure**:
   - Maintain the strict hierarchy: `<batch-id>/module-NN-<topic>/lecture-NN-<topic>/`.
   - Only `pre-read.md` and `lecture-script.md` (plus optional `images/` and `data/` subfolders). No `.gitkeep` or stray scripts.
