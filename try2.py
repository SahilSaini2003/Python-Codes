import csv
import pandas as pd
import numpy as np
grf=pd.read_csv('graph.csv')
amg=100
mont='Febuary'
qw=(grf[grf['Month']==mont].index.values)
print(*qw)
nw=np.array(grf)
print(*nw)
nw1=nw[qw,0]
print(*nw1)
amg1=amg+nw1
print(amg1)
gr={'Profit Amount per Transection':[amg1],'Month':[mont]}
print(gr)
gf1=pd.DataFrame(gr)
gf2=grf.append(gf1)
gf2.to_csv('Graph.csv',index=False)
