import os

def get_file_path(filename):
    """
    Get correct file path for different environments
    Vercel-compatible path handling
    """
    if os.environ.get('VERCEL'):
        # Running on Vercel - files are in root
        return filename
    else:
        # Running locally - might be in data/ directory
        if os.path.exists(f'data/{filename}'):
            return f'data/{filename}'
        elif os.path.exists(filename):
            return filename
        else:
            # Fallback to original structure
            return f'MyApp/{filename}'

def get_model_path():
    """
    Get model file path for different environments
    """
    model_name = 'ProjectXOAdv.pt'
    
    if os.environ.get('VERCEL'):
        # On Vercel, model should be in root or model directory
        if os.path.exists(f'model/{model_name}'):
            return f'model/{model_name}'
        else:
            return model_name
    else:
        # Local development paths
        if os.path.exists(f'model/{model_name}'):
            return f'model/{model_name}'
        elif os.path.exists(model_name):
            return model_name
        else:
            # Fallback to original structure
            return f'MyApp/{model_name}'
