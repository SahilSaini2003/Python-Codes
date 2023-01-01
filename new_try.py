from asyncio import as_completed
import pandas as pd
import numpy as np
def wrong_details():
    print("\t\t\t           OOPS! User not found")
    print("\t\t< Weather You entered Wrong Name/Password or User Not Present >")
def user_check(usi,pas):
    global i,w,x
    udf=pd.read_excel(r'User.xlsx')
    udf2=udf[(udf['User Id']==usi) & (udf['Password']==pas)]
    if(udf2.empty):
        wrong_details()
        i=0
        w=1
    else:
        i=0
        w=0
        x=1
        data=(udf[udf['User Id']==usi].index.values)
        b=np.array(udf)
        usn=b[data,1]
        print("\t\t\t\t Hurray ! We got You")
        print("\t\t\t\t      Welcome",*usn,"!")
w=1
i=0
x=0
while(w==1):
    print("\t\t\t    # 1.Log in with User Id/Email-Address #")
    print("\t\t\t             # 2.Log in with Mobile no. #")
    c=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
    if(c==1):
        usi=input("\t\t\t  Enter User id/Email-Address:-")
        pas=input("\t\t\t\t Enter Password:-")
        user_check(usi,pas)
        print("Going Right")
    # elif(c==2):
    #     mo=int(input("\t\t\t\t Enter Mobile no.:-"))
    #     pas=input("\t\t\t\t Enter Password:-")
    #     udf=pd.read_excel(r'User.xlsx')
    #     udf2=udf[(udf['Mobile No.']==mo) & (udf['Password']==pas)]
    #     if(udf2.empty):
    #         w=1
    #         i=0
    #         m=0
    #         print("\t\t\t           OOPS! User not found")
    #         print("\t\t< Weather You entered Wrong Name/Password or User Not Present >")
    #     else:
    #         x=1
    #         i=0
    #         w=0
    #         m=0
    #         data=(udf[udf['Mobile No.']==mo].index.values)
    #         b=np.array(udf)
    #         usn=b[data,1]
    #         print("\t\t\t\t Hurray ! We got You")
    #         print("\t\t\t\t      Welcome",*usn,"!")