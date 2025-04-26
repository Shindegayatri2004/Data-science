# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 15:07:45 2025

@author: Hp
"""

"""write python program to drwa a line with suitable label 
in the x- axis ,y axis and a title"""

import matplotlib.pyplot as plt
x=range(1,50)
y=[value *3 for value in x]
print("value of x:")
print(*range(1,50))
print("values of y (thrice of x):")
print(y)
 # plot lines and/or markers to the axes
plt.plot(x,y)

#set axis lable to current axis
plt.xlabel('x-axis')

#set the y axis label of the current axis
plt.ylabel('y -axis')

#set a title
plt.title('Draw a line')

#display figure
plt.show()

##################################################################
"""write a python program to draw line  useing suitable 
given axis values with suitable label index x axis and y axixs """

import matplotlib.pyplot as plt
# x axis value 
x=[1,2,3]
#y axis value
y=[2,4,1]
#plot lines and/or markers to the axes
plt.plot(x,y)
#set the  x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label to current axis
plt.ylabel('y-axis')
#set the title
plt.title('sample graph!')
#display figure
plt.show()

###################################################
#write a python program to draw line charts of
#the financial data of alphabet inc.
#between oct 3, 2016 to oct 7, 2016
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/3-python_for_DS/fdata.csv")
df.plot()
pd.show()


################################################################

#write python program to plot two or more lines with legends,
#differenet width and colours

import matplotlib.pyplot as plt

x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('two or more lines with different widths and colours')

plt.plot(x1,y1,color='blue',linewidth=3,label='line1-width-3')

plt.plot(x2,y2,color='red',linewidth=5,label='line2-width-5')

#show legends
plt.legend()

plt.show()

#################################################################


import matplotlib.pyplot as plt

x1=[10,20,30]
y1=[20,40,10]

#line 2 points
x2=[10,20,30]
y2=[40,10,30]

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.plot(x1,y1,color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2,color='red',linewidth=5,label='line2-dashed',linestyle='dashed')

plt.legend()
plt.show()

######################################################################
""" write a python program to plot two or more liness and set
the line markers"""

import matplotlib.pyplot as plt

x=[1,4,5,6,7]
y=[2,6,3,6,3]

plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)

#set the y limits of current axis
plt.ylim(1,8)
#set x limits of current axis
plt.xlim(1,8)
#naming x-axis
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('dispaly markerr')
plt.show()

###############################################################
#write python program to plot several lines with different format styles in one command
#using array

import numpy as np
import matplotlib.pyplot as plt 

t=np.arange(0.,5.,0.2)

plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
"""'g---':green(g) dashed line(--)
t,t**2,'bs'
x=t,y=t**2(squares)
'bs'=blue(b)squares(s) as markers
plots t2 as blue squares

t,t**3,'r^'
x=t,y=t**3(cubes)
'r^'=red(r) triangle-up markers(^)
"""

plt.show()

#################################################################
#use of plt.xticks

import matplotlib.pyplot as plt

x_pos=[0,1,2,3]
x=['apple','banana','mango','orange']
plt.bar(x_pos,[10,15,7,12])
plt.xticks(x_pos,x)
plt.ylabel('quantity')
plt.title('fruit stock')
plt.show()
#########################################################
#use of plt.xticks
import matplotlib.pyplot as plt

x_pos = [0,1,2,3]
x=['Apple','Bannana', 'mango', 'orange']

plt.bar(x_pos, [10, 15, 7, 12])
plt.xticks(x_pos, x)
plt.ylabel('quantity')
plt.title('fruit stock')
plt.show()


##################################################################

#write a python program to  display a bar chart
#of the popularity of programming languages
import matplotlib.pyplot as plt
x = ['java', 'python', 'javascript', 'c#', 'c++']
popularity = [22.2, 17.6, 8.8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
"""
x_pos = [i for i, _ in enumerate(x)]
this create a list of index positions for each lang

enumerate(x) gives (index, lnang) pairs:

(0, 'java'), (1, 'python'),...,(5,'c++')

[i for i, _ in enumerate(x)] extract just indices

x_pos = [0,1,2,3,4,5]
"""
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("language")
plt.ylabel("popularity")
plt.title("popularity of programming language\n"+"worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
plt.show()

################################################################
import matplotlib.pyplot as plt
x = ['java', 'python', 'javascript', 'c#', 'c++']
popularity = [22.2, 17.6, 8.8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("popularity")
plt.ylabel("language")
plt.title("popularity of programming language\n"+"worldwide, oct 2017 compared to a year ago")
plt.xticks(x_pos,x)
plt.show()

###############################################################

import numpy as np
import matplotlib.pyplot as plt

n_groups=5
men_means=(22,30,33,30,26)
women_means=(25,32,30,35,29)
#create plot
fig,ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8
rects1=plt.bar(index,men_means,bar_width,alpha=opacity,color='g',label='men')
rects2=plt.bar(index+bar_width,women_means,bar_width,alpha=opacity,color='r',label='women')

plt.xlabel('person')
plt.ylabel('scores')
plt.title('scores by person')
plt.xticks(index+bar_width,('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()

##################################################################




















