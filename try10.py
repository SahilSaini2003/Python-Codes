import csv
import pandas as pd
df=pd.read_csv('try2.csv')
a=(df['Money'])*0.01
print(a)
