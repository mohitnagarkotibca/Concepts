import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, BatchNormalization, Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train= pd.read_csv('data/train.csv')
test= pd.read_csv('data/test.csv')

X= train.drop('label',axis=1)
y= train['label']

def display_image(X,i):    
    plt.imshow(np.matrix(X.iloc[i].values.reshape(28,28,1)))
    plt.show()

from sklearn.model_selection import train_test_split

train_x,val_x,train_y,val_y= train_test_split(X,y)

model= tf.keras.Sequential([
    Dense(units=32,input_shape=(784,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(x= train_x,y= train_y,validation_split=0.2,epochs=10)
model.evaluate(x= val_x,y= val_y)

predictions= np.argmax(model.predict(val_x), axis=-1)

test.iloc[0]
np.argmax(predictions[0])

li=[]
for i in range(1000):
    if val_y.iloc[i] != predictions[i]:
        li.append(val_y.iloc[i])
li= pd.Series(li)

from sklearn.metrics import 