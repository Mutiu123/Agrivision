from tensorflow.keras import layers, Sequential

# Function to create a Sequential model with convolutional and dense layers
def create_model(input_shape, num_classes):
    try:
        model = Sequential([
            layers.Rescaling(1./255, input_shape=input_shape),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dropout(0.2),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes, activation='softmax')
        ])
        return model
    except Exception as e:
        print(f"An error occurred while creating the model: {e}")
        return None