# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 21:14:19 2025

@author: Hp
"""

def plus_one(number):
    def add(number):
        
        number1=number+1  
        return number1
    result=add(number)
    return result
plus_one(6)


def plus_one(number):
    result1=number+1 
    return result1

def function_call(function):
    result=function(8)
    return result
function_call(plus_one)



def hello_function():
    def say_hii():
        return "hii" 
    return say_hii 
hello =hello_function()
hello()

import time
def cal_square(numbers):
    start=time.time()
    result=[]
    for number in  numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time of execution square is:{total_time}")
    return result 

array=range(1,1000)
out_square = cal_square(array)

import time
def cal_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    total_time = (end-start)*1000
    print(f"total time of execution cube is : {total_time}")
    return result

#cal_square(6) it will give error
array = range(1,1000)
out_cube = cal_cube(array)


def say_hii():
    return "hello world"

def upper_case(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper  

decorate=upper_case(say_hii)
decorate()
##############################

def upper_case(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper  

@upper_case 
def say_hii():
    return "hello world" 
say_hii()

def split_string(function):
    def wrapper():
        func= function()
        make_splitted=func.split()
        return make_splitted
    return wrapper()

def upper_case(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper 

@split_string 
@upper_case 
def say_hii():
    return "hello world"
say_hii()



def split_string(function):
    def wrapper():
        func = function()
        make_splitted = func.split()
        return make_splitted
    return wrapper

def upper_case(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@split_string
@upper_case
def say_hii():
    return "hello world"
say_hii()
