# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 08:05:23 2025

@author: Hp
"""

"""
matplotlib: to visualize data 
matplotlib is old and seaborn is new
data types
numerical:visualization ,23,23.4
(histograph,pair plots,join plots,box plot)
chatarotical:male ,female,animals
(count plot,bar graph,pie diagram)
EDA :visualize data ,preprocessing data,model.

bell shaped
right/+ srewed data
left /- srewed data
"""

import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
tips.head()
sns.displot(tips.total_bill,kde=True)
""" the distribution is right-skewed (possitively skewed)
-meaning most total bills are on the lower side(left),
but there are a few large bills that stretch the 
distribution to the right.this is typical restaurant or 
service data ,wheree the most meals fall within an average
range,but a few partis may spend much more"""

sns.displot(tips.tip,kde=True)
#sns.displot(tips.size,kde=True)
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='reg') #positive corelation

'''
scatter plot(center):
each plot represents one observation(a customers bill and the 
corresponding tip) there is positive corelation: as the total
bill increases ,the tip tend to increse as well. howerver,
the increse is not perfectly linear-some variation exists
especiallynfor higher bills .histogram on the x -axis(top):
show the distribution of the tip amount, most tips falls between  
2 and 4.with fever tips at the higher end.
histogram of the y axis(right):
show the distribution of the total bill.the majority
of bills are in the 10 - 20 range.'''

sns.jointplot(x=tips.tip,y=tips.total_bill,kind='reg')
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex')
sns.pairplot(tips)
sns.pairplot(tips,kind='reg')

""" total bill vs size 
positive correlation: 
   the tip amount generally increasaes the points are fairly
   spread but there visible upward trend
   
   total bill vs size
   weak positive corellation: larger group sizes trend
   to have higher total bills.
   still,there a lot of overlap-small
   groups can also have high bills.
   tip vs size
   weak correaltion: bigger group dont always gave higher tips.
   most tips,even in larger groups,still hover around $2.5
   """

tips.time.value_counts()
sns.pairplot(tips,hue='time')

"""size(party size)
total bill distribution: 
dinner(orange) bill tend to the higher than lunch
(blue) bills.dinner show winder spread,peaking higher around the 15-20 range.
lunch bill are more tightly clustered under $ 20.
tip distribution:
tips during dinner are also genreally higher than those at lunch.
the distribution for dinner is broader and more positively skewed.
size distribution:
dinner has larger party sizes overall"""

sns.pairplot(tips,hue='day')

""" total bill distribution:
saturday(green) shows the highest frequency of larger bills.
sunday(red) follows closely with a broad range of bills.
friday(orange) has narrower spread.
indicating fewer total_bills,mostly lower.
thursday(blue) is more consisitant but less frequent
than weeakends.
tip distribution:
    tip follows a similar trend to total  bills"""

sns.heatmap(tips.corr(numeric_only=True),annot=True)
#corelation ranges from -1 to +1
sns.boxplot(tips.total_bill)
#there are outliers in total_bill
sns.boxplot(tips.tip)
sns.countplot(tips.day)

sns.countplot(tips.sex)

tips.sex.value_counts().plot(kind='pie')
tips.sex.value_counts().plot(kind='bar')

sns.countplot(data=tips[tips.time=='Dinner'],x='day')
sns.countplot(data=tips[tips.time=='lunch'],x='day')


fg=sns.FacetGrid(tips,row='smoker',col='time')
fg.map(sns.histplot,'total_bill')

""" tis is facet grid of histogram ,showing the distribution of total_bills
across different smoking statues and time of the day 
(lunch vs dinner)
top-left:smokers during lunch
top-right:smokers during dinner
bottom_left: non- smokers during lunch
bottom_right:non-smokers during dinner
smokers vs non -smokers
dinner(top-right vs bottom-right):
    both smokers and non smokers shows similar bill"""







import matplotlib.pyplot as plt
import seaborn as sns
Salary_Data=sns.load_dataset('Salary_Data')
Salary_Data.head()
sns.displot(Salary_Data.Salary,kde=True)


