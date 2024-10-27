from backend.utils.data_transform import preprocess_image_with_crop
from backend.core.prediction_engine.model_setup.submodels import MangoExpert
from PIL import Image
import numpy as np
import os

dataset_path = os.path.join(os.path.dirname(__file__), "../../../..", "model/dataset/mangos")

mango_data = []

for filename in os.listdir(dataset_path):
  if filename.endswith(".jpg") or filename.endswith(".png"):
    img_path = os.path.join(dataset_path, filename)
    img_array = preprocess_image_with_crop(img_path, True)

    mango_data.append(img_array)

# Convert list of img data to numpy array
mango_data = np.array(mango_data)

mango_labels = np.full(
  (mango_data.shape[0],),
  1,
  dtype=int
)

mango_expert = MangoExpert()
mango_expert.train(mango_data, mango_labels)
mango_expert.save_model("mango_expert.h5")