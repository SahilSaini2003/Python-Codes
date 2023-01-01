a=int(input("enter no."))
b=a%3
if(b==0):
    print("divisible by 3")
else:
    print("not divisible by 3")
    print("required no =",a+(3-b))
