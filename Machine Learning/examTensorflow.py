import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
import tensorflow as tf

dataraw = pd.read_csv("literacy_rates.csv")
# print(dataraw.head())
# print(dataraw.info())
# print(dataraw.describe())

dataraw.fillna(method='ffill',inplace=True)

dataraw.rename(columns={'Country/ States/ Union Territories Name' : 'States',
                        'Literacy Rate (Persons) - Total - 2011' : '2011_Total',
                        'Literacy Rate (Persons) - Rural - 2011' : '2011_Rural',
                        'Literacy Rate (Persons) - Urban - 2011' : '2011_Urban'
                        },
                        inplace=True)
# print(dataraw.info())
# print(dataraw['States'].unique())

# # using seaborn and pyplot for visualizing
# plt.figure(figsize=(12,6))
sb.barplot(x='States',y='2011_Total',data=dataraw)
plt.xticks(rotation=90)
plt.title("Literacy Rates of Indian States of Year 2011")
plt.show()

X = dataraw[['2011_Total']]
y = dataraw['2011_Rural']

X_train , X_test , y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=32)

X_train = tf.convert_to_tensor(X_train,dtype=tf.float32)
X_test = X_train = tf.convert_to_tensor(X_test,dtype=tf.float32)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10,activation='relu',input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam',
              loss='mean_squared_error')


model.fit(X_train,y_train, epochs=50,batch_size=10,validation_split =0.2)

loss = model.evaluate(X_test,y_test)
print(f'Test Loss: {loss: .2f}')

predictions = model.predict(X_test)