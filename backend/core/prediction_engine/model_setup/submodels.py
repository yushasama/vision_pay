from .expert_model import ExpertModel
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping

class AppleExpert:
  def __init__(self, gpu_train: bool = False):
    self.model = ExpertModel()
    self.model.compile()
    self.gpu_train = gpu_train

  def train(self, data, labels, initial_epochs=5, final_epochs=10, batch_size=32):
    device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'
    early_stopping = EarlyStopping(monitor='loss', patience=3, restore_best_weights=True)

    # Stage 1: Train on apple-specific data
    with tf.device(device):
      print(f"Training AppleExpert on {device} for Stage 1 (apple data only)")
      apple_data = data[labels == 0]
      apple_labels = labels[labels == 0]
      self.model.fit(apple_data, apple_labels, epochs=initial_epochs, batch_size=batch_size, callbacks=[early_stopping])

    # Stage 2: Train on the full multi-class dataset
    with tf.device(device):
      print(f"Training AppleExpert on {device} for Stage 2 (full multi-class data)")
      self.model.fit(data, labels, epochs=final_epochs, batch_size=batch_size, callbacks=[early_stopping])

  def save_model(self, file_path="apple_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="apple_expert.h5"):
    self.model = tf.keras.models.load_model(file_path)

# Repeat for other expert classes: BananaExpert, OrangeExpert, MangoExpert
