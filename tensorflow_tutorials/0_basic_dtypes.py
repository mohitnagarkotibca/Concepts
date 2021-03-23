import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
k = tf.constant([
    [1, 0, 1],
    [2, 1, 0],
    [0, 0, 1]
], dtype=tf.float32, name='k')


i = tf.constant([
    [4, 3, 1, 0],
    [4, 1, 1, 0],
    [4, 2, 4, 0],
    [4, 1, 1, 0]
], dtype=tf.float32, name='i')

plt.imshow(i.numpy())
# [batch, in_height, in_width, in_channels]
image  = tf.reshape(i, [1, 4, 4, 1], name='image')

#[filter_height, filter_width, in_channels, out_channels]
kernel = tf.reshape(k, [3, 3, 1, 1], name='kernel')

import numpy as np
plt.imshow(np.matrix(tf.nn.conv2d(image, kernel, [1, 1, 1, 1], "VALID").numpy()))