# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:28:08 2023

@author: renuk
"""

#**********************Advanced python******************************** 
#______________________list comprehension______________________________
#it is optimisation techniques

list1=[]
for n in range(0,20):
    list1.append(n)
print(list1)

#we can write this code using list compprehension
l1=[num for num in range(0,20)]
print(l1)

#capitalized method 
l1=['renuka','pooja','shivani']
l1=[name.capitalize() for name in l1]
print(l1)

#list comprehension with if statement
#for even number
def even(num):
    return num%2==0
list1=[num for num in range(10) if even(num)]
print(list1)


#for loop inside for loop
l1=[f'{x}{y}'for x in range(3)for y in range(3)]
print(l1)


#______________set comprehension____(rarly use)
Set={x for x in range(3)}
print(Set)

#_____________________dictionary comprehension_______________________
dict1={x:x*x for x in range(4)}
print(dict1)

#________________Generator___________________

gen=(x for x in range(3))
print(gen)
for i in gen:
    print(i)
    
#next() method
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)

#function which return multiple values

def even(end):
    for n in range(0,end,3):
        yield n
for i in even(6):
    print(i,end=" ")
    
#instead of using for loop we can write our own generator
def even(end):
    for n in range(0,end,2):
        yield n
gen=even(6)
next(gen)

#__________________chaining  of generator____________

def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
password=["Not-good","renu#123","not-known"]
for i in hide(length(password)):
    print(i)    

#________________enumerate____________________
#it show key and values
#printing list with index

lst=["milk","Egg","bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}') 
    
#by using enumerate method   
lst=["milk","Egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')

#find all number from 1-1000 that are divid=sible by 3    
div=[n for n in range(1,1000) if n%7==0]
print(div) 

#find all number from 1-1000 that have 3 in them
lst=[n for n in range(1,1000) if '3' in str(n) ]  
print(lst)   

#count number of space in given string
string='the slow solid squid swam sumptuously through the slimy swap' 
a=[n for n in string if n==' '] 
print(len(a)) 
#create a list of all cosonent in the string 
sentence="the Yellow yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
s=[n for n in sentence if n not in ('a','e','i','o','u',' ')]
print(s)

#find common number in lists(without using tuple and set) list
l1=[1,2,3,5,4]
l2=[6,3,7,8,9,2]
common=[n for n in l1 if n in l2]
print(common)

#***********get only the number in sentence like "i n 2002 there where 10 instances
sen="In 2002 there where 10 instances of a protest with over a 1000 people attending"
word=sen.split()
result=[n for n in word if not n.isalpha()]
print(result)

#given number in range 20 produce a list containing the word even if a number is oddthe print 'odd'
list1=[]
for i in range(20):
    if i%2==0:
        list1.append('even')
    else:
        list1.append('odd')
print(list1)

#by using list comprehension
result=['even' if n%2==0 else 'odd' for n in range(20)]
print(result)

#produce the list of tuples consisting of only the matching number in this list
l1=[1,2,3,4,5,6,7,8]
l2=[2,7,1,12]
result=[(a,b) for a in l1 for b in l2 if a==b]
print(result)

