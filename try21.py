import pandas as pd
import numpy as np
s=pd.Series([6,12,18,24,30,36,42,48,54,60],index=['a','b','c','d','e','f','g','h','i','j'])
print(s[2])
print(s[ :4])
print(s[ : :-2])
print(s['d'])
##print(s['a','d','h','j'])
print(s.size)
print(s.head(3))
print(s.tail(2))
