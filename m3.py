import matplotlib.pyplot as plt
n=['Sahil','Aman','Shailesh','Bahu','Akshita']
m=[78,67,56,34,24]
plt.bar(n,m,color="r")
plt.title('Result',fontsize="30",color='pink')
plt.xlabel('Name',color='blue',fontsize=20)
plt.ylabel('Marks')
plt.yticks([15,30,45,60,75,90,100])
plt.xticks(['Sahil','Shailesh'])
plt.show()
