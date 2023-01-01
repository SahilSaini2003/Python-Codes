import csv
with open ('Vodafone plans.csv','w',newline='')as f:
    d=csv.writer(f)
    a=[['Data/day','Taketime/day','Sms/day','Valibity','Cost in Rs.'],['1gb','Unlimited','100','28 Days','219'],['1.5gb','Unlimited','100','28 Days','249'],['3gb','Unlimited','100','56 Days','399']]
    for r in a:
        d.writerow(r)
