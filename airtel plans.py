import csv
with open ('Airtel plans.csv','w',newline='')as f:
    d=csv.writer(f)
    a=[['Data/day','Taketime/day','Sms/day','Valibity','Cost in Rs.'],['1gb','Unlimited','50','28 Days','219'],['1.5gb','Unlimited','100','56 Days','399'],['2gb','Unlimited','100','56 Days','449']]
    for r in a:
        d.writerow(r)
