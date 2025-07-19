# How to Replace and Change Data Types?

import pandas as pd

dataset=dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

# print(dataset.info())

dataset["Dependents"].replace("3+","3",inplace=True)

dataset["Dependents"]=dataset["Dependents"].astype("int64")

# print(dataset.info())
print(dataset)
