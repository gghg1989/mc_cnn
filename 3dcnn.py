import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

def load_data(filename):
    loaded_data = np.load(filename)
    return loaded_data['data'], loaded_data['labels']

# Function to create a 3D CNN model
def create_3d_cnn(input_shape):
    model = models.Sequential()

    # 3D convolutional layers with padding
    model.add(layers.Conv3D(32, kernel_size=(3, 3, 3), activation='relu', padding='same', input_shape=input_shape))
    model.add(layers.MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(layers.Conv3D(64, kernel_size=(3, 3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling3D(pool_size=(2, 2, 2)))
    model.add(layers.Conv3D(128, kernel_size=(3, 3, 3), activation='relu', padding='same'))
    model.add(layers.MaxPooling3D(pool_size=(2, 2, 2)))

    # Flatten layer
    model.add(layers.Flatten())

    # Fully connected layers
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(1, activation='sigmoid'))

    return model

# Function to train a 3D CNN model
def train_3d_cnn(model, train_data, train_labels, epochs, batch_size):
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(train_data, train_labels, epochs=epochs, batch_size=batch_size)

# Function to test a 3D CNN model
def test_3d_cnn(model, test_data, test_labels):
    test_loss, test_acc = model.evaluate(test_data, test_labels)
    print(f'Test accuracy: {test_acc}')

# Generate synthetic training and testing data
num_train_samples = 1000
num_test_samples = 200
input_shape = (16, 16, 384, 1)

train_data, train_labels = load_data('data/training_data.npz')
test_data, test_labels = load_data('data/test_data.npz')


# Create and train the 3D CNN model
model = create_3d_cnn(input_shape)
train_3d_cnn(model, train_data, train_labels, epochs=10, batch_size=16)

# Test the 3D CNN model
test_3d_cnn(model, test_data, test_labels)
