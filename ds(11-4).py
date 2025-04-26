# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 08:16:12 2025

@author: Hp
"""

import numpy as np
arr=np.random.randint(1,100,9)
arr
arr.ndim
new_arr=arr.reshape(3,3)
new_arr.ndim
new_arr.ravel()
arr[2]
#extarcting elements from 2 to 5
arr[2:6]
new_arr

new_arr[2,1:3]
#extracting specific number
new_arr[1,1:3]
#extracting elements
new_arr[[0,2,0,2],[0,0,2,2]]
#diagonals
new_arr[[0,1,2],[0,1,2]]

###########################################################
arr=np.random.randint(1,100,9)
arr
#square root
np.sqrt(arr)
#sin of array
np.sin(arr)
# exponent of arr
np.exp(arr)
#finding log
np.log(arr)
#finding mean
np.mean(arr)
#finding median
np.median(arr)
###################################################
"""finding q1,q2,q3 by percentile i.e 25,50,75"""
arr1=np.array([10,20,30,40,50,60,70])
arr1
arr1.mean()
np.percentile(arr1, 25) #q1
np.percentile(arr1, 50)    #q2
np.percentile(arr1, 75)   #q3
 
#####################################################
import numpy as np
import matplotlib.pyplot as plt

"""consider list ,list contains 3 nested """

a=[[11,12,13],[14,15,16],[17,18,19]]
a
#converting list numpy to array
A=np.array(a)
A
#show numpy array dimentions
A.ndim
#show numpy  shape
A.shape
A.size

A[1,2]  #16
A[0,0]   #11
A[0][0:2]  #11 12
A[0:2,2] #13 16

#BASIC OPERATIONS
#create numpy array x
x=np.array([[1,0],[0,1]])
x

#create numpy array y
y=np.array([[2,1],[1,2]])
y

#add x and y
z=x+y
z

#multiplying array
z=2*y
z

x=np.array([[2,0],[0,2]])
x
y=np.array([[0,2],[2,0]])
y
z=x*y
z

#creating matrix

A=np.array([[0,1,1],[1,0,1]])
A
B=np.array([[1,1],[1,1],[-1,1]])
B
Z=np.dot(A,B)
Z
#calculate sin of z
np.sin(Z)

#TRANSPOSE MATRIX
C=np.array([[1,1],[2,2],[3,3]])
C
C.T # T TO CALCULATE transpose

##################################################

"""write numpy program to test eleemnts wise for,complex num,real num
is a given array,also test if given numver is of scalar type or not"""
import numpy as np
a=np.array([1+1j,1+0j,4.5,3,2,2j])
print("original array")
print(a)
print("checking for complex number:")
print(np.iscomplex(a))
print("checkingg for real number:")
print(np.isreal(a))
print("checking for scalar type:")
print(np.isscalar(a))
print(np.isscalar(3.1))
print(np.isscalar([3.1]))

#################################################

"""write numpy program to compute the multiplication
of two given matrices"""
import numpy as np
p=[[1,0],[0,1]]
p=np.array(p)
q=[[1,2],[3,4]]
q=np.array(q)
print("original matrix:")
print(p)
print(q)
result1=np.dot(p,q)
print("result of said matrix multiplication:")
print(result1)
#outer product is hadaward product
res=np.outer(p,q)
print(res)

#############################################

#hadamard product
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[ 7,8]])
hadamard=a*b
print("hadamard product:\n",hadamard)
#############################################

#usually works with 1D vector
import numpy as np 
x=np.array([1,2])
y=np.array([3,4,5])

outer=np.outer(x,y)
print("outer product:\n",outer)

#####################################################
import numpy as np
p=[[1,0],[0,1]]
p=np.array(p)
q=[[1,2],[3,4]]
q=np.array(q)

print("original matrix:\n")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)
print("cross product of said two vectors(p,q)")
print(result1)
print("cross product of the said two vectors(q,p)")
print(result2)
####################################################
#numpy program to compute determinant

import numpy as np
from numpy import linalg  as LA

a=np.array([[1,0],[1,2]])
print("original 2-D array")
print(a)
print("determinant of  2-D array:")
print(np.linalg.det(a))
#################################################
"""write numpy program to cumpute eigen value and eigen vector"""
import numpy as np
m=np.mat("3 -2 ; 1 0")
print("original matrix:\n")
print("a\n",m)
w,v=np.linalg.eig(m)
print("eigen vector of said value:",w)
print("eigen value of said value :",v)

#######################################################
""" numpy program to calculate inverse of the matrix"""
import numpy as np
m=np.array([[1,2],[3,4]])

print("original matrix:")
print(m)
result=np.linalg.inv(m)
print("inverse of the said matrix:")
print(result)

####################################################

#write a Numpy program to generate five random numbers fraction
import numpy as np 
x=np.random.randint(low=10,high=30,size=6) 

#write a numpy program to create a 5x5 matrix 
import numpy as np 
x=np.random.random((5,5)) 
x 
xmin,xmax=x.min(),x.max()  
print(f"minimum:{xmin} maximum:{xmax}")

#write a numpy program to get the minimum and maximum value of a given array along the second axis
import numpy as np 
x=np.arange(8).reshape((4,2))
print("original array:")
print(x)
print("maximum value along second axis:") 
print(np.amax(x,1))
print("minimum value along second axis:")
print(np.amin(x,1))






