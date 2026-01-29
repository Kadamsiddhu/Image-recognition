import os
from flask import Flask
from services.model_service import load_model_service
from routes.main import main_bp

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configuration
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model on startup
load_model_service()

# Register Blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
