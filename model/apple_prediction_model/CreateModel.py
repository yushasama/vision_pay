import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import numpy as np


X = pickle.load(open("C:/Users/syngu/OneDrive/Documents/GitHub/vision_pay/model/apple_prediction_model/training_fruit_features.pickle",'rb'))
y = pickle.load(open("C:/Users/syngu/OneDrive/Documents/GitHub/vision_pay/model/apple_prediction_model/training_fruit_label.pickle",'rb'))

X = X/255.0
strategy = tf.distribute.MirroredStrategy()

with strategy.scope():
    model = Sequential()

    # convolutional layer 1 (2D)
    model.add(Conv2D(64, (3,3), input_shape = X.shape[1:]))
    model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))

    # convolutional layer 2 (2D)
    model.add(Conv2D(64, (3,3)))
    model.add(tf.keras.layers.LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.2))

    # neural network layer 3 (1D)
    model.add(Flatten())
    model.add(Dense(32))
    
    #out put layer
    model.add(Dense(1))
    model.add(Activation("sigmoid"))

    model.compile(loss = "binary_crossentropy",
                    optimizer = "adam",
                    metrics = ["accuracy"])
y = np.array(y)
model.fit(X, y, batch_size = 16, validation_split = 0, epochs = 11)

model.save('apple_prediction_model.h5')
