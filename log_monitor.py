# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 16:09:07 2025

@author: Hp
"""


import time
file_path='C:/1-python/server.log'
def tail_log_file(file_path):
    """generator that continuosly reads a new lines from the log """
    with open (file_path,"r") as file:
        file.seek(0,2) #move to end of the file
        while True:
            line=file.readline()
            if not line:
                time.sleep(1) # wait for new logs to be added
                continue
            yield line.strip() #yield new log line

#Example usage:process logs as they come in            
for log in tail_log_file(file_path):
    if "Error" in log:
        print(f"Alert:{log}") # trigger alert for error logs
        
        
        
        
        
        
        
        