# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:30:58 2025

@author: Hp
"""
#########################################
'''
GCD=gretest common divisor
euclidean algorithm
'''
def gcd(a,b):               ##by euclidean method
    while b:
        a,b=b,a % b
    return a

num1=int(input("enter first number:"))
num2=int(input("enter secound number:"))
## Output
ans=gcd(num1,num2)
print(f"GCD of {num1} and {num2} is:{ans}")

################################################
## With math function
import math
num1=int(input("enter first number:"))
num2=int(input("enter secound number:"))
ans=math.gcd(num1,num2)
print(f"GCD of {num1} and {num2} is:{ans}")

###############################################
## finding secound largest element in the list
def secound_largest(lst):
         n=len(lst)
         for i in range(n-1):
             for j in range(n-i-1):
                 if lst[j]>lst[j+1]:
                     lst[j],lst[j+1]=lst[j+1],lst[j]
         return lst
                 
lst=[2,8,6,4,1]
secound_largest(lst)
print(lst[-2])   ##secound largest
print(lst[+1])    ## secound smallest

##############################################
## secound largest in array 
def secound_largest(lst):
    unique_num=list(set(lst))
    unique_num.sort(reverse=True)
    if len(unique_num)>1:
        return unique_num[1]
    else:
        return None
    
lst=[10,30,40,60,10,70]
print("secound largest:",secound_largest(lst))
        
#########################################
## secound smallest
def secound_smallest(lst):
    unique_num=list(set(lst))
    unique_num.sort()
    if len(unique_num)>1:
        return unique_num[1]
    else:
        return None

lst=[100,40,50,10,70,90]
print("secound smallest:",secound_smallest(lst))

###############################################
## Finding missing numbers
def missing_num(lst,n):
    expected_num=n*(n+1)//2
    actual_num=sum(lst)
    missing_num=expected_num-actual_num
    return missing_num
lst=[1,2,4,5,6]
n=6
print("missing number:",missing_num(lst,n))

##############################################
## reverse the string
def rev_string(s):
    rev_s=s[::-1]
    return rev_s
s="My name is anthony"
rev_s=rev_string(s)
print(rev_s) 

rev_stringg=(input("enter new string"))
rev_s=rev_string(rev_stringg)
print(rev_s)           

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

#############################