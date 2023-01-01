import matplotlib.pyplot as plt
a=['Sahil','Sam','Jon']
b=[20,15,5]
plt.bar(a,b,color=('red','green','Black'))
plt.title('Mast')
plt.xlabel('Name')
plt.ylabel('Number')
plt.grid(True)
c=(5,10,15,20,25)
plt.yticks(c)
plt.show()
