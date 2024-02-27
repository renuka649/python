# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:33:57 2023

@author: renuk
"""
#1 tuple orered and immutable
tup=(1,3,4,5)
print(f'tup[0] : {tup[0]}')
print(f'tup[1] : {tup[1]}')
print(f'tup[2] : {tup[2]}')
print(f'tup[3] : {tup[3]}')
print(tup[0])
#print different datatypes
tup=(1,'john',4,'renuka')
print(tup)

# iterating over tuple

t=('apple','mango','banana','chikoo')
for i in t:
    print(i)
len(t) 

t=('apple','mango','banana','chikoo','apple','orange')   
t.count('apple')
print(t.index('apple')) # checking index of element

if 'orange' in t:               #checking if element is exist or not
    print("it is present....")
    
#nested tuples
#tuple can be nested within tuple
t1=(1,2,3,4)
t2=('renu','john','pooja','sai')
t3=(34,t1,t2,44)
print(t3)
# we can't add and remove elements in tuple


#2 list ordered mutable and index

l1=['renuka','prerna','heena']
print(l1)

#nested list
l1=['renuka','prerna','heena']
l2=[1,3,4,5,2]
l3=['john',11,l1,l2]
print(l3)
print(l1[0])
print(l2[1])

#accessing  elements
l1=['renuka','prerna','heena','shravani','sai']
print(l1[1:3])
print(l1[:3])
print(l1[1:])
print(l1[-4:-1])
print(l1[-1])

#adding to a list

l1=['renuka','prerna','heena','shravani','sai']
l1.append('sonu')
print(l1)
l1.extend(['rima','piya'])
print(l1)
#insert the list
#insert by using this method we can add elements at specific position

l1=['renuka','prerna','heena','shravani','sai']
l1.insert(2, 'riya')
print(l1)

#list concatenation
l1=['renuka','prerna','heena','shravani','sai']
l2=[1,3,4,5,2]
l3=l1+l2
print(l3)

#removing from the list it is used in web scrapping
l1=['renuka','prerna','heena','shravani','sai']
l1.remove('sai')
print(l1)

#pop() method
#it remove element from list

l1=['renuka','prerna','heena','shravani','sai']
l1.pop(2)
print(l1)

l1=['renuka','prerna','heena','shravani','sai']
l1.pop()
print(l1)

#inserting a list

l1=['renuka','prerna','heena','shravani','sai']
l1.insert(3, 'shivani')
print(l1)

#set
#creating a set
S1={'renuka','prerna','heena','sai','shravani','sai'}
print(S1)

#adding into set
basket={'apple','orange','banana','chikoo','mango'}
basket.add('strawberry')
print(basket)
#when we want to add more the one item them it is necessary to pass more item in the list
#for this we use update()method
basket={'apple','orange','banana','chikoo','mango'}
basket.update(['strawberry','grapes','watermelon'])
print(basket)
#length
basket={'apple','orange','banana','chikoo','mango','banana','apple'}
print(len(basket))

#obtainnig the max and min
basket={'apple','orange','banana','chikoo','mango'}
print(max(basket))
print(min(basket))

#removing elements
basket={'apple','orange','banana','chikoo','mango'}
basket.remove('orange')
basket.discard('strawberry')
print(basket)


#set operation 
s1={'apple','orange','banana','chikoo','mango'}
s2={'apple','strawberry'}
print("union : ",s1|s2)
print("intersection : ",s1&s2)
print("difference : ",s1-s2)


#Dictionaries
capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
print(capitals)

#accessing element by using key
capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
print(capitals['Gujarat'])

#adding new entry
capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
capitals['West_Bengal']='Kolkatta'
print(capitals)

#change the elements
capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
capitals['Gujarat']='Gandhinagar'
print(capitals)

#removing an entry
capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
capitals.pop('Gujarat')
print(capitals)

#second method
capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
del capitals['Gujarat']
print(capitals)

#iterating over keys

capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
for state in capitals:
    print(state,end=':')
    print(capitals[state])
    print()

#values keys and items
capitals={'maharashtra':'mumbai','karnatka':'Banglore','Gujarat':'Ahmdabad'}
print(capitals.values())
print(capitals.keys())
print(capitals.items())
print(len(capitals))
print('karnatka' in capitals)
print('Bihar' not in capitals)#checking ket=y membership 

#dictionaries can have values in tuple
season={'summer':('feb','march','apr','may'),
        'rainy':('june','july','aug','sept'),
        'winter':('oct','nov','dec','jan')}
print(season['rainy'])
print(season['rainy'][3])

#dictionary method
season={'summer':('feb','march','apr','may'),
        'rainy':('june','july','aug','sept'),
        'winter':('oct','nov','dec','jan')}
print(season.get('rainy'))


