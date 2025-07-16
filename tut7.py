# What is Ordinal Encoding?

import pandas as pd

df=pd.DataFrame({"size":["s","m","l","xl","s","l","s","xl","m"]})
# print(df)

ord_data=[["s","m","l","xl"]]

from sklearn.preprocessing import OrdinalEncoder

le=OrdinalEncoder(categories=ord_data)

df["en_size"]=le.fit_transform(df[["size"]])

print(df)



dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")


dataset["Area"].unique()

dataset["Area"].fillna(dataset["Area"].mode()[0])

# print(dataset["Area"].unique())

ord_area=[['Urban' 'Semi urban' 'Rural']]

from sklearn.preprocessing import OrdinalEncoder

li=OrdinalEncoder()

dataset["Area"]=li.fit_transform(dataset[["Area"]])

print(dataset)



