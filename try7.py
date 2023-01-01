import pandas as pd
import matplotlib.pyplot as plt
import csv
df=pd.read_csv('History.csv')
print(df)
plt.plot(df['User Name'],df['Amount of Transection'])
plt.show()


