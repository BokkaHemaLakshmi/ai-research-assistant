import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

def train_and_save_classifier():
    os.makedirs("./models", exist_ok=True)
    if not os.path.exists("./data/dataset"):
        os.makedirs("./data/dataset", exist_ok=True)

    # Standard Python list for texts
    train_texts = [
        "Deep learning neural networks for computer vision image recognition and object detection.",
        "Convolutional neural networks and image segmentation techniques in visual systems.",
        "Supervised machine learning algorithms, linear regression, and decision trees for predictive analytics.",
        "Gradient boosting, XGBoost models, and feature engineering for structured data prediction.",
        "Natural language processing transformers, BERT architecture, and sentiment analysis pipelines.",
        "Large language models, tokenization, attention mechanisms, and conversational AI generation.",
        "Cyber security threat detection, network intrusion detection, encryption, and malware analysis.",
        "Cloud computing infrastructure, Kubernetes orchestration, Docker containers, and microservices.",
        "Robotics kinematics, path planning, autonomous navigation, and sensor fusion algorithms.",
        "Artificial intelligence general reasoning, expert systems, and automated knowledge bases."
    ]
    
    train_labels = np.array([0, 0, 1, 1, 2, 2, 3, 4, 5, 6], dtype=np.int32)
    num_classes = 7
    vocab_size = 1000
    max_len = 50

    # 1. Text Vectorization Layer
    vectorize_layer = layers.TextVectorization(
        max_tokens=vocab_size,
        output_mode='int',
        output_sequence_length=max_len
    )
    vectorize_layer.adapt(train_texts)

    model = models.Sequential([
        vectorize_layer,
        layers.Embedding(vocab_size, 32, mask_zero=True),
        layers.GlobalAveragePooling1D(),
        layers.Dense(32, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    print("Training TensorFlow Classification Model...")
    # Pass train_texts as a numpy array of objects or direct list
    model.fit(np.array(train_texts, dtype=object), train_labels, epochs=5, batch_size=2, verbose=1)

    model.save("./models/tf_classifier.h5")
    print("TensorFlow Model successfully saved to ./models/tf_classifier.h5")

if __name__ == "__main__":
    train_and_save_classifier()