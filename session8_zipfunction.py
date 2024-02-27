# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:22:21 2023

@author: renuk
"""
##################itertools###############################
#use of Zip function 
name=['renuka','shivani','sai','reva']
info=[3453,3234,67567,2424]
for n,f in zip(name,info):
    print(n,f)
    
name=['renuka','shivani','sai','reva','ishika']
info=[3453,3234,67567,2424]
for n,f in zip(name,info):
    print(n,f)#-----o/p renuka 3453 shivani 3234 sai 67567 reva 2424


#*****zip longest
from itertools import zip_longest
name=['renuka','shivani','sai','reva','ishika']
info=[3453,3234,67567,2424]
for n,f in zip_longest(name,info):
    print(n,f)
 
#use of fill value instead none
#fillvalue=assign some value 
#all this method is use in data preparation

from itertools import zip_longest
name=['renuka','shivani','sai','reva','ishika']
info=[3453,3234,67567,2424]
for n,f in zip_longest(name,info,fillvalue=0):
    print(n,f)
#******************selection**********************************
#use of all function, if all valus=es are true then it will produce o/p
#it will tell non-zero value
#value must be non-zero,+ve,-ve
l1=[3,2,3,5,7,8]
if(all(l1)):
    print('all values are true')
else:
    print('useless')
    
#any() function
l1=[3,0,0,5,0,8]
if(any(l1)):
    print('It has some value')
else:
    print('useless')
    
l1=[0,0,0,0,0,0]
if(any(l1)):
    print('It has some value')
else:
    print('useless')#---o/p useless
    
#count() function
#usually use in iot fuction

from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

#start with 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))   

#---------------cycle()----------------------
#suppose you have repeated tasks to be done ,then you canuse this method
import itertools

instruction=('eat','sleep','run','jump')
for instruction in itertools.cycle(instruction):
    print(instruction)
    
#repeat()
from itertools import repeat
for msg in repeat("keep patiense",times=3):
    print(msg)

#***********************************************
    
#***************combination**************** 
from itertools import combinations
players=['john','jony','janardhan']
for i in combinations(players, 2):
    print(i)

#************permutation*************
#it gives all possible outcome from given condition
from itertools import permutations
players=['john','jony','janardhan']
for i in permutations(players, 2):
    print(i)
    
#product()
from itertools import product
l1=['rohit','pandya','Bumrah']
l2=['virat','manish','sami']
for pair in product(l2,l1):
    print(pair)
    
#filter()
age=[12,15,34,26,43,89]
adult=filter(lambda age:age>=18,age)
print([age for age in adult])


# shallow copy and deep copy
l1=[1,2,3,4,5]
l2=l1
l1[0]=-10
print(l1)
print(l2)

#shallow copy

import copy
l1=[1,2,3,4,5,6]
l2=copy.copy(l1)
l2[0]=-10
print(l1)
print(l2)
#drawback if there is nested object modifying of level 2 it affect the other 
import copy
l1=[[1,2,3,4,5,6],[8,7,4,9,2]]
l2=copy.copy(l1)
#affect the other
l1[0][0]=-10
print(l1)
print(l2)

#deep copies
#full independent clones use copy.deepcopy()
import copy
l1=[[1,2,3,4,5,6],[8,7,4,9,2]]
l2=copy.deepcopy(l1)
l1[0][0]=-10
print(l1)
print(l2)
    
'''write python program to create a iterator from several 
iterables in a sequence and display the type of element of new iterator'''
from itertools import chain
def chain_func(l1,l2,l3):
    return chain(l1,l2,l3)
result=chain_func([2, 4, 3],['a','r','y','f'],[34,67,23,65])
print("type of new iterator : ")
print(type(result))
print('element of the new iterator')
for i in result :
    print(i)    
 #############################
   
from itertools import chain
def chain_func(l1,l2,l3):
    return chain(l1,l2,l3)
result=chain_func((2, 4, 3),('a','r','y','f'),(34,67,23,65))
print("type of new iterator : ")
print(type(result))
print('element of the new iterator')
for i in result :
    print(i)  

#write a python program that generate running product of the element in an iterable
#in this we use accumulate method
#list
from itertools import accumulate
import operator
def accumulate_product(lst):
    return accumulate(lst,operator.mul)
result=accumulate_product([1,4,3,6,7,6])
print("running product of the list ")
for i in result:
    print(i)
#tuple
   
from itertools import accumulate
import operator
def accumulate_product(lst):
    return accumulate(lst,operator.mul)
result=accumulate_product((1,4,3,6,7,6))
print("running product of the list ")
for i in result:
    print(i)
    
#to construct infinite iterator that return evenly spaced 
#values strating number and stop
import itertools as it
start=10  
step=1
print('the starting number is',start,'and step is ',step)
counter=it.count(start,step)
for i in counter:
    print(i)
#asdwasdwwasdwasdwasdwasdwasdwasdwasdwasdwasdwasdwwdsawdsawdsawdsawdawdsawdsaw

#to generate infinite cycle of element from an iterable
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
result=cycle_data(['A','B','C','D'])
for i in result:
    print(i)   
#string   
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
result=cycle_data('python iterator')
for i in result:
    print(i)

#to make an iterator that drop element from the iterable as soon as element is +ve no
#dropwhile()method is used

import itertools as it
def drop_element(num):
    return it.dropwhile(lambda x:x<0,num)
num=[1,4,-2,5,7,8,9,-1,-4,-5]
print('original number : ',num)
result=drop_element(num)
print('drop element is :',list(result))