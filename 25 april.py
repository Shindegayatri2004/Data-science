# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 08:31:33 2025

@author: Hp
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create the dataframe
data={
      'person name':['rob','tom','xi','mohan','pooja','soham'],
      'credit score':[750,310,475,600,820,780],
      'income':[3000,5000,6000,7000,8000,9000],
      'age':[32,34,10,23,45,56],
      'loan aproved':['Y','N','Y','N','Y','N']
      }

df=pd.DataFrame(data)

#apply log transformation to income
df['log_income']=np.log(df['income'])

#plotting
plt.figure(figsize=(10,6))

# original income
plt.bar(df['person name'],df['income'],color='skyblue',label='original income')

#log trnasformed income(ploted next to original) 
plt.bar(df['person name'],df['log_income']*1000,color='orange',alpha=0.7,label='log(income)x 10000')
plt.xlabel('person name')
plt.ylabel('income')
plt.title('original vs log transformed income')
plt.legend()
plt.grid(True,linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()

###################################################################3

"""
use case:salaries
mean salary=40000
standard deviation=10000
we want to konw:
    what percentage of data lies betweeen 10000 and 70000
    
    the range is u+-3sigma
    u+-3sigma ,so we will use chebysheves ineuality property
    """
    
def chebyshev_inequality(mu,sigma,lower_bound,upper_bound):
    # calculate number of SD
    k=min(abs(lower_bound-mu),abs(upper_bound-mu))/sigma;
    
    """
    start with your range (e.g,from 10 k to 70k salaries):
        lower_bound=10
        upper_bound=70
        know your average and SD
        mu=40(mean)
        sigma=10(standard deviation)
        
    """
    #apply chebyshevs ineuality
    probability=1-(1/k**2)
    
    #format the result'
    return round(probability*100,2),k
"""
if probability=0.8888
then probability *100=88.88
then round(88.88,2)ensures its round to 2
decimal places ,like 88.89
"""
#inputs from the slide
mean_salary=40000
std_dev_salary=10000
lower=10000
upper=70000

percent,k_val=chebyshev_inequality(mean_salary,std_dev_salary,lower,upper)
print(f"according to chebyshevs in equality:")
print(f"at least {percent} % of salaries lie between ${lower} and ${upper}")
print(f"(tis range is +-{int(k_val)}standard deviations from the mean)")



