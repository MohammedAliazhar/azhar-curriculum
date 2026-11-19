---
name: cc-preread
description: >
  Create a curiosity-first pre-read for a session in any batch.
  Triggered by /create-pre_read "BATCH-ID" "Module Name" "Session Name" "Topics" "Learning Objectives" "Yes|No" ["setup text"].
  Handles the full pipeline: creator agent writes the preread, reviewer agent
  verifies it, output saved to <batch>/<module>/<lecture>/pre-read.md (no PNG).
---

# Pre-Read Skill

## Preread Creation Pipeline

A pre-read makes a beginner curious about the session. It is not a lesson. It uses one everyday scenario, tells the
student what they will be able to do, and ends with a question that the session answers.

### Standards the creator and reviewer enforce

Full rules live in `preread/guidelines.md`. In short:

- **One everyday scenario per pre-read**: Easy to picture, relevant to the course, never reused from an earlier pre-read.
- **GUARDRAIL: No Jargon**: Keep language simple, intuitive, and friendly. Grade 7 reading level. No ungrounded academic buzzwords or complex abstractions. Define any core term once in plain English.
- **GUARDRAIL: Strict Curriculum Alignment**: Cross-reference the batch curriculum CSV. Only connect to topics already covered in prior sessions. **Do NOT mention or assume topics that haven't been taught yet.** Zero forward references.
- **What You'll Learn**: a "Have you ever wondered" hook, the lead-in "By the end of this session, you will be able to:", then 4 to 6 outcome bullets. Each bullet opens with one Bloom's verb from the bank, never repeated.
- **Sentences of 20 words or fewer**, grade 7 reading level, none of the banned vague words.
- **Any code preview** is run before it stays.
- **Technical names only** in the Topics callout and one core-term definition. Never print the Module Name.
- **Exactly 3 Think It Through questions** with hints and no answers.
- **The Set Up section** appears only when Setup is Yes, using the pasted text without inventing a link.

### Inputs

| Input | Required | Example |
|---|---|---|
| `batch_id` | Yes | `"IITP-AIML-TA-II-2607"` |
| `module_name` | Yes | `"Core Programming & Analytical Foundations"` (context only, never printed) |
| `session_name` | Yes | `"Probability Distributions"` |
| `topics` | Yes | `"Discrete vs continuous; Binomial; Normal and z-scale; Empirical rule"` |
| `learning_objectives` | Yes | `"Classify a random variable; Compute a binomial probability; ..."` |
| `setup` | Yes | `Yes` or `No` |
| `setup_text` | Only if setup is Yes | The setup text or documentation link to paste into the Set Up section |

### Pipeline Steps

1. Resolve the target lecture folder via `python3 tools/resolve_folder.py "<batch_id>" "<session_name>"`.
2. Cross-reference `curriculum/<batch_id>.csv` to ensure strict curriculum alignment (no future concepts).
3. `agent_preread_creator` writes `pre-read.md` into the resolved lecture folder.
4. `agent_preread_verifier` reviews against all rules (including No Jargon and Curriculum Alignment) and auto-fixes issues.
5. Report status, scenario, and output path.
