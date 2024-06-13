
import tensorflow as tf

# Function to set up GPU configuration to prevent memory overflow
def setup_gpu():
    try:
        gpuAvai = tf.config.experimental.list_physical_devices('GPU')
        for gpu in gpuAvai:
            tf.config.experimental.set_memory_growth(gpu, True)
    except Exception as e:
        print(f"An error occurred while setting up GPU: {e}")

# Function to load data from directories without augmentation
def load_data(data_path, img_size, batch_size):
    try:
        return tf.keras.preprocessing.image_dataset_from_directory(
            data_path,
            shuffle=True,
            image_size=img_size,
            batch_size=batch_size
        )
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None

# Function to load and augment data from directories
def load_and_augment_data(data_path, img_size, batch_size):
    try:
        # Data augmentation settings
        datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )

        # Load images and apply augmentation settings
        return datagen.flow_from_directory(
            data_path,
            target_size=img_size,
            batch_size=batch_size,
            class_mode='binary'  # or 'categorical' if you have more than two classes
        )
    except Exception as e:
        print(f"An error occurred while loading and augmenting data: {e}")
        return None