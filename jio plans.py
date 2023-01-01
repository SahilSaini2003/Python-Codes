import csv
with open ('Jio plans.csv','w',newline='')as f:
    d=csv.writer(f)
    a=[['Data/day','Taketime/day','Sms/day','Valibity','Cost in Rs.'],['1gb','500min','50','34 Days','200'],['1.5gb','1000min','100','54 Days','300'],['2gb','Unlimited','200','70 Days','499']]
    for r in a:
        d.writerow(r)
