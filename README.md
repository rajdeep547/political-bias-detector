# 📰 Political Bias Detector

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/Transformers-4.30+-yellow)](https://huggingface.co/docs/transformers/index)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/rajdeep547/political-bias-detector/pulls)

A fine-tuned **BERT-based** machine learning model for detecting political bias in news articles. Classifies text as **Left**, **Neutral**, or **Right** with confidence scores and probability distributions.

---

## 📋 Table of Contents

- [🌟 Features](#-features)
- [🧠 Model Overview](#-model-overview)
- [📊 Dataset](#-dataset)
- [🚀 Quick Start](#-quick-start)
- [💻 Installation](#-installation)
- [🎯 Usage Examples](#-usage-examples)
- [📁 Project Structure](#-project-structure)
- [📊 Performance Metrics](#-performance-metrics)
- [🛠️ Technologies Used](#️-technologies-used)
- [🔧 Advanced Configuration](#-advanced-configuration)
- [📝 License](#-license)
- [🤝 Contributing](#-contributing)
- [📧 Contact](#-contact)

---

## 🌟 Features

| Feature | Description |
|---------|-------------|
| 🔍 **Accurate Classification** | Fine-tuned BERT model with high accuracy |
| 📊 **Confidence Scores** | See probability distribution for each prediction |
| 🚀 **Easy to Use** | Simple web interface powered by Gradio |
| 💻 **Local Deployment** | Run on your machine with minimal setup |
| 📦 **Batch Processing** | Process multiple articles at once |
| 🔄 **Real-time Analysis** | Instant predictions with detailed breakdown |

---

## 🧠 Model Overview

### Model Architecture
- **Base Model**: BERT-base-uncased (110M parameters)
- **Fine-tuning**: Custom training on political news dataset
- **Task**: Multi-class text classification (3 classes)

### Why BERT?
BERT's bidirectional attention mechanism captures context better than traditional models, making it ideal for understanding nuanced political language.

| Aspect | Details |
|--------|---------|
| **Input Length** | Up to 512 tokens |
| **Embedding Size** | 768 dimensions |
| **Layers** | 12 transformer layers |
| **Attention Heads** | 12 attention heads |

---

## 📊 Dataset

The model is fine-tuned on the **TriLabel Political News Dataset** from Kaggle:

| Split | Samples | Classes |
|-------|---------|---------|
| **Training** | 10,000 | Left, Neutral, Right |
| **Testing** | 1,000 | Left, Neutral, Right |

### Class Distribution
| Class | Training Samples | Percentage |
|-------|------------------|------------|
| Left | ~3,300 | 33% |
| Neutral | ~3,300 | 33% |
| Right | ~3,400 | 34% |

---

## 🚀 Quick Start

### Run the Web Interface
```bash
# Clone the repository
git clone https://github.com/rajdeep547/political-bias-detector.git
cd political-bias-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Open browser at: http://127.0.0.1:7860
