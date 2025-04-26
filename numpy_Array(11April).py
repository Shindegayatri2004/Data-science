# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 08:19:36 2025

@author: om
"""

import numpy as np
arr = np.random.randint(1,100,9)
arr
arr.ndim
new_arr = arr.reshape(3,3)
new_arr.ndim
new_arr.ravel() #convert multidimendional array to 1D
new_arr[2]
new_arr
"""
array([[50, 99, 36],
       [27, 20, 41],
       [87, 47, 40]])
"""
#extract element 47 and 40
new_arr[2,1:3]
#extract 20 and 41
new_arr[1,1:3]
###############################
#extract 50, 87, 36, 40
new_arr[[0,2,0,2],[0,0,2,2]]
#####################################
arr = np.random.randint(1,100,9)
#geberate 9 integer random number
arr
#sqr
np.sqrt(arr)
#finding sin of array
np.sin(arr)
#find exponential
np.exp(arr)
#find log
np.log(arr)
#find mean
np.mean(arr)
#median
np.median(arr)
###########################################
#find Q1, Q2, Q3 i.e 25 percentile, 50, 75
arr = np.array([10,20,30,40,50,60,70])
arr
np.mean()
np.percentile(arr, 25) #Q1
np.percentile(arr, 50) #Q2 i.e median
np.percentile(arr,75)
############################################

#create 2D array

import numpy as np
import matplotlib.pyplot as plt

#consider list a it contain 3 nested

a = [[11,12,13], [21,22,23], [31, 32, 33]]
#convert list numpy to array
A = np.array(a)
A
#show numpy array dimensions
A.ndim
#shape
A.shape
#array size
A.size

#access ele of 2nd row and 3rd column
A[1,2]
#23
A[0,0]
#11
A[0][0:2]
#array([11, 12])
A[0,0:2]
A[0:2, 2]
#array([13, 23])

########################################
#basic operation of array
x = np.array([[1,0],[0,1]])
x
""" 
array([[1, 0],
       [0, 1]])
"""

y = np.array([[2,1],[1,2]])
y
"""
array([[2, 1],
       [1, 2]])
"""
#add x and y
z = x+y
z
"""
array([[3, 1],
       [1, 3]])
"""
#multiply y with 2
#scalar mul
z = 2*y
z
"""
array([[4, 2],
       [2, 4]])
"""
#create numpy array y
y = np.array([[2,1],[1,2]])
y

z = 2*y
z

A = np.array([[0,1,1],[1,0,1]])
A
B = np.array([[1,1],[1,1],[-1,1]])
B
z = np.dot(A,B)
z
##############################
#calculate sin of z
np.sin(z)

#############################
#transpose matrx
c = np.array([[1,1],[2,2],[3,3]])
c
c.T

#######################################

import numpy as np
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
#1+0j is not complex bcz 0j become 0
a
#write code to test elementwise complex no.
np.iscomplex(a)

#write code to test ele real no
np.isreal(a)

#check scalar type
np.isscalar(3.1) #it will check separate no. 3.1 
np.isscalar([3.1]) #it will check [] from array

##########################################
#multiplication of 2 given matrix
import numpy as np
p = [[1,0],[0,1]]
p = np.array(p)
q= [[1,2],[3,4]]
q = np.array(q)
res = np.dot(p,q)
res

##outer product is hadamard product
res = np.outer(p,q)
res
