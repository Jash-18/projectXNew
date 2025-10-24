---
title: ProjectXNew Plant Disease Detection
emoji: 🌿
colorFrom: green
colorTo: lime
sdk: gradio
sdk_version: 4.44.0
python_version: 3.11
app_file: app.py
pinned: false
---

# ProjectXNew - Hugging Face Space

This Space runs a Gradio app that performs plant disease detection using a PyTorch CNN. Upload a leaf image to get a diagnosis, suggested steps, and supplement recommendations.

## Files
- `app.py`: Gradio entrypoint
- `CNN.py`: Model architecture
- `data/disease_info.csv`: Disease descriptions
- `data/supplement_info.csv`: Supplement mapping
- `model/ProjectXOAdv.pt`: Trained weights (add this file)

## Run locally
```
pip install -r requirements.txt
python app.py
```
