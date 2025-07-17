# What is an Outlier and How to Handle It?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset=dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

print(dataset.describe())

sns.boxplot(x="Age",data=dataset)

sns.distplot(dataset["Age"])

plt.show()