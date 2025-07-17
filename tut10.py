# How to Remove Outliers using Z Score?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset=dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

dataset["Age"].fillna(dataset["Age"].mode()[0])

min_range=(dataset["Age"].mean()) - (3*dataset["Age"].std())
max_range=(dataset["Age"].mean()) + (3*dataset["Age"].std())

# print(min_range)
# print()
# print(max_range)

new_dataset=dataset[dataset["Age"] <= max_range]

sns.boxplot(x="Age",data=new_dataset)
plt.show()
