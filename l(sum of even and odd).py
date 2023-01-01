l=list(input("enter list items"))
e=0
o=0
i=0
while i<len(l):
    if(int(l[i])%2==0):
        e=e+int(l[i])
    else:
        o=o+int(l[i])
    i+=1
print("sum of even no",e)
print("sum of odd no",o)
