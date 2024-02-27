# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 22:08:53 2023

@author: renuk
"""

#Exception handling 
''' exception are handled by try-except blocks'''
#handling ZeroDivisionError exception

print(5/0)
#exception error occur

try:
    print(5/0)
except ZeroDivisionError:
    print("we can't divide by zero!")

a=5
b=6
c=a+b
print(5/0)
'''try:
    print(5/0)
except ZeroDivisionError:
    print("we can't divide by zero!")'''
print(c)

a=5
b=6
c=a+b
try:
    print(5/0)
except ZeroDivisionError:
    print("we can't divide by zero!")
print(c)

# handling FileNotFoundError Exception
file='alice.txt'
with open(file,encoding='utf-8') as file_obj:
    content=file_obj.read()
print(content)

file='alice.txt'
try:
    with open(file,encoding='utf-8') as file_obj:
        content=file_obj.read()
except FileNotFoundError :
    print(f"There is no {file},file is exist")
