import cv2
import numpy as np
import os
import time
from services.model_service import predict_image_service

def create_dummy_image(filename):
    # Create a 224x224x3 image with random colors
    img = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
    cv2.imwrite(filename, img)
    print(f"Created dummy image: {filename}")
    return filename

def test_prediction_service():
    dummy_file = "test_image_phase2.jpg"
    try:
        create_dummy_image(dummy_file)
        
        print("Testing prediction service with inference time...")
        predictions, inference_time = predict_image_service(dummy_file)
        
        print(f"\nInference Time: {inference_time} ms")
        print("Predictions:")
        for p in predictions:
            print(f"{p['rank']}. {p['label']} ({p['confidence']:.2f}%)")
            
        if len(predictions) == 3 and inference_time > 0:
            print("\nSUCCESS: Service returned predictions and inference time.")
        else:
            print(f"\nFAILURE: Validation failed.")
            
    except Exception as e:
        print(f"\nERROR: {e}")
    finally:
        if os.path.exists(dummy_file):
            os.remove(dummy_file)
            print("Cleaned up dummy image.")

if __name__ == "__main__":
    test_prediction_service()
