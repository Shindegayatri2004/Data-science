# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 09:31:21 2025

@author: Hp
"""

#####################################
## lcm of two numbers

num1=int(input("enter first number:"))
num2=int(input("enter secound number:"))
def gcd(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return num1

gcd(num1,num2)
def lcm(num1,num2):
    lcm=abs(num1*num2)/gcd(num1,num2)
    return lcm
lcm(num1,num2)    #lcm(12,18=36.0)

##################################################

