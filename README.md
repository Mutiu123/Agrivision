**Project Description:**

"Agrivision" is an innovative image classification tool designed to recognise and categorise a wide array of farm produce. Utilizing advanced machine learning techniques, this project aims to bridge the gap between agricultural production and technological advancement.

**Problem Statement:**

In the realm of agriculture, accurately identifying and classifying various crops can be challenging and time-consuming. The Farm Crop Identifier named Agrivision seeks to address this issue by automating the process, thus enhancing efficiency and accuracy.

**Methodology:**

The "Farm Crop Identifier" employs a sophisticated Convolutional Neural Network (CNN) architecture tailored for the precise classification of farm produce images. The methodology unfolds in several key stages:

1. **Data Preparation:**
   - The dataset, comprising images of various farm produce, is divided into training, validation, and test sets.
   - Data augmentation techniques are applied to the training set to simulate variations in real-world conditions, such as different angles and lighting.

2. **GPU Configuration:**
   - GPU memory growth is configured to accommodate the computational demands of the model without causing memory overflow.

3. **Model Architecture:**
   - The CNN model consists of three convolutional blocks, each followed by max-pooling layers to reduce spatial dimensions and extract features.
   - After flattening the output, a dropout layer is introduced to mitigate overfitting.
   - The network concludes with two dense layers, the final layer employing a softmax activation function to yield a probability distribution across the classes.

4. **Model Training:**
   - The model is compiled with the Adam optimizer and Sparse Categorical Crossentropy loss function.
   - It is then trained on the augmented data, with the validation set used to monitor performance and prevent overfitting.

5. **Model Evaluation:**
   - Post-training, the model's accuracy and loss are evaluated on the test set to ensure reliable performance.

6. **Web Interface Integration:**
   - A Streamlit-based web application is developed to enable users to upload images and receive predictions.
   - The app displays the classified produce along with the prediction confidence.

7. **Fine-Tuning:**
   - The model parameters, such as the number of filters and kernel sizes in the convolutional layers, are fine-tuned.
   - Hyperparameters like learning rate and epochs are adjusted to optimize the model's accuracy.

8. **Deployment:**
   - The trained model is saved and integrated into the Streamlit app, ready for deployment and user interaction.


**Project Modules:**

1. **Configuration Module (`config.py`):**
   - Sets up the paths for training, testing, and validation datasets.
   - Defines image standardization parameters such as height, width, and channels.
   - Specifies the number of epochs for model training.

2. **Data Preparation Module (`data_preparation.py`):**
   - Configures GPU settings to optimize memory usage.
   - Implements data augmentation techniques to enhance the robustness of the model.

3. **Model Architecture Module (`model.py`):**
   - Constructs a CNN with sequential layers, including convolutional, max-pooling, dropout, and dense layers.
   - Tailors the model to process input images and output class probabilities.

4. **Training Module (`train.py`):**
   - Compiles the model with appropriate loss functions and optimizers.
   - Manages the training process, utilizing both training and validation datasets.

5. **Prediction Module (`predict.py`):**
   - Converts new images into a format suitable for model input.
   - Generates predictions and interprets the model's output.

6. **Streamlit Application Module (`streamlit_app.py`):**
   - Provides a user-friendly interface for uploading images and displaying classification results.
   - Integrates the trained model to enable real-time predictions.

7. **Main Execution Module (`main.py`):**
   - Orchestrates the entire process from setting up the environment to running the Streamlit app.
   - Saves the trained model for future use.

To run the "Farm Crop Identifier" model using Streamlit, you'll need to follow these steps:

1. **Install Streamlit:**
   If you haven't already installed Streamlit, you can do so using pip:
   ```shell
   pip install streamlit
   ```

2. **Prepare Your Streamlit Script:**
   Ensure your `streamlit_app.py` script is set up correctly with the necessary imports and functions to load the model and handle image uploads.

3. **Run the Streamlit App:**
   Navigate to the directory containing your `streamlit_app.py` file in the terminal and run the following command:
   ```shell
   streamlit run streamlit_app.py
   ```

4. **Interact with the App:**
   - Once the command is executed, Streamlit will start a local server, and your default web browser should automatically open the app.
   - If the browser doesn't open automatically, you can manually navigate to the local URL provided in the terminal output, typically `http://localhost:8501`.

5. **Upload Images:**
   - Use the file uploader in the Streamlit interface to upload images of the farm produce you want to classify.
   - The model will process the images and display the classification results along with the prediction confidence.

6. **Close the App:**
   - When you're done, you can stop the Streamlit server by pressing `Ctrl+C` in the terminal.


This should give you a functional Streamlit app that allows users to upload images and get instant classifications from your model.

 **Classifiable Products:**

The model is adept at identifying a comprehensive list of farm produce, including:

- Apple, Banana, Beetroot, Bell Pepper, Cabbage, Capsicum, Carrot, Cauliflower, Chilli Pepper, Corn, Cucumber, Eggplant, Garlic,  Ginger, Grapes, Jalepeno, Kiwi, Lemon, Lettuce, Mango, Onion, Orange, Paprika, Pear, Peas, Pineapple, Pomegranate, Potato, Radish, Soy Beans, Spinach, Sweetcorn, Sweetpotato, Tomato, Turnip, Watermelon.

**Contribution:**
The project's contribution lies in its meticulous approach to model fine-tuning, which significantly enhances classification accuracy. The Streamlit interface contributes to the project's accessibility, allowing users to interact with the model conveniently through a webpage.

This detailed methodology underscores the project's systematic approach to developing a robust image classification system, from data handling to model deployment.

**Applications:**
This tool has practical applications in various sectors, including agriculture for monitoring crop quality, retail for inventory management, and education for aiding in botanical studies. Its web-based interface, powered by Streamlit, allows for easy access and interaction by users across different platforms.
The "Farm Crop Identifier" stands as a testament to the potential of AI in enhancing agricultural practices and represents a step forward in the fusion of technology and farming.

**Conclusion:**

The "Farm Crop Identifier" represents a significant advancement in agricultural technology. By fine-tuning model parameters and employing a user-friendly web interface, this project contributes to the efficient and accurate classification of farm produce, paving the way for future innovations in the field.

**Future Directions:**
The project anticipates integration with IoT devices for real-time field analysis, expansion of the dataset to include more crop varieties, and the implementation of real-time feedback mechanisms for continuous learning and improvement.

 **Demo results:**
![The System Demo](https://github.com/Mutiu123/Agrivision/blob/main/demo/demo.png)

![The System Demo](https://github.com/Mutiu123/Agrivision/blob/main/demo/demo2.png)

![The System Demo](https://github.com/Mutiu123/Agrivision/blob/main/demo/demo3.png)
![The System Demo](https://github.com/Mutiu123/Agrivision/blob/main/demo/demo4.png)

![The System Demo](https://github.com/Mutiu123/Agrivision/blob/main/demo/demo5.png)


