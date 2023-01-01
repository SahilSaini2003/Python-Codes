import csv
with open('Admin.csv','w', newline='') as f:
    d=csv.writer(f)
    a=[['Admin','Password'],['Sahil','sah'],['Aman','ama']]
    for r in a:
        d.writerow(r)
