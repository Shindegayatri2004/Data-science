# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 08:13:19 2025

@author: Hp
"""
# two types of path file:1] absolute addresss 2] relative address

a=10
b=0
# THROWS ARITHMATIC ERROR
try:
    result=a/b 
except ZeroDivisionError:
    print("cannot divide by zero!")

################################################

a=int(input("enter the numbers"))
b=int(input("enter the numbers"))
# THROWS ARITHMATIC ERROR
try:
    result=a/b 
except ZeroDivisionError:
    print("cannot divide by zero")
    
#################################################
#index error
numbers=[1,2,3]
try:
    print(numbers[5])
except IndexError:
    print("index out of range")

##############################################
"""handling exceptions without naming"""

try:
    numerator=50
    denom=int(input("enter the number"))
    quotient=(numerator/denom)
    print("division performded successfully")
except ValueError:
    print("only integer sholud be interded")
except:
    print("OOPS.........some exceptions raised")
    
##################################################
"""handling exceptions with try...except... else..."""
try:
    numerator=50
    denom=int(input("enter the number"))
    quotient=(numerator/denom)
    print("division performded successfully")
except ZeroDivisionError:
    print("Denominator as zero is not allowed")
except ValueError:
    print("only integer sholud be entered")
else:
    print("Result of the divicion operation is:",quotient)
    
####################################################
""" handling exceptions with try...except... else...finally"""
try:
    numerator=50
    denom=int(input("enter the number"))
    quotient=(numerator/denom)
    print("division performded successfully")
except ZeroDivisionError:
    print("Denominator as zero is not allowed")
except ValueError:
    print("only integer sholud be entered")
else:
    print("Result of the divicion operation is:",quotient)
finally:
    print("over and out")
    
####################################################
#file not found error
with open('C:/1-python/py_digits.txt','r')as file:
    contents=file.read()
print(contents.rstrip()) ## to remove space
#################################################

try:
    with open('C:/1-python/py_digit.txt','r')as file:
        contents=file.read()
except FileNotFoundError:
    print("file not found")
        
###############################################
##permission error
with open('C:/1-python/py_digits.txt')as file:
    contents=file.read()
print(contents.rstrip())

#################################################
"""permission error with try and except"""
try:
    with open('C:/1-python/py_digits.txt')as file:
        contents=file.read()
    print(contents.rstrip())
except PermissionError:
    print("permission error occured")
    
#################################################
#attribute error
obj=None
print(obj.some_attribute) ###attribute error

#############################
if obj is not None:
    print(obj.some_attribute)
else:
    print("object is None!")

###############################################
"""memory error"""
huge_list=[1]*(10**10)

#########################################
""" Handling using generator"""
def generate_numbers():
    for i in range(10**10):
        yield i
gen =generate_numbers()
print(next(gen))

###############################################
#recursive error

def recursive_function():
    return recursive_function()
recursive_function()

##########################################
""" file handling """
"""recursion"""
import sys
sys.setrecursionlimit(1000) #set recursion limit

def safe_recursive_function(depth=0,max_depth=10):
    if depth>=max_depth:
        return "Done"
    return safe_recursive_function(depth+1,max_depth)
print(safe_recursive_function())
    
############################################
#write program to read first n line from the text file.
with open('C:/1-python/py_digits.txt','r')as file:
    lines=file.readlines()
    if lines:
        print("first line:",lines[0].strip())
        print("last line:",lines[-1].strip())

#############################################
""" write program to accept input from user and append it"""
filename='C:/1-python/programming.txt'
with open(filename,'w')as file:
    file.write("I love programming.\n")
    file.write("I love creating new games.\n")
    in_line=input("enter the line")
    file.write(in_line)

##################################################
"""write a program to  read contents from a text file line by line"""
""" line and store each line into a list"""

filename='C:/1-python/py_digits.txt'
with open(filename) as file :
    lines=file.readlines()
    pi_string=[]
    for line in lines:
        pi_string.append(line.rstrip())
        print(pi_string)
    print(len(pi_string))
    
###################################################
"""write a program to find  longest word from the text file"""
filename='C:/1-python/programming.txt'
with open (filename,'r') as file:
    lines=file.readlines()
    longest_word=''
    for line in lines:
        words=line.split()
        for word in words:
            if(len(word)>len(longest_word)):
                longest_word=word
print("the longest word:",longest_word)
 
#########################################################
"""write a program to find  smallest word from the text file"""
filename='C:/1-python/programming.txt'
with open (filename,'r') as file:
    lines=file.readlines()
    smallest_word=None
    for line in lines:
        words=line.split()
        for word in words:
            if(smallest_word is None or len(word)<len(smallest_word)):
                smallest_word=word
print("the smallest word:",smallest_word)

###############################################
""" write a program to count the frequency of a user entered text file"""
filename='C:/1-python/programming.txt'
input_line=input("enter the text:")
words=input_line.split()
word_count=len(words)

# write user input to file
with open(filename,'w')as file:
    file.write(input_line)

# display the word count
print("the total words entered:",word_count)

###############################################
# write program to accept the two numbers from user and perform division.
try:
    num1=float(input("enter number1"))
    num2=float(input("enter number2"))
    num=num1/num2
    print('result is :',num)
except ZeroDivisionError:
    print("Error:division by zero is not allowed")
except ValueError:
    print("Error:please enter numeric value")
    num1=float(input(" "))
######################################################
    


    
    