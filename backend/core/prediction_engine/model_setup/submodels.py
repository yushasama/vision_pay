from tensorflow.keras.callbacks import EarlyStopping
from .expert_model import ExpertModel
import tensorflow as tf

class AppleExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, epochs, batch_size=32, callbacks=[]):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'
        with tf.device(device):
            print(f"Training AppleExpert on {device}")
            self.model.fit(data, labels, epochs=epochs, batch_size=batch_size, callbacks=callbacks)

    def save_model(self, file_path="apple_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="apple_expert.h5"):
        self.model = tf.keras.models.load_model(file_path)

class BananaExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, epochs, batch_size=32, callbacks=[]):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'
        with tf.device(device):
            print(f"Training BananaExpert on {device}")
            self.model.fit(data, labels, epochs=epochs, batch_size=batch_size, callbacks=callbacks)


    def save_model(self, file_path="banana_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="banana_expert.h5"):
        self.model = tf.keras.models.load_model(file_path)

class OrangeExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, epochs, batch_size=32, callbacks=[]):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'
        with tf.device(device):
            print(f"Training OrangeExpert on {device}")
            self.model.fit(data, labels, epochs=epochs, batch_size=batch_size, callbacks=callbacks)

    def save_model(self, file_path="orange_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="orange_expert.h5"):
        self.model = tf.keras.models.load_model(file_path)

class MangoExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, epochs, batch_size=32, callbacks=[]):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'
        with tf.device(device):
            print(f"Training MangoExpert on {device}")
            self.model.fit(data, labels, epochs=epochs, batch_size=batch_size, callbacks=callbacks)

    def save_model(self, file_path="mango_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="mango_expert.h5"):
        self.model = tf.keras.models.load_model(file_path)