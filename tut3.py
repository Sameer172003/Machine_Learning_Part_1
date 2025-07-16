# Handling Missing Values (Imputing category data)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

print(dataset.isnull().sum())
print()

# Direct and wrong way to fill missing data 

print(dataset.fillna(39))

print()

# Correct way to fill missing data according to its variables

# 1) Filling Categorical Missing Data

print(dataset.info())

print(dataset.fillna(method="bfill"))
print(dataset.fillna(method="bfill"),axis=1)
print(dataset.fillna(method="bfill"),axis=0)
print(dataset.fillna(method="ffill"))
print(dataset.fillna(method="ffill"),axis=1)
print(dataset.fillna(method="ffill"),axis=0)

# Fill missing data by using mode in categorical variables

for i in dataset.select_dtypes(include="object").columns:
    dataset[i].fillna(dataset[i].mode()[0],inplace=True)

print(dataset)