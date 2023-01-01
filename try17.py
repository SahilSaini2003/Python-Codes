import pandas as pd
db=pd.read_excel(r'C:\Users\DELL\Documents\try.xlsx')
print(db)
a={'Name':['Jam'],'Class':[12],'Marks':[34]}
df=pd.DataFrame(a)
df2=db.append(df)
df2.to_excel(r'C:\Users\DELL\Documents\try.xlsx',index=False)
