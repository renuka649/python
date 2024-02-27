# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 08:37:07 2023

@author: renuk
"""

s=int(input("enter the saving :"))
if s == 0:
    print("no saving..")
elif s<500:
    print("well done")
elif s<1000:
    print("thats a tidy sum")
elif s<10000:
    print("great job...")
else:
    print("thank you.....")
    
#while loop
c=1
print("starting")
while(c<=10):
    print(c)
    c+=1
#for loop
for i in range(1,11):
    print(i)
#only print code if all iteration is completed
n=int(input("enter the number : "))
for i in range(1,16):
    if i==n:
        break;
    print(i)
print("done")
#anonymous value
for _ in range(0,10):
    print("*",end="")
    print()
#for horizontal
for _ in range(0,10):
    print("*",end=" ")
n=int(input("enter the number : "))
for i in range(0,10):
    if i==n:
        break;
    print(i," ",end="")
print("done")
#print odd number
start,end=2,20
for i in range(start,end):
    if i%2!=0:
        print(i,end=' ')
#even number
start,end=2,20
for i in range(start,end):
    if i%2==0:
        
        print(i,end=' ')
#it create steps 
start,end=2,20
for i in range(start,end,3):
    if i%2==0:
        print(i,end=' ')

start=int(input("enter the number :"))
end=int(input("enter the number :"))        
for i in range(start,end,3):
    if i%2==0:
        print(i,end=' ')
        
#prime number 
a=int(input("enter the starting number"))
b=int(input("enter the ending number "))
for num in range(a,b+1): 
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
        
#palindrome 
n=int(input("enter the number : "))
temp=n
rev=0
while(n>0):
    dig=n%10;
    rev=rev*10+dig
    n=n//10;
if temp==rev:
    print("it is palindrome....")
else:
    print("it is not pallindrome...")
    
#leap year
n=int(input("enter the year : "))
if n%400==0 or (n%4==0 and n%100!=0):
    print("it is leap year")
else:
    print("it is not leap year")
    
#mario pyramid
n=int(input("enter the number : "))
for i in range (0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("\n")
n=int(input("enter the number : "))
for i in range (n):
    for j in range(n):
        print("*",end="")
    print("\n")
n=int(input("enter the number : "))
for i in range (n):
    for j in range(n-i):
        print("*",end="")
    print("\n")

#pallindrome string
s=input("enter the string  : ")
p=""
for i in s:
    p=i+p
if(s==p):
    print("it is pallindrome...")
else:
    print("it is not pallindrome.....")
    
#global variable
n="awesome"
def fun():
    n="fantastic"
    print("python is "+n)
fun()
a={"name":"renuka","age":20}
print(type(a))
print(a)

#print multiple string
x=""" this is afternoon time.
Take a break for sometime."""
print(x) 
#string slicing 
x="this is python"
print(x[2:8])
print(x[1:9:2])  
print(x[9:2:-1])
print(x[:3])
print(x[3:])
print(x[-9:-2])
x="renuka Shirsath"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.replace("renuka", "prerna"))
print(x.strip())
x="Hello world"
print(x.split(" "))#give seperater it can be anything
s=input('enter the string : ')
t=s[::-1]
print(t)
if(t==s):
    print("it is pallindrome..")
else:
    print("it is not pallindrome...")
    
s=input('enter the string : ')
t=s[::-2]
print(t)
n="this is python"
print(n.find("is"))
#concatenation of string
a="Renuka"
b="Shirsath"
print(a+" "+b)
#concatenation of integer with string
b=20
print(f"my name is renuka and my age is,{b}")
a=4
b=45
c=585
print(f"I want {a} pieces,having item number {b} and price is {c}")
a=4
b=45
c=585
p="I want {} pieces,having item number {} and price is {}"
print(p.format(a, b,c))
a=4
b=45
c=585
p="I want {0} pieces,having item number {1} and price is {2}"
print(p.format(a,b,c))
x="i am renuka, i am from \"Shrirampur\""
print(x)
#operator precedence
print(3*3+3/3-3)

