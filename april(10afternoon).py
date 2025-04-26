# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:19:46 2025

@author: om
"""

import pandas as pd
tech = {'courses':["spark","pyspark","python","pandas"],
        'fee':[20000,22000,25000,23000],
        'duration':['30days','20days','25days','28days']
        }
index_label = ['r1','r2','r3','r4']
df1 = pd.DataFrame(tech, index = index_label)
df1
tech2 = {'courses':["spark","java","python","go"],
         'discount':[2000,2300,2400,2000]}
index_label2 = ['r1','r2','r3','r4']
df2 = pd.DataFrame(tech2, index = index_label2)
df2

#pandas join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right")
df3

#######################################
#pandas inner join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')
df3

#############################
#pandas outer join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how='outer')
df3

#using pandas merge()
df3 = pd.merge(df1, df2)
df3

#using dataframe merge()
df3 = df1.merge(df2)
df3

##################################

import pandas as pd
tech1 = {"courses":["spark","pyspark","python","pandas"],
       "fees":[20000,25000,22000,24000]}
df1 = pd.DataFrame(tech1)
df1
tech2 = {"courses":["pandas","hadoop","hyperion","spark"],
         "fees":[25000,24000,22000,21000]}
df2 = pd.DataFrame(tech2)
df2

data = [df1, df2]
df3 = pd.concat(data)
df3

###########################################

import pandas as pd
tech1 = {"courses":['spark','pyspark','python','pandas'],
         "fees":[20000, 25000, 22000, 24000]}
df1 = pd.DataFrame(tech1)
df1

tech2 = {"courses":["unix","hadoop","hyperion","java"],
         "fees":[25000,25000,24000,24000]}
df2 = pd.DataFrame(tech2)
df2
tech3 = {"duration":["30daya","40days","35daya","60days","55days"],
         "discount":[1000,2300,2500,2000,3000]}
df3 = pd.DataFrame(tech3)
df3

data = [df1, df2, df3]
df4 = pd.concat(data)
df4
#################################


#read csv file into dataframe
df = pd.read_csv('courses.csv')
df

#write dataframe to excel file
df.to_excel('C:/3-python_for_DS/courses.xlsx')
#####################################
df = pd.read_excel('C:/3-python_for_DS/courses.xlsx')
df