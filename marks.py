ip=int(input("enter marks(out of 50) in ip"))
maths=int(input("enter enter marks(out of 50) in maths"))
physics=int(input("enter enter marks(out of 50) in physics"))
percentage=((ip+maths+physics)*100)/150
if(percentage < 30):
    print("FAIL")
elif(30<=percentage<40):
      print ("3rd Division") 
elif(40<=percentage<50):
       print ("2nd Division") 
else:
    print ("Ist Division") 
