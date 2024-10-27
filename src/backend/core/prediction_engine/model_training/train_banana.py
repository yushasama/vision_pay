from backend.utils.data_transform import preprocess_image_with_crop
from backend.core.prediction_engine.model_setup.submodels import BananaExpert
from PIL import Image
import numpy as np
import os

dataset_path = os.path.join(os.path.dirname(__file__), "../../../..", "model/dataset/bananas")

banana_data = []

for filename in os.listdir(dataset_path):
  if filename.endswith(".jpg") or filename.endswith(".png"):
    img_path = os.path.join(dataset_path, filename)
    img_array = preprocess_image_with_crop(img_path, True)

    banana_data.append(img_array)

# Convert list of img data to numpy array
banana_data = np.array(banana_data)

banana_labels = np.full(
  (banana_data.shape[0],),
  1,
  dtype=int
)

banana_expert = BananaExpert()
banana_expert.train(banana_data, banana_labels)
banana_expert.save_model("banana_expert.h5")
