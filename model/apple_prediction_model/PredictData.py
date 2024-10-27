import tensorflow as tf 
import pickle
import numpy as np

model = tf.keras.models.load_model('apple_prediction_model.h5')

X = open('C:/Users/syngu/OneDrive/Documents/GitHub/vision_pay/model/apple_prediction_model/testing_fruit_features.pickle','rb')
y = open('C:/Users/syngu/OneDrive/Documents/GitHub/vision_pay/model/apple_prediction_model/testing_fruit_label.pickle','rb')
X = pickle.load(X)
y = pickle.load(y)

y = np.array(y)


X = X/255.0

loss, accuracy = model.evaluate(X, y)

print( accuracy)