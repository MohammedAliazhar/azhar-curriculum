---
name: curriculum
description: >-
  Master curriculum generation skill for SME / Curriculum Creator Azhar.
  Activates the complete curriculum pipeline memory, frozen v2 templates,
  zero-jargon guardrails, realistic dataset generation, publication-grade visuals,
  and strict curriculum CSV alignment to generate, update, or verify 120-minute
  lecture scripts (lecture-script.md) and learner pre-reads (pre-read.md) across
  all IITP and IITR batches.
---

# Master Curriculum Generation Pipeline (`curriculum`)

Whenever the user invokes the `/curriculum` command or requests lecture scripts and pre-reads, execute the **exact 6-step curriculum generation pipeline** detailed below. Every step is mandatory and non-negotiable.

---

## 1. Active Batches & Sources of Truth

Always cross-reference the batch's curriculum CSV in `curriculum/` before drafting any content:

| Batch ID | Program | Curriculum CSV | Primary Module |
|:---|:---|:---|:---|
| **`IITP-AIML-TA-II-2607`** | IIT Patna AI & Machine Learning | `curriculum/IITP-AIML-TA-II-2607.csv` | `module-03-genai-and-agents` |
| **`IITR-AIML-TA-I-2606`** | IIT Roorkee AI & Machine Learning | `curriculum/IITR-AIML-TA-I-2606.csv` | `module-03-genai-and-agents` |
| **`IITP-GenAI-TA-I2606`** | IIT Patna Generative AI Batch I | `curriculum/IITP-GenAI-TA-I2606.csv` | `module-04-genai-analytics-workflows-python` |
| **`IITP-GenAI-TE-I-2608`** | IIT Patna GenAI for Tech Executives | `curriculum/IITP-GenAI-TE-I-2608.csv` | `module-04-genai-analytics-workflows-python` |

### Column Mapping:
- **`Session Title`**: Folder name slug and verbatim lecture title.
- **`Topics / Topics Covered`**: Pre-read *"Topics you will meet"*; mapped to four lecture topics.
- **`Learning Objectives / LO_Statement`**: Verbatim LOs in the lecture Agenda and Closing summary table.
- **`Tools Used`**: Runtime environment and platform rules (see Step 3 below).

---

## 2. Mandatory Guardrails

1. **Zero Jargon (Grade 7 Reading Level)**:
   - Approachable, empathetic senior mentor talking to a colleague.
   - **Intuition first**: Explain *why* a concept exists using concrete everyday analogies before code or syntax.
   - Never use ungrounded academic abstractions. Define any essential technical term once immediately upon introduction.
   - **Banned Buzzwords**: `leverage`, `utilize`, `robust`, `seamlessly`, `empower`, `cutting-edge`, `dive into`, `delve`.
2. **Strict Curriculum Alignment (Prerequisite Hard-Boundary)**:
   - Content, examples, code, and quiz questions must be generated **strictly based on the sessions already completed**.
   - Check libraries, functions, and SQL syntax: if not taught previously or in today's LOs, it is strictly banned.
   - **Zero forward references**: Never write "more on this later", "we will cover this next week", or preview upcoming topics.
3. **Emoji Restriction**:
   - Only the **🎯** emoji is permitted in instructor notes and section headers. All other emojis are strictly banned.
4. **Code Block Cap**:
   - Every code block must strictly be $\le 10$ lines (excluding fences), followed immediately by its real, exact execution output.
   - Code blocks never use placeholder comments (`# add code here`).

---

## 3. Platform & Runtime Rules (`Tools Used`)

* **Google Colab Sessions**:
  * *Pre-read*: Mention notebook cells; file paths only as future filenames (no terminal commands).
  * *Lecture script*:
    - *"What We Will Use"* explicitly states Google Colab.
    - Include a **🎯 Instructor Note** instructing learners to upload the `data/` CSV to Colab.
    - Treat each code block as an independent notebook cell.
    - Tracebacks must use `File "<cell>"` (never `<stdin>` or `script.py`).
  * **Strict Ban**: Never write a file session as local terminal Python (`python script.py` or `<stdin>` tracebacks) when `Tools Used` is Google Colab.
* **ChatGPT / Claude / Gemini Sessions**:
  * *Pre-read*: Mention "AI tool" in outcomes if the session teaches prompt + test fix.
  * *Lecture script*: Topic teaching debugging explicitly names the tools; paste prompt in prose; re-run the Colab cell before accepting.
* **SQL / MySQL Sessions**:
  * Follow SQL playbook rules; no live SQL in pre-read unless taught.

---

## 4. End-to-End Generation Workflow (Step-by-Step)

Whenever generating or refining a lecture, execute these 6 steps in sequence:

### Step 1: Resolve Directory & Read Curriculum Context
```bash
python3 tools/resolve_folder.py "<BATCH-ID>" "<Session Title>"
python3 lecture/tools/curriculum_context.py "curriculum/<BATCH-ID>.csv" "<Session Title>"
```
Create the subdirectories if they do not exist:
```text
<batch-id>/<module-folder>/<lecture-folder>/
├── data/
└── images/
```

