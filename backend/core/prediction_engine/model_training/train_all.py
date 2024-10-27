from backend.core.prediction_engine.model_setup.submodels import AppleExpert, BananaExpert, OrangeExpert, MangoExpert
from backend.utils.data_transform import preprocess_image_with_crop
import numpy as np
import os
from tensorflow.keras.callbacks import EarlyStopping

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

def train_and_save_expert(expert, fruit_label, model_name, initial_epochs=5, full_epochs=10, batch_size=32):
    # Define early stopping
    early_stopping = EarlyStopping(monitor='loss', patience=3, restore_best_weights=True)

    # Stage 1: Train on only the designated fruit data
    fruit_data = data[labels == fruit_label]
    fruit_labels = labels[labels == fruit_label]
    print(f"Training {model_name} on {fruit_label} data only.")
    expert.train(fruit_data, fruit_labels, epochs=initial_epochs, batch_size=batch_size, callbacks=[early_stopping])

    # Stage 2: Train on full multi-class data
    print(f"Training {model_name} on full multi-class data.")
    expert.train(data, labels, epochs=full_epochs, batch_size=batch_size, callbacks=[early_stopping])

    # Save the trained expert model
    expert.save_model(f"{model_name}.h5")

# Initialize and train each expert with early stopping
apple_expert = AppleExpert(gpu_train=True)
train_and_save_expert(apple_expert, fruit_label=class_labels["apple"], model_name="apple_expert")

banana_expert = BananaExpert(gpu_train=True)
train_and_save_expert(banana_expert, fruit_label=class_labels["banana"], model_name="banana_expert")

orange_expert = OrangeExpert(gpu_train=True)
train_and_save_expert(orange_expert, fruit_label=class_labels["orange"], model_name="orange_expert")

mango_expert = MangoExpert(gpu_train=True)
train_and_save_expert(mango_expert, fruit_label=class_labels["mango"], model_name="mango_expert")
