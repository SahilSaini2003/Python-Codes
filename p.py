import pandas as pd
a={'Name':pd.Series(['a','b','c','d'],index=[1,2,3,4]),'Age':pd.Series([10,12,11,12],index=[1,2,3,4])}
b=pd.DataFrame(a)
print("Given Dataframe=",b)
print("Changed Dataframe=")
b['Age'].replace([1],12)
print(b)
