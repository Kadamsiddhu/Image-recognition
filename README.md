# Image Recognition System (MVP)

This is a Flask-based web application that uses a pre-trained MobileNetV2 model (TensorFlow/Keras) to classify images uploaded by the user.

## Features
- Upload images (PNG, JPG, JPEG).
- Server-side validation.
- Real-time object classification.
- Displays top 3 predictions with confidence scores.
- Beginner-friendly interface.

## Project Structure
```
/
├── app.py              # Flask backend application
├── utils.py            # Model loading and image processing logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # HTML frontend
└── static/
    └── style.css       # CSS styling
```

## Prerequisites
- Python 3.7+ installed on your machine.

## Installation & Setup

1.  **Clone or Download** this project folder.

2.  **Open a terminal** inside the project folder.

3.  **Create a Virtual Environment** (Recommended):
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application**:
    ```bash
    python app.py
    ```

6.  **Access the App**:
    Open your web browser and go to: `http://127.0.0.1:5000/`

## How it Works
1.  **Upload**: You upload an image via the web interface.
2.  **Processing**: The server receives the image, saves it, and preprocesses it using OpenCV (resizing, color conversion).
3.  **Inference**: The pre-trained MobileNetV2 model analyzes the image.
4.  **Result**: The app displays the top 3 predicted classes along with their confidence scores.

## Notes
- The first prediction might take a few seconds as the model loads into memory.
- Ensure the image is clear for better accuracy.
