# Handling Missing Values (Scikit-Learn)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn as sk

dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")
# print(dataset)

# 2) Filling Numerical Missing Data

print(dataset.select_dtypes(include="float64").columns)

from sklearn.impute import SimpleImputer

si=SimpleImputer(strategy="mean")
ar=si.fit_transform(dataset[['Age', 'Salary']])

print(pd.DataFrame(ar,columns=dataset.select_dtypes(include="float64").columns))

