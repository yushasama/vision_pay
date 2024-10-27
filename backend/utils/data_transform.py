from PIL import Image
import numpy as np
import cv2

# Direct resize
def preprocess_image(img_path: str, rgb_conversion: bool = True) -> np.array:
  if rgb_conversion:
    img = Image.open(img_path).convert("RGB")
  
  img = img.resize(
    (224, 224)
  )

  # Normalize to RGB values
  return np.array(img) / 255.0

# Best for square images that are already cented
def preprocess_image_with_crop(img_path: str, rgb_conversion: bool = True) -> np.array:
  if rgb_conversion:
    img = Image.open(img_path).convert("RGB")
  
  w, h = img.size

  min_dim = min(w, h)

  left = (w - min_dim) / 2
  top = (h - min_dim) / 2

  img = img.crop(
    (left, top, left + min_dim, top + min_dim)
  )

  img = img.resize(
    (224, 224)
  )

  # Normalize to RGB values
  return np.array(img) / 255.0

# Add padding to make image square then resize
def preprocess_image_with_padding(img_path: str) -> np.array:
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    old_size = img.shape[:2]  # (height, width)
    ratio = float(224) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])
    img = cv2.resize(img, (new_size[1], new_size[0]))

    delta_w = 224 - new_size[1]
    delta_h = 224 - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    color = [0, 0, 0]
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

    # Normalize to RGB values
    return np.array(img) / 255.0