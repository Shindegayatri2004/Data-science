# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 16:48:55 2025

@author: Hp
"""

import pandas as pd
import numpy as np

salary=pd.read_csv('C:/2-python_DS/Salary_Data.csv')
print()

import matplotlib.pyplot as plt
import seaborn as sns
salary.head()
sns.displot(salary.Age,kde=True)

sns.displot(salary.Age,kde=True)
#sns.displot(tips.size,kde=True)
sns.jointplot(x=salary.Age,y=salary.Salary,kind='reg') #positive corelation

sns.jointplot(x=salary.Age,y=salary.Salary,kind='reg')
sns.jointplot(x=salary.Age,y=salary.Salary,kind='hex')
sns.pairplot(salary)
sns.pairplot(salary,kind='reg')


salary.Gender.value_counts()
sns.pairplot(salary,hue='Gender')

###########################################################
###########################################################

import pandas as pd
import numpy as np


customer=pd.read_csv('C:/2-python_DS/Mall_Customers.csv')
print()

import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('C:/2-python_DS/Mall_Customers.csv')
df.columns=['cust_id','Gender','Age','annual_salary','spend_score']
df.head
sns.displot(df.Age,kde=True)
df.dtypes
sns.displot(x=df.Age,y=df.annual_salary)
sns.displot(x=df.Age,y=df.spend_score)

sns.displot(df.annual_salary,kde=True)
sns.displot(df.spend_score,kde=True)
df.dtypes

sns.jointplot(x=df.Age,y=df.spend_score)

#histogram for annual salary
plt.hist(df.annual_salary,bins=20,alpha=0.7,edgecolor="black")
plt.title('anual income distribution')
plt.xlabel('anual income')
plt.ylabel('frequency')
plt.show() 

#################################################################

#histogram for spending score
plt.hist(df.spend_score,bins=20,alpha=0.7,edgecolor="black")
plt.title('spending score distribution')
plt.xlabel('spending score')
plt.ylabel('frequency')
plt.show()

####################################################################

#histogram for age vs spending score
plt.scatter(df.Age,df.spend_score,alpha=0.6)
plt.title(' Age vs spending score distribution')
plt.xlabel('Age')
plt.ylabel('spending score')
plt.show()
corr=df.corr(numeric_only=True) #  slightly corelated but in negative direction

##################################################################

#scatter plot with regression line
from numpy.polynomial.polynomial import polyfit
x= df.Age
y=df.spend_score
b,m=polyfit(x,y,1)
plt.scatter(x,y,alpha=0.5)
plt.scatter(x,m*x+b,color='red')
plt.title('Age vs Spending score with trend line')
plt.xlabel('Age')
plt.ylabel('Spending score')
plt.show() # negative regression line

####################################################################

#pairplot scatter matrix(subset of features)
pd.plotting.scatter_matrix(df[['Age','annual_salary','spend_score']],figsize=(8,8))
plt.suptitle('pairwise scatter matrix')
plt.show()

##############################################################

#gender distribution
gender_counts=df.Gender.value_counts()

###################################################

#pie chart
gender_counts.plot(kind='pie',autopct='%1.1f%%',startangle=90)
plt.ylabel('')
plt.title('gender distribution')
plt.show()

##############################################################

#bar chart
gender_counts.plot(kind='bar',color=['skyblue','salmon'])
plt.title('gender count')
plt.show()
corr=df.corr(numeric_only=True) # to show corelation

#corelation heatmap
import numpy as np
import seaborn as sns

corr=df[['Age','annual_salary','spend_score']].corr()
plt.imshow(corr,cmap='coolwarm',interpolation='none') # for colouring purpose
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation=45)
plt.yticks(range(len(corr)),corr.columns)
plt.title('corelation heatmap')
plt.show()

#box plot
plt.boxplot(df.Age)
plt.title('Boxplot:Age')
plt.show()

plt.boxplot(df.spend_score)
plt.title('Boxplot:spending score')
plt.show()







#####################################################################
#####################################################################

# 16 april
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#load dataset
tips=sns.load_dataset('tips')

#histogram of total_bill
plt.hist(tips['total_bill'],bins=20,color='skyblue',edgecolor='black')
plt.title('total bill distribution')
plt.xlabel('total bill')
plt.ylabel('count')
plt.show()

#################################################

#histogram for tip
plt.hist(tips['tip'],bins=20,color='lightgreen',edgecolor='black')
plt.title('total distribution')
plt.xlabel('tip')
plt.ylabel('count')
plt.show()  # right skewed :most of the people giving tip is 2 $

##################################################
# scatter plot of histogram vs total bill
plt.scatter(tips['tip'],tips['total_bill'],color='purple',alpha=0.6)
plt.title('tip vs total_bill')
plt.xlabel('tip')
plt.ylabel('total_bill')
plt.show()
tips.head() #moderately corelate 
#slightly corelate :at one side
#perfectly corelate : at center only
# not at all corelated
####################################################

#simple corelation heatmap
corr=tips.corr(numeric_only=True)
plt.imshow(corr,cmap='coolwarm',interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation=45)

"""
plt.xticks (......)
this function controls the labels on x axis
where the ticks are placed.
what labels are shown
how the labels are rotated and styled.
range(len(corr))
this generates the position for the strick:
    corr is a square matrix (like 3 x 3 if there are 3
                             numeric columns).
    len(corr) gives how many columns and rows are there
    say:3
    range(len(corr)->[0,1,2]-> places the ticks at position 0,
          corr.columns
          these are the labels for those tick position
          ['total_ bill'],'tip','size']
          so now you are labeling tick 0 as 'total bill ,tick 1 as tip
          
          """

plt.yticks(range(len(corr)),corr.columns)
plt.title('corealation matrix')
plt.show()


##############################################
#box plot

plt.boxplot(tips['total_bill'])
plt.title('boxplot-total bill')
plt.show()

plt.boxplot(tips['tip'])
plt.title('boxplot-tip')
plt.show()


############################################
# count of days
tips['day'].value_counts().plot(kind='bar',color='orange')
plt.title('count by day')
plt.xlabel('day')
plt.ylabel('count')
plt.show()   # calculating the days count according to the dataset given tip

#################################################
#count of gender
tips['sex'].value_counts().plot(kind='bar',color='lightblue')
plt.title('count by gender')
plt.xlabel('sex')
plt.ylabel('count')
plt.show() 
"""male customers in higher range as comapre to 
the female customers"""

#################################################
#gender pie chart
tips['sex'].value_counts().plot(kind='pie',autopct='%1.1f%%')
"""
autopct='%1.1f%%' parameter is used in matplilib pie()
function to display the percentage value on each slice of a pie chart

