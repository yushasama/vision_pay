from model_setup.mixture_of_experts import MixtureOfExperts
from model_setup.gating_network import GatingNetwork
from collections import Counter 
import tensorflow as tf
import numpy as np
import os

class ModelEngine:
  def __init__(self, model_save_path="moe_model.h5", num_classes=4):
    self.model_save_path = model_save_path
    self.num_classes = num_classes
    self.class_labels = {
      0: "APPLE",
      1: "BANANA",
      2: "ORANGE",
      3: "MANGO"
    }

    # Load compiled MoE model if it exists
    if os.path.exists(self.model_save_path):
      print("Loading precompiled model.")
      self.moe_model = tf.keras.models.load_model(self.model_save_path)
    else:
      # Load expert models individually
      self.model_paths = {
        "apple": "apple_expert.h5",
        "banana": "banana_expert.h5",
        "orange": "orange_expert.h5",
        "mango": "mango_expert.h5"
      }

      self.experts = []
      for fruit, path in self.model_paths.items():
        if os.path.exists(path):
          self.experts.append(tf.keras.models.load_model(path))
        else:
          print(f"Warning: Model file for {fruit} not found at {path}.")

      # Initialize gating network and compile MoE model
      gating_network = GatingNetwork()
      self.moe_model = MixtureOfExperts(self.experts, gating_network)
      self.moe_model.compile()
      
      # Save compiled model for reuse
      self.moe_model.save(self.model_save_path)
      print("Model compiled and saved for future use.")

  def predict(self, input_data: np.array) -> dict[str, int]:
    predictions = self.moe_model.predict(input_data)

    predicted_indices = np.argmax(predictions, axis=1)

    predicted_labels = Counter(self.class_labels[idx] for idx in predicted_indices)
    predicted_labels = dict(predicted_labels)

    """
    Example of predicted_labels = {
    "apples": 3,
    "bananas": 5,
    "oranges": 0,
    "mangos": 2
    }
    """
    return predicted_labels