import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

mnist = tf.keras.datasets.mnist # Dataset of 60,000 handwritten digits
(x_train, y_train), (x_test, y_test) = mnist.load_data() # Loads and splits data (90:10)