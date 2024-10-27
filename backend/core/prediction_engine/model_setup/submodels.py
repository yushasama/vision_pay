from .expert_model import ExpertModel
import tensorflow as tf

epoch_count = 10
batch_size = 32

class AppleExpert:
  def __init__(self, gpu_train: bool = False):
    self.model = ExpertModel()
    self.model.compile()
    self.gpu_train = gpu_train

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

    with tf.device(device):

       # Display device in training output
      print(f"Training AppleExpert on {device}")
      
      self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="apple_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="apple_expert.h5"):
    self.model.load(file_path)

class BananaExpert:
  def __init__(self, gpu_train: bool = False):
    self.model = ExpertModel()
    self.model.compile()
    self.gpu_train = gpu_train

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

    with tf.device(device):
      
      # Display device in training output
      print(f"Training AppleExpert on {device}")

      self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="banana_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="banana_expert.h5"):
    self.model.load(file_path)

class OrangeExpert:
  def __init__(self,  gpu_train: bool = False):
    self.model = ExpertModel()
    self.model.compile()
    self.gpu_train = gpu_train

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

    with tf.device(device):
            
      # Display device in training output
      print(f"Training AppleExpert on {device}")

      self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="orange_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="orange_expert.h5"):
    self.model.load(file_path)

class MangoExpert:
  def __init__(self, gpu_train: bool = False):
    self.model = ExpertModel()
    self.model.compile()

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    
    # Display device in training output
    print(f"Training AppleExpert on {device}")
      
    device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

    with tf.device(device):
      self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="mango_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="mango_expert.h5"):
    self.model.load(file_path)