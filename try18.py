import matplotlib.pyplot as plt
import pandas as pd
import csv
grf=pd.read_csv('Graph.csv')
print("\t\t\t\tWe have these Graph Options:-")
print("\t\t\t\t      # 1.Line graph #")
print("\t\t\t\t       # 2.Bar Graph #")
print(grf)
a=grf.sum(('Month')['Profit Amount per Transection'])
print(a)
'''pd.DataFrame(a)
print(a)
b=a['Month']
print(b)
plt.plot(a)
l=['October','November','December','January']
plt.xticks(a['Month'],l)
plt.show()'''
