# How to Handle Duplicate Data?

import pandas as pd

data={"name":["a","b","c","d","a","c"],"maths":[8,7,5,8,8,4],"hindi":[2,3,4,5,2,6]}

df=pd.DataFrame(data)

# df["duplicate"]=df.duplicated()

# print(df)
print(df.drop_duplicates())