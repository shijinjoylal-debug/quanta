import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

#input data (patterns)
x=np.array([[0,0],[0,1],[1,0],[1,1]])
#output data (labels)
y=np.array([0,1,1,0])
#create neural network
model=Sequential([
    Dense(8,activation='relu',input_shape=(2,)),#hidden layer
    Dense(4,activation='relu'),
#hidden layer
    Dense(1,activation='sigmoid')
#output layer
])
#compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
#train the model
model.fit(x,y,epochs=5000,verbose=0)
#test the network
predictions=model.predict(x)
print("predictions:")
for inp,pred in zip(x,predictions):
    print(f"{inp} -> {round(float(pred))}")
#load data
(x_train,y_train),(x_test,y_test)=mnist.load_data()
#normalize
x_train=x_train/255.0
x_test=x_test/255.0
#one-hot encoding
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)
#model
model=Sequential([
    Flatten(input_shape=(28,28)),
    Dense(128,activation='relu'),
    Dense(64,activation='relu'),
    Dense(10,activation='softmax')
])
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train,y_train,epochs=7)
model.evaluate(x_test,y_test)
model.save("digit_model.h5")



