# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 15:26:11 2025

@author: Hp
"""

#decorator

#pre-requisite to decorator
def plus_one(number):
    number1 = number+1
    return number1
plus_one(5)
##############################################
#defining functions inside other functions
def plus_one(number):
    def add_one(number):
        number1 = number+1
        return number1
    result = add_one(number)
    return result
plus_one(4)

########################################

#passing function as argumnets
#to other functions
def plus_one(number):
    result1 = number+1
    return result1

def function_call(function):
    result = function(5)
    return result

function_call(plus_one)
############################################

#function returning other function
"""
when we returning the function then it will not give 
output it will returning an object.
"""
"""
when we returning function then we have to only give
function name not function_name()
"""
def hello_function():
    def say_hii():
        return "hii"
    return say_hii
#hello_function() #it will create object
hello = hello_function()
hello()

##########################################

#need for decorators

import time
def cal_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    total_time = (end-start)*1000
    print(f"total time of execution square is : {total_time}")
    return result

#cal_square(6) it will give error
array = range(1,1000)
out_square = cal_square(array)

import time
def cal_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    total_time = (end-start)*1000
    print(f"total time of exrcution cube is : {total_time}")
    return result

array = range(1,1000)
out_cube = cal_cube(array)

###################################################

#decorator

def say_hii():
    return 'hello world'

def upper_case(function): #pass function as argument
    def wrapper():
        func = function() #create object of function
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

"""
#upper_case(say_hii)
when use 
return wrapper()
"""


decorate = upper_case(say_hii) #pass another function
decorate()

"""
python provide much better to use decorater 
i.e '@' symbol
"""

####################################

#decorater using @

def upper_case(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@upper_case
def say_hii():
    return 'hello world'
say_hii()

"""
@decorator 
we use for multiple code in same file
"""
#################################
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

############################################
"""
*args :- use when we don't know how many arguments we have to pass
**kwargs :- use for pass key value pair
"""
import time
def time_it(func):
    #it is a decorator function takes another function as argumnet
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        #call original function (func)
        #with the provided argument
        end = time.time()
        print(func.__name__+" took "+str((end-start)*1000)+"mil sec")
        return result
    return wrapper

@time_it
def cal_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def cal_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = cal_square(array)
out_cube = cal_cube(array)
######################################################

"""automatically logs function calls and their arguments"""

##use cases of decorators:
    
    
#automatically logs function calls and their arguments
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@log_decorator
def add(a,b):
    return a+b
print(add(3,4)) #logs the function call

#############################################
#access control / authentication
#checks if a user is authenticate before executing a function
def auth_required(func):
    def wrapper(user):
        if not user.get("authenticated",False):
            #the .get("authenticated", False) method
            #is used to safely retrive the value of
            #the "authenticated" key from the
            #dictionary
            print("Access Denied")
            return
        return func(user)
    return wrapper

@auth_required
def dashboard(user):
    print(f"welcome {user['name']}!")
user1 = {"name": "Alice","authenticated": True}
user2 = {"name": "Bob", "authenticated": False}

dashboard(user1) #access granted
dashboard(user2) #access denied
##########################################

#Input validation
#Ensures input meet certain criteria before execution
def validate_positive(func):
    def wrapper(x):
        if x<0:
            raise ValueError("Negative value not allowed")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x**0.5

print(square_root(4)) #works fine
print(square_root(-4)) #raise error

########################################################

import time 
def rate_limiter(max_calls,time_frame):
    calls=[]
    
    def decorator(func):
        def wrapper(*args,**kwargs):
            now=time.time()
            while calls and now -calls[0]>time_frame:
                
                calls.pop(0)
            
            if len(calls)>=max_calls:
                print("rate limit exceeded.try again ")
                return
            
            calls.append(now)
            return func(*args,**kwargs)
        return wrapper   
    return decorator           
"""condition:while calls and now -calls[0]>time_frame
 calls is alist that stores timestamps of previous function 
 calls .calls [0]represents the oldest function call in the list
 now is the current time when the function is being called.
 now -calls[0] computs ho long ago the oldest call occured.
 if that time execeeds time frame,
 it menas the function call is no longer
 within the allowed window so it can be removed
 """
@rate_limiter(3,10)
def say_hello():
     print("Hello!") 

say_hello() 
say_hello() 
say_hello()          
say_hello() 
        
            
            
            
            
            