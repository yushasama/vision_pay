import tensorflow as tf
layers = tf.keras.layers
layers = tf.keras.models

class GatingNetwork(tf.keras.Model):
  def __init__(self):
    super(GatingNetwork, self).__init__()

    self.input_layer = layers.InputLayer(input_shape=
      (224, 224, 3)
    )
    # Convulation layers to extract features and patterns
    self.conv1 = tf.keras.layers.Conv2D(16, (3,3), activation='relu')
    self.conv2 = tf.keras.layers.Conv2D(32, (3,3), activation='relu')
    self.conv3 = tf.keras.layers.Conv2D(64, (3,3), activation='relu')

    self.flatten = tf.keras.layers.Flatten()

    self.dense = tf.keras.layers.Dense(32, activation='relu')

    self.output_layer = tf.keras.layers.Dense(4, activation='softmax')

  def call(self, x):
    x = self.conv1(x)
    x = self.conv2(x)
    x = self.conv3(x)
    
    x = self.flatten(x)

    x = self.dense(x)

    return self.output_layer(x)