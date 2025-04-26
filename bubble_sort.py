# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 09:17:05 2025

@author: Hp
"""

'''
pass 1:moves largest element to index n-1
pass 2:moves largest element to index n-2
pass 3:moves largest element to index n-3
pass 4:moves largest element to index n-4
pass 5:moves largest element to index n-5
pass 6:(not needed) elements are sorted
'''
def bubble_sort(lst):
    n=len(lst)
    for i in range(n-1):
        
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                
    return lst
lst=[2,6,4,8,7,1]
bubble_sort(lst)

