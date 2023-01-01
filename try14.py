import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="sahil")
mydb.execute("use Admin;")
