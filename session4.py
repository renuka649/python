# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:47:54 2023

@author: renuk
"""

#returning dictionary
def fun(f,l):
    p={'first':f,'last':l}
    return p
m=fun('renuka','shirsath')
print(m)

# passing a list
def fun(user):
    for name in user:
        msg=f"hello,{name.title()}"
        print(msg)
user=['renuka','shivani','ishika','pooja']
fun(user)

#passing an arbitrary number of a argument
def make_pizza(*toppings):
    print(toppings)
make_pizza('cheese')
make_pizza('capcicum','mushroom','pepperoni')

def make_pizza(*toppings):
    for t in toppings:
        print(f"-{t}")
make_pizza('cheese')
make_pizza('capcicum','mushroom','pepperoni')

#making positional and arbitrary argument

def make_pizza(size,*toppings):
    print(f"making a {size}-inch pizza with the folling toppings: ")
    for t in toppings:
        print(f"-{t}")
make_pizza(12,'cheese')
make_pizza(16,'capcicum','mushroom','pepperoni')


import pizza

pizza.make_pizza(14,'capcicum','cheese','mushroom')

#importing specific functions from module
from pizza import make_pizza

make_pizza(14,'capcicum','cheese','mushroom')

#give function as alias name

from pizza import make_pizza as mp

mp(14,'capcicum','cheese','mushroom')

#give module as alias name
import pizza as p

p.make_pizza(14,'capcicum','cheese','mushroom')

#importing all functions from the module
from pizza import*

make_pizza(12,'cheese')
make_pizza(16,'capcicum','mushroom','pepperoni')

#scope of variables
x=x+1
x=9
print(x)
#don't defined variable after some instruction
#always declare variable first
#correct code is
x=9
x=x+1
print(x)
#***************lambda function or anonymous function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(2, 4, 5))


add=lambda a,b,c:a+b+c
add(4,5,6)

def mul(a,b,c):
    m=a*b*c
    return m
print(mul(2, 4, 5))

mul=lambda a,b,c:a*b*c
mul(3,4,5)

val=lambda *arg: sum(arg)
val(1,2,3,4,5,5,6,7,4)
 
#keyword argument
def person(name,**data):
    print(name)
    print(data)
person(name='renuka',age=34,place='shrirampur',mob=123473)

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person(name='renuka',age=34,place='shrirampur',mob=123473)

val=lambda **data : sum(data.values()) 
print(val(a=2,b=3,c=5))#or          
val(a=2,b=3,c=5)
# maximum after writing if we must write else condition
max=lambda a,b:x if(a>b)else b
max(1,2)




