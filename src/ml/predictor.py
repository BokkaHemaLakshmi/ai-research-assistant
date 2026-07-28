import tensorflow as tf
import numpy as np
import os

class DocumentClassifier:
    def __init__(self, model_path: str = "./models/tf_classifier.h5"):
        self.categories = [
            "Computer Vision",
            "Machine Learning",
            "Natural Language Processing",
            "Cyber Security",
            "Cloud Computing",
            "Robotics",
            "Artificial Intelligence"
        ]
        if os.path.exists(model_path):
            self.model = tf.keras.models.load_model(model_path)
        else:
            self.model = None

    def predict_category(self, text_snippet: str) -> str:
        if not self.model or not text_snippet.strip():
            return "Artificial Intelligence"
        
        preds = self.model.predict(np.array([text_snippet]), verbose=0)
        predicted_idx = np.argmax(preds[0])
        if predicted_idx < len(self.categories):
            return self.categories[predicted_idx]
        return "Artificial Intelligence"