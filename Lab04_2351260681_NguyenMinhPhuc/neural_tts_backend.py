"""Offline Piper VITS wrapper for the Vietnamese pretrained voice used in Lab 4."""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy import signal

PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = Path(os.environ.get(
    "PIPER_MODEL", PROJECT_ROOT / "models" / "vi_VN-vais1000-medium.onnx"
))


@lru_cache(maxsize=1)
def _load_voice(model_path: str):
    from piper import PiperVoice
    path = Path(model_path)
    if not path.exists():
        raise FileNotFoundError(
            f"Missing offline Piper voice at {path}. See models/README.md to download it."
        )
    return PiperVoice.load(str(path))


def synthesize(text: str):
    """Synthesize Vietnamese speech; returns float waveform, sample rate, extras."""
    voice = _load_voice(str(MODEL_PATH.resolve()))
    chunks = list(voice.synthesize(text))
    if not chunks:
        raise RuntimeError("Piper returned no audio chunks")
    waveform = np.concatenate([np.asarray(chunk.audio_float_array, dtype=np.float32) for chunk in chunks])
    sample_rate = int(chunks[0].sample_rate)
    frequencies, times, power = signal.spectrogram(
        waveform, fs=sample_rate, nperseg=512, noverlap=384, mode="psd"
    )
    mel = 10 * np.log10(np.maximum(power, 1e-12))
    return waveform, sample_rate, {"mel": mel, "mel_times": times, "mel_frequencies": frequencies}
