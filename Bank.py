import csv
import pandas as pd
with open('Bank.csv','w',newline='')as f:
    d=csv.writer(f)
    a=[["User Id","Password","Card No.","Expiry/Validity No.","CVV No.","PIN","Debit/Credit Card"]]
    for r in a:
        d.writerow(r)
        
