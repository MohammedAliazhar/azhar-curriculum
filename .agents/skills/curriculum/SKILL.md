---
name: curriculum
description: >-
  Master curriculum generation skill for SME / Curriculum Creator Azhar.
  Activates the complete curriculum pipeline memory, frozen v2 templates,
  zero-jargon guardrails, and strict curriculum CSV alignment to generate,
  update, or verify 120-minute lecture scripts (lecture-script.md) and
  learner pre-reads (pre-read.md) across all IITP and IITR batches.
---

# Curriculum Generation & Pipeline Skill

This skill activates the complete curriculum development environment, memory, templates, and strict pedagogical guardrails for Azhar.

---

## 1. Active Batches & Sources of Truth

Always cross-reference the batch's curriculum CSV before writing any content:

| Batch ID | Program | Curriculum CSV |
|:---|:---|:---|
| **`IITP-AIML-TA-II-2607`** | IIT Patna AI & Machine Learning | `curriculum/IITP-AIML-TA-II-2607.csv` |
| **`IITR-AIML-TA-I-2606`** | IIT Roorkee AI & Machine Learning | `curriculum/IITR-AIML-TA-I-2606.csv` |
| **`IITP-GenAI-TA-I2606`** | IIT Patna Generative AI Batch I | `curriculum/IITP-GenAI-TA-I2606.csv` |
| **`IITP-GenAI-TE-I-2608`** | IIT Patna GenAI for Tech Executives | `curriculum/IITP-GenAI-TE-I-2608.csv` |

---

## 2. Mandatory Guardrails (Non-Negotiable)

### Guardrail 1: Zero Jargon (High Accessibility)
- **Mentor voice**: Approachable, clear, conversational tone of a patient senior engineer.
- **Intuition first**: Explain *why* a concept exists in the physical world using an everyday analogy before presenting code, math, or syntax.
- **Banned jargon**: Never use ungrounded academic abstractions or buzzwords (`leverage`, `utilize`, `robust`, `seamlessly`, `empower`, `cutting-edge`, `dive into`, `delve`).
- **Define once**: If a technical term is essential, define it once in plain English immediately upon introduction.

### Guardrail 2: Strict Curriculum Alignment (Prerequisite Hard-Boundary)
- **Zero forward references**: Never write "we will cover this next week", "more on this later", or preview upcoming topics.
- **Prerequisite check**: Every tool, library, SQL keyword, or algorithm used must be either:
  1. Part of today's learning objectives, OR
  2. Already taught in a prior session listed in `curriculum/<BATCH_ID>.csv`.
- If an algorithm or library belongs to a future session, **it is strictly banned**. Solve the problem using only the tools learners already possess.

### Guardrail 3: Mandatory Real Data and Publication-Grade Visuals
- **Dataset (`data/`)**: Every lecture using data must have a 100-150 row realistic dataset in `data/<name>.csv` (with planned edge cases: duplicates, missing values, messy text casing/spaces). Never use synthetic toy dictionaries alone.
- **Visuals (`images/`)**: Every lecture must generate 5-6 real PNG charts/diagrams saved in `images/` (900px wide, 200 dpi), embedded with `<p align="center"><img src="images/XX_name.png" alt="..." width="900"></p>`.
- **Closing & Outcome**: Every lecture must include an Outcome comparison table (Before vs After across the full dataset), `Therefore,` conclusion, Poll reveal note, Summary table with a `**Practical value**` row, and `# <font color='red'>Launch the Feedback Poll</font>` with reminder note.

---

## 3. Standard File & Folder Layout

Every lecture lives in its own sequentially numbered directory with exactly two primary files:
```text
<batch-id>/
└── module-<NN>-<topic-slug>/
    └── lecture-<NN>-<topic-slug>/
        ├── pre-read.md        # Student self-study guide
        ├── lecture-script.md  # 120-minute mentor teaching script
        ├── images/            # Only when the script creates charts (PNG 900px width, 200 dpi)
        └── data/              # Only when the script uses datasets (100-150 rows with edge cases)
```

---

## 4. Workflows

### A. Generating a Lecture Script (`lecture-script.md`)
1. **Resolve Folder**:
   ```bash
   python3 tools/resolve_folder.py "<BATCH_ID>" "<Session Name>"
   ```
2. **Inspect Completed Context**:
   ```bash
   python3 lecture/tools/curriculum_context.py "curriculum/<BATCH_ID>.csv" "<Session Name>"
   ```
3. **Fill the Frozen v2 Template** ([`templates/lecture-script-template.md`](templates/lecture-script-template.md)):
   - **Agenda**: 4 topics with verbatim LOs, minutes summing to exactly 120.
   - **Scenario**: One famous Indian company framing (e.g. Swiggy, Flipkart, Ola).
   - **Problem Statement**: Story of a mistake + purple question + poll note.
   - **What We Will Use**: Short toolkit table.
   - **How**: Mermaid flow of Topics 1 to 4 and Closing.
   - **Topics 1 to 4**: Purple bridge question -> Worked Example -> Extending it (variations) -> Quiz (4 options with 1-line explanations). Code blocks <= 10 lines.
   - **Closing**: Outcome table ("Therefore,"), poll reveal, Summary table.
   - **Feedback Poll**: Final H1 header.
4. **Validate Deterministically**:
   ```bash
   python3 lecture/tools/check_script.py <path/to/lecture-script.md> --los "<LO1;LO2>" --announcements no
   ```

### B. Generating a Pre-Read (`pre-read.md`)
1. **Resolve Folder** using `tools/resolve_folder.py`.
2. **Fill the Pre-Read Template** ([`templates/pre-read-template.md`](templates/pre-read-template.md)):
   - **Mental Map**: Mermaid flowchart (`flowchart TB`) connecting Current Session, The Big Question, Course use case, and Real-world example.
   - **What You'll Learn**: Hook question followed by 4 Bloom's action verb bullets (plain English, no jargon, no buzzwords).
   - **Why You Are Learning This Topic**: 4-6 sentences introducing the Indian company scenario and defining the core term once upon introduction.
   - **Scenario Puzzle**: Small markdown table of messy data, 3 bulleted goals, and "Wonder about this" reflection questions.
   - **Think It Through**: Exactly 3 guided questions with one-line hints (no answers given).
   - **One Question to Carry Into the Session**: Thought-provoking open-ended question.
   - **Setup**: Included only if new software installation is required (omitted by default).

---

## 5. Automated Pipeline Commands

You can also run the full automated Claude Code creator and verifier pipeline:
```bash
/create-lecture-script "<BATCH_ID>" "<Module Name>" "<Session Name>" "<Topics>" "<LOs>" "No"
/create-pre_read "<BATCH_ID>" "<Module Name>" "<Session Name>" "<Topics>" "<LOs>" "No"
```
