import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import date
import mysql.connector as s
print("~:~"*36)
print("\t\t      -:-:-:-:-Welcome to S.A.S Online Transactions-:-:-:-:-")
print("~:~"*36)
m=1
x=0
while(m==1):
    print("\t\t\t\t # 1.Admin #")
    print("\t\t\t\t   # 2.User #")
    a=int(input("\t\t\t\t Whom you are:-"))
    if(a==1):
        mdb=s.connect(host="localhost",user="root",password="sahil",database="Admin")
        cur=mdb.cursor()
        print("\t\t\t$ Lets Check Weather You Are Admin or Not $")
        ad=input("\t\t\t\t Enter Admin Name:-")
        pa=input("\t\t\t\t Enter Password:-")
        q="select * from Admin_list where Admin='{}' AND Password='{}'".format(ad,pa)
        cur.execute(q)
        rec=cur.fetchall()
        if(cur.rowcount==0):
            print("\t\t\t           OOPS! Admin not found")
            print("\t\t< Weather You entered Wrong Details or You Are not a Admin >")
            m=1
        else:
            q=1
            print("\t\t\t\t Hurray! We got you")
            print("\t\t\t\t  Welcome",ad,"!")
            while(q==1):
                print("\t\t\t      & You can check one off these &")
                print("\t\t\t\t# 1.Admin list #")
                print("\t\t\t\t  # 2.User list #")
                print("\t\t\t\t# 3.Check profit #")
                b=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                if(b==1):
                    w=1
                    while(w==1):
                        print("\t\t\t       & Here Is Your Admin List &")
                        print("\t\t\t\t # 1.Admin details #")
                        print("\t\t\t\t   # 2.Add Admin #")
                        print("\t\t\t\t# 3.Remove Admin #")
                        print("\t\t\t\t# 4.Change Password #")
                        c=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                        if(c==1):
                            sq="select * from Admin_list"
                            cur.execute(sq)
                            rec=cur.fetchall()
                            for x in rec:
                                print(x)
                                q=0
                                w=0
                        elif(c==2):
                            adn=input("\t\t\t\tEnter Admin Name:-")
                            Pass=input("\t\t\t\tEnter Password:-")
                            sq="insert into Admin_list values('{}','{}')".format(adn,Pass)
                            cur.execute(sq)
                            mdb.commit()
                            sq="select * from Admin_list"
                            cur.execute(sq)
                            rec=cur.fetchall()
                            q=0
                            w=0
                            for x in rec:
                                print(x)
                        elif(c==3):
                            add=input("\t\t\t        Enter Admin you want to Delete:-")
                            sq="select * from Admin_list where Admin='{}'".format(add)
                            cur.execute(sq)
                            rec=cur.fetchall()
                            if(cur.rowcount==0):
                                q=0
                                w=1
                                print("\t\t\t           OOPS! Admin not found")
                                print("\t\t< Weather You entered Wrong Name or Admin Not Present >")
                            else:
                                print("\t\t\t\t `Admin Found`")
                                sq="Delete from Admin_list where Admin='{}'".format(add)
                                cur.execute(sq)
                                mdb.commit()
                                sq="select * from Admin_list"
                                cur.execute(sq)
                                rec=cur.fetchall()
                                q=0
                                w=0
                                for x in rec:
                                    print(x)
                        elif(c==4):
                            add=input("\t\t\t\t Enter Admin Name:-")
                            sq="select * from Admin_list where Admin='{}'".format(add)
                            cur.execute(sq)
                            rec=cur.fetchall()
                            if(cur.rowcount==0):
                                q=0
                                w=1
                                print("\t\t\t           OOPS! Admin not found")
                                print("\t\t< Weather You entered Wrong Name or Admin Not Present >")
                            else:
                                pa=input("\t\t\t\t Enter New Password:-")
                                sq="update Admin_list set Password='{}' where Admin='{}'".format(pa,add)
                                cur.execute(sq)
                                mdb.commit()
                                sq="select * from Admin_list where Admin='{}'".format(add)
                                cur.execute(sq)
                                rec=cur.fetchall()
                                q=0
                                w=0
                                for x in rec:
                                    print(x)
                        else:
                            w=1
                            q=0
                            print("\t\t    Please enter Correct Numeric value of your choice")
                        if(w==0):
                            cho=input("\t\t\t      Do You want to do anything else (y/n)~")
                            if(cho=="y"):
                                q=1
                            else:
                                print("~:~"*36)
                                print("\t\t\t\t Thanks For Coming!")
                                print("~:~"*36)
                                q=0
                                m=0             
                elif(b==2):
                    w=1
                    while(w==1):
                        print("\t\t\t                # 1.User Details #")
                        print("\t\t\t           # 2.Ban/Remove User #")
                        print("\t\t\t           #3.User Joining Graph #")
                        u=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                        if(u==1):
                            dfu=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                            print(dfu)
                            w=0
                            q=0
                        elif(u==2):
                            usr=input("\t\t\t    *Enter User Name that you want to Ban:-")
                            df2=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                            df3=df2[df2['User Name']==usr]
                            if(df3.empty):
                                print("\t\t\t           OOPS! User not found")
                                print("\t\t< Weather You entered Wrong Name or User Not Present >")
                                w=1
                                q=0
                            else:
                                w=0
                                q=0
                                print("\t\t\t\t| User exists |")
                                print("\t\t\t   Kindly Confirm to ban",usr )
                                s=input("\t\t\t\t      yes/no(y/n):-")
                                if(s=="y"):
                                    data=(df2[df2['User Name']==usr].index.values)
                                    df2=df2.drop(data)
                                    print("\t\t\t\t *Banned Successfully*")
                                    df2.to_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx',index=False)
                                else:
                                    q=0
                                    w=0
                                    print("\t\t\t\t| No-one is banned |")
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
                            print("\t\t    Please enter Correct Numeric value of your choice")
                        if(w==0):
                            cho=input("\t\t\t      Do You want to do anything else (y/n)~")
                            if(cho=="y"):
                                q=1
                            else:
                                q=0
                                print("~:~"*36)
                                print("\t\t\t\t Thanks For Coming!")
                                print("~:~"*36)
                elif(b==3):
                    grf=pd.read_csv('Graph.csv')
                    print("\t\t\t\tWe have these Graph Options:-")
                    print("\t\t\t\t      # 1.Line graph #")
                    print("\t\t\t\t       # 2.Bar Graph #")
                    gh=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                    if(gh==1):
                        a=grf.groupby('Month')['Profit Amount per Transection'].sum()
                        #plt.plot(grf['Month'],grf['Profit Amount per Transection'],marker='*')
                        plt.plot(a,marker='*')
                        plt.title("Profit made per Month",fontsize=20)
                        #plt.xticks()
                        plt.xlabel('Month',fontsize=10)
                        plt.ylabel('Profit',fontsize=10)
                        plt.show()
                    elif(gh==2):
                        plt.bar(grf['Month'],grf['Profit Amount per Transection'])
                        plt.title("Profit made per Month",fontsize=20)
                        plt.xlabel('Month',fontsize=10)
                        plt.ylabel('Profit',fontsize=10)
                        plt.show()
                else:
                    print("\t\t    Please enter Correct Numeric value of your choice")
                    q=1
    elif(a==2):
        m=0
        print("\t\t\t\t   # 1.New User #")
        print("\t\t\t\t   # 2.Old User #")
        x=0
        b=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
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
                usi=input("\t\t\t      Enter User id/Email-Address:-")
                usn=input("\t\t\t\t Enter User name:-")
                pas=input("\t\t\t\t Enter Password:-")
                mo=input("\t\t\t\t Enter Mobile No.:-")
                dob=input("\t\t\t\t Enter D.O.B/Date of birth:-")
                usf=pd.read_csv('User Joining Details.csv')
                udata={'User Joining date':[lod],'Month':[mont]}
                usf2=pd.DataFrame(udata)
                usf3=usf.append(usf2)
                usf3.to_csv('User Joining Details.csv',index=False)
                df2=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                data={"User Id":[usi],"User Name":[usn],"Password":[pas],"Mobile No.":[mo],"D.O.B":[dob],"User login Date":[lod]}
                df3=pd.DataFrame(data)
                df4=df2.append(df3)
                df4.to_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx',index=False)
                print("\t\t\t\t  ||Successfully added new user||")
                i=1
                if(i==1):
                    b=2
            elif(b==2):
                w=1
                while(w==1):
                    print("\t\t\t    # 1.Log in with User Id/Email-Address #")
                    print("\t\t\t             # 2.Log in with Mobile no. #")
                    c=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                    if(c==1):
                        usi=input("\t\t\t  Enter User id/Email-Address:-")
                        pas=input("\t\t\t\t Enter Password:-")
                        udf=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                        udf2=udf[(udf['User Id']==usi) & (udf['Password']==pas)]
                        if(udf2.empty):
                            print("\t\t\t           OOPS! User not found")
                            print("\t\t< Weather You entered Wrong Name/Password or User Not Present >")
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
                    elif(c==2):
                        mo=int(input("\t\t\t\t Enter Mobile no.:-"))
                        pas=input("\t\t\t\t Enter Password:-")
                        udf=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                        udf2=udf[(udf['Mobile No.']==mo) & (udf['Password']==pas)]
                        if(udf2.empty):
                            w=1
                            i=0
                            m=0
                            print("\t\t\t           OOPS! User not found")
                            print("\t\t< Weather You entered Wrong Name/Password or User Not Present >")
                        else:
                            x=1
                            i=0
                            w=0
                            m=0
                            data=(udf[udf['Mobile No.']==mo].index.values)
                            b=np.array(udf)
                            usn=b[data,1]
                            print("\t\t\t\t Welcome",*usn,"!")
                    else:
                        w=1
                        i=0
                        m=0
                        print("\t\t    Please enter Correct Numeric value of your choice")
            else:
                m=0
                x=1
                print("\t\t    Please enter Correct Numeric value of your choice")
    else:
        m=1
        print("\t\t    Please enter Correct Numeric value of your choice")
