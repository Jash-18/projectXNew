import os
import sys
import io
from flask import Flask, redirect, render_template, request, jsonify
from PIL import Image
import torchvision.transforms.functional as TF
import numpy as np
import torch
import pandas as pd

# Add project root to Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CNN import CNN
from config import get_file_path, get_model_path

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

model = None
disease_info = None
supplement_info = None


def load_model_and_data():
    global model, disease_info, supplement_info
    try:
        disease_info = pd.read_csv(get_file_path('disease_info.csv'), encoding='cp1252')
        supplement_info = pd.read_csv(get_file_path('supplement_info.csv'), encoding='cp1252')
        model = CNN(K=39)
        model_path = get_model_path()
        model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        model.eval()
    except Exception as e:
        print(f"Startup load error: {e}")


def predict_from_bytes(byte_data: bytes) -> int:
    image = Image.open(io.BytesIO(byte_data)).convert('RGB')
    image = image.resize((224, 224))
    input_data = TF.to_tensor(image).unsqueeze(0)
    with torch.no_grad():
        out = model(input_data).numpy()
        return int(np.argmax(out))


load_model_and_data()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/index')
def ai_engine_page():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({
        "model_loaded": model is not None,
        "disease_info": disease_info is not None,
        "supplement_info": supplement_info is not None
    })

@app.route('/submit', methods=['POST'])
def submit():
    if 'image' not in request.files:
        return "No image uploaded", 400
    file = request.files['image']
    if not file or file.filename == '':
        return "No file selected", 400
    pred = predict_from_bytes(file.read())
    title = disease_info.iloc[pred]['disease_name']
    description = disease_info.iloc[pred]['description']
    prevent = disease_info.iloc[pred]['Possible Steps']
    image_url = disease_info.iloc[pred]['image_url']
    sname = supplement_info.iloc[pred]['supplement name']
    simage = supplement_info.iloc[pred]['supplement image']
    buy_link = supplement_info.iloc[pred]['buy link']
    return render_template('submit.html', title=title, desc=description, prevent=prevent,
                           image_url=image_url, pred=pred, sname=sname, simage=simage, buy_link=buy_link)

# Vercel entry
app = app
