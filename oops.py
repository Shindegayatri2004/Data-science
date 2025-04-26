# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 08:25:11 2025

@author: Hp
"""

# a blueprint for creating objects(a kind of template)
class circle:
    def __init__(self,x,y,r):
        self.x=x;
        self.y=y;
        self.r=r;
    
    def circumference(self):
        return 2*3.14*self.r
     
    def area(self):
        return 3.14*self.r*self.r
    
#creating a object
a_circle=circle(2.0,2.0,1.0)
b_circle=circle(3.0,3.0,2.0)

#accesing data and methods
print("radius:",a_circle.r)
print("circumferenece:",a_circle.circumference())
print("area:",a_circle.area())

print("radius:",b_circle.r)
print("circumference:",b_circle.circumference())
print("area:",b_circle.area())

#encapsulation

class Circle:
    def __init__(self,x,y,r):
        self.x=x;
        self.y=y;
        self.r=r;
        
    def get_radius(self):
        return self.r 
    
    def set_radius(self,r):
        if r>0:
            self.r=r
        else:
            print("invalid radius")
            
c2=Circle(1,1,3)
print(c2.get_radius())
c2.set_radius(10)
print(c2.set_radius(10))
#####################################################
#inheritance
#base class

class Circle:
    def __init__(self,x,y,r):
        self.x=x;
        self.y=y;
        self.r=r;
    
    def area(self):
        return 3.14*self.r*self.r
    
    def circumference(self):
        return 2*3.14*self.r
    
    def display_info(self):
        print(f"center:({self.x},{self.y}),radius:{self.r}")
        print(f"area:{self.area():.2f}")
        print(f"circumference:{self.circumference():.2f}")
        
#derived class
class ColoredCircle(Circle):
    def __init__(self,x,y,r,color):
        super().__init__(x,y,r)
        self.color=color
        
        #overriding the dispaly_info method
        
        def display_info(self):
            super().display_info()
            print(f"color:{self.color}")
            
#usage
c1=ColoredCircle(0,0,5,"red")
c1.display_info()

#######################################################
#polymorphism
class Circle:
    def area(self):
        return "calculating arae of circle"

class Square:
    def area(Self):
        return "calculating area of square"

#usage
shapes=[Circle(),Square()] 
for shape in shapes:
    print(shape.area())
#########################################################
#abstraction
class Person:
    def  __init__(self,name,age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"hello ,my name is {self.name} and I am{self.age}years old")
        
#an instance of the class
Person1=Person("alice", 25 )
Person1.greet()
####################################################
#encapsulation
"""hiding internal data and exposing only necessary parts"""

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance  #private atrribute
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            
    def get_balance(self):
        return self.__balance 
    
ba1=BankAccount(300)
print(ba1.get_balance())
ba1.deposit(100)
#data is protected ;direct access is avoided using__r

print(ba1.get_balance())
######################################################

#inheritance
"""allow a class to inherit attributes and methods from
 another class"""

class Animal:
    def speak(self):
        print("some sound")
        
class Dog(Animal):
    def speak(self):
        print("bark")
        
d=Dog()
d.speak()

#########################################################
#polymorphism
"""deiffeent classes can have methods with same name but 
different behaviour"""
class Cat:
    def speak(self):
        print("mow mow")
    
animals=[Dog(),Cat(),Dog()]
for animal in animals:
    animal.speak()

####################################################
#abstraction
from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod 
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14 * self.radius * self.radius 
    
circle1=Circle(5)
print("area of the circle :",circle1.area())
    
#########################################################
   


      
        