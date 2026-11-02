# Lab 4 - Vietnamese queue-announcement word-unit dataset

## Contents
- `units/<unit_id>/<unit_id>_01.wav` and `_02.wav`: 16 word units x 2 candidates = 32 WAV files.
- `metadata.csv`: label, speaker, duration, RMS, relative path and recording/synthesis settings.
- `text_normalization_examples.csv`: three queue-announcement examples and expected tokens.

## Vocabulary (16 units)
`mời, khách, hàng, số, không, một, hai, ba, bốn, năm, sáu, bảy, tám, chín, đến, quầy`.

## Audio format
- WAV, PCM signed 16-bit, mono, 16,000 Hz.
- 80 ms leading/trailing silence is retained as context.
- Audio is gently RMS-matched with peak protection; RMS in metadata is measured after this step.

## Important limitation
This is a **synthetic starter dataset**, generated locally with eSpeak Vietnamese voice `vi`, not human microphone recordings. Candidate 01 and 02 use the same synthetic voice with slightly different speaking rate and pitch settings. This makes it reproducible for implementing normalization, inventory metadata/statistics, concatenation, join-cost, cross-fade and duration/pitch experiments. It does **not** represent real-speaker diversity or natural human coarticulation. For a final naturalness/listening evaluation, replace or supplement these WAVs with at least two human recordings per unit, recorded using the same microphone, distance and environment.

## Suggested first sentence
`Mời khách hàng số 23 đến quầy 5.` -> `mời khách hàng số hai ba đến quầy năm`.

## Lab alignment
Meets the inventory size (>=15 units), two candidates per unit, 16 kHz mono WAV format, and required metadata fields. The Lab's HMM-based and neural pretrained TTS backends are separate components; this inventory alone does not constitute those backends.
