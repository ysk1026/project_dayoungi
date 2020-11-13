from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, Sequential
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, GlobalAveragePooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import RMSprop, SGD
from keras import backend as K
import keras
import matplotlib.pyplot as plt
import os
print(os.listdir("../input"))
print(os.listdir("../input/keras-pretrained-models/"))

data_dir = '../input/5-celebrity-faces-dataset/data'
vgg16weight = '../input/keras-pretrained-models/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
resnet50weight = '../input/keras-pretrained-models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'

def prepare_data(self):
    img_width, img_height = 200, 200
    train_data_dir = os.path.join(data_dir, 'train')
    validation_data_dir = os.path.join(data_dir, 'val')
    nb_train_samples = 93
    nb_validation_samples = 25
    epochs = 50
    batch_size = 16
    numclasses = 5