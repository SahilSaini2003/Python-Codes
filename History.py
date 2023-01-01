import csv
import pandas as pd
with open ('History.csv','w',newline='') as f:
    d=csv.writer(f)
    a=[['Transection ID','User Name','Transection Amount','Amount Type','MobileNo./K.No./E-Mitra CID Code','Date']]
    for r in a:
        d.writerow(r)
