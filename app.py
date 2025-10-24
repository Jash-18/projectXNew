import os
import io
import numpy as np
import pandas as pd
from PIL import Image
import torch
import torchvision.transforms.functional as TF
import gradio as gr

from CNN import CNN

DATA_DIR = "data"
MODEL_DIR = "model"
MODEL_NAME = "ProjectXOAdv.pt"

def get_file(path_candidates):
    for p in path_candidates:
        if p and os.path.exists(p):
            return p
    return None

def load_resources():
    disease_path = get_file([
        os.path.join(DATA_DIR, "disease_info.csv"),
        "disease_info.csv"
    ])
    supp_path = get_file([
        os.path.join(DATA_DIR, "supplement_info.csv"),
        "supplement_info.csv"
    ])
    if disease_path is None or supp_path is None:
        raise FileNotFoundError("CSV files not found in data/ or repo root.")

    disease_df = pd.read_csv(disease_path, encoding="cp1252")
    supp_df = pd.read_csv(supp_path, encoding="cp1252")

    model_path = get_file([
        os.path.join(MODEL_DIR, MODEL_NAME),
        MODEL_NAME
    ])
    if model_path is None:
        raise FileNotFoundError(
            f"Model file {MODEL_NAME} not found. Place it under model/ or repo root."
        )

    model = CNN(K=39)
    state = torch.load(model_path, map_location=torch.device("cpu"))
    model.load_state_dict(state)
    model.eval()

    return model, disease_df, supp_df

MODEL, DISEASE_DF, SUPP_DF = load_resources()

def predict(image: Image.Image):
    try:
        image = image.convert("RGB")
        image = image.resize((224, 224))
        x = TF.to_tensor(image).unsqueeze(0)
        with torch.no_grad():
            out = MODEL(x).numpy()
            idx = int(np.argmax(out))
        def safe_get(df, col, i):
            try:
                return df.iloc[i][col]
            except Exception:
                return ""
        title = safe_get(DISEASE_DF, "disease_name", idx)
        desc = safe_get(DISEASE_DF, "description", idx)
        steps = safe_get(DISEASE_DF, "Possible Steps", idx)
        url = safe_get(DISEASE_DF, "image_url", idx)
        sname = safe_get(SUPP_DF, "supplement name", idx)
        simage = safe_get(SUPP_DF, "supplement image", idx)
        buy = safe_get(SUPP_DF, "buy link", idx)
        result_md = f"""### Prediction
- Disease: {title}
- Description: {desc}
- Steps: {steps}
- Supplement: {sname}
- Buy: {buy}
"""
        return result_md, url, simage
    except Exception as e:
        return f"Error during prediction: {e}", "", ""

with gr.Blocks(title="Plant Disease Detection") as demo:
    gr.Markdown("# 🍁 Plant Disease Detection")
    gr.Markdown("Upload a plant leaf image to get disease prediction and suggestions.")
    with gr.Row():
        with gr.Column():
            inp = gr.Image(type="pil", label="Upload leaf image")
            btn = gr.Button("Analyze")
        with gr.Column():
            out_text = gr.Markdown(label="Result")
            out_img1 = gr.Image(label="Disease Reference Image")
            out_img2 = gr.Image(label="Suggested Supplement Image")
    btn.click(fn=predict, inputs=inp, outputs=[out_text, out_img1, out_img2])

if __name__ == "__main__":
    demo.launch()
