# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 08:18:19 2025

@author: Hp
"""

#5.	Using the tips dataset from Seaborn:
#•	Create a scatter plot showing the relationship between total_bill and tip.
#•	Color the points by sex and vary the size by size (number of people at the table).
#•	Add titles and axis labels.

import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
tips.head()

sns.jointplot(x=tips.tip,y=tips.total_bill,kind='reg')
plt.xlabel('X-LABEL')
plt.ylabel('Y-LABEL')
plt.title('scatter plot')
plt.show()

#########################################################################
#4.	Create a line chart showing the monthly average temperature of a city over a year.
#•	x-axis: Months (January to December)
#•	y-axis: Temperature (in Celsius)
#•	Add a title, axis labels, and gridlines.
#•	Customize the line style (e.g., dashed, color, markers)

import matplotlib.pyplot as plt

months=['jan','feb','march','april','may','june','july','aug','sep','oct','nov','dec']
temp=[123,120,140,240,300,200,100,200,100,250,150,130]
plt.plot(months,temp,color='red',linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)

plt.plot(months, temp)
plt.xlabel('months')
plt.ylabel('temperature')
plt.title('line plot')
plt.show()

################################################################
#2.	Visualize the distribution of test scores for students from three different schools.
#•	Data includes score and school columns.
#•	Use a box plot to compare distributions.

import matplotlib.pyplot as plt
score=[120,130,140,110,150]
school=['KBP','ABC','SND']

plt.boxplot(score,school)
plt.xlabel('X-AXIS')
plt.ylable=('Y-AXIS')
plt.title('box plot')
plt.show()

###########################################################################
#1.	Create a heatmap of a correlation matrix for a dataset with numerical features.
#•	Use the iris dataset from Seaborn.
#•	Display the correlation matrix as a heatmap with annotations.

import matplotlib.pyplot as plt
import seaborn as sns
iris=sns.load_dataset('iris')
iris.head()

sns.heatmap(iris.corr(numeric_only=True),annot=True)
iris.describe()

########################################################################
#3.	Plot a bar chart showing the number of products sold by a store across five different categories.
#•	Categories: Electronics, Clothing, Groceries, Furniture, Toys
#•	Add color to each bar.
#•	Rotate x-axis labels and annotate the bars with their values.
#Note: Use below data
#categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
#sales = [150, 200, 300, 120, 90]
#colors = ['blue', 'green', 'orange', 'red', 'purple']

import matplotlib.pyplot as plt
import seaborn as sns

categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture', 'Toys']
sales = [150, 200, 300, 120, 90]
colors = ['blue', 'green', 'orange', 'red', 'purple']

plt.bar(categories,sales,color=colors)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
measurements=np.random.normal(loc=20,scale=5,size=100)
stats.probplot(measurements,dist="norm",plot=plt)
plt.show()







