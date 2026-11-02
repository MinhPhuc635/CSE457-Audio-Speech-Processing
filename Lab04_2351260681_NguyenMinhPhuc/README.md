# Lab 4 - Speech synthesis

Deliverables for CSE457 Lab 4.

- `Lab04.ipynb`: runnable notebook, with its plots and result tables saved.
- `Bao_cao_Lab04.pdf` and `.docx`: 8-page report; personal identifying details removed.
- `lab4_data/`: relative-path starter inventory used by the notebook.
- `audio_output/`: synthesized WAV files, plots, comparison tables, and the anonymous listening set.
- `hmm_tts_backend.py`: educational source-filter parameter-generation demo.
- `neural_tts_backend.py`: offline Piper VITS wrapper.

## Setup

From this directory, install `requirements.txt` and open `Lab04.ipynb`. The notebook finds `lab4_data/` relative to the project, including when the Jupyter server is started at the repository root.

The 63 MB pretrained voice is intentionally excluded from Git. Follow `models/README.md` to download it locally before running the neural TTS cells.

`audio_output/ratings.csv` is a blank score sheet for the listening study; no subjective MOS or intelligibility scores are fabricated.
