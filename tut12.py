# What is Feature Scaling (Normalization)?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")
# print(dataset)
dataset["Age"].fillna(dataset["Age"].mode()[0],inplace=True)

from sklearn.preprocessing import MinMaxScaler
ms=MinMaxScaler()

dataset["Age_ms"]=pd.DataFrame(ms.fit_transform(dataset[["Age"]]),columns=["X"])

plt.subplot(1,2,1)
plt.title("Before")
sns.distplot(dataset["Age_ms"])

plt.subplot(1,2,2)
plt.title("After")
sns.distplot(dataset["Age"])

plt.show()

