# One Hot Encoding & Dummy Variables

import pandas as pd

dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")
# print(dataset)
dataset["Gender"].fillna(dataset["Gender"].mode()[0],inplace=True)
# dataset["Name"].fillna(dataset["Name"].mode()[0],inplace=True)
# dataset["City"].fillna(dataset["City"].mode()[0],inplace=True)
# dataset["Email"].fillna(dataset["Email"].mode()[0],inplace=True)
# dataset["Age"].fillna(dataset["Age"].mode()[0],inplace=True)
# dataset["Salary"].fillna(dataset["Salary"].mode()[0],inplace=True)


en_data=dataset[["Gender"]]
# print(pd.get_dummies(en_data))

from sklearn.preprocessing import OneHotEncoder

ohe=OneHotEncoder()
ar=ohe.fit_transform(en_data).toarray()
print(pd.DataFrame(ar,columns=["Gender_Male","Gender_Female"]))


