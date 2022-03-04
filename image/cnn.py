import random

import tensorflow as tf
import tensorflow_datasets as tfds



# hyper-parameters
batch_size = 64
# 10 categories of images (CIFAR-10)
num_classes = 10

def load_data():
    """
    This function loads CIFAR-10 dataset, and preprocess it
    """
    def preprocess_image(image, label):
        # convert [0, 255] range integers to [0, 1] range floats
        image = tf.image.convert_image_dtype(image, tf.float32)
        return image, label
    # loading the CIFAR-10 dataset, splitted between train and test sets
    ds_train, info = tfds.load("cifar10", with_info=True, split="train", as_supervised=True)
    ds_test = tfds.load("cifar10", split="test", as_supervised=True)
    # repeat dataset forever, shuffle, preprocess, split by batch
    ds_train = ds_train.repeat().shuffle(1024).map(preprocess_image).batch(batch_size)
    ds_test = ds_test.repeat().shuffle(1024).map(preprocess_image).batch(batch_size)
    return ds_train, ds_test, info


from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

# CIFAR-10 classes
categories = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"
}

# load the testing set
ds_train, ds_test, info = load_data()
# load the model with final model weights
model = load_model("results/cifar10-model-v1.h5")

# get prediction for this image
def get_prediction():
    data_sample = next(iter(ds_test))
    sample_image = data_sample[0].numpy()[0]
    sample_label = categories[data_sample[1].numpy()[0]]
    prediction = np.argmax(model.predict(sample_image.reshape(-1, *sample_image.shape))[0])

    # plt.savefig('static/images/image'+str(random.randint(1, 100))+'.png')

    predicted_label = categories[prediction]
    true_label = sample_label

    return predicted_label, true_label, sample_image



