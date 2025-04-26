# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 16:27:41 2025

@author: om
"""

import numpy as np
x = np.array([1,2,3])
x
np.all(x)
x = np.array([1,2,3,4,0])
np.any(x)
x = np.array([1,2,np.nan,np.inf])
x
np.isfinite(x)
np.isnan(x)
x = np.array([3,5])
y = np.array([2,5])
np.greater_equal(x,y)
np.greater(x,y)
array_2D = np.identity(3)
array_2D
rand_no = np.random.normal(0,1,5)#random number but in normal form 
rand_no
a = np.arange(10,22) #it will generate number
a

#####################################

####array
#1D
import numpy as np
lst=[1,2,3]
arr = np.array(lst)
arr
arr.ndim
arr.shape
type(arr)
################
#2D
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr.ndim
arr.shape
###############
#3D
arr = np.array([[[1,2,3],[4,5,6],[1,3,4]]])
arr.ndim
arr.shape
#####################
#matrix
mat = np.matrix([[1,2,3],[4,5,6],[6,7,8]])
mat.ndim
mat.shape
############################
arr = np.random.randint(1,100,9)
arr
arr.ndim
new_arr = arr.reshape(3,3)
new_arr.ndim
new_arr.ravel()
arr[2]
