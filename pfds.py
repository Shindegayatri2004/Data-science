# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:48:49 2025

@author: Hp
"""

#dataframe

#create using constructor
#create pandas DataFrame from list

import pandas as pd 
technologies = [["spark",20000,"30days"],
                ["pandas",20000,"40days"],
                ]
df=pd.DataFrame(technologies)
print(df)
##############################################

#since we have give label to column and row
import pandas as pd 
column_names=["Courses","fee","Duration"]
technologies = [["spark",20000,"30days"],
                ["pandas",20000,"40days"],
                ]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)

df.dtypes
########################################################

#you can also assign custom
#dat types to column
#set custom type to dataframe
types={'courses':str,'fee':float,'duration':str}
df.dtypes

########################################################
#create dataframe from dictionary
import pandas as pd 
technologies={
    'courses':["spark","pyspark","hadoop"],
    'fee':[20000,50000,80000],
    'Duration':['30 days','20 days','80 days'],
    'discount':[1000,3000,4000]
    }
df=pd.DataFrame(technologies)
df

#######################################################
#converting dataframe to csv
df.to_csv('data file.csv')

########################################################
#create dataframe from csv file
df=pd.read_csv('data file.csv')
df=pd.read_csv('C:/1-python/data file.csv')

######################################################
#pandas dataframe-basic operations
#create dataframe with none to wok with examples

import pandas as pd
import numpy as np
technologies=({
    'courses':["spark",None,"pandas","numpy","hadoop","pyspark","sspark","ppython"],
    'fee':[1000,2000,3000,4000,np.nan,6000,7000,80000],
    'Duration':['10 days','20 days','30 days','40 days','50 days','60 days','70 days','80 days'],
    'discount':[10,20,30,40,50,60,70,80]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']

df=pd.DataFrame(technologies,index=row_labels)
print(df)

#########################################################
#dataframe properties

df.shape  #(8,4)
df.size    #32
df.columns
df.columns.values
df.index
df.dtypes

#####################################################
#accesing one column contents
df['fee']

#accesing two columns contents
df[['fee','Duration']]

#Select certain rows and assign it to another
df2=df[:6]
print(df2)
df3=df[:]
print(df3)
df4=df[-1: :]
print(df4)
df5=df[:5  ]
print(df5)

#accesing certain cell from column duration
df['Duration'][3]

#subtracting specific value  from column
df['fee']=df['fee']-500
df['fee']

#pandas to mainpulate dataframe
#describe dataframe
#describe datframe for all numeric columns
#its is an function for 5 number summary (interview)
df.describe()

#rename()-rename pandas dataframe column
df=pd.DataFrame(technologies,index=row_labels)
#assign new header by setting new column names
df.columns=['A','B','C','D']
df

####################################################
#rename column names using rename() method
import pandas as pd
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'C3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})

###################################################
#drop datframe rows and colunmns
import pandas as pd
import numpy as np
technologies=({
    'courses':["spark",None,"pandas","numpy","hadoop","pyspark","sspark","ppython"],
    'fee':[1000,2000,3000,4000,np.nan,6000,7000,80000],
    'Duration':['10 days','20 days','30 days','40 days','50 days','60 days','70 days','80 days'],
    'discount':[10,20,30,40,50,60,70,80]
    })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']

df=pd.DataFrame(technologies,index=row_labels)
df
df=pd.DataFrame(technologies,index=row_labels)
#drop rows by labels
df1=df.drop(['r1','r2'])
df1
df=pd.DataFrame(technologies,index=row_labels)
#delete rows by position
df1=df.drop(df.index[[1,3]])

#delete rows by index range
df1=df.drop(df.index[2:])
df1

#when you have default indexs for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1

df=pd.DataFrame(technologies)
df1=df.drop([0,3])  #it will delete row 0 n row 3
df1=df.drop(range(0,2)) #it will delte 0 and 1
###########################################################
#pandas select rows by index(position/label)

df=pd.DataFrame(technologies,index=row_labels)
#below are quit examples
#select rows by integer index
df2=df.iloc[2]                 # select row by index
df2=df.iloc[[2,3,6]]          # select rows by index list
df2=df.iloc[1:5]            #select rows by integer index range
df2=df.iloc[:3]           #select 1 3 rows
df2=df.iloc[:1]            # select 1  row
df2=df.iloc[-1:]             #last row
df2=df.iloc[-3:]               #last 3 row
df2=df.iloc[::2]                #select alternate rows

#select rows by index labels
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']

df2=df.loc['r2'] 
df2              #select index by index label
df2=df.loc[['r2','r3','r6']]   #select row by index label
df2=df.loc['r1':'r5']        #select row by by label index range
df2=df.loc['r1':'r5':2]       #select alternate rows

#####################################################
#pandas select colunmns by name or index
#by using df ()notation

df2=df['courses']
#select multiple colunms
df2=df[["courses","fee","Duration"]]

df2=df.loc[:,["courses","fee","Duration"]] #multiple colunms
df2=df.loc[:,["courses","fee","discount"]] # range columns

#select columns between two columns
df2=df.loc[:,'fee':'discount']

#select columns by range
df2=df.loc[:,'Duration':]

#all the columns up to duration
df2=df.loc[:,:'Duration']

# SELECT EVERY ALETRNATE COLUMN
df2=df.loc[:,::2]

######################################################
import pandas as pd

df=pd.read_csv('C:/2-python_DS/melb_data.csv')
print()

#slicing
df2=df.iloc[2]                 # select row by index            #select rows by integer index range
df2=df.iloc[:3]           #select 1 3 rows
df2=df.iloc[-1:]             #last row
df2=df.iloc[-3:]               #last 3 row
df2=df.iloc[::2]  

#properties
df.shape  
df.size    
df.index
df.dtypes
df.describe()

column_names=["address","rooms","types"]
row_labels=["A","B","C"]
df=pd.DataFrame(index=row_labels)

































