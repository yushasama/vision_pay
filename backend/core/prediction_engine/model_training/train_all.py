import logging
import numpy as np
import os
from backend.core.prediction_engine.model_setup.submodels import AppleExpert, BananaExpert, OrangeExpert, MangoExpert
from backend.utils.data_transform import preprocess_image_with_crop
import tensorflow as tf

dataset_paths = {
    "apple": os.path.join("model/dataset/apples"),
    "banana": os.path.join("model/dataset/bananas"),
    "orange": os.path.join("model/dataset/oranges"),
    "mango": os.path.join("model/dataset/mangos")
}
class_labels = {"apple": 0, "banana": 1, "orange": 2, "mango": 3}

def load_data():
    data, labels = [], []
    for fruit, path in dataset_paths.items():
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                img_path = os.path.join(path, filename)
                img_array = preprocess_image_with_crop(img_path, True)
                data.append(img_array)
                labels.append(class_labels[fruit])
    return np.array(data), np.array(labels)

data, labels = load_data()

def train_and_save_expert(expert, fruit_label, model_name, initial_epochs=5, final_epochs=10, batch_size=32):
    model_path = f"{model_name}.h5"
    
    # Check if the model already exists to prevent re-training
    if os.path.exists(model_path):
        logging.info(f"Model '{model_name}' already exists. Loading the saved model instead of re-training.")
        expert.load_model(model_path)
        return
    
    # Stage 1: Train on only the designated fruit data
    fruit_data = data[labels == fruit_label]
    fruit_labels = labels[labels == fruit_label]
    logging.info(f"Training '{model_name}' on class label {fruit_label} data only.")
    
    # Early stopping callback
    early_stopping_stage1 = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3, restore_best_weights=True)
    
    expert.train(fruit_data, fruit_labels, initial_epochs=initial_epochs, batch_size=batch_size, callbacks=[early_stopping_stage1])
    logging.info(f"Completed Stage 1 training for '{model_name}'.")
    
    # Stage 2: Train on full multi-class data
    logging.info(f"Training '{model_name}' on full multi-class data.")
    
    # Early stopping callback
    early_stopping_stage2 = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3, restore_best_weights=True)
    
    expert.train(data, labels, final_epochs=final_epochs, batch_size=batch_size, callbacks=[early_stopping_stage2])
    logging.info(f"Completed Stage 2 training for '{model_name}'.")
    
    # Save the trained expert model
    expert.save_model(model_path)
    logging.info(f"Model '{model_name}' saved at '{model_path}'.")

def train_all_models():
    experts = [
        (AppleExpert(gpu_train=True), class_labels["apple"], "apple_expert"),
        (BananaExpert(gpu_train=True), class_labels["banana"], "banana_expert"),
        (OrangeExpert(gpu_train=True), class_labels["orange"], "orange_expert"),
        (MangoExpert(gpu_train=True), class_labels["mango"], "mango_expert")
    ]
    
    for expert, fruit_label, model_name in experts:
        train_and_save_expert(expert, fruit_label, model_name)

train_all_models()