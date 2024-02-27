# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:06:01 2023

@author: renuk
"""
#functions
def prime(n):
    for i in range(2,n):
        if (n%i)==0:
            return "it is not prime"
            break
    return "the number is prime..."
prime(15)
#function without argument
def fun():
    print("hello world")
fun()
def fun(username):
    print(f"hello {username}")
fun("shivani")
#positional arguments
#order matters in positional arguments
def fun(a,b):
    print(f"I have {a} pens, and also having {b} pencil.")
fun(4,6)
#default values
def fun(pet_n,animal_n="dog"):
    print(f"my {animal_n}'s name is {pet_n.title()}.")
fun(pet_n="moti")

#assignment2 question 2
height=int(input("enter the height : "))
if height>=120:
    print("you are eligible to play rollar coaster")
    age=int(input("enter the age : "))
    if(age<=18):
        print("ticket will be 20Rs")
    elif(age>18):
        print("ticket will be 50Rs")
    elif(age<=12):
        print("Ticket will be 10Rs")
    elif(12<age<18):
        print("ticket will be 15Rs")
else:
    print("not eligible for ride")
    
#assignment2 question 1
def fun(age,max_age=80):
    if age>80:
        return 0,0,0;
    year=max_age-age
    days=year*365
    week=year*52
    month=year*12
    
    print(f" the remaining Days are {days},remaining weeks are {week} and months are {month}")
fun(age=34)
#question 3
users=["admin","manager","employee","workers","staff"]
for user in users:
    if(user=="admin"):
        print("Hello admin,would you like to see status report")
    elif(user=="employee"):
        print("Hello admin")
    elif(user=="manager"):
        print("Hello manager")
    elif(user=="workers"):
        print("Hello workers")
    else:
        print("Hello")
    
#password picker
import string
adjectives=["intelligent","brave","sleepy","green","orange","yellow","sharp","slow","fast","smelly","fluffy"]
noun=["apple","mango","renuka","shivani","tree","table","banana","rose","book","pen"]
import random

adjectives=random.choice(adjectives)
noun=random.choice(noun)
n=random.randrange(0,100)#select the number
special_char=random.choice(string.punctuation)#special_char
password=adjectives+noun+str(n)+special_char
print("your new password is %s",password)

import string
adjectives=["intelligent","brave","sleepy","green","orange","yellow","sharp","slow","fast","smelly","fluffy"]
noun=["apple","mango","renuka","shivani","tree","table","banana","rose","book","pen"]
import random
while True:
    adjectives=random.choice(adjectives)
    noun=random.choice(noun)
    n=random.randrange(0,100)#select the number
    special_char=random.choice(string.punctuation)#special_char
    password=adjectives+noun+str(n)+special_char
    print("your new password is %s",password)
    response=input("would you like to change password : ")
    if response=="n":
        break
    
def checkpassword(password):
    upper=False
    lower=False
    num=False
    for ch in password:
        if ch>="A" and ch<="Z":
            upper=True
        elif ch>="a" and ch<="z":
            lower=True
        elif ch>="0" and ch<="9":
            num=True
    if len(password)>=8 and upper and lower and num:
        return True
    else:
        return False
p=input("enter the password")
if checkpassword(p):
    print("strong password")
else:
    print("Weak password")
    
    
#question 4

size_pizza=input("enter the size of pizza : ")
add_pepp=input("add extra pepperony : ") 
extra_cheese=input("add extra cheese :")  
bill=0     
if size_pizza=='s':
    print("pay 15$")
    bill=15
elif size_pizza=='m':
    print("pay 20$")
    bill=20
elif size_pizza=='l':
    print("pay 25$")
    bill=25
if add_pepp=='y':
    if size_pizza=='s':
        bill+=2
    else:
        bill+=3
if extra_cheese=='y':
    bill+=1
    print(f"total bill is {bill}")
else:
    print(f"total bill is {bill}")
    
