# What is missing value and how to find it

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")


print(dataset.shape)
print()
print(dataset.isnull().sum())
print()
print(dataset.isnull().sum().sum())
print()
print((dataset.isnull().sum().sum()/(dataset.shape[0]*dataset.shape[1]))*100)
print()
print((dataset.isnull().sum()/(dataset.shape[0]))*100)

# sns.heatmap(dataset.isnull())

# plt.show()