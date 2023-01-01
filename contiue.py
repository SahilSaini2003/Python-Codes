i='y'
while i=='y':
    a=int(input("enter no"))
    b=int(input("enter no"))
    c=input("enter operator")
    if(c=='/'):
        print("Division",a/b)
    elif(c=='*'):
        print("Multiplicatiom",a*b)
    elif(c=='+'):
        print("Addition",a+b)
    elif(c=='-'):
        print("Subtraction",a-b)
    else:
        print("Invalid operator")
    i=input("Do you want to continue")
