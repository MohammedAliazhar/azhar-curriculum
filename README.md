# AIML & GenAI — pre-reads and lecture scripts

Published course content for IIT Patna and IIT Roorkee AIML & GenAI batches. Each batch is a top-level folder (batch ID from the INI sheet).

### Repository layout

```text
├── README.md
├── templates/
│   ├── pre-read-template.md
│   └── lecture-script-template.md
├── curriculum/
│   ├── IITP-AIML-TA-II-2607.csv
│   ├── IITR-AIML-TA-I-2606.csv
│   ├── IITP-GenAI-TA-I2606.csv
│   └── IITP-GenAI-TE-I-2608.csv
├── <batch-id>/
│   ├── module-03-<topic>/
│   │   ├── lecture-01-<topic>/
│   │   │   ├── pre-read.md
│   │   │   ├── lecture-script.md
│   │   │   ├── data/      # 100-150 row CSV dataset with realistic edge cases
│   │   │   └── images/    # 6 PNG charts/diagrams at width 900 in the script
│   │   └── ...
│   └── ...
```

### Batches in this repo

| Batch ID | Program | Primary Module |
|:---|:---|:---|
| **`IITP-AIML-TA-II-2607`** | IIT Patna AI & Machine Learning | `module-03-genai-and-agents` |
| **`IITR-AIML-TA-I-2606`** | IIT Roorkee AI & Machine Learning | `module-03-genai-and-agents` |
| **`IITP-GenAI-TA-I2606`** | IIT Patna Generative AI Batch I | `module-04-genai-analytics-workflows-python` |
| **`IITP-GenAI-TE-I-2608`** | IIT Patna GenAI for Tech Executives | `module-04-genai-analytics-workflows-python` |

Session folders are created when pre-reads and lecture scripts are added. Assets for a session (`images/` or `data/`) live inside that session's `lecture-XX-<topic>/` folder.

Templates under `templates/` are reference skeletons only. Session files in batch folders are the source of truth.

---

### Curriculum CSV Alignment

Authoring uses the curriculum CSVs in `curriculum/<batch-id>.csv`. Important columns:

| Column | Use in Content |
|:---|:---|
| **Session Title** | Folder name and verbatim lecture title |
| **Topics / Topics Covered** | Pre-read "Topics you will meet"; mapped to four lecture topics |
| **Learning Objectives / LO_Statement** | Verbatim LOs in lecture Agenda and Closing summary table |
| **Tools Used** | Runtime and platform — must match the script (see below) |

Resolve a session (paths, LOs, tools):
```bash
python3 tools/resolve_folder.py "<BATCH-ID>" "<Session Name>"
```

Context for bridges (completed sessions + tools_used on target):
```bash
python3 lecture/tools/curriculum_context.py "curriculum/<BATCH-ID>.csv" "<Session Name>"
```

---

### Tools Used -> how to write

Read the `Tools Used` cell for the session before drafting:

| Tools Used (CSV) | Pre-read | Lecture Script |
|:---|:---|:---|
| **Google Colab** | Mention notebook cells; file paths only as future filenames, not terminal commands | What We Will Use states Colab; upload `data/`; each block is a code cell; tracebacks use `File "<cell>"`; Instructor Note for Colab file upload |
| **ChatGPT / Claude / Gemini** | "AI tool" in outcomes if session teaches prompt + test fix | Topic that teaches debugging names the tools; paste prompt in prose; re-run the Colab cell before accepting |
| **SQL / MySQL** | No live SQL in pre-read unless taught | Per SQL playbook when CSV says so |

> **Rule**: Do not write a file-I/O session as local terminal Python (`<stdin>` tracebacks, `python script.py`) when Tools Used is Google Colab.

---

### Authoring Checklist (before push)

1. `python3 lecture/tools/check_script.py <lecture-script.md> --los "<LO1;LO2>" --announcements yes` (structure, LOs, minutes, quizzes, images).
2. Verification on the session (Output matches, images embedded, Tools Used aligned, Grade 7 plain language, zero jargon).
3. Regenerated PNG — use a new filename and update `img src` (GitHub caches identical paths).
4. Push only under `<batch-id>/` (keep tools, tests, and master templates clean).
