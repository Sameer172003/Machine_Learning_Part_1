# Handling Missing Values (Dropping)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

print(dataset.shape)
print()
print(dataset.isnull().sum())
print()

# If we want to delete the whole data of a particular column

print(dataset.drop(columns="Email",inplace=True))
print()
print(dataset.shape)

# If we want to delete the data of a all rows which have missing values

print(dataset.dropna(inplace=True))
print(dataset.isnull().sum())
print()
print(dataset.shape)

sns.heatmap(dataset.isnull())

plt.show()