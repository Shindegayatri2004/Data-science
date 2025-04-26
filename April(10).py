# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 08:34:45 2025

@author: om
"""

import pandas as pd
import numpy as np
data=[(3,5,7),(2,4,6),(5,8,9)]
df=pd.DataFrame(data,columns=['A','B','C'])
print(df)
df['A'] = df['A'].map(lambda A: A/2)
print(df)

#using numpy function on single column
#using DataFrame .apply() and [] operator
df['A'] = df['A'].apply(np.square)
print(df)
###########################################

import pandas as pd
tech = ({'courses':['spark','pyspark','hadoop','python','pandas','hadoop','spark','python','NA'],
         'Fee':[22000,24000,25000,22000,23000,24000,25000,22000,21000],
         'duration':['30days','25days','28days','31days','23days','27days','29days','25days','30days'],
         'discount':[1000,2000,3000,1200,2500,None,14000,16000,0]})
df = pd.DataFrame(tech)
print(df)
#use groupby to compute sum
df2 = df.groupby(['courses']).sum()
df2
#group by multiple columns
df2 = df.groupby(['courses','duration']).sum()
df2
#add index to groupby data
df2 = df.groupby(['courses','duration']).sum().reset_index()
df2

###################################################

#get the all column names from headers
column_header = list(df.columns.values)
print("the column headr=",column_header)
##############################################
#using list(df) to get column headers as a list
column_header = list(df.columns)
column_header
#using list(df) to get the list of all column names
column_headers = list(df)
column_headers
############################################

#pandas shuffle dataframe rows
import pandas as pd
tech = ({'courses':['spark','pyspark','hadoop','python','pandas','hadoop','spark','python','NA'],
         'Fee':[22000,24000,25000,22000,23000,24000,25000,22000,21000],
         'duration':['30days','25days','28days','31days','23days','27days','29days','25days','30days'],
         'discount':[1000,2000,3000,1200,2500,None,14000,16000,0]})
df = pd.DataFrame(tech)
print(df)
#pandas shuffle dataframe  rows
#shuffle the dataframe rows and returns all rows
df1 = df.sample(frac=1)
df1
#############################
#create a new index starting from zero
df1 = df.sample(frac=1).reset_index()
print(df1)

#drop suffle index
df1 = df.sample(frac=1).reset_index(drop=True)
df1
