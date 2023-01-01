import csv
with open('User.csv','w',newline='')as f:
    d=csv.writer(f)
    a=[['User Id','User Name','Password','Mobile No.','D.O.B','User login Date']]
    for r in a:
        d.writerow(r)
        
