# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:09:28 2023

@author: renuk
"""
import json

n=[1,2,3,5,4,7]
file='numbers.json'
with open(file,'w') as f:
    json.dump(n,f)

#saving data with json is useful 

import json

n=input("enter the name : ")
file='username.json'
with open(file,'w') as f:
    json.dump(n,f)
print(f"we will remember when you come back,{n}")
'''new program when that greet users whoose name is already stored'''

import json
file='username.json'
with open(file) as f:
    n=json.load(f)
print(f" Welcome back,{n}!")

#load the username if it has been stored previously
#otherwise, prompt for the username and store it


