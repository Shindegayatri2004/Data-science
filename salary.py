# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:25:33 2025

@author: Hp
"""
#one module
def calculate_salary(experiance,role):
    base_salary={
        "intern":30000,
        "junior":50000,
        "mid-level":80000,
        "senior":120000,
        "manager":150000
        }
    if role not in base_salary:
        raise ValueError("invalid job role")
        
    return base_salary[role] + (experiance*2000)
