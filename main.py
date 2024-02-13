import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import idx2numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

DATA_DIR = 'data/'

TEST_DATA_FILENAME = DATA_DIR + 't10k-images-idx3-ubyte'
TEST_LABELS_FILENAME = DATA_DIR + 't10k-labels-idx1-ubyte'
TRAIN_DATA_FILENAME = DATA_DIR + 'train-images-idx3-ubyte'
TRAIN_LABELS_FILENAME = DATA_DIR + 'train-labels-idx1-ubyte'


def show_random_image_prediction(X_train, y_train, knn_classifier):
    # Select a random index
    random_index = np.random.randint(0, len(X_train))

    # Retrieve the random image and label
    random_image = X_train[random_index]
    random_label = y_train[random_index]

    # Reshape the image into a 28x28 matrix
    random_image = random_image.reshape(28, 28)

    # Use the trained KNN classifier to predict the label of the image
    predicted_label = knn_classifier.predict([random_image.ravel()])

    # Display the image and the predicted label
    plt.imshow(random_image, cmap='gray')
    plt.title(f"Actual Label: {random_label}, Predicted Label: {predicted_label[0]}")
    plt.axis('off')
    plt.show()


def main():
    X_train = idx2numpy.convert_from_file(TRAIN_DATA_FILENAME)
    y_train = idx2numpy.convert_from_file(TRAIN_LABELS_FILENAME)
    X_test = idx2numpy.convert_from_file(TEST_DATA_FILENAME)
    y_test = idx2numpy.convert_from_file(TEST_LABELS_FILENAME)

    # Normalize the pixel values to be between 0 and 1
    # X_train, X_test = X_train / 255.0, X_test / 255.0

    X_train_flattened = X_train.reshape(X_train.shape[0], -1)
    X_test_flattened = X_test.reshape(X_test.shape[0], -1)

    # Display the shape of the datasets
    print("Training data shape:", X_train_flattened.shape)
    print("Testing data shape:", X_test_flattened.shape)

    k = 3  # Number of neighbors
    knn_classifier = KNeighborsClassifier(n_neighbors=k)

    # Train the classifier
    knn_classifier.fit(X_train_flattened, y_train)

    # for i in range(100):
    # show_random_image_prediction(X_train, y_train, knn_classifier)
    # time.sleep(1)

    # Predict on the test data
    y_pred = knn_classifier.predict(X_test_flattened)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)


if __name__ == '__main__':
    main()
