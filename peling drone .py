a=int (input("enter no"))
x=0
b=a
while a>0:
    rem=a%10
    x=(x*10)+rem
    a=int(a/10)
if(x==b):
    print("no is pelling drone")
else:
    print ("nois not pellling drone")