if(x==1):
    q=1
    while(q==1):
        print("\t\t\t\t # 1.Personal Changes #")
        print("\t\t\t\t# 2.Online Transection #")
        print("\t\t\t\t# 3.Transection History #")
        uc=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
        w=1
        while(w==1):
            if(uc==1):
                y=0
                p=1
                print("\t\t\t\t# 1.Change Password #")
                print("\t\t\t        # 2.Change User Id/Email-Address #")
                print("\t\t\t\t# 3.Change Mobile No. #")
                uc1=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                if(uc1==1):
                    usn=input("\t\t\t\t Enter User Name:-")                        
                    dob=input("\t\t\t\t Enter D.O.B/Date Of Birth:-")
                    udf=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                    udf1=udf[(udf['User Name']==usn) & (udf['D.O.B']==dob)]
                    if(udf1.empty):
                        w=1
                        q=0
                        p=0
                        print("\t\t\t           OOPS! User not found")
                        print("\t\t< Weather You entered Wrong User Name/D.O.B or User Not Present >")
                    else:
                        w=0
                        pas=input("\t\t\t\t Enter New Password:-")
                        d=(udf[udf['User Name']==usn].index.values)
                        udf.loc[d,["Password"]]=pas
                        udf.to_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx',index=False)
                        print("\t\t\t\t || Successfully changed ||")
                        v=0
                        q=1
                elif(uc1==2):
                    usn=input("\t\t\t\t Enter User Name:-")
                    pas=input("\t\t\t\t Enter Password:-")
                    udf=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                    udf2=udf[(udf['User Name']==usn) & (udf['Password']==pas)]
                    if(udf2.empty):
                        w=1
                        q=0
                        p=0
                        print("\t\t\t           OOPS! User not found")
                        print("\t\t< Weather You entered Wrong User Name/Password or User Not Present >")
                    else:                               
                        w=0
                        usi=input("\t\t\t        Enter New User Id/Email-Address:-")
                        d=(udf[udf['User Name']==usn].index.values)
                        udf.loc[d,["User Id"]]=usi
                        udf.to_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx',index=False)
                        print("\t\t\t\t || Successfully Changed ||")
                        q=1
                        v=0
                elif(uc1==3):
                    usi=input("\t\t\t\t Enter User Id/Email-Address:-")
                    pas=input("\t\t\t\t Enter Password:-")
                    udf=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                    udf2=udf[(udf['User Id']==usi) & (udf['Password']==pas)]
                    if(udf2.empty):
                        w=1
                        q=0
                        p=0
                        print("\t\t\t           OOPS! User not found")
                        print("\t\t< Weather You entered Wrong Name/Password or User Not Present >")
                    else:
                        w=0
                        mo=int(input("\t\t\t\t Enter New Mobile No.:-"))
                        d=(udf[udf['User Id']==usi].index.values)
                        udf.loc[d,["Mobile No."]]=mo
                        udf.to_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx',index=False)
                        print("\t\t\t\t || Successfully Changed ||")
                        q=1
                        v=0
                else:
                    w=0
                    q=1
                    print("\t\t    Please enter Correct Numeric value of your choice")
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
                    print("\t\t\t\t     # 1.Recharge #")
                    print("\t\t\t\t      # 2.Pay Bills #")
                    uc1=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                    grf=pd.read_csv('Graph.csv')
                    if(uc1==1):
                        uc1="Recharge"
                        us=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                        usn=input("\t\t\t\t Enter your User Name:-")
                        dr=us[(us['User Name']==usn)]
                        if(dr.empty):
                            print("\t\t\t           OOPS! User not found")
                            print("\t\t< Weather You entered Wrong Name or User Not Present >")
                            q=1
                        else:
                            print("\t\t\t\t         # 1.Mobile #")
                            print("\t\t\t\t           # 2.DTH #")
                            re=int(input("\t\t\tWaana Enter the Numeric Value Of Your Choice:-"))
                            if(re==1):
                                s=0
                                no=int(input("\t\t\t\tEnter Mobile No.:-"))
                                print("\t\t\t\t      Available Operator")
                                print("\t\t\t\t            # 1.Jio #")
                                print("\t\t\t\t      # 2.Vodafone #")
                                print("\t\t\t\t          # 3.Airtel #")
                                op=int(input("\t\t\tWaana Enter the Numeric Value of Operator:-"))
                                if(op==1):
                                    op="Jio"
                                    print("\t\t\t\t   || Plans available ||")
                                    jp=pd.read_csv('Jio plans.csv')
                                    print(jp)
                                    pa=int(input("\t\t\t     Enter the Amount of Choosen Plan:-"))
                                    d=(jp[jp['Cost in Rs.']==pa].index.values)
                                    print(jp.loc[d])
                                    print("\t\t\t\t     *Pay=",pa)
                                    pay=input("\t\t\t\t       yes/no(y/n):-")
                                    y=0
                                    if(pay=="y"):
                                        s=0
                                        y=1
                                        amg=pa*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        h=hf.tail(1)
                                        h1=np.array(h)
                                        h2=h1[0,0]
                                        h3=h2+1
                                        a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[pa],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    else:
                                        p=1
                                elif(op==2):
                                    op="Vodafone"
                                    print("\t\t\t\t      # 1.Prepaid #")
                                    print("\t\t\t\t     # 2.Postpaid #")
                                    pp=int(input("\t\t\tWaana Enter the Numeric Value Of Service:-"))
                                    if(pp==1):
                                        print("\t\t\t\t || Plans available ||")
                                        jp=pd.read_csv('Vodafone plans.csv')
                                        print(jp)
                                        pa=int(input("\t\t\t     Enter the Amount of Choosen Plan:-"))
                                        d=(jp[jp['Cost in Rs.']==pa].index.values)
                                        print(jp.loc[d])
                                        y=0
                                        print("\t\t\t\t *Pay=",pa)
                                        amg=pa*0.01
                                        pay=input("\t\t\t\t      yes/no(y/n):-")
                                        if(pay=="y"):
                                            y=1
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[pa],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1
                                    elif(pp==2):
                                        am=int(input("\t\t\t\t Enter Amount to Pay in Rupees:-"))
                                        print("\t\t\t\t *Pay=",am)
                                        pay=input("\t\t\t\t        yes/no(y/n):-")
                                        y=0
                                        if(pay=="y"):
                                            y=1
                                            amg=am*0.01
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1
                                elif(op==3):
                                    op="Airtel"
                                    print("\t\t\t\t      # 1.Prepaid #")
                                    print("\t\t\t\t     # 2.Postpaid #")
                                    pp=int(input("\t\t\tWaana Enter the Numeric Value Of Service:-"))
                                    if(pp==1):
                                        print("\t\t\t\t   || Plans available ||")
                                        jp=pd.read_csv('Airtel plans.csv')
                                        print(jp)
                                        pa=int(input("\t\t\t     Enter the Amount of Choosen Plan:-"))
                                        d=(jp[jp['Cost in Rs.']==pa].index.values)
                                        print(jp.loc[d])
                                        print("\t\t\t\t     *Pay=",pa)
                                        pay=input("\t\t\t\t      yes/no(y/n):-")
                                        y=0
                                        if(pay=="y"):
                                            y=1
                                            amg=pa*0.01
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[pa],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1
                                    elif(pp==2):
                                        am=int(input("\t\t\t\t Enter Amount to Pay in Rupees:-"))
                                        print("\t\t\t\t    *Pay=",am)
                                        pay=input("\t\t\t\t       yes/no(y/n):-")
                                        y=0
                                        if(pay=="y"):
                                            y=1
                                            amg=am*0.01
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1  
                            elif(re==2):
                                w=0
                                q=0
                                s=0
                                print("\t\t\t\t        Available Operator")
                                print("\t\t\t\t       # 1.D2h Videocon #")
                                print("\t\t\t\t           # 2.Tata Sky #")
                                print("\t\t\t\t            # 3.Dish Tv #")
                                to=int(input("\t\t\tWaana Enter the Numeric Value of Choosen Operator:-"))
                                if(to==1):
                                    op="D2h Videocon"
                                    print("\t\t\t    # 1.Pay Using Registered Mobile No.(10 digits) #")
                                    print("\t\t\t           # 2.Pay Using Customer Id(7 Digits) #")
                                    to1=int(input("\t\t\tWaana Enter the Numeric Value of Choice:-"))
                                    if(to1==1):
                                        no=int(input("\t\t\t       Enter Registered Mobile No.(10 digits):-"))
                                        print("\t\t\t\t *Confirm Your Number:-",no)
                                        z=input("\t\t\t\t      yes/no(y/n):-")
                                        if(z=="y"):
                                            y=0
                                            am=int(input("\t\t\t\t Enter Amount in Rupee:-"))
                                            print("\t\t\t\t *Pay=",am)
                                            r=input("\t\t\t\t      yes/no(y/n):-")
                                            if(r=="y"):
                                                y=1
                                                amg=am*0.01
                                                gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                                gf1=pd.DataFrame(gr)
                                                gf2=grf.append(gf1)
                                                gf2.to_csv('Graph.csv',index=False)
                                                at=uc1+"-"+op
                                                hf=pd.read_csv('History.csv')
                                                h=hf.tail(1)
                                                h1=np.array(h)
                                                h2=h1[0,0]
                                                h3=h2+1
                                                a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                                hf1=pd.DataFrame(a)
                                                hf2=hf.append(hf1)
                                                hf2.to_csv('History.csv',index=False)
                                            else:
                                                p=1
                                        else:
                                            q=1
                                    elif(to1==2):
                                        no=int(input("\t\t\t\tEnter Customer Id(7 Digits):-"))
                                        print("\t\t\t\t *Confirm Your Id:-",no)
                                        z=input("\t\t\t\t yes/no(y/n):-")
                                        if(z=="y"):
                                            y=0
                                            am=int(input("\t\t\t\tEnter Amount in Rupee:-"))
                                            print("\t\t\t\t *Pay=",am)
                                            r=input("\t\t\t\t yes/no(y/n):-")
                                            if(r=="y"):
                                                y=1
                                                amg=am*0.01
                                                gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                                gf1=pd.DataFrame(gr)
                                                gf2=grf.append(gf1)
                                                gf2.to_csv('Graph.csv',index=False)
                                                at=uc1+"-"+op
                                                hf=pd.read_csv('History.csv')
                                                h=hf.tail(1)
                                                h1=np.array(h)
                                                h2=h1[0,0]
                                                h3=h2+1
                                                a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                                hf1=pd.DataFrame(a)
                                                hf2=hf.append(hf1)
                                                hf2.to_csv('History.csv',index=False)    
                                            else:
                                                p=1
                                        else:
                                            q=1
                                elif(to==2):
                                    op="Tata Sky"
                                    no=int(input("\t\t\t\t Enter Customer Id(10 Digits):-"))
                                    print("\t\t\t\t *Confirm your Id:-",no)
                                    z=input("\t\t\t\t yes/no(y/n):-")
                                    if(z=="y"):
                                        y=0
                                        am=int(input("\t\t\t\t Enter Amount in Rupee:-"))
                                        print("\t\t\t\t *Pay=",am)
                                        r=input("\t\t\t\t yes/no(y/n):-")
                                        if(r=="y"):
                                            y=1
                                            amg=am*0.01
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1
                                    else:
                                        q=1
                                elif(to==3):
                                    op="Dish Tv"
                                    no=int(input("\t\t\t\t Enter Customer Id(12 Digits):-"))
                                    print("\t\t\t\t *Confirm Your Id",no)
                                    z=input("y/n")
                                    if(z=="y"):
                                        y=0
                                        am=int(input("\t\t\t\t Enter Amount in Rupee:-"))
                                        print("\t\t\t\t *Pay=",am)
                                        r=input("y/n")
                                        if(r=="y"):
                                            y=1
                                            amg=am*0.01
                                            gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                            gf1=pd.DataFrame(gr)
                                            gf2=grf.append(gf1)
                                            gf2.to_csv('Graph.csv',index=False)
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1
                                    else:
                                        q=1
                    elif(uc1==2):
                        w=0
                        q=0
                        s=0
                        uc1="Bills Payment"
                        us=pd.read_excel(r'C:\Users\DELL\AppData\Local\Programs\Python\Python38\User.xlsx')
                        usn=input("\t\t\t\t Enter your User Name:-")
                        dr=us[(us['User Name']==usn)]
                        if(dr.empty):
                            print("\t\t\t           OOPS! User not found")
                            print("\t\t< Weather You entered Wrong Name or User Not Present >")
                            q=1
                        else:
                            print("\t\t\t\t # 1.Electricity Bills #")
                            print("\t\t\t\t   # 2.Water Bills #")
                            print("\t\t\t\t # 3.Money Transfer #")
                            bi=int(input("\t\t\tWaana Enter the Numeric Value of Your Choice:-"))
                            if(bi==1):
                                op="Electricity Bills"
                                print("\t\t\t\t     Available Boards")
                                print("\t\t\t\t     # JVVNL #")
                                no=int(input("\t\t\t\t Enter K.No:-"))
                                print("\t\t\t\t *Confirm Your K.No.=",no)
                                r=input("\t\t\t\t yes/no(y/n):-")
                                if(r=="y"):
                                    y=0
                                    am=int(input("\t\t\t\tEnter Amount in Rupee:-"))
                                    print("\t\t\t\t *Pay=",am)
                                    p=input("y/n")
                                    if(p=="y"):
                                        y=1
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        h=hf.tail(1)
                                        h1=np.array(h)
                                        h2=h1[0,0]
                                        h3=h2+1
                                        a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    else:
                                        p=1
                                else:
                                    q=1
                            elif(bi==2):
                                op="Water Bills"
                                print("\t\t\t\t   Available Boards")
                                print("\t\t\t\t    # PHED #")
                                no=int(input("\t\t\t\t Enter E-Mitra CID Code:-"))
                                print("\t\t\t\t *Confirm E-Mitra CID Code=",no)
                                r=input("\t\t\t\t      yes/no(y/n):-")
                                if(r=="y"):
                                    y=0
                                    am=int(input("\t\t\t\t Enter Amount in Rupee:-"))
                                    print("\t\t\t\t *Pay=",am)
                                    p=input("\t\t\t\t      yes/no(y/n):-")
                                    if(p=="y"):
                                        y=1
                                        amg=am*0.01
                                        gr={'Profit Amount per Transection':[amg],'Month':[mont]}
                                        gf1=pd.DataFrame(gr)
                                        gf2=grf.append(gf1)
                                        gf2.to_csv('Graph.csv',index=False)
                                        at=uc1+"-"+op
                                        hf=pd.read_csv('History.csv')
                                        h=hf.tail(1)
                                        h1=np.array(h)
                                        h2=h1[0,0]
                                        h3=h2+1
                                        a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                        hf1=pd.DataFrame(a)
                                        hf2=hf.append(hf1)
                                        hf2.to_csv('History.csv',index=False)
                                    else:
                                        p=1
                                else:
                                    q=1
                            elif(bi==3):
                                op="Money Transfer" 
                                print("\t\t\t\t # 1.Using Bank Account no. #")
                                print("\t\t\t\t     # 2.Using Mobile no. #")
                                ba=int(input("\t\t\tWaana Enter the Numeric Value of Choice:-"))
                                if(ba==1):
                                    bc=input("\t\t\t\t Enter Bank name:-")
                                    no=int(input("\t\t\t\t Enter Bank Account No.:-"))
                                    print("\t\t\t\t *Confirm Bank=",bc)
                                    print("\t\t\t\t *Confirm Account No=",no)
                                    r=input("\t\t\t\t yes/no(y/n):-")
                                    if(r=="y"):
                                        y=0
                                        am=int(input("\t\t\t\tEnter Amount in Rupee:-"))
                                        print("\t\t\t\t *Pay=",am)
                                        p=input("\t\t\t\t      yes/no(y/n):-")
                                        if(p=="y"):
                                            y=1
                                            at=uc1+"-"+op+bc
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1
                                    else:
                                        q=1
                                elif(ba==2):
                                    no=int(input("\t\t\t\t Enter Mobile No.:-"))
                                    print("\t\t\t\t *Confirm Mobile No=",no)
                                    r=input("\t\t\t\t yes/no(y/n):-")
                                    if(r=="y"):
                                        y=0
                                        am=int(input("\t\t\t\t Enter Amount in Rupee:-"))
                                        print("\t\t\t\t *Pay=",am)
                                        p=input("\t\t\t\t yes/no(y/n):-")
                                        if(p=="y"):
                                            y=1
                                            at=uc1+"-"+op
                                            hf=pd.read_csv('History.csv')
                                            h=hf.tail(1)
                                            h1=np.array(h)
                                            h2=h1[0,0]
                                            h3=h2+1
                                            a={"Transection ID":[h3],"User Name":[usn],"Transection Amount":[am],"Amount Type":[at],"MobileNo./K.No./E-Mitra CID Code":[no],"Date":[dat]}
                                            hf1=pd.DataFrame(a)
                                            hf2=hf.append(hf1)
                                            hf2.to_csv('History.csv',index=False)
                                        else:
                                            p=1
                                    else:
                                        q=1
                                else:
                                    print("t\t    Please enter Correct Numeric value of your choice")
                                    q=1
                            else:
                                print("t\t    Please enter Correct Numeric value of your choice")
                                q=1
            elif(uc==3):
                q=0
                m=0
                w=0
                usn=input("\t\t\t\t Enter Your User Name:-")
                uf=pd.read_csv('History.csv')
                uf1=uf[(uf['User Name']==usn)]
                if(uf1.empty):
                    print("\t\t\t           OOPS! User not found")
                    print("\t\t< Weather You entered Wrong Name or User Not Present >")
                    q=1
                    w=0
                    m=0
                else:
                    data=(uf[uf['User Name']==usn].index.values)
                    print(uf.loc[data])
                    p=1
                    y=0
            else:
                print("t\t    Please enter Correct Numeric value of your choice")
                q=1
                w=0
                m=0
            if(y==1):
                v=1
                while(v==1):
                    p=0
                    print("\t\t\t\t Payment methods")
                    print("\t\t\t         # 1.Already saved Credit Card or Debit card")
                    print("\t\t\t\t  # 2.Add Credit Card or Debit card #")
                    c=int(input("\t\t\tWaana Enter the Numeric Value of Choice-"))
                    if(c==1):
                        df=pd.read_csv('Bank.csv')
                        u=input("\t\t\t\t Enter User Id:-")
                        p=input("\t\t\t\t Enter Password:-")
                        pi=int(input("\t\t\t\t Enter Pin:-"))
                        df1=df[(df['User Id']==u) & (df['Password']==p) & (df['PIN']==pi)]
                        if(df1.empty):
                            v=1
                            print("\t\t\t           OOPS! not found")
                            print("\t\t< Weather You entered Wrong Details or Not Present >")
                        else:
                            v=0
                            d=(df[df['User Id']==u].index.values)
                            print("\t\t\t\t || Account Found")
                            print(df.loc[d])
                            ps=input("\t\t\t\t Pay yes/no(y/n):-")
                            if(ps=="y"):
                                print("\t\t\t\t || *Successfully Paid* ||")
                                p=1
                    elif(c==2):
                            print("\t\t\t\t # 1.Debit Card #")
                            print("\t\t\t\t # 2.Credit Card #")
                            cd=int(input("\t\t\tWaana Enter the Numeric Value of Choice:-"))
                            if(cd==1):
                                dc="Debit Card"
                            elif(cd==2):
                                dc="Credit card"
                            us=input("\t\t\t\tEnter Your User Id/E-mail Address:-")
                            pa=input("\t\t\t\t Enter Your Password:-")
                            ca=int(input("\t\t\t\t Enter Card no(16 Digits No.):-"))
                            va=input("\t\t\t\t Card Validity:-")
                            cv=int(input("\t\t\t\t Enter CVV No.:-"))
                            pin=int(input("\t\t\t  Enter New Pin(Can't Be Changed in FUTURE):-"))
                            a={"User Id":[us],"Password":[pa],"Card No.":[ca],"Expiry/Validity No.":[va],"CVV No.":[cv],"PIN":[pin],"Debit/Credit Card":[dc]}
                            bk=pd.read_csv('Bank.csv')
                            bk2=pd.DataFrame(a)
                            bk3=bk.append(bk2)
                            bk3.to_csv('Bank.csv',index=False)
                            print("\t\t\t\t || Successfully Added ||")
                            v=1
            if(p==1):
                du=input("\t\t\t Do You Want To do Anything Else yes/no(y/n):- ")
                if(du=="y"):
                    q=1
                else:
                    print("\t\t\t\t || Thanks ! For Using ||")
                    print("\t\t\t\t  ||Have A Good Day ||")
                    print("~:~"*36)
    
