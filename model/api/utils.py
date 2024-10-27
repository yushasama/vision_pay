import tensorflow as tf
import numpy as np

__model = None

def get_fruit(img_input):
<<<<<<< HEAD
    # Add batch dimension and make prediction
    img_input = np.expand_dims(img_input, axis=0)
    prediction = __model.predict(img_input)
    
    # Map the prediction to the correct fruit
    fruits = ['apple', 'banana', 'mango', 'orange']
    predicted_index = np.argmax(prediction)
    return fruits[predicted_index]
=======

    input_size = 97200

    class_names = ['apples', 'banana', 'mango', 'orange']

    prediction = np.argmax(__model.predict(np.array((img_input / 255).flatten()).reshape(1, -1)))
    
    return class_names[prediction]


>>>>>>> origin/main

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    if __model is None:
        __model = tf.keras.models.load_model("model/fruit_recognizer.keras")
        print(__model.summary())
    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
