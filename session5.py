# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:36:08 2023

@author: renuk
"""


def sum(item):
    s=0
    for i in item:
        s=s+i
    return s
print(sum([4,5,7]))


#python program to multiply all items in list
def mul(item):
    m=1
    for i in item:
        m=m*i
    return m
print(mul([4,5,7]))

#find largest number in the list

l1=[1,4,5,6,3]
max=l1[0]
for i in range(1,len(l1)):
    if l1[i]>max:
        max=l1[i]
print("the maximum number is : ",max)
#or
l1=[1,4,5,6,3]
x=max(l1)
print(x)


#python program to smallest number in list

l1=[1,4,5,6,3]
min=l1[0]

for i in range(1,len(l1)):
    if l1[i]<min:
        min=l1[i]
print("the minimum is : ",min)

''' to count the number of string which satisfies the condition that the string length is 
2 or more and first and last character from a given list
 of string given list is ['abc','xyz','aba','1221']
'''
def words(word):
    ch=0
    for i in word:
        if(len(i))>2 and i[0]==i[-1]:
            ch+=1
    return ch
print(words(['abc','xyz','aba','1221']))

''' python program to  get a list sorted
 in increasing order by the last element in each 
 tuple from a given list of non empty tuples 
 sample list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
 expected =[(2,1),(1,2),(2,3),(4,4),(2,5)]'''
 
def List(item):
        item[-1]
def sorted_list(tuple):
    r=sorted(tuple,key=List)
    return r
print(List([(2,5),(1,2),(4,4),(2,3),(2,1)]))

#program for remove the duplicate item in list

l=[1,3,1,4,5,3,6,6,4,7]
dup=set()
l1=[]
for i in l:
    if i not in dup:
        l1.append(i)
        dup.add(i)
print(l1)
#or 
l=[1,3,1,4,5,3,6,6,4,7]
dup=set(l)
l1=[]
for i in dup:
    l1.append(i)
print(l1)

#python program to clone and copy the list
l=[1,3,1,4,5,3,6,6,4,7]
new_list=list(l)
print(new_list)

#python program to find list of words thst are longer than n from a given list of words
def longer_word(n,str):
    list1=[]
    t=str.split(" ")
    for i in t:
        if len(i)>n:
            list1.append(i)
    return list1
print(longer_word(3, "The quick brown fox for jumps over the lazy dog"))


#python function that takes two list and return true if they have at least one common number 

def common(l1,l2):
    r=False
    for i in l1:
        for j in l2:
            if i==j:
                r=True
                return r
print(common([1,3,2,5,3,7],[12,45,56,2,1]))

#python program to calculate difference between two list
l1=[1,3,2,5,3,7]
l2=[12,45,56,2,1]
d1=list(set(l1)- set(l2))
d2=list(set(l2)- set(l1))
diff=d1+d2
print(diff)

#python program to convert a list of character into a string
l=['R','e','n','u']
str1=''.join(l)#**********
print(str1)

#python program to find index of an item in a specified list
l1=[1,3,2,5,3,7]
print(l1.index(3))

#python program to append a list into second list
l1=[1,3,2,5,3,7]
l=['R','e','n','u']
l3=l1+l
print(l3)
l.append(l1)
print(l)
