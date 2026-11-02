"""Educational, offline HMM-parameter TTS demo for Lab 4.

This is a small source-filter resynthesis demo, not a production Vietnamese TTS.
It creates a deterministic three-state-per-word sequence and exposes the
generated parameter tracks for inspection in the lab notebook.
"""
from __future__ import annotations

import re
import numpy as np
from scipy import signal

SAMPLE_RATE = 16_000
FRAME_SECONDS = 0.01
DIGITS = {"0":"không", "1":"một", "2":"hai", "3":"ba", "4":"bốn", "5":"năm", "6":"sáu", "7":"bảy", "8":"tám", "9":"chín"}
VOWEL_FORMANTS = {
    "mời": (460, 1500), "khách": (700, 1450), "hàng": (650, 1350), "số": (480, 950),
    "không": (500, 1000), "một": (600, 1250), "hai": (650, 1450), "ba": (750, 1300),
    "bốn": (500, 1050), "năm": (650, 1250), "sáu": (480, 1750), "bảy": (600, 1650),
    "tám": (620, 1500), "chín": (500, 1850), "đến": (500, 1450), "quầy": (600, 1550),
}


def _tokens(text: str) -> list[str]:
    cleaned = re.sub(r"[^\w\sÀ-ỹĐđ]", " ", str(text).lower(), flags=re.UNICODE)
    output = []
    for token in cleaned.split():
        if token.isdigit():
            output.extend(DIGITS[d] for d in token)
        else:
            output.append(token)
    return output


def synthesize_hmm(text: str):
    """Return a simple source-filter waveform and HMM-like state trajectories."""
    tokens = _tokens(text)
    if not tokens:
        raise ValueError("Input text contains no pronounceable tokens")

    rng = np.random.default_rng(457)
    frame_n = int(SAMPLE_RATE * FRAME_SECONDS)
    audio_frames, f0_track, f1_track, energy_track, states, word_track = [], [], [], [], [], []
    phase = 0.0

    for word_index, token in enumerate(tokens):
        f1, f2 = VOWEL_FORMANTS.get(token, (550, 1450))
        # A small, deterministic tone contour stands in for a state-conditioned F0 model.
        base_f0 = 125 + (word_index % 4) * 9
        tone = (word_index % 3) - 1
        state_specs = [
            ("onset", 0.20, base_f0, f1 * 0.82, f2 * 0.92, 0.55),
            ("vowel", 0.60, base_f0 + tone * 11, f1, f2, 1.00),
            ("coda", 0.20, base_f0 + tone * 6, f1 * 1.04, f2 * 0.96, 0.72),
        ]
        base_frames = max(15, int(round(0.36 / FRAME_SECONDS)))
        durations = [max(3, int(round(base_frames * share))) for _, share, *_ in state_specs]
        durations[-1] += base_frames - sum(durations)

        for (state, _, state_f0, state_f1, state_f2, amplitude), n_frames in zip(state_specs, durations):
            for frame_idx in range(n_frames):
                f0 = state_f0 + 2.5 * np.sin(2 * np.pi * frame_idx / max(n_frames, 1))
                t = np.arange(frame_n, dtype=np.float64) / SAMPLE_RATE
                phase += 2 * np.pi * f0 * FRAME_SECONDS
                local_phase = 2 * np.pi * f0 * t + phase
                voiced = np.zeros(frame_n, dtype=np.float64)
                for harmonic in range(1, 22):
                    hz = harmonic * f0
                    envelope = (np.exp(-0.5 * ((hz - state_f1) / 180) ** 2)
                                + 0.70 * np.exp(-0.5 * ((hz - state_f2) / 260) ** 2)
                                + 0.25 * np.exp(-0.5 * ((hz - 2800) / 550) ** 2))
                    voiced += envelope / harmonic * np.sin(harmonic * local_phase)
                noise = rng.normal(0, 1, frame_n)
                mix = 0.30 if state == "onset" else (0.08 if state == "coda" else 0.015)
                frame = amplitude * (voiced + mix * noise)
                frame *= np.hanning(frame_n)
                audio_frames.append(frame.astype(np.float32))
                f0_track.append(float(f0)); f1_track.append(float(state_f1))
                energy_track.append(float(amplitude)); states.append(state); word_track.append(token)

        audio_frames.append(np.zeros(int(0.025 * SAMPLE_RATE), dtype=np.float32))

    waveform = np.concatenate(audio_frames)
    peak = max(float(np.max(np.abs(waveform))), 1e-8)
    waveform = (waveform * (0.72 / peak)).astype(np.float32)
    tracks = {
        "f0": np.asarray(f0_track, dtype=np.float32),
        "spectral": np.asarray(f1_track, dtype=np.float32),
        "energy": np.asarray(energy_track, dtype=np.float32),
        "state": np.asarray(states),
        "word": np.asarray(word_track),
        "frame_hz": int(round(1 / FRAME_SECONDS)),
    }
    return waveform, SAMPLE_RATE, tracks
