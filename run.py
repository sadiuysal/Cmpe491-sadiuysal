# -*- coding: utf-8 -*-
"""beginner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb

##### Copyright 2019 The TensorFlow Authors.
"""

#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from keras import applications
import matplotlib.pyplot as plt
import tensorflow as tf
import model as model_class
from tensorflow import keras

tf.config.run_functions_eagerly(True)

x_train, x_test = model_class.x_train , model_class.x_test
#print(x_train[0])
batch_size=64


IMG_SIZE=tf.shape(x_train)[1]
#resize_and_scale with layers
resize_and_rescale = model_class.resize_and_rescale
#data augmentation layers
data_augmentation = model_class.data_augmentation
#resize-scale+augmentation
preprocess_layer = model_class.preprocess


inputs=keras.Input(shape=(32, 32, 3))
base_model = applications.resnet50.ResNet50(weights= None, include_top=False, input_shape= (IMG_SIZE,IMG_SIZE,3))
"""Build the `tf.keras.Sequential` model by stacking layers. Choose an optimizer and loss function for training:"""
model = model_class.CustomModel(inputs,model_class.model_layers(inputs))
#model = model_class.CustomModel(base_model.input,base_model.output)

def display_aug_images():
  image=x_train[0]
  # Add the image to a batch
  image = tf.expand_dims(image, 0)
  plt.figure(figsize=(10, 10))
  for i in range(9):
    augmented_image = data_augmentation(image)
    print(augmented_image)
    ax = plt.subplot(3, 3, i + 1)
    plt.show(augmented_image[0],block=True)
    plt.axis("off")


def train():
  model.compile(optimizer='adam') # ['accuracy'])
  """ The `Model.fit` method adjusts the model parameters to minimize the loss: """
  x_train_processed=preprocess_layer(x_train)
  model.fit(x_train, epochs=1 , batch_size=batch_size)
  """The `Model.evaluate` method checks the models performance, usually on a "[Validation-set](https://developers.google.com/machine-learning/glossary#validation-set)" or "[Test-set](https://developers.google.com/machine-learning/glossary#test-set)"."""

  #model.evaluate(x_test,  y_test, verbose=2)

  """The image classifier is now trained to ~98% accuracy on this dataset. To learn more, read the [TensorFlow tutorials](https://www.tensorflow.org/tutorials/).

  If you want your model to return a probability, you can wrap the trained model, and attach the softmax to it:
  """
  """
  probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
  ])

  probability_model(x_test[:5])
  """
#print(loss_fn(model(input_2N)))
train()



