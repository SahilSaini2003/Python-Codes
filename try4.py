import csv
import numpy as np
import pandas as pd
udf=pd.read_csv('User.csv')
b=np.array(udf)
usi=input("Enter User id/Email-Address")
data=(udf[udf['User Id']==usi].index.values)
#usn=(udf.loc[data,'User Name']) 
#print("Welcome",usn)
#print(data)
#c=(*data)
#print(c)
r=b[data,2]
#r=np.where(b=="Superdon")
print(*r)

