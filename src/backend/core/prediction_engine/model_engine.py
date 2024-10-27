from mixture_of_experts import MixtureOfExperts
from gating_network import GatingNetwork
from expert_model import ExpertModel
import numpy as np


# moe_model.compile()

# num_classes = 4

# predictions = moe_model.predict("input_data")

# predicted_class_indices = np.argmax(predictions, axis=1)
# predicted_labels = [class_labels[index] for index in predicted_class_indices]

for i, label in enumerate(predicted_labels):
    print(f"Input {i+1}: {label}")

class ModelEngine:
  def __init__(self, num_classes: int = 4, epoch_count: int = 10, batch_size: int = 32):
    self.num_classes = num_classes
    self.epoch_count = epoch_count
    self.batch_size = batch_size
    
    class_labels = {
      0: "APPLE",
      1: "BANANA",
      2: "ORANGE",
      3: "MANGO"
    }

    apple_expert = ExpertModel()
    banana_expert = ExpertModel()
    orange_expert = ExpertModel()
    mango_expert = ExpertModel()
    
    experts = [
      apple_expert,
      banana_expert,
      orange_expert,
      mango_expert
    ]
    
    gating_network = GatingNetwork() 
    moe_model = MixtureOfExperts(experts, gating_network)