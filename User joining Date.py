import csv
with open('User Joining Details.csv','w',newline='')as f:
    d=csv.writer(f)
    a=[['Month','User Joining date']]
    for r in a:
        d.writerow(r)
        