breakddown of %1.1f%%'
% starts the formating string
1.1f means: 1= minimum width of the number (not strictly
                                            neededed)
format the number as float with 1 decimal value"""

plt.title('Gender distribution')
plt.ylabel('')

"""even though pie chart not uses y axis
matplotlib still has that axis object in the background. so
 setting ylable('') just makes .sure nothing is dispalyed there.
 """
plt.show()

######################################################################
######################################################################

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

salary=pd.read_csv('C:/2-python_DS/Salary_Data.csv')
salary.head()
salary1=salary.rename({'Education level':'educational_inf','job title':'heading'})
salary1
salary.dtypes

############################################################

#histogram of age
plt.hist(salary1['Age'],bins=20,color='skyblue',edgecolor='black')
plt.title('Age data distribution')
plt.xlabel('Age')
plt.ylabel('frequency')
plt.show()

###############################################################

#histogram of salary
plt.hist(salary1['Salary'],bins=20,color='skyblue',edgecolor='black')
plt.title('Salary data distribution')
plt.xlabel('Salary')
plt.ylabel('frequency')
plt.show()

###############################################################

# scatter plot of age vs salary
plt.scatter(salary1['Age'],salary1['Salary'],color='purple',alpha=0.6)
plt.title('age vs salary')
plt.xlabel('Salary')
plt.ylabel('total_bill')
plt.show()
salary1.head()

################################################################

#simple corelation heatmap
corr=salary1.corr(numeric_only=True)
plt.imshow(corr,cmap='coolwarm',interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)),corr.columns,rotation=45)

plt.yticks(range(len(corr)),corr.columns)
plt.title('corealation matrix')
plt.show()

#################################################################

#box plot
plt.boxplot(salary1['Salary'])
plt.title('boxplot-salary')
plt.show()

plt.boxplot(salary1['Age'])
plt.title('boxplot-Age')
plt.show()

##################################################################
##################################################################

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df=pd.read_csv('C:/2-python_DS/fdata.csv')
df.head()
df1=df.rename({'high':'High','low':'Low'})
df1
df.dtypes






