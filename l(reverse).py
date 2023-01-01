l=list(input("enter list items"))
x=len(l)-1
i=0
while(i<x) :
    l.insert (i,l[x])
    l.remove (x-1)
    i+=1
print ("new list",l)
    
