import mysql.connector as s
mdb=s.connect(host="localhost",user="root",password="sahil",database="Admin")
cur=mdb.cursor()
u=input("User name")
p=input("User password")
q="select * from Admin_list where Admin='{}' AND Password='{}'".format(u,p)
cur.execute(q)
rec=cur.fetchall()
for x in rec:
    print(x.center(20))
