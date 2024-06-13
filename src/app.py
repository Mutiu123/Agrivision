import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from predict import predict
import config
import numpy as np

# Function to run the Streamlit app for user interaction
def run_streamlit_app(model_path, data_categories, img_size):
    # Set page title and favicon
    st.set_page_config(page_title="Fruit Classifier", page_icon="🍎")

    # Add a colorful header
    st.title("Fruits and Vegetables Classification Model")
    st.markdown("---")

    # Load the pre-trained model
    model = load_model(model_path)

    # File uploader for image selection
    uploaded_files = st.file_uploader("Choose images to classify", accept_multiple_files=True)

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            img = tf.keras.utils.load_img(uploaded_file, target_size=img_size)
            score = predict(model, img, img_size)
            predicted_category = data_categories[np.argmax(score)]
            prediction_accuracy = np.max(score) * 100

            # Display the uploaded image
            st.image(uploaded_file, use_column_width=True)

            # Show classification results
            st.write(f"Predicted category: **{predicted_category}**")
            st.write(f"Prediction accuracy: **{prediction_accuracy:.2f}%**")
            st.markdown("---")

            # Add a "Reset" button with a unique key
            if st.button("Reset", key=f"reset_button_{uploaded_file.name}"):
                uploaded_files.clear()  # Clear uploaded files

# Load the model and class names
model_path = "../model/fruit_classifier.keras"
data_categories = ["apple", "banana", "beetroot", "bell pepper", "cabbage", "capsicum", "carrot", "cauliflower",
                   "chilli pepper", "corn", "cucumber", "eggplant", "garlic", "ginger", "grapes", "jalepeno",
                   "kiwi", "lemon", "lettuce", "mango", "onion", "orange", "paprika", "pear", "peas", "pineapple",
                   "pomegranate", "potato", "raddish", "soy beans", "spinach", "sweetcorn", "sweetpotato", "tomato",
                   "turnip", "watermelon"]  # Replace with actual class names
img_size = (config.img_height, config.img_width)

# Run the Streamlit app
run_streamlit_app(model_path, data_categories, img_size)
