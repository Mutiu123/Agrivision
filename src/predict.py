# predict.py
import tensorflow as tf
import numpy as np

# Function to make predictions on new data
def predict(model, img, img_size):
    try:
        img_array = tf.keras.utils.img_to_array(img)
        img_process = tf.expand_dims(img_array, 0)
        yhat = model.predict(img_process)
        score = tf.nn.softmax(yhat[0])
        return score
    except Exception as e:
        print(f"An error occurred while making a prediction: {e}")
        return None