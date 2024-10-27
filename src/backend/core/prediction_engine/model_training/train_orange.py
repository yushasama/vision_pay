from backend.utils.data_transform import preprocess_image_with_crop
from backend.core.prediction_engine.model_setup.submodels import OrangeExpert
from PIL import Image
import numpy as np
import os

dataset_path = os.path.join(os.path.dirname(__file__), "../../../..", "model/dataset/oranges")

orange_data = []

for filename in os.listdir(dataset_path):
  if filename.endswith(".jpg") or filename.endswith(".png"):
    img_path = os.path.join(dataset_path, filename)
    img_array = preprocess_image_with_crop(img_path, True)

    orange_data.append(img_array)

# Convert list of img data to numpy array
orange_data = np.array(orange_data)

orange_labels = np.full(
  (orange_data.shape[0],),
  1,
  dtype=int
)

orange_expert = OrangeExpert()
orange_expert.train(orange_data, orange_labels)
orange_expert.save_model("orange_expert.h5")