from .expert_model import ExpertModel
from tensorflow.keras.utils import custom_object_scope
import tensorflow as tf

class BaseExpert:
    def __init__(self, model_name, gpu_train=False):
        self.model_name = model_name
        self.model = ExpertModel()
        self.model.compile()
        self.gpu_train = gpu_train

    def train(self, data, labels, initial_epochs=5, final_epochs=10, batch_size=32):
        device = '/GPU:0' if self.gpu_train and tf.config.list_physical_devices('GPU') else '/CPU:0'

        # Stage 1: Train on specific fruit data only
        with tf.device(device):
            print(f"Training {self.model_name} on {device} for Stage 1 (single-class data)")
            fruit_data = data[labels == 0]
            fruit_labels = labels[labels == 0]
            self.model.fit(fruit_data, fruit_labels, epochs=initial_epochs, batch_size=batch_size)

        # Stage 2: Train on full multi-class dataset
        with tf.device(device):
            print(f"Training {self.model_name} on {device} for Stage 2 (full multi-class data)")
            self.model.fit(data, labels, epochs=final_epochs, batch_size=batch_size)

    def save_model(self, file_path=None):
        file_path = file_path or f"{self.model_name}.h5"
        self.model.save(file_path)

    def load_model(self, file_path=None):
        file_path = file_path or f"{self.model_name}.h5"
        with custom_object_scope({'ExpertModel': ExpertModel}):
            self.model = tf.keras.models.load_model(file_path)

class AppleExpert(BaseExpert):
    def __init__(self, gpu_train=False):
        super().__init__("apple_expert", gpu_train)

class BananaExpert(BaseExpert):
    def __init__(self, gpu_train=False):
        super().__init__("banana_expert", gpu_train)

class OrangeExpert(BaseExpert):
    def __init__(self, gpu_train=False):
        super().__init__("orange_expert", gpu_train)

class MangoExpert(BaseExpert):
    def __init__(self, gpu_train=False):
        super().__init__("mango_expert", gpu_train)
