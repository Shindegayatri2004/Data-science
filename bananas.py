# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:55:08 2025

@author: Hp
"""

'''
alex wants to buy exactly N bananas from two vendors.
each vendor sell bananas in fixed sized bunches.alex can only purchase
full bunches and not individual bananas.
he needs your help to determine the minimum cost required to buy exactly N bananas
'''
no_bananas=int(input("enter the no of bananas you want to purchase"))
lot1=int(input("what is the size of lot1 that vendor can provide"))
price1=int(input("whta is the prize of lot1"))
lot2=int(input("what is the size of lot2 that vendor provide"))
price2=int(input("what is the price of lot2"))

def min_cost(no_bananas,lot1,price1,lot2,price2):
    lot_a=no_bananas//lot1
    print(f'lot_a:{lot_a}')
    
    lot_b=no_bananas//lot2
    print(f'lot_b:{lot_b}')
    
    cost_a=lot_a*price1
    print(f'cost_a:{cost_a}')
    
    cost_b=lot_a*price2
    print(f'cost_b:{cost_b}')
    
    return min(cost_a,cost_b)
min_cost(no_bananas,lot1,price1,lot2,price2)

##############################################
    
    
    
    