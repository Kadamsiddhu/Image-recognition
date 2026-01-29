import cv2
import numpy as np
import os
from utils import predict_image

def create_dummy_image(filename):
    # Create a 224x224x3 image with random colors
    img = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
    cv2.imwrite(filename, img)
    print(f"Created dummy image: {filename}")
    return filename

def test_prediction():
    dummy_file = "test_image.jpg"
    try:
        create_dummy_image(dummy_file)
        
        print("Testing prediction logic...")
        predictions = predict_image(dummy_file)
        
        print("\nPredictions:")
        for p in predictions:
            print(f"{p['rank']}. {p['label']} ({p['confidence']:.2f}%)")
            
        if len(predictions) == 3:
            print("\nSUCCESS: Got 3 predictions.")
        else:
            print(f"\nFAILURE: Expected 3 predictions, got {len(predictions)}")
            
    except Exception as e:
        print(f"\nERROR: {e}")
    finally:
        if os.path.exists(dummy_file):
            os.remove(dummy_file)
            print("Cleaned up dummy image.")

if __name__ == "__main__":
    test_prediction()
