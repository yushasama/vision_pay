from tensorflow.keras import layers, models
import tensorflow as tf

class ExpertModel(tf.keras.Model):
    def __init__(self, trainable=True, **kwargs):
        super(ExpertModel, self).__init__()

        # Define input size
        self.input_layer = layers.InputLayer(input_shape=(224, 224, 3))

        # Convolutional layers with dropout
        self.conv1 = layers.Conv2D(32, (3, 3), activation='relu')
        self.dropout1 = layers.Dropout(0.3)
        self.conv2 = layers.Conv2D(64, (3, 3), activation='relu')
        self.dropout2 = layers.Dropout(0.3)
        self.conv3 = layers.Conv2D(128, (3, 3), activation='relu')
        self.dropout3 = layers.Dropout(0.3)

        # Flatten and dense layers with dropout
        self.flatten = layers.Flatten()
        self.dense = layers.Dense(64, activation='relu')
        self.dropout4 = layers.Dropout(0.5)

        # Output layer for probabilistic classification
        self.output_layer = layers.Dense(4, activation='softmax')

    def call(self, x):
        x = self.conv1(x)
        x = self.dropout1(x)
        x = self.conv2(x)
        x = self.dropout2(x)
        x = self.conv3(x)
        x = self.dropout3(x)
        x = self.flatten(x)
        x = self.dense(x)
        x = self.dropout4(x)
        return self.output_layer(x)

    def compile(self, **kwargs):
        kwargs.setdefault('optimizer', 'adam')
        kwargs.setdefault('loss', 'sparse_categorical_crossentropy')
        kwargs.setdefault('metrics', ['accuracy'])
        super(ExpertModel, self).compile(**kwargs)

    def get_config(self):
        config = super(ExpertModel, self).get_c
