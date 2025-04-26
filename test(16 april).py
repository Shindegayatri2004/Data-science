# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 08:10:34 2025

@author: Hp
"""
#     TEST 
import numpy as np

p = np.array([3,5])
q = np.array([2,5])
np.greater_equal(p,q)
np.greater(p,q)

r=np.array([5,6])
s=np.array([8,9])
np.less_equal(r,s)
np.less(r,s)

########################################

import pandas as pd
import numpy as np
data={
      'name':['alice','bob','charlie','david','eva'],
      'age':[25,30,35,45,28],
      'department':['HR','IT','Finance','IT','HR'],
      'joining_year':[2018,2016,2015,2019,2020]
      }
df=pd.DataFrame(data)
df
# first rows
df1=df[:2]
df1

#column names
df.columns

#datatypes of each column
df.dtypes

# summary statistices for numeric column
df.describe()

#############################################

data={
      'name':['alice','bob','charlie','david','eva'],
      'age':[25,30,35,45,28],
      'department':['HR','IT','Finance','IT','HR'],
      'joining_year':[2018,2016,2015,2019,2020],
      }
df['salary']=[50000,60000,70000,65000,48000]
df=pd.DataFrame(data)
df
df=pd.DataFrame.add.column({'salary':[50000,60000,70000,65000,48000]})
df





#################################################
# compute multiplication

p=[[1,0],[0,1]]
p=np.array(p)
q=[[4,2],[1,3]]
q=np.array(q)

r=p*q
r
i=np.cross(p,q)
i
j=np.dot(p,q)
j


