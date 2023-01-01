import csv
import pandas as pd
z=1
while(z==1):
    print("1.Recharge")
    print("2.Pay Bills")
    uc1=int(input("Enter Your choice"))
    if(uc1==1):
        print("1.Mobile")
        print("2.D.T.H")
        re=int(input("Enter choice"))
        if(re==1):
            print("Available Operator")
            print("1.Jio")
            print("2.Vodafone")
            print("3.Airtel")
            op=int(input("Enter operator no"))
            if(op==1):
                print("Plans available")
                jp=pd.read_csv('Jio plans.csv')
                print(jp)
                pa=int(input("Plan costs"))
                d=(jp[jp['Cost in Rs.']==pa].index.values)
                print(jp.loc[d])
                print("Pay=",pa)
                pay=input("y/n")
                y=0
                if(pay=="y"):
                    z=0
                    y=1
                else:
                    print("Thanks")
