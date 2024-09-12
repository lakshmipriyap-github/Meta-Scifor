import pandas
import pandas as pd

dataCsv = pd.read_csv('data.csv')
print(dataCsv)
#
# print("count:",dataCsv.count())
# print("shape:",dataCsv.shape)
# print("columns:",dataCsv.columns)
# print("Info:",dataCsv.info())
# print("head:",dataCsv.head(2))
# print("tail:",dataCsv.tail(1))
# print("is null:",dataCsv.isnull())
# print("sum of null:",dataCsv.isnull().sum())

dataCsv.dropna(inplace=True)
print(dataCsv)