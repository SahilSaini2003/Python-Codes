import pandas as pd
MINUTES=(40,50,35,50,40)
a=pd.Series(MINUTES,index=['Series1','Series2','Series3','Series4','Series5'],columns=['MINUTES'])
#a.index=['Series1','Series2','Series3','Series4','Series5']
#a.column=['MINUTES']
print(a)
