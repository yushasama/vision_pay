import tensorflow as tf

class GatingNetwork(tf.keras.Model):
  def __init__(self):
    super(GatingNetwork, self).__init__()

    self.conv1 = tf.keras.layers.Conv2d(16, (3,3), activation='relu')

    self.conv1 = tf.keras.layers.Conv2d(32, (3,3), activation='relu')

    self.conv1 = tf.keras.layers.Conv2d(64, (3,3), activation='relu')

    self.flatten = tf.keras.layers.Flatten()

    self.dense = tf.keras.layers.dense(32, activation='relu')

    self.output_layer = tf.keras.layers.Dense(3, activation='softmax')

  def call(self, x):
    x = self.conv1(x)
    x = self.conv2(x)
    x = self.conv3(x)
    
    x = self.flatten(x)

    x = self.dense(x)

    return self.output_layer(x)