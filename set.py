# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 09:14:56 2025

@author: Hp
"""

""" program to remove items from the set"""
st={1,4,6}
st.remove(4)
print(st)

#########################################
""" program to find intersection of set"""
st1={1,4,6}
st2={2,4,6}
st=st1&st2
print(st)

##############################################
""" program to create union of set1"""
st=st1|st2
print(st)

##############################################
for x in range(1,16):
    print(x,x*x)
    
############################################
dict={x:x*x for x in range(1,16)}
print(dict)

##############################################
""" program to find maximum and minimum of set """
max_set=max(st)
print(max_set)
min_set=min(st)
print(min_set)

##################################################
"""string is palindrome or not"""
text="madam"
text1=text[::-1]
if text==text1:
    print("string is palindrome")
    
#################################################
"""printing 5 times times first two letters"""
text="wipro"
text1=text[:2]
final=text1*len(text)
print(final)

##################################################
""" given a string,if 1 and last letters is x ,then display
the string without x ,else print as it is"""

text="madam"
if(text[0]=="m" and text[-1]=="m"):
    final=text[1:-1]
    print(final)
else:
    print(text)
    
text="nayan"
if(text[0]== text[-1]):
    final=text[1:-1]
    print(final)
else:
    print(text)

##################################################
""" return string in mode of repetations ,printing last letters 3 times """
text="wipro"
text1=text[2:]
final=text1*len(text)
print(final)

text="wipro"
n=3
text1=text[2:5]
final=text1*n
print(final)

####################################################

""" take otp and check whether it si numeric and 6 digits 
if valid print ok else not valid"""
otp=input("enter the otp")
if otp.isdigit() and len(otp)==6:
    print("ok")
else:
    print("invalid")

################################################
"""validating password (letters are allowed but not special characters)
lenghth more than 8 characters ,print valid else in valid"""

password=input("enter the password")
if password.isalpha() and len(password)>=8:
    print("valid")
else:
    print("invalid")
