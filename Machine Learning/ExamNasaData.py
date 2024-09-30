import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
import tensorflow as tf

climateData = pd.read_csv('Rainfall_data.csv')
print(climateData.head())
print(climateData.info())
print(climateData.describe())

climateData.fillna(method='ffill',inplace=True)



sb.lineplot(x='Year',y='Specific Humidity',data=climateData)
plt.title("Year and Humidity")
plt.xlabel('Year')
plt.ylabel('Humidity')
plt.xticks(ticks=climateData['Year'].unique())
plt.title('Year and humidity')
plt.show()

X = climateData.drop(columns=['Year'])
y = climateData['Specific Humidity']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=40)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64,activation='relu',input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam',loss='mean_squared_error')
model.fit(X_train,y_train,epochs=100,validation_split=0.2)

loss = model.evaluate(X_test,y_test)
print(f'Test Loss: {loss}')

predict = model.predict(X_test)

plt.scatter(y_test,predict)
plt.xlabel('True values')
plt.ylabel('predictions')
plt.title("Predictions")
plt.show()