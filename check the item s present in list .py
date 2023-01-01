l1=list(input("enter list items"))
n=input("enter items")
i=0
x=0
while i<len(l1):
    if (l1[i]==n):
        print (l1.index(n))
        x=1
        break
    i+=1
if(x==0):
    print("no value exists")
