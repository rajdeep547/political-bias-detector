---
title: Political Bias Detector
emoji: 📰
colorFrom: blue
colorTo: red
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
---

# 📰 Political Bias Detector

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/rajdeep547/political-bias-detector)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black)](https://github.com/rajdeep547/political-bias-detector)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A fine-tuned **BERT-based** model for detecting political bias in news articles. Classifies text as **Left**, **Neutral**, or **Right** with confidence scores.

## 🌟 Features

- 🔍 **Accurate Classification**: Fine-tuned BERT model with ~85% accuracy
- 📊 **Confidence Scores**: See probability distribution for each prediction
- 🚀 **Easy to Use**: Simple web interface powered by Gradio
- 🌐 **Public API**: Deployed on Hugging Face Spaces
- 💻 **Local Deployment**: Run on your machine with minimal setup

## 🧠 Model Details

| Feature | Description |
|---------|-------------|
| **Base Model** | BERT-base-uncased |
| **Dataset** | TriLabel Political News (10,000 samples) |
| **Classes** | Left, Neutral, Right |
| **Accuracy** | ~85% |
| **Framework** | PyTorch + Transformers |

### Dataset Distribution
| Class | Samples |
|-------|---------|
| Left | ~3,300 |
| Neutral | ~3,300 |
| Right | ~3,400 |

## 🚀 Live Demo

Try the model right now without installing anything:

**[👉 Click here for Live Demo](https://huggingface.co/spaces/rajdeep547/political-bias-detector)**

## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Step 1: Clone the Repository
```bash
git clone https://github.com/rajdeep547/political-bias-detector.git
cd political-bias-detector
