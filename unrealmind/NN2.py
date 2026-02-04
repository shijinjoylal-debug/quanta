import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
x=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([0,1,1,0])
model=Sequential([
Dense(8,activation='relu',input_shape=(2,)),
Dense(1,activation='sigmoid')])
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x,y,epochs=500,verbose=0)
print(model.predict(x))

x=np.array([[1.0],[1.2],[1.8]])
proportions=np.array([0.068,0.268,0.868])
for i in range(len(proportions)):
    print(proportions[i])
model=Sequential([
Dense(8,activation='relu',input_shape=(1,)),
Dense(1,activation='sigmoid')])
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x,proportions,epochs=500,verbose=0)
print(model.predict(x))