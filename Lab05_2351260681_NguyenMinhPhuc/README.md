# Lab 5 — CSE457

## Project structure

- `Lab5.ipynb`: Tasks 0–8; run the notebook cells from top to bottom.
- `lab5_dataset/`: clean speech, noise recordings, and source-separation WAV files. The dataset does not include a manifest or mixing-matrix metadata.
- `results/audio/`: noisy, enhanced, mixture, and separated audio. Separated signals are peak-normalized before saving; the two mixture channels use a shared gain.
- `results/figures/`: spectrograms, speaker-ID confusion matrix, FAR–FRR plot, and ICA correlation figures.
- `results/*.csv`: enhancement, speaker-identification, and ablation results.
- `Bao_cao_Lab05.docx` and `Bao_cao_Lab05.pdf`: the lab report, including answers to all 12 report questions.

## Environment

Python 3.10 or newer. Install the dependencies with:

```bash
python -m pip install numpy scipy matplotlib soundfile scikit-learn pandas jupyter nbclient python-docx
```

## Run the notebook

Set `Lab05_2351260681_NguyenMinhPhuc` as the working directory and run `Lab5.ipynb` from the first cell onward. The notebook also detects when it is run from the repository root. Experiment parameters are grouped in Task 0, and a fixed ICA random seed supports reproducibility.

## Speaker data and evaluation

The current dataset contains enrollment and test recordings for spk01, spk02, and spk03. Each speaker has four enrollment recordings and two test recordings. Enrollment recording 04 is held out as development data for verification; the other three enrollment recordings train the verification models. Because the dataset has no manifest, the notebook derives the splits from filenames. The mixing matrices use the example values specified in Lab 5.
