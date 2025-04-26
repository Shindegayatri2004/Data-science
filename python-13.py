# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 08:18:25 2025

@author: Hp
"""

"""find password .
stable numbers:if each of the digit occurs same number of times then it is stable
ex:1221,13,2002
unstable:
    ex:123,122,34445"""
    
from collections import Counter
def find_password(input1,input2,input3,input4,input5):
    def is_stable(number):
        digit_counts=Counter(str(number)).values()
        unique_counts=set(digit_counts)
        only_one_unique_count=len(unique_counts)==1
        
        return only_one_unique_count
    numbers=[input1,input2,input3,input4,input5]
    stable_sum=sum(num for num in numbers if is_stable(num))
    unstable_sum=sum(num for num in numbers if not is_stable(num))
    return stable_sum - unstable_sum

input1,input2,input3,input4,input5 = 12,1313,122,678,898
password=find_password(input1,input2,input3,input4,input5)
print("Password:",password)

##################################################################
""" for input n print following pattern 
ex : n=4
1222
2333
3444
4555"""

n=int(input("enter the number:"))
for i in range(n):
    print(i+1,end="")
    for j in range(n-1):
        print(i+2,end="")
    print("")
    
##############################################################

""" reverse string without using python in-build functions"""

def reverse_string(s):
    return s[: : -1]

input_string="AbcdE"
output_string=reverse_string(input_string)
print(output_string)

######################################################

def reverse_stringe(s):
    return ''.join(s[i] for i in range(len(s)-1,-1,-1,-1))

input_string="AbcdE"
output_string=reverse_string(input_string)
print(output_string)

##########################################################
""" write program to generate pascal triangle"""
def pascal_triangle(n):
    triangle=[] # craete an empty list to store rows.
    
    for i in range(n):
        row=[1]  # every row start with 1
        if i > 0:
            for j in range(1,i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle

# function to print pascal triangle
def print_triangle(triangle):
    for row in triangle:
        print(*row)
        
#input:number of rows        
n=int(input("enter the number of rows:"))
triangle=pascal_triangle(n)
print_triangle(triangle)

###################################################












    
    
    
    
    
    
    
    
    