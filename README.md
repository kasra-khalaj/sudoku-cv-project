# Intelligent Sudoku Detection & Solving System

Computer Vision project: detect a Sudoku grid from a photo, recognize its digits, solve the puzzle, and display the solution back on the original image.

## Team

| Member | Responsible for |
|---|---|
| Member 1 | Phase 1 (grid extraction), Phase 2 (digit recognition), Bonus #4 (overlay on original image) |
| Member 2 | Phase 3 (solver), Phase 5 (UI — Bonus #3) |
| Joint | Phase 4 wiring review, Phase 6 (integration, testing, docs, report) |

## Architecture

```
image_processing/   Phase 1 — grid detection, perspective transform, cell extraction
digit_recognition/  Phase 2 — CNN/MobileNet digit classifier (10 classes: 1-9 + empty)
solver/              Phase 3 — Backtracking Sudoku solver
pipeline/            Phase 4 — orchestrates the above + Bonus #4 overlay
ui/                  Phase 5 — Streamlit/Gradio/PyQt front-end (Bonus #3)
utils/               shared helpers
models/              trained model weights
datasets/            training/eval data (gitignored — see below)
tests/               unit tests per module
notebooks/           Colab development notebooks (dev record, not the deliverable)
checkpoints/         persisted intermediate artifacts (see Checkpoint Policy)
```

Each module exposes a minimal, documented input/output interface so the two of you can work independently — see each module's docstring once implemented.

## Setup

```bash
git clone <repo-url>
cd sudoku-cv-project
pip install -r requirements.txt
```

## Running the pipeline

*(added once Phase 4 is complete)*

## Checkpoint Policy

Every major phase persists its outputs (trained weights, processed datasets, evaluation results) to `checkpoints/` so development can resume after a Colab disconnect without rerunning from scratch. Each phase's notebook checks for an existing checkpoint before recomputing.

## Attribution

- Sudoku solver: educational/open-source backtracking implementations are permitted per the assignment spec. Any code adapted from external sources will be credited here with source, license justification, and description of modifications, once selected in Phase 3.

## Large files

Model weights and datasets are tracked via **Git LFS**. Run `git lfs install` once after cloning.
