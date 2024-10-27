from backend.core.prediction_engine.model_setup.submodels import AppleExpert, BananaExpert, OrangeExpert, MangoExpert
from backend.utils.data_transform import preprocess_image_with_crop
import numpy as np
import os

dataset_paths = {
    "apple": "model/dataset/apples",
    "banana": "model/dataset/bananas",
    "orange": "model/dataset/oranges",
    "mango": "model/dataset/mangos"
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

def train_and_save_expert(expert, fruit_label, initial_epochs=5, final_epochs=10, batch_size=32):
    # Check if the model already exists
    model_path = f"{expert.model_name}.h5"
    if os.path.exists(model_path):
        print(f"{model_path} already exists. Loading the model instead of retraining.")
        expert.load_model(model_path)
    else:
        print(f"Training and saving {expert.model_name} model.")
        expert.train(data, labels, initial_epochs=initial_epochs, final_epochs=final_epochs, batch_size=batch_size)
        expert.save_model(model_path)

# Initialize and train each expert
apple_expert = AppleExpert(gpu_train=True)
train_and_save_expert(apple_expert, fruit_label=class_labels["apple"])

banana_expert = BananaExpert(gpu_train=True)
train_and_save_expert(banana_expert, fruit_label=class_labels["banana"])

orange_expert = OrangeExpert(gpu_train=True)
train_and_save_expert(orange_expert, fruit_label=class_labels["orange"])

mango_expert = MangoExpert(gpu_train=True)
train_and_save_expert(mango_expert, fruit_label=class_labels["mango"])
