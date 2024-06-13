# plot_results.py
import matplotlib.pyplot as plt

# Function to plot the training history
def plot_training_history(hist, epochs):
    epochs_range = range(epochs)

    plt.figure(figsize=(9, 5))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, hist.history['accuracy'], label='Training Accuracy')
    plt.plot(epochs_range, hist.history['val_accuracy'], label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, hist.history['loss'], label='Training Loss')
    plt.plot(epochs_range, hist.history['val_loss'], label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()
