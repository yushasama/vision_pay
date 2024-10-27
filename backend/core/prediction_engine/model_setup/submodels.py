from .expert_model import ExpertModel
import tensorflow as tf

epoch_count = 10
batch_size = 32

class AppleExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, initial_epochs=5, final_epochs=10, batch_size=32):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

        # Stage 1: Train on apple data only
        with tf.device(device):
            print("-" * 16)
            print(f"Training AppleExpert on {device} for Stage 1 (apple data only)")
            print("-" * 16)

            apple_data = data[labels == 0]
            apple_labels = labels[labels == 0]
            self.model.fit(apple_data, apple_labels, epochs=initial_epochs, batch_size=batch_size)

        # Stage 2: Train on the full multi-class dataset
        with tf.device(device):
            print("-" * 16)
            print(f"Training AppleExpert on {device} for Stage 2 (full multi-class data)")
            print("-" * 16)
            
            self.model.fit(data, labels, epochs=final_epochs, batch_size=batch_size)

    def save_model(self, file_path="apple_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="apple_expert.h5"):
        self.model = tf.keras.models.load_model(file_path)

class BananaExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, initial_epochs=5, final_epochs=10, batch_size=32):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

        # Stage 1: Train on banana data only
        with tf.device(device):
            print("-" * 16)
            print(f"Training BananaExpert on {device} for Stage 1 (banana data only)")
            print("-" * 16)

            banana_data = data[labels == 1]
            banana_labels = labels[labels == 1]
            self.model.fit(banana_data, banana_labels, epochs=initial_epochs, batch_size=batch_size)

        # Stage 2: Train on the full multi-class dataset
        with tf.device(device):
            print("-" * 16)
            print(f"Training BananaExpert on {device} for Stage 2 (full multi-class data)")
            print("-" * 16)

            self.model.fit(data, labels, epochs=final_epochs, batch_size=batch_size)

    def save_model(self, file_path="banana_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="banana_expert.h5"):
        self.model = tf.keras.models.load_model(file_path)

class OrangeExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, initial_epochs=5, final_epochs=10, batch_size=32):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

        # Stage 1: Train on orange data only
        with tf.device(device):
            print("-" * 16)
            print(f"Training OrangeExpert on {device} for Stage 1 (orange data only)")
            print("-" * 16)

            orange_data = data[labels == 2]
            orange_labels = labels[labels == 2]
            self.model.fit(orange_data, orange_labels, epochs=initial_epochs, batch_size=batch_size)

        # Stage 2: Train on the full multi-class dataset
        with tf.device(device):
            print("-" * 16)
            print(f"Training OrangeExpert on {device} for Stage 2 (full multi-class data)")
            print("-" * 16)

            self.model.fit(data, labels, epochs=final_epochs, batch_size=batch_size)

    def save_model(self, file_path="orange_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="orange_expert.h5"):
        self.model = tf.keras.models.load_model(file_path)

class MangoExpert:
    def __init__(self, gpu_train: bool = False):
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, initial_epochs=5, final_epochs=10, batch_size=32):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

        # Stage 1: Train on mango data only
        with tf.device(device):
            print("-" * 16)
            print(f"Training MangoExpert on {device} for Stage 1 (mango data only)")
            print("-" * 16)

            mango_data = data[labels == 3]
            mango_labels = labels[labels == 3]
            self.model.fit(mango_data, mango_labels, epochs=initial_epochs, batch_size=batch_size)

        # Stage 2: Train on the full multi-class dataset
        with tf.device(device):
            print("-" * 16)
            print(f"Training MangoExpert on {device} for Stage 2 (full multi-class data)")
            print("-" * 16)

            self.model.fit(data, labels, epochs=final_epochs, batch_size=batch_size)

    def save_model(self, file_path="mango_expert.h5"):
        self.model.save(file_path)

    def load_model(self, file_path="mango_expert.h5"):
        self.model = tf.keras.models.load_model
