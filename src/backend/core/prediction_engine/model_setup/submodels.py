from expert_model import ExpertModel

epoch_count = 10
batch_size = 32

class AppleExpert:
  def __init__(self):
    self.model = ExpertModel()
    self.model.compile()  # Assuming compile is a method in ExpertModel

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="apple_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="apple_expert.h5"):
    self.model.load(file_path)

class BananaExpert:
  def __init__(self):
    self.model = ExpertModel()
    self.model.compile()  # Assuming compile is a method in ExpertModel

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="banana_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="banana_expert.h5"):
    self.model.load(file_path)

class OrangeExpert:
  def __init__(self):
    self.model = ExpertModel()
    self.model.compile()  # Assuming compile is a method in ExpertModel

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="orange_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="orange_expert.h5"):
    self.model.load(file_path)

class MangoExpert:
  def __init__(self):
    self.model = ExpertModel()
    self.model.compile()

  def train(self, data, labels, epochs = epoch_count, batch_size = batch_size):
    self.model.fit(data, labels, epochs = epochs, batch_size = batch_size)

  def save_model(self, file_path="mango_expert.h5"):
    self.model.save(file_path)

  def load_model(self, file_path="mango_expert.h5"):
    self.model.load(file_path)