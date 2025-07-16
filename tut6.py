# What is Label Encoding?

import pandas as pd

df=pd.DataFrame({"name":["cat","black","dog","cow","boy"]})

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

df["en_name"]=le.fit_transform(df["name"])
# print(df)

dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

dataset["City"].fillna(dataset["City"].mode()[0],inplace=True)

li=LabelEncoder()
dataset["City"]=li.fit_transform(dataset["City"])
print(dataset)
