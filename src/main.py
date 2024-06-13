# main.py
from data_preparation import setup_gpu, load_and_augment_data, load_data
from model import create_model
from train import train_model
from plot_results import plot_training_history
import config

# Main function to set up the environment, train the model, and plot results
def main():
    setup_gpu()
    input_shape = (config.img_height, config.img_width, config.num_channels)
    train_data_gen = load_and_augment_data(config.train_data_path, (config.img_width, config.img_height), 32)
    val_data_gen = load_data(config.val_data_path, (config.img_width, config.img_height), 32)
    data_categories = list(train_data_gen.class_indices.keys())
    model = create_model(input_shape, len(data_categories))
    hist = train_model(model, train_data_gen, val_data_gen, config.epochs)
    model.save('../model/fruit_classifier.keras')

    # Plot the training results
    plot_training_history(hist, config.epochs)

if __name__ == '__main__':
    main()
