# The TensorFlow Method (DeepLearning)
import numpy as np
import time
import matplotlib.pyplot as plt
import tensorflow
import keras
from keras.datasets import mnist # download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense, Dropout, SimpleRNN
from keras.layers import BatchNormalization
from keras.models import load_model

# Initialize a training process with given some critical arguments
def training_process(model_history):
    fig = plt.figure(figsize=(15, 5))
    # Accuracy Increasing, sub-plot 1 on the left
    plt.subplot(1, 2, 1)
    plt.plot(range(1, epochs + 1), model_history.history['accuracy'], 'blue')
    plt.plot(range(1, epochs + 1), model_history.history['val_accuracy'], 'red')
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy', fontsize=15)
    plt.yticks(fontsize=18)
    plt.xlabel('Epoch', fontsize=15)
    plt.xticks(np.arange(1, epochs + 1), fontsize=15)
    # Loss Decreasing, sub-plot 2 on the right
    plt.subplot(1, 2, 2)
    plt.plot(range(1, epochs + 1), model_history.history['loss'], 'blue')
    plt.plot(range(1, epochs + 1), model_history.history['val_loss'], 'red')
    plt.title('Model Loss')
    plt.ylabel('Loss', fontsize=15)
    plt.xlabel('Epoch', fontsize=15)
    plt.xticks(np.arange(1, epochs + 1), fontsize=15)
    plt.show()
    return fig

# mnist.load is a dataset of 60,000 28x28 grayscale images of the 10 digits, along with a test set of 10,000 images.
mnist.load_data() # check the data set and its structure
(X_train, y_train), (X_test, y_test) = mnist.load_data() # is tuple of NumPy arrays
# X_train: uint8 NumPy array of grayscale image data with shapes (60000, 28, 28), containing the training data. Pixel values range from 0 to 255.
# y_train: uint8 NumPy array of digit labels (integers in range 0-9) with shape (60000,) for the training data.
# X_test: uint8 NumPy array of grayscale image data with shapes (10000, 28, 28), containing the test data. Pixel values range from 0 to 255.
# y_test: uint8 NumPy array of digit labels (integers in range 0-9) with shape (10000,) for the test data.

train_sample_size = X_train.shape[0] # X_train.shape is (60000,28,28)
test_sample_size = X_test.shape[0] # X_test.shape is (10000,28,28)
row_size = X_train.shape[1]
col_size = X_train.shape[2]
train_sample_size, row_size, col_size == X_train.shape # a simple check

# use f-string to see how the dataset is divided by X_train, y_train, X_test, y_test
print(f'Total Sample Size: {train_sample_size + test_sample_size},'
      f'Training Sample Size: {train_sample_size},'
      f'Testing Sample Size: {test_sample_size}')
print(f'row pixel: {row_size}, column pixel: {col_size}')

# Parameter Specification
np.random.seed(123)  # for reproducibility
nb_filters = 32
pool_size = (2, 2)
kernel_size = (3, 3)
input_shape = (row_size, col_size, 1)
num_classes = 10
batch_size = 128
epochs = 12

# data pre-processing
X_train = X_train.reshape(train_sample_size, *input_shape).astype('float32') # astype() converts the data type; (60000,28,28,1)
X_test = X_test.reshape(test_sample_size, *input_shape).astype('float32') # (10000,28,28,1)
# Normalize pixel data
X_train = X_train / 255
X_test = X_test / 255
# Transform label set into binary representation, or so called "One-hot encoding"
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

# build RNN model
model = Sequential() # There might be some warnings

# RNN model specification
model.add(Convolution2D(nb_filters, *kernel_size, padding='valid', input_shape=input_shape))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Convolution2D(nb_filters, *kernel_size, padding='valid'))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=pool_size))  # Pool layer
model.add(Dropout(0.25))  # Randomly deactivate neurons
model.add(Flatten())  # Transform into 1 dimensional data
model.add(Dense(128))  # Full connected
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(BatchNormalization())
model.add(Activation("softmax"))

# Compile with defined parameters
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# training
start_time = time.time()
model_result = model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(X_test, y_test))
end_time = time.time()
process_plot = training_process(model_result)
process_plot.savefig(direct + 'training_process_plot.png', dpi=300)
print(f'Training takes {round((end_time - start_time)/60, 1)} minutes to complete')  # Takes about two minutes to finish
validation_acc = model_result.history['val_accuracy'][-1]
print(f'The final accuracy is {validation_acc*100}%')  # The final cross validation accuracy is 93.51%

direct = r'C:/Users/admin/PycharmProjects/pythonProject4/' + '/DEDA_MachineLearning/'
model.save(direct + 'cnn_model.h5')

# ============Load Trained Model=============
model_loaded = load_model(direct + 'cnn_model.h5')
test_accu = model_loaded.evaluate(X_test, y_test)
print(f'Test Accuracy is: {test_accu[1]}')