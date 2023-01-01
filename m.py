import csv
import pandas as pd
with open('math2.csv','w',newline='') as f:
    d=csv.writer(f)
    a=[['formula','F.expension'],['Cos (x+y)','cos x.sin y – sin x.cos y'],['Cos (x-y)','cos x.sin y + sin x.cos y']]
    for r in a:
        d.writerow(r)
       

        
        
