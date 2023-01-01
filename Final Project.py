import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import date
print("-:-:-:-:-Welcome to S.A.S Online Transactions-:-:-:-:-")
m=1
while(m==1):
    print("1.Admin")
    print("2.User")
    a=int(input("Enter your choice"))
    if(a==1):
            ad=input("Enter Admin Name")
            pa=input("Enter Password")
            df=pd.read_csv('Admin.csv')                                                       
            df1=df[(df['Admin']==ad) & (df['Password']==pa)]
            if(df1.empty):
                print("Admin Not Exists")
                print("Please Enter Correct Details")
                m=1
            else:
                q=1
                print("Welcome",ad)
                while(q==1):
                    print("What do you want to check")
                    print("1.Admin list")
                    print("2.User list")
                    print("3.Check profit")
                    b=int(input("Enter your choice"))
                    if(b==1):
                        w=1
                        while(w==1):
                            print("1.Admin details")
                            print("2.Add Admin")
                            print("3.Remove Admin")
                            print("4.Change Password")
                            c=int(input("Enter your choice"))
                            if(c==1):
                                print(df)
                                q=0
                                w=0
                            elif(c==2):
                                adn=input("Enter Admin Name")
                                Pass=input("Enter Password")
                                df2=pd.read_csv('Admin.csv')
                                data={"Admin":[adn],"Password":[Pass]}
                                df3=pd.DataFrame(data)
                                df4=df2.append(df3)
                                df4.to_csv('Admin.csv',index=False)
                                df4=pd.read_csv('Admin.csv')
                                q=0
                                w=0
                                print(df4)
                            elif(c==3):
                                add=input("Enter Admin you want to Delete")
                                df2=pd.read_csv('Admin.csv')
                                df3=df2[df2['Admin']==add]
                                if(df3.empty):
                                    q=0
                                    w=1
                                    print("Not Found")
                                    print("Admin not exists")
                                else:
                                    print("Admin exists")
                                    data=(df2[df2['Admin']==add].index.values)
                                    df2=df2.drop(data)
                                    df2.to_csv('Admin.csv',index=False)
                                    df2=pd.read_csv('Admin.csv')
                                    q=0
                                    w=0
                                    print(df2)
                            elif(c==4):
                                adnp=input("Admin name whose password you want to change")
                                df2=pd.read_csv('Admin.csv')
                                df3=df2[df2['Admin']==adnp]
                                if(df3.empty):
                                    q=0
                                    w=1
                                    print("Admin not exists")
                                else:
                                    w=0
                                    q=0
                                    pas=input("Enter Password")
                                    d=(df2[df2['Admin']==adnp].index.values)
                                    df2.loc[d,["Password"]]=pas
                                    df2.to_csv('Admin.csv',index=False)
                                    print(df2)
                            else:
                                w=1
                                q=0
                                print("Choose correct option")
                            if(w==0):
                                cho=input("Do You want to do anything else y/n")
                                if(cho=="y"):
                                    q=1
                                else:
                                    q=0
                                    print("Thanks")
                    elif(b==2):
                        w=1
                        while(w==1):
                            print("1.User Details")
                            print("2.Ban/Remove User")
                            print("3.User Joining Graph")
                            u=int(input("Enter your choice"))
                            if(u==1):
                                dfu=pd.read_csv('User.csv')
                                print(dfu)
                                w=0
                                q=0
                            elif(u==2):
                                usr=input("Enter User Name you want to Ban")
                                df2=pd.read_csv('User.csv')
                                df3=df2[df2['User Name']==usr]
                                if(df3.empty):
                                    print("User not exists")
                                    print("Enter Correct User Name")
                                    w=1
                                    q=0
                                else:
                                    w=0
                                    q=0
                                    print("User exists")
                                    print("Are you sure you want to ban",usr)
                                    s=input("y/n")
                                    if(s=="y"):
                                        data=(df2[df2['User Name']==usr].index.values)
                                        df2=df2.drop(data)
                                        print("Banned Successfully")
                                        df2.to_csv('User.csv',index=False)
                                        df2=pd.read_csv('User.csv')
                                        print(df2)
                                    else:
                                        q=0
                                        w=0
                                        print("No-one is banned")
                            elif(u==3):
                                udf=pd.read_csv('User Joining Details.csv')
                                plt.hist(udf['Month'])
                                plt.title("User Joined Per Month",fontsize=15)
                                plt.xlabel("Month",fontsize=10)
                                plt.ylabel("User Joined",fontsize=10)
                                plt.show()
                            else:
                                w=1
                                q=0
                                print("Choose correct option")
                            if(w==0):
                                cho=input("Do You want to do anything else y/n")
                                if(cho=="y"):
                                    q=1
                                else:
                                    q=0
                                    print("Thanks")
                    elif(b==3):
                        grf=pd.read_csv('Graph.csv')
                        print("Check using")
                        print("1.Line graph")
                        print("2.Bar Graph")
                        gh=int(input("Enter choice"))
                        if(gh==1):
                            plt.plot(grf['Month'],grf['Profit Amount per Transection'])
                            plt.title("Profit",fontsize=20)
                            plt.xlabel('Month',fontsize=10)
                            plt.xlabel('Profit made per Month',fontsize=10)
                            plt.show()
                        elif(gh==2):
                            plt.bar(grf['Month'],grf['Profit Amount per Transection'])
                            plt.title("Profit",fontsize=20)
                            plt.xlabel('Month',fontsize=10)
                            plt.xlabel('Profit made per Month',fontsize=10)
                            plt.show()
                    else:
                        print("Choose corrct option")
                        q=1
    elif(a==2):
        m=0
        print("1.New User")
        print("2.Old User")
        x=0
        b=int(input("Enter your choice"))
        i=1
        while(i==1):
            if(b==1):
                lod=date.today()
                mon=lod.month
                if(mon==1):
                    mont="January"
                elif(mon==2):
                    mont="Febuary"
                elif(mon==3):
                    mont="March"
                elif(mon==4):
                    mont="Aparil"
                elif(mon==5):
                    mont="May"
                elif(mon==6):
                    mont="June"
                elif(mon==7):
                    mont="July"
                elif(mon==8):
                    mont="August"
                elif(mon==9):
                    mont="September"
                elif(mon==10):
                    mont="October"
                elif(mon==11):
                    mont="November"
                elif(mon==12):
                    mont="December"
                usi=input("Enter User id/Email-Address")
                usn=input("Enter User name")
                pas=input("Enter Password")
                mo=input("Enter Mobile No.")
                dob=input("Enter D.O.B/Date of birth")
                usf=pd.read_csv('User Joining Details.csv')
                udata={'User Joining date':[lod],'Month':[mont]}
                usf2=pd.DataFrame(udata)
                usf3=usf.append(usf2)
                usf3.to_csv('User Joining Details.csv',index=False)
                df2=pd.read_csv('User.csv')
                data={"User Id":[usi],"User Name":[usn],"Password":[pas],"Mobile No.":[mo],"D.O.B":[dob],"User login Date":[lod]}
                df3=pd.DataFrame(data)
                df4=df2.append(df3)
                df4.to_csv('User.csv',index=False)
                print("Successfully added new user")
                i=1
                if(i==1):
                    b=2
            elif(b==2):
                w=1
                while(w==1):
                    print("1.Log in with User Id/Email-Address")
                    print("2.Log in with Mobile no.")
                    c=int(input("Enter your choice"))
                    if(c==1):
                        usi=input("Enter User id/Email-Address")
                        pas=input("Enter Password")
                        udf=pd.read_csv('User.csv')
                        udf2=udf[(udf['User Id']==usi) & (udf['Password']==pas)]
                        if(udf2.empty):
                            print("User Not Exists")
                            i=0
                            w=1
                        else:
                            i=0
                            w=0
                            x=1
                            data=(udf[udf['User Id']==usi].index.values)
                            b=np.array(udf)
                            usn=b[data,1]
                            print("Welcome",*usn)
                    elif(c==2):
                        mo=int(input("Enter Mobile no."))
                        pas=input("Enter Password")
                        udf=pd.read_csv('User.csv')
                        udf2=udf[(udf['Mobile No.']==mo) & (udf['Password']==pas)]
                        if(udf2.empty):
                            w=1
                            i=0
                            m=0
                            print("Enter Correct Details")
                            print("User Not Exists")
                        else:
                            x=1
                            i=0
                            w=0
                            m=0
                            data=(udf[udf['Mobile No.']==mo].index.values)
                            b=np.array(udf)
                            usn=b[data,1]
                            print("Welcome",*usn)
                    else:
                        w=1
                        i=0
                        m=0
                        print("Choose corret option")
            else:
                m=0
                x=1
                print("Choose correct option")
    else:
        m=1
        print("Choose correct option")
