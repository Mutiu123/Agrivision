import tensorflow as tf

# Function to compile and train the model
def train_model(model, train_data, val_data, epochs):
    try:
        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])
        return model.fit(train_data, validation_data=val_data, epochs=epochs)
    except Exception as e:
        print(f"An error occurred while training the model: {e}")
        return None
