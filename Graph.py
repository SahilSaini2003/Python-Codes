import csv
with open('Graph.csv','w',newline='')as f:
    d=csv.writer(f)
    a=[['Profit Amount per Transection','Month']]
    for r in a:
        d.writerow(r)
