# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 09:14:15 2025

@author: Hp
"""

# -- coding: utf-8 --
"""
Created on Thu Apr  3 08:26:33 2025

@author: 
"""


lst=[f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)
################################################
set_one={x for x in range(3) }
print(set_one)
####################################
dict={x:x*x for x in range(5)}
print(dict)
######################################
#Generator
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
##################################
gen=(x for x in range(4))
next(gen)
##############################
#function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
#########################
gen=range_even(6)
next(gen)    #0
next(gen)   #2
next(gen)   #4
####################################
#let us hide password entered on screen
#chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
""" ele* is a palceholder for an element form an iterable.
(*) is likely a wildcard charcter use to represent in palce of 
charcter
For instance,if you iterating over list of element"""
passwords=["not-good","give'm-pass","00100-100"]
for password in hide(lengths(passwords)):
    print(password)
    
########################################

#printing list with index
lst=["milk","egg","bread","tea","biscuit"]
for index in range(len(lst)):
    print(f"{index+1}:{lst[index]}")
#enumerate
lst=["milk","egg","bread","tea","biscuit"]
for index,item in enumerate(lst,start=1):
    print(f"{item}:[{index}]")
    
#########################################
#use of zip function witn mis match list
name=["dada","mama","kaka","baba"]
info=[9404,6789,7890,7890]
for nm,inf in zip(name,info):
    print(nm,inf) 
    
#########################################
##zip longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,3297]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

#############################################

#use of fill value insted none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9850,6032,3297]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

################################################
"""use of all(),if all values are true then it will produce 
output"""
lst=[2,3,-6,8,9]
if all(lst):
    print('all values are true')
else:
    print('there are null values')
    
lst=[2,3,0,8,9]
if all(lst):
    print('all values are true')
else:
    print('there are null values')
    
#################################################
# use of any if any one non zero value
lst=[0,0,0,-8,0]
if any(lst):
    print("it has some non zero values")
else:
    print("useless")
    
# use of any
lst=[0,0,0,0,0]
if any(lst):
    print("it has same non zero values")
else:
    print("it has all null values in the list")
    
####################################################
#count()
from itertools import count 
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

###########################################

# now let us start from 1
from itertools import count 
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

##################################################
#cycle()
#suppose you have repeated tasks to be done ,then you can 

import itertools
intructions=("Eat","Code","Sleep")
for intruction in itertools.cycle(intructions):
    print(intruction)

##############################################





























































