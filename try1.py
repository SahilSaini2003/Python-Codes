import csv
import pandas as pd
jp=pd.read_csv('Jio plans.csv')
#print(jp)
pa=input("Plan costs")
d=(jp[jp['Cost']==pa].index.values)
#jp2=jp.get(2,jp[Validity])
print(jp.loc[d])