### Step 2: Generate Realistic CSV Dataset (`data/<name>.csv`)
- Create a 100–150 row CSV dataset reflecting a realistic Indian business operation (e.g., Swiggy, Zomato, Flipkart, Blinkit, Tata CLiQ, Meesho).
- Column headers: lowercase with underscores (`order_id`, `customer_text`, `status`, etc.).
- Deliberately include planned edge cases: duplicate rows, nulls/NaNs, inconsistent casing, leading/trailing spaces, and tied values.
- Code blocks in the script start by inspecting rows 1–10 and scale to all 120+ rows in Topic 4 and Closing.

### Step 3: Generate 5–6 High-Resolution PNG Visuals (`images/`)
- Write a Python script using `matplotlib` and `PIL` to generate 5 to 6 crisp diagrams/charts.
- Resolution specs: **900px wide**, **200 DPI**, clear legible typography.
- Standard diagram types:
  1. Concept / Workflow flow (e.g. tokenization, API lifecycle, multi-tool architecture).
  2. Data / Parameter distributions (e.g. temperature curves, latency vs cost, darkstore metrics).
  3. Side-by-side architecture comparisons (e.g. Monolithic vs Modular, Classical ML vs LLM).
  4. Inspection and error profiles across the 120-row dataset.
  5. Decision matrices and trade-off trees.
  6. End-to-end Before vs After outcome visual.
- Embed in markdown using:
  ```html
  <p align="center"><img src="images/01_visual_name.png" alt="Descriptive visual title" width="900"></p>
  ```
- **Cache-Busting Rule**: When regenerating an existing image, always assign a new filename to bypass GitHub image caching.

### Step 4: Author the Learner Pre-Read (`pre-read.md`)
Follow `templates/pre-read-template.md`:
1. **Mental Map**: Mermaid flowchart (`flowchart TB`) linking Session Topic, The Big Question, Course Use Case, and Real-World Example.
2. **What You'll Learn**: Hook question followed by 4 Bloom's action verbs (`Recall`, `Explain`, `Analyze`, `Compare`).
3. **Why You Are Learning This Topic**: 4–6 sentences framing the business risk and intuition.
4. **Core Concepts Walkthrough**: Everyday physical analogy first, followed by clear definition.
5. **Scenario Puzzle**: Small markdown table of messy data, 3 numbered goals, and reflection prompts.
6. **Think It Through**: Exactly 3 guided questions with one-line hints (no answers given).
7. **One Question to Carry**: Thought-provoking question for the live session.

### Step 5: Author the Mentor Lecture Script (`lecture-script.md`)
Follow `templates/lecture-script-template.md` (Frozen Format v2):
1. **Title**: `# <font color='#1d4ed8'>Lecture Script: [Verbatim Session Title]</font>`
2. **Agenda**: Exactly 4 topics + Closing row with `—` marker (`| — | Closing: Outcome & Summary | | MIN |`) with minutes summing to **`**120**`**. LO column contains verbatim LO strings from CSV.
3. **Pacing Note**: `> <font color="red">**🎯 Instructor Note**</font>`
4. **Scenario**: Real Indian business setting (Swiggy, Flipkart, etc.).
5. **Problem Statement**: Story of an operational mistake + purple question + opening poll question with 30s timer.
6. **What We Will Use**: Runtime and tools table (explicitly states Google Colab when applicable, with file upload note).
7. **How**: Mermaid flowchart (`flowchart LR`) tracing Topics 1–4 to Closing.
8. **Topics 1 to 4**:
   - Purple bridge question: `> <font color='purple'>**Question?**</font>`
   - `### <font color='green'>Example: [Action]</font>`
   - Predict prompt + Instructor note.
   - Python code block ($\le 10$ lines) + Output block.
   - `#### <font color='#c2410c'>Code Explanation</font>` (line-by-line breakdown).
   - `> <font color='green'>**Result**</font>`
   - `### <font color='green'>Extending it: [Variation]</font>` (common mistake, edge case, or exception).
   - `### <font color='green'>Quiz [N]</font>`: 4 options, each with a one-line explanation below.
9. **Closing: Outcome & Summary**:
   - Outcome table (Before vs After across the entire 120-row dataset).
   - `Therefore,` deduction paragraph.
   - Reveal answer to opening poll note.
   - Verbatim LO summary table with a `**Practical value**` row.
10. **Announcements**: If required, formatted with reminder note.
11. **Feedback Poll**: `# <font color='red'>Launch the Feedback Poll</font>` with reminder note.

### Step 6: Deterministic Verification & Validation
Run `check_script.py` with exact CSV LOs:
```bash
python3 lecture/tools/check_script.py <path/to/lecture-script.md> --los "<Verbatim LOs from CSV>" --announcements yes
```
Iterate until the script produces:
```text
PASS: 0 fail, 0 warn
```

---

## 5. Pre-Push Verification Checklist

Before pushing any lecture to git:
- [ ] `check_script.py` returns `PASS: 0 fail, 0 warn`.
- [ ] Dataset in `data/` has 100–150 rows with planned edge cases.
- [ ] Exactly 5–6 PNG diagrams exist in `images/` at 900px wide, and all are referenced.
- [ ] 0 banned words (`leverage`, `utilize`, `robust`, `seamlessly`, `empower`, `cutting-edge`, `dive into`, `delve`).
- [ ] Only 🎯 emoji is used.
- [ ] Code blocks are $\le 10$ lines with exact matching outputs.
- [ ] Tracebacks use `File "<cell>"` for Colab sessions.
- [ ] Only files under `<batch-id>/` are committed.