if(x==1):
    q=1
    while(q==1):
        print("1.Personal Changes")
        print("2.Online Transection")
        print("3.Transection History")
        uc=int(input("Enter your choice"))
        w=1
        while(w==1):
            if(uc==1):
                print("1.Change Password")
                print("2.Change User Id/Email-Address")
                print("3.Change Mobile No.")
                uc1=int(input("Enter your choice"))
                if(uc1==1):
                    usn=input("Enter User Name")                        
                    dob=input("Enter D.O.B")
                    udf=pd.read_csv('User.csv')
                    udf1=udf[(udf['User Name']==usn) & (udf['D.O.B']==dob)]
                    if(udf1.empty):
                        w=1
                        q=0
                        print("User not exists")
                    else:
                        w=0
                        pas=input("Enter New Password")
                        d=(udf[udf['User Name']==usn].index.values)
                        udf.loc[d,["Password"]]=pas
                        udf.to_csv('User.csv',index=False)
                        print("Successfully changed")
                        q=1
                elif(uc1==2):
                    usn=input("Enter User Name")
                    pas=input("Enter Password")
                    udf=pd.read_csv('User.csv')
                    udf2=udf[(udf['User Name']==usn) & (udf['Password']==pas)]
                    if(udf2.empty):
                        w=1
                        q=0
                        print("User not exists")
                    else:                               
                        w=0
                        usi=input("Enter New User Id/Email-Address")
                        d=(udf[udf['User Name']==usn].index.values)
                        udf.loc[d,["User Id"]]=usi
                        udf.to_csv('User.csv',index=False)
                        print("Successfully Changed")
                        q=1
                elif(uc1==3):
                    usi=input("Enter User Id/Email-Address")
                    pas=input("Enter Password")
                    udf=pd.read_csv('User.csv')
                    udf2=udf[(udf['User Id']==usi) & (udf['Password']==pas)]
                    if(udf2.empty):
                        w=1
                        q=0
                        print("User not exists")
                    else:
                        w=0
                        mo=int(input("Enter New Mobile No."))
                        d=(udf[udf['User Id']==usi].index.values)
                        udf.loc[d,["Mobile No."]]=mo
                        udf.to_csv('User.csv',index=False)
                        print("Successfully Changed")
                        q=1
                else:
                    w=0
                    q=1
                    print("Choice not available")
                    print("Choose correct option")
            elif(uc==2):
                w=0
                q=0
                s=1
                dat=date.today()
                mon=dat.month
                if(mon==1):
                    mont="January"
                elif(mon==2):
                    mont="Febuary"
                elif(mon==3):
                    mont="March"
                elif(mon==4):
                    mont="Aparil"
                elif(mon==5):
                    mont="May"
                elif(mon==6):
                    mont="June"
                elif(mon==7):
                    mont="July"
                elif(mon==8):
                    mont="August"
                elif(mon==9):
                    mont="September"
                elif(mon==10):
                    mont="October"
                elif(mon==11):
                    mont="November"
                elif(mon==12):
                    mont="December"
                while(s==1):
                    print("1.Recharge")
                    print("2.Pay Bills")
                    uc1=int(input("Enter your Choice"))
                    grf=pd.read_csv('Graph.csv')
                    if(uc1==1):
                        uc1="Recharge"
                        us=pd.read_csv('User.csv')
                        usn=input("Enter your User Name")
                        dr=us[(us['User Name']==usn)]
                        if(dr.empty):
                            print("User Name Not Exists")
                            q=1
                        else:
                            print("1.Mobile")
                            print("2.DTH")
                            re=int(input("Enter your Choice"))
                            if(re==1):
                                s=0
                                no=int(input("Enter Mobile No."))
                                print("Available Operator")
                                print("1.Jio")
                                print("2.Vodafone")
                                print("3.Airtel")
                                op=int(input("Enter operator no"))
                                if(op==1):
                                    op="Jio"
                                    print("Plans available")
                                    jp=pd.read_csv('Jio plans.csv')
                                    print(jp)
                                    pa=int(input("Plan costs"))
                                    d=(jp[jp['Cost in Rs.']==pa].index.values)
                                    print(jp.loc[d])
                                    amg=pa*0.01
                                    gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                    gf1=pd.DataFrame(gr)
                                    gf2=grf.append(gf1)
                                    gf2.to_csv('Graph.csv',index=False)
                                    print("Pay=",pa)
                                    pay=input("y/n")
                                    y=0
                                    if(pay=="y"):
                                        s=0
                                        y=1
                                    else:
                                        print("Thanks")
                                    at=uc1+"-"+op
                                    hf=pd.read_csv('History.csv')
                                    a={"User Name":[usn],"Transection Amount":[pa],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                    hf1=pd.DataFrame(a)
                                    hf2=hf.append(hf1)
                                    hf2.to_csv('History.csv',index=False)
                                elif(op==2):
                                    op="Vodafone"
                                    print("1.Prepaid")
                                    print("2.Postpaid")
                                    pp=int(input("Choose option"))
                                    if(pp==1):
                                        print("Plans available")
                                        jp=pd.read_csv('Vodafone plans.csv')
                                        print(jp)
                                        pa=int(input("Plan costs"))
                                        d=(jp[jp['Cost in Rs.']==pa].index.values)
                                        print(jp.loc[d])
                                        print("Pay=",pa)
                                        amg=pa*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        pay=input("y/n")
                                        y=0
                                        if(pay=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[pa],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    elif(pp==2):
                                        am=int(input("Enter Amount to Pay in Rupees"))
                                        print("Pay=",am)
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        pay=input("y/n")
                                        y=0
                                        if(pay=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                elif(op==3):
                                    op="Airtel"
                                    print("1.Prepaid")
                                    print("2.Postpaid")
                                    pp=int(input("Choose option"))
                                    if(pp==1):
                                        print("Plans available")
                                        jp=pd.read_csv('Airtel plans.csv')
                                        print(jp)
                                        pa=int(input("Plan costs"))
                                        d=(jp[jp['Cost in Rs.']==pa].index.values)
                                        print(jp.loc[d])
                                        print("Pay=",pa)
                                        amg=pa*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        pay=input("y/n")
                                        y=0
                                        if(pay=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[pa],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    elif(pp==2):
                                        am=int(input("Enter Amount to Pay in Rupees"))
                                        print("Pay=",am)
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        pay=input("y/n")
                                        y=0
                                        if(pay=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                            elif(re==2):
                                w=0
                                q=0
                                s=0
                                print("Available Operator")
                                print("1.D2h Videocon")
                                print("2.Tata Sky")
                                print("3.Dish Tv")
                                to=int(input("Choose Operator no."))
                                if(to==1):
                                    op="D2h Videocon"
                                    print("1.Pay Using Registered Mobile No.(10 digits)")
                                    print("2.Pay Using Customer Id(7 Digits)")
                                    to1=int(input("Enter Choice"))
                                    if(to1==1):
                                        no=int(input("Enter Registered Mobile No.(10 digits)"))
                                        print("Confirm",no)
                                        z=input("y/n")
                                        if(z=="y"):
                                            y=0
                                            am=int(input("Enter Amount"))
                                            print("Pay=",am)
                                            amg=am*0.01
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            r=input("y/n")
                                            if(r=="y"):
                                                y=1
                                            else:
                                                print("Thanks")
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                    elif(to1==2):
                                        no=int(input("Enter Customer Id(7 Digits)"))
                                        print("Confirm",no)
                                        z=input("y/n")
                                        if(z=="y"):
                                            y=0
                                            am=int(input("Enter Amount"))
                                            print("Pay=",am)
                                            amg=am*0.01
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            r=input("y/n")
                                            if(r=="y"):
                                                y=1
                                            else:
                                                print("Thanks")
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)                                       
                                        else:
                                            print("Thanks")
                                elif(to==2):
                                    op="Tata Sky"
                                    no=int(input("Enter Customer Id(10 Digits)"))
                                    print("Confirm",no)
                                    z=input("y/n")
                                    if(z=="y"):
                                        y=0
                                        am=int(input("Enter Amount"))
                                        print("Pay=",am)
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        r=input("y/n")
                                        if(r=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    else:
                                        print("Thanks")
                                elif(to==3):
                                    op="Dish Tv"
                                    print("Pay Using Customer Id(12 Digits)")
                                    no=int(input("Enter Customer Id(12 Digits)"))
                                    print("Confirm",no)
                                    z=input("y/n")
                                    if(z=="y"):
                                        y=0
                                        am=int(input("Enter Amount"))
                                        print("Pay=",am)
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        r=input("y/n")
                                        if(r=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                    elif(uc1==2):
                        w=0
                        q=0
                        s=0
                        uc1="Bills Payment"
                        us=pd.read_csv('User.csv')
                        usn=input("Enter your User Name")
                        dr=us[(us['User Name']==usn)]
                        if(dr.empty):
                            print("User Name Not Exists")
                            q=1
                        else:
                            print("1.Electricity Bills")
                            print("2.Water Bills")
                            print("3.Money Transfer")
                            bi=int(input("Enter Bills Choice"))
                            if(bi==1):
                                op="Electricity Bills"
                                print("Available Boards")
                                print("JVVNL")
                                no=int(input("Enter K.No"))
                                print(" Confirm K.No.=",no)
                                r=input("y/n")
                                if(r=="y"):
                                    y=0
                                    am=int(input("Enter amount"))
                                    print("Pay=",am)
                                    amg=am*0.01
                                    gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                    gf1=pd.DataFrame(gr)
                                    gf2=grf.append(gf1)
                                    gf2.to_csv('Graph.csv',index=False)
                                    p=input("y/n")
                                    if(p=="y"):
                                        y=1
                                    else:
                                        print("Thanks")
                                    at=uc1+"-"+op
                                    hf=pd.read_csv('History.csv')
                                    a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                    hf1=pd.DataFrame(a)
                                    hf2=hf.append(hf1)
                                    hf2.to_csv('History.csv',index=False)
                                else:
                                    print("Thanks")
                            elif(bi==2):
                                op="Water Bills"
                                print("Available Boards")
                                print("PHED")
                                no=int(input("Enter E-Mitra CID Code"))
                                print(" Confirm E-Mitra CID Code=",no)
                                r=input("y/n")
                                if(r=="y"):
                                    y=0
                                    am=int(input("Enter amount"))
                                    print("Pay=",am)
                                    amg=am*0.01
                                    gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                    gf1=pd.DataFrame(gr)
                                    gf2=grf.append(gf1)
                                    gf2.to_csv('Graph.csv',index=False)
                                    p=input("y/n")
                                    if(p=="y"):
                                        y=1
                                    else:
                                        print("Thanks")
                                    at=uc1+"-"+op
                                    hf=pd.read_csv('History.csv')
                                    a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                    hf1=pd.DataFrame(a)
                                    hf2=hf.append(hf1)
                                    hf2.to_csv('History.csv',index=False)
                                else:
                                    print("Thanks")
                            elif(bi==3):
                                op="Money Transfer" 
                                print("1.Using Bank Account no.")
                                print("2.Using Mobile no.")
                                ba=int(input("Enter Choice no."))
                                if(ba==1):
                                    bc=input("Enter Bank name")
                                    no=int(input("Enter Bank Account No."))
                                    print(" Confirm Bank=",bc)
                                    print("Confirm Account No=",no)
                                    r=input("y/n")
                                    if(r=="y"):
                                        y=0
                                        am=int(input("Enter amount"))
                                        print("Pay=",am)
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        p=input("y/n")
                                        if(p=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op+bc
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    else:
                                        print("Thanks")
                                elif(ba==2):
                                    no=int(input("Enter Mobile No."))
                                    print("Confirm Mobile No=",no)
                                    r=input("y/n")
                                    if(r=="y"):
                                        y=0
                                        am=int(input("Enter amount"))
                                        print("Pay=",am)
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        p=input("y/n")
                                        if(p=="y"):
                                            y=1
                                        else:
                                            print("Thanks")
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        a={"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    else:
                                        print("Thanks")
                                else:
                                    print("Choice not Available")
                            else:
                                print("Thanks")
            elif(uc==3):
                q=0
                m=0
                w=0
                usn=input("Enter Your User Name")
                uf=pd.read_csv('History.csv')
                uf1=uf[(uf['User Name']==usn)]
                if(uf1.empty):
                    print("User Not found")
                    print("Enter correct User Name")
                    q=1
                    w=0
                    m=0
                else:
                    data=(uf[uf['User Name']==usn].index.values)
                    print(uf.loc[data])
            else:
                print("Choice not available")
                q=1
                w=0
                m=0
if(y==1):
    v=1
    while(v==1):
        p=0
        print("Payment methods")
        print("1.Already saved Credit Card or Debit card")
        print("2.Add Credit Card or Debit card")
        c=int(input("Enter Choice"))
        if(c==1):
            df=pd.read_csv('Bank.csv')
            u=input("Enter User Id")
            p=input("Enter Password")
            pi=int(input("Enter Pin"))
            df1=df[(df['User Id']==u) & (df['Password']==p) & (df['PIN']==pi)]
            if(df1.empty):
                v=1
                print("Account not Exists")
            else:
                v=0
                d=(df[df['User Id']==u].index.values)
                print("Account Found")
                print(df.loc[d])
                ps=input("Pay y/n")
                if(ps=="y"):
                    print("Successfully Paid")
                    p=1
        elif(c==2):
            print("1.Debit Card")
            print("2.Credit Card")
            cd=int(input("Enter Choice"))
            if(cd==1):
                dc="Debit Card"
            elif(cd==2):
                dc="Credit card"
            us=input("Enter Your User Id/E-mail Address")
            pa=input("Enter Your Password")
            ca=int(input("Enter Card no(16 Digits No.)"))
            va=input("Card Validity")
            cv=int(input("Enter CVV No."))
            pin=int(input("Enter New Pin"))
            a={"User Id":[us],"Password":[pa],"Card No.":[ca],"Expiry/Validity No.":[va],"CVV No.":[cv],"PIN":[pin],"Debit/Credit Card":[dc]}
            bk=pd.read_csv('Bank.csv')
            bk2=pd.DataFrame(a)
            bk3=bk.append(bk2)
            bk3.to_csv('Bank.csv',index=False)
            print("Successfully Added")
            v=1
        
    
