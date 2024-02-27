
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:43:37 2023

@author: renuk
"""

#write a python code to add a key in dictionaries
#sample dict={0:10,1:20}
#expected o/p={0:10,1:20,2:30}
d={0:10,1:20}
print(d)
d.update({2:30})
print(d)
#or
d={0:10,1:20}
print(d)
d[2]=30
print(d)

'''write python code to concatenate dictionaries
to create a new one'''
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)

#python program to check whether givenkey is already exist in a dictionary

d={1:10,2:20,3:30,4:40,5:50,6:60}
def key_check(x):
    if x in d:
        print("key is present...")
    else:
        print('not present')
key_check(9)

#write program to iterate over dictionary using  for loop 
d={'x':10,'y':20,'z':30}
for d_key,d_values in d.items():
    print(d_key,':',d_values)
    