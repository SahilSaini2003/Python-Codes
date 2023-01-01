import csv
import pandas as pd
import matplotlib.pyplot as plt
udf=pd.read_csv('User Joining Details.csv')
plt.hist(udf['Month'])
plt.show()
