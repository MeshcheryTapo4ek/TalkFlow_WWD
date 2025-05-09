# Wake Word Detection (WWD) — Open Source Toolkit

> ⚡ I started this project because I couldn't find a good open-source tool for wake word detection — most commercial solutions are expensive, and for my future voice assistant app, it makes more sense to build the functionality in-house.

## 🎯 Goal

This repository is designed to help **train a neural network** for Wake Word Detection (WWD) and integrate it into your own application.

It includes:
- Tools for **recording and preprocessing audio data**
- Scripts for **training**, **testing**, and **buffered inference**
- Future support for **data augmentation** (noise overlay, time stretching, compression, etc.)

---

## 🧠 Neural Network Training

We use a lightweight **LSTM-based neural network**, ideal for real-time, low-resource applications.

Training is performed inside a Jupyter Notebook, with step-by-step explanations.

### Planned Additions:
- Data augmentation pipeline (noise overlay, tempo shift, pitch shift, etc.)
- Dataset balancing and visualization tools

---

## 🎙️ Audio Data Collection

To train the model, we need labeled wake word and background samples.

A simple recording script is included:

- `scripts/prepare_data.py` — collect wake words and background noise
- Files are saved as `.wav` in structured folders

---

## 🚀 Real-Time Wake Word Detection

The file `scripts/run_detector.py` shows how to use the trained model in a live setting with a **sliding audio buffer**.

This module:
- Continuously records audio in short fragments (e.g., 0.25s)
- Maintains a buffer of recent fragments
- Triggers detection when the buffer is full

Useful for integrating into a voice assistant frontend.

---

## 📁 Project Structure

```
src/
├── buffer/           # Sliding audio buffer implementation
├── model/            # Wake word detection model wrapper
├── recording/        # Audio recording tools
scripts/              # CLI scripts for training / running
tests/                # Unit tests
saved_model/          # Trained models (excluded from repo)
```

---

## 📦 Installation

```bash
uv pip install -r pyproject.toml
```

---

## 🧪 Testing & Evaluation

Use the test scripts and `pytest` to verify logic inside the buffer and prediction flow.

You can also feed in your own audio segments to test individual cases.

---

## 📚 License

MIT — Free for personal and commercial use.

---

Built with ❤️ by an engineer who wants WWD to be **simple, cheap, and effective**.