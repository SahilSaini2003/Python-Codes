import csv
import pandas as pd
import numpy as np
df=pd.read_csv("History.csv")
a=df.tail(1)
print(a)
a1=np.array(a)
a2=a1[0,0]
print(a2)

a3=a2+1
print(a3)
