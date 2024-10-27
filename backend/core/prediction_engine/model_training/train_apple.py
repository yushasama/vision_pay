from backend.utils.data_transform import preprocess_image_with_crop
from backend.core.prediction_engine.model_setup.submodels import AppleExpert
import numpy as np
import os

dataset_path = os.path.join(os.path.dirname(__file__), "../../../..", "model/dataset/apples")

apple_data = []

for filename in os.listdir(dataset_path):
  if filename.endswith(".jpg") or filename.endswith(".png"):
    img_path = os.path.join(dataset_path, filename)
    img_array = preprocess_image_with_crop(img_path, True)

    apple_data.append(img_array)

# Convert list of img data to numpy array
apple_data = np.array(apple_data)

apple_labels = np.full(
  (apple_data.shape[0],),
  0,
  dtype=int
)

apple_expert = AppleExpert()
apple_expert.train(apple_data, apple_labels)
apple_expert.save_model("apple_expert.h5")