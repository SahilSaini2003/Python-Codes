import pandas as pd
import csv
df=pd.read_csv("Admin.csv")
#print(df)
a=input("Name")
z=(df[df['Admin']==a].index.values)
print("\t\t\t\t",df.values)
s=pd.Series(df)
print(s)

