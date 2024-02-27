# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:16:26 2023

@author: renuk
"""
#relative path
with open('pi_digits.txt') as file_object:
    content=file_object.read()
print(content)

#rstrip()method is used to remove space after reading file 
with open('pi_digits.txt') as file_object:
    content=file_object.read()
print(content.rstrip())

#in this we are giving the absolute path
file_path=open('C:/1-python/pi_digits.txt')
content=file_path.read()
print(content.rstrip())

#or 
file_path='C:/1-python/pi_digits.txt'
with open(file_path) as file_object:
    content=file_object.read()
print(content.rstrip())

#read line by line
file_name='pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip()) #added rstrip()method
        
#working with file's content
file='pi_digits.txt'
with open(file) as file_object:
    line=file_object.readlines()
    string=''
    for li in line:
        string+=li.rstrip()
        print(string)
        print(len(string))
        
#writing lines
file_path='programming.txt'
with open(file_path,'w') as file_object:
    file_object.write('I love programming.')
    
#writing multiple lines

file_path='programming.txt'
with open(file_path,'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love to get knowledge about new things.')
    
#append mode

file_path='programming.txt'
with open(file_path,'a') as file_object:
    file_object.write('\nI love programming.\n')
    file_object.write('I love to get knowledge about new things.')
    


    

    