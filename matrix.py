# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 08:21:13 2025

@author: Hp
"""

mat1=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
for i in mat1:
    print(i)
    
##########################################

mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]
rows=len(mat)
cols=len(mat[0])

print("rows:",rows)
print("columns:",cols)

for i in range(rows):
    for j in range(cols):
        print(f"Elements of [{i}][{j}]={mat[i][j]}")


#################################################
##matrix addition
mat1=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
mat2=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
result=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]
rows=len(mat1)
cols=len(mat1[0])
for i in range(rows):
    for j in range(cols):
        result[i][j]=mat1[i][j]+mat2[i][j]
result

##############################################
## diagonal matrix

mat1=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
rows=len(mat1)
cols=len(mat1[0])
for i in range(rows):
    for j in range(cols):
        if i==j:
            print(mat1[i][j])
            
################################################
#sparse matrix
## matrix having more no of zero

mat=[
     [1,0,0],
     [0,4,0],
     [1,0,6]]
rows=len(mat)
cols=len(mat[0])
count=0
for i in range(rows):
    for j in range(cols):
        if mat[i][j]==0:
            count=count+1 
if count>(rows*cols)/2:
    print("sparse")
else:
    print("not sparse")

################################################
## to check matrix is identical

def is_identical(mat1,mat2):
    
    rows1,cols1=len(mat1),len(mat1[0])
    rows2,cols2=len(mat2),len(mat2[0])
    
    if rows1 != rows2 or cols1 != cols2:
        return False
    
    for i in range(rows1):
        for j in range(cols1):
            if mat1[i][j]!= mat2[i][j]:
                return False
            
    return True

mat1=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
mat2=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
print("are ths matrices identical?",is_identical(mat1,mat2))

###################################################

mat1=[[1,2,3],[4,5,6]]
mat2=[[1,2],[4,5]]
if is_identical(mat1,mat2):
    print("matrices are identical")
else:
    print("matrices are not identical")
    
################################################
#convert 2D array in 1D array in spiral order
'''1 2 3 4
   5 6 7 8
   9 10 11 12
   13 14 15 16  ''' #HOMEWORK
   
################################################


        

