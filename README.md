# ProjectXNew - Plant Disease Detection Web Application

🍁 **Optimized for Vercel Deployment** 🍁

An AI-powered web application that detects plant diseases from uploaded leaf images using a trained Convolutional Neural Network (CNN). The application provides disease identification, treatment recommendations, and supplement suggestions.

## 🚀 Features

- **AI Disease Detection**: Upload plant leaf images to get instant disease diagnosis
- **39 Disease Classes**: Supports detection of diseases across 13 plant types
- **Treatment Recommendations**: Provides actionable steps for disease management
- **Supplement Suggestions**: Recommends appropriate fertilizers and treatments
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Serverless Ready**: Optimized for deployment on Vercel, Render, Railway

## 🌱 Supported Plants

- Apple, Blueberry, Cherry, Corn
- Grape, Orange, Peach, Pepper Bell
- Potato, Raspberry, Soybean, Squash
- Strawberry, Tomato

## 🔧 Technology Stack

- **Backend**: Python, Flask
- **ML Framework**: PyTorch
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Deployment**: Vercel-compatible serverless architecture

## 📦 Installation & Local Development

### Prerequisites
- Python 3.8+
- Git

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jash-18/projectXNew.git
   cd projectXNew
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add model file** (Required)
   - Download your trained model file `ProjectXOAdv.pt`
   - Place it in the `model/` directory or project root
   - The app will automatically detect the correct path

5. **Run locally**
   ```bash
   python api/index.py
   ```
   
   Visit `http://localhost:5000` to use the application

## 🚀 Deployment Options

### Option 1: Vercel (Recommended for Light Use)

1. **Connect Repository**
   - Fork/clone this repository
   - Connect to Vercel through GitHub integration
   - Vercel will auto-detect the Python project

2. **Configure Build**
   - Framework Preset: `Other`
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: `api`
   - Install Command: `pip install -r requirements.txt`

3. **Deploy**
   - Push to main branch
   - Vercel will automatically deploy

**Note**: If you encounter bundle size limits on Vercel, consider Option 2 or 3.

### Option 2: Railway (Better for ML Apps)

1. **Connect Repository**
   - Sign up at Railway.app
   - Connect GitHub repository
   - Railway auto-detects Python and requirements.txt

2. **Deploy**
   - Railway handles the build and deployment automatically
   - Supports larger applications and longer build times

### Option 3: Render

1. **Create Web Service**
   - Sign up at Render.com
   - Create new Web Service from GitHub
   - Select this repository

2. **Configure**
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn api.index:app`

## 📁 Project Structure

```
projectXNew/
├── api/
│   └── index.py          # Main Flask application (Vercel entry point)
├── data/
│   ├── disease_info.csv   # Disease information database
│   └── supplement_info.csv # Treatment recommendations
├── templates/             # HTML templates (to be added)
│   ├── base.html
│   ├── home.html
│   ├── index.html
│   ├── contact-us.html
│   └── submit.html
├── static/               # CSS, JS, images (to be added)
├── model/                # ML model files
│   └── ProjectXOAdv.pt   # Trained PyTorch model
├── CNN.py                # CNN model architecture
├── config.py             # Environment-aware configuration
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel deployment config
└── README.md            # This file
```

## 🔍 API Endpoints

- `GET /` - Home page
- `GET /index` - AI prediction interface
- `GET /contact` - Contact page
- `POST /submit` - Image upload and prediction
- `GET /health` - Health check endpoint

## 🛠️ Configuration

The application automatically handles different environments:

- **Local Development**: Uses relative paths and local files
- **Vercel**: Optimized for serverless functions
- **Other Platforms**: Flexible path resolution

## 📊 Model Information

- **Architecture**: Custom CNN with 4 convolutional blocks
- **Input Size**: 224x224 RGB images
- **Output Classes**: 39 disease categories
- **Framework**: PyTorch
- **Preprocessing**: Automatic image resizing and normalization

## 🚨 Troubleshooting

### Common Issues

1. **Model file not found**
   - Ensure `ProjectXOAdv.pt` is in the correct directory
   - Check file permissions and size limits

2. **Import errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility (3.8+)

3. **Vercel deployment fails**
   - Check bundle size limits (250MB for Vercel)
   - Consider using Railway or Render for larger applications

4. **Memory errors**
   - Reduce model size or use model quantization
   - Consider using CPU-only inference

### Debug Mode

For local debugging, set Flask debug mode:
```python
app.run(debug=True)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ for helping farmers and gardeners detect plant diseases early and take appropriate action.**
