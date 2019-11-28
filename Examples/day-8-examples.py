# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:42:53 2019

@author: Ahmad ALaarg
"""

import pandas as pd
"""
data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data)
print(s)

print('\n')

data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(s)
print(s.index)
print(s.values)
print(s[0])
print(s['b'])
print(s['f'],s['g'])
print ( sum(s))


print('\n')


data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data)
print(s)
print( s.head())
print( s.head(2))
print( s.tail())
print( s.tail(2))


data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data)
print( s.describe())
#s.plot(kind="bar")
s.plot(kind="pie")


data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data)
print(s)
s.index= ["a", "b", "c", "d", "e","f","g"]
print(s)
print("mean :",s.mean())
print("std:",s.std())
print( s.agg(['sum','max']))
s.plot()

"""


import numpy as np

dates = pd.date_range('20190101', periods=8)
df= pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
print(df.head())
print(df['P'])


dates = pd.date_range('20190101', periods=8)
df= pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
print(df.head())
print(df.iloc[:, 1:3])






