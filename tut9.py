# How to Remove Outliers using IQR?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset=dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")
dataset["Age"].fillna(dataset["Age"].mode()[0])

q1=dataset["Age"].quantile(0.25)
q3=dataset["Age"].quantile(0.75)

iqr=q3-q1

min_range=q1-(1.5*iqr)
max_range=q1+(1.5*iqr)

# print(min_range)
# print()
# print(max_range)

new_dataset=dataset[dataset["Age"] <= max_range]

sns.boxplot(x="Age",data=new_dataset)
plt.show()