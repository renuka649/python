# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:19:26 2023

@author: renuk
"""
# 1. Determine if a letter is a vowel or a consonant

letter=input()
l=letter.lower()
a=['a','e','i','o','u']
if(letter.isalpha() and len(letter)==1):
    if letter in a:
        print('it is vowels...') 
    else:
       print('it is Consonents....')


# 2. Convert from a letter grade to a number of grade points
grade={'A+':5.0,'A':4.5,'B+':4.0,'B':3.5,'C+':3.0}
letter=input().upper()
if letter in grade:
    g=grade[letter]
    print(f"the grade points is {g}")
else:
    print('It is not grade letter')
    
    

    
    
    
    
