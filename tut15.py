# Function Transformer

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset=dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")

dataset["Age"].fillna(dataset["Age"].mode()[0],inplace=True)

q1=dataset["Age"].quantile(0.25)
q3=dataset["Age"].quantile(0.75)
iqr=q3-q1

min_r=q1-(1.5*iqr)
max_r=q1+(1.5*iqr)

dataset=dataset[dataset["Age"] <= max_r]

# sns.distplot(dataset["Age"])
# plt.show()

from sklearn.preprocessing import FunctionTransformer

ft=FunctionTransformer(func=np.log1p)

dataset["Age_tf"]=ft.fit_transform(dataset[["Age"]])

plt.subplot(1,2,1)
sns.distplot(dataset["Age"])
plt.title("Before")

plt.subplot(1,2,2)
sns.distplot(dataset["Age_tf"])
plt.title("After")

plt.show()
