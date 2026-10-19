# Lab 3 – Vietnamese isolated-command dataset (synthetic starter set)

## Contents
- `train/`: 30 WAV files (6 utterances per class × 5 classes)
- `test/`: 10 WAV files (2 utterances per class × 5 classes)
- `metadata.csv`: labels and audio-format metadata

Classes:
- `mo` = mở
- `dong` = đóng
- `len` = lên
- `xuong` = xuống
- `dung` = dừng

## Audio format
- WAV, mono, 16 kHz, 16-bit PCM
- Approximately 0.30 s of silence before and after the spoken command
- One command per file

## Important limitation
These files were generated with the local eSpeak Vietnamese text-to-speech voices (`vi`, `vi-hue`, `vi-sgn`). They are suitable for testing the Lab 3 code pipeline, file loading, MFCC extraction, HMM training/scoring, plotting, and train/test handling. They are **not genuine human recordings**, and the test set is not an independent real-world speech evaluation. For the final lab report, replace or supplement them with your own recordings (or recordings from real speakers) if your instructor expects real speech data. Do not describe these as human-recorded data.

## Suggested recording protocol for a real dataset
Record each command 8 times per class, with one command per WAV file, mono 16 kHz 16-bit PCM, and 0.2–0.5 s silence at the beginning and end. Keep the 6 training and 2 test recordings separate. For speaker-independent evaluation, use different speakers for train and test.
