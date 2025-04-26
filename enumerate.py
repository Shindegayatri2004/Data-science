# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 15:13:52 2025

@author: Hp
"""

import csv

def process_transaction(transaction):
    """ dummy function to stimulate processing of the transaction"""
    if "ERROR" in transaction[2]:
        """stimulate an error for some transactions"""
        raise ValueError("transaction failed")
    return f"processd transaction:{transaction}"

#open and read the csv file
with open("C:/1-python/transaction.csv","r")as file:
    reader=csv.reader(file)
    next(reader) # skip the header
    
    for index,transaction in enumerate(reader,start=1):
        try:
            result=process_transaction(transaction)
            print(f"Row{index}:{result}")
        except ValueError as e:
            print(f"Error at row{index}:{e}")

#########################################################
            
"""scenario__
imagine a customer support team where new tickets
 are assigned to availabele agents in around -robin manner.
 each agent should receive the next ticket in sequence.
 if the last agent is reached,the cycle shoild restart 
 from the first agent automatically"""

import itertools

#list of availabel support agents 
agents=["alice","bob","charlie","david"]

#create a cycling iteratotr over the agents 
agent_cycle=itertools.cycle(agents)

#stimulate incoming support tickets
tickets=["ticket-101","ticket-102","ticket-103",
         "ticket-104","ticket-105","ticket-106"]

#assign tickets to agents ina round -robin manner
assignments={ticket:next(agent_cycle)for ticket in tickets}

#print the asssignment
for ticket,agent in assignments.items():
    print(f"{ticket}->assigned to:{agent}")

########################################################

#shallow copy
import copy

report_template={
    "name":"",
    "scores":[0,0,0],
    "remarks":"pending"
    }

#shallow copy for a new student
student1_report=copy.copy(report_template)
student1_report["name"]="alice"
student1_report["scores"][0]=85

print(report_template["scores"]) #output:[85,0,0]

########################################################

#deep copy
import copy

report_template={
    "name":"",
    "scores":[0,0,0],
    "remarks":"pending"
    }

#deep copy for a ccomplete isolation
student2_report=copy.deepcopy(report_template)
student2_report["name"]="bob"
student2_report["scores"][0]=92

print(report_template["scores"]) #output:[0,0,0]

########################################################
#used in deep learning tool
import copy

params={
        "layers":[64,128,256],
        "activation":"relu"
        }

experiment1=copy.deepcopy(params)
experiment2=copy.deepcopy(params)
experiment1["layers"][0]=32

print(params["layers"])

#######################################################
#use  case filter
users=[
       {"name":"alice","role":"admin"},
       {"name":"bob","role":"editor"},
       {"name":"charlie","role":"admin"},]
admins=list(filter(lambda user:user["role"]=="admin",users))

print(admins)

######################################################      
           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            