# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:38:24 2025

@author: Hp
"""

#validation module
def validate_experiance(exp):
    if not isinstance(exp,int) or exp<0:
        raise ValueError("experiance must be a non-nagative int ")
    return exp

def validate_role(role):
    valid_roles={"intern","junior","mid-level","senior"}
    if role not in valid_roles:
        raise ValueError(f"invalid role! choose from valid_roles")
    return role
