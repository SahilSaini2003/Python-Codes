import csv
import pandas as pd
a=pd.DataFrame([['32.26','October'],['79.27','November'],['69.1','December'],['7.99','January']],columns=['Profit Amount per Transection','Month'])
print(a)
a.to_csv('Graph.csv')
