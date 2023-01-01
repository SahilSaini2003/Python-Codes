import csv
import pandas as pd
p="100"
pa="Rechage"
op="Jio"
d=pa+"-"+op
print(d)
hf=pd.read_csv('History.csv')
a={"Amount of Transection":[p],"Amount Type":[d]}
hf1=pd.DataFrame(a)
print(hf1)
hf2=hf.append(hf1)
hf2.to_csv('History.csv',index=False)
hf=pd.read_csv('History.csv')
print(hf)
