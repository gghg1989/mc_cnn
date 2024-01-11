import numpy as np

# Function to generate synthetic 3D data with non-binary elements
def generate_synthetic_data_non_binary(num_samples, input_shape):
    data = np.random.random((num_samples, *input_shape))  # Random float values between 0 and 1
    labels = np.random.randint(2, size=num_samples)  # Binary labels (0 or 1)

    return data, labels

# Function to save data to a file
def save_data(filename, data, labels):
    np.savez(filename, data=data, labels=labels)

# Function to load data from a file
def load_data(filename):
    loaded_data = np.load(filename)
    return loaded_data['data'], loaded_data['labels']

# Generate synthetic training and testing data with non-binary elements
num_train_samples = 1000
num_test_samples = 200
input_shape = (16, 16, 384, 1)

train_data, train_labels = generate_synthetic_data_non_binary(num_train_samples, input_shape)
test_data, test_labels = generate_synthetic_data_non_binary(num_test_samples, input_shape)

# Save data to a file
save_data('synthetic_data.npz', train_data, train_labels)

# Load data from the file
loaded_train_data, loaded_train_labels = load_data('synthetic_data.npz')

# Print shapes of loaded data
print("Loaded Train Data Shape:", loaded_train_data.shape)
print("Loaded Train Labels Shape:", loaded_train_labels.shape)