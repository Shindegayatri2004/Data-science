# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:01:32 2025

@author: om
"""

#create using constructor
#create pandas for data frame
#8-4-2025
import pandas as pd

#for row wise
technologies=[['spark','20000','20days'],['data','20000','30days']]
df=pd.DataFrame(technologies)
print(df) #o/p:0      1       2
#           0  spark  20000  20days
#           1   data  20000  30days

#########################
#add columns and rows in data frame
import pandas as pd

technologies=[['spark','20000','20days'],['data','20000','30days']]
column_names=["cources","fee","duration"]
row_lable=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_lable)
print(df)
###########
'''o/p: cources    fee duration
a   spark  20000   20days
b    data  20000   30days'''
#################
df.dtypes #PROPERTY(it returns the data type of the column)
'''cources     object
fee         object
duration    object
dtype: object'''


#################
#assign custom type to a column 
types={'cources':str,'fee':float,'duration':str}
df.dtypes

###########
#create data frame from dictionary
#dictionary display in rows and list display in columns
technologies={
    'cources':["spark","pyx","hadoop"],'fees':[2000,23000,24000],'duration':['20days','23days','30days'],'discount':[100,2000,3000]}
df=pd.DataFrame(technologies)
df

########################
#convert dataframe to csv
df.to_csv('data_file.csv')
#create dataframe from csv file
df=pd.read_csv('data_file.csv')
df_new=pd.read_csv('C:/data science/1-python/data_file.csv')

##############################
#install numpy(anacon-prompt-pip install numpy)
#create dataframe with None/null 
import pandas as pd
import numpy as np 
#for column wise use dictionary
techno=({
        'courses':['spark','pyspark','gandoop','python','pandas',None,'spark','python'],
        'fees':[22000,23000,23000,40000,np.nan,25000,23000,22000],'duration':['22days','23day','30day','20day','30day','20day','','20day']
        })
row_lables=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(techno,index=row_lables)
print(df)

#dataframe properties
df.size
df.shape
df.columns
df.columns.values
df.index
df.dtypes
###########
#access one column
df['fees'] #single column only one list

#access two column
df[['fees','duration']]   #access two column list inside list

#select rows from 6
#index start from 0
df2=df[6:]
df2
#ex.,select upto 4 rows and all column

df3=df[:5] 
df3
##################
#access certain cell from column
df['duration'][3]
###################3
#subtracting value from any column
df['fees']-500
df['fees']


#.describe is numerical column 
#describe dataframe
df.describe()
#this function also called as 5 number summary
 
#############################
#rename() -rename pandas dataframe columns
df=pd.DataFrame(techno,index=row_lables)
#assign new header 
df.columns=['A','B','C','D']
df
####################
#code not work properly
#reanme column  names using renam() method
df=pd.DataFrame(techno,index=row_lables)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})
df2=pd.DataFrame(techno,index=row_lables)     
print(df2)
##################################################


import pandas as pd
import numpy as np
techno=({
        'courses':['spark','pyspark','gandoop','python','pandas',None,'spark','python'],
        'fees':[22000,23000,23000,40000,np.nan,25000,23000,22000],'duration':['22days','23day','30day','20day','30day','20day','','20day']
        })
row_lables=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(techno,index=row_lables)
print(df)
df1 = df.drop(['r3','r5'])
df1

#delete rows by position
df1 = df.drop(df.index[[1,3]])
df1

#delete rows by index range
df1 = df.drop(df.index[2:])
df1
##################################
#when you have default indexs for rows
df = pd.DataFrame(techno)
df1 = df.drop(0)
df1
df = pd.DataFrame(techno)
df1 = df.drop([0,3]) #it will delete row0 and row3
df1 = df.drop(range(0,2)) #it will delete 0 and 1
#########################################

#iloc
#select rows by index
import pandas as pd
import numpy as np
techno=({
        'courses':['spark','pyspark','andoop','python','pandas',None,'spark','python'],
        'fees':[22000,23000,23000,40000,np.nan,25000,23000,22000],'duration':['22days','23day','30day','20day','30day','20day','','20day']
        })
row_lables=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(techno,index=row_lables)
print(df)
df1 = df.iloc[2] #select specific index
df1
df1 = df.iloc[[2,3,6]] #select multiple specific rows
df1
df1 = df.iloc[2:] #slice row
df1
df1 = df.iloc[2:5]
df1
df1 = df.iloc[::2] #select by alternate 
df1

##################################
#loc
#select by row labels
import pandas as pd
import numpy as np
techno=({
        'courses':['spark','pyspark','gandoop','python','pandas',None,'spark','python'],
        'fees':[22000,23000,23000,40000,np.nan,25000,23000,22000],'duration':['22days','23day','30day','20day','30day','20day','','20day']
        })
row_lables=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(techno,index=row_lables)
print(df)
df1 = df.loc['r1'] #get r1
df1
df1 = df.loc[['r1','r2','r5']] #get r1, r2, r5
df1
df1 = df.loc['r1':'r5'] #here get all rows r1 to r5
df1
df1 = df.loc[::2] #get alternate rows
df1

##############################################

#pandas select columns by name or index
#by using df[] notation
import pandas as pd
import numpy as np
techno=({
        'courses':['spark','pyspark','gandoop','python','pandas',None,'spark','python'],
        'fees':[22000,23000,23000,40000,np.nan,25000,23000,22000],'duration':['22days','23day','30day','20day','30day','20day','','20day']
        })
row_lables=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(techno,index=row_lables)
print(df)
df2 = df['courses']
df2
df2 = df[["courses","fees","duration"]]
df2
df2 = df.loc[:"fees"]
df2
df2 = df.loc[::2]
df2

#using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
#select multiple columns
df2 = df.loc[:,["courses","fees","duration"]]
df2
#select random columns
df2 = df.loc[:,["courses","fees","duration"]]
df2
#select columns between two columns
df2 = df.loc[:,'fees':'duration']
df2
#select column by range
df2 = df.loc[:,'duration']
df2
#select column by range
#all the column upto duration
df2 = df.loc[:,:'duration']
df2
df2 = df.loc[:,::2]
df2
