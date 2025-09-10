#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 02:01:07 2025

From:Codebasics
Exercise: Array DataStructure

1.) Let us say your expense for every month are listed below,

January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to 
our monthly expense list 
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this


2) You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


3) Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function

@author: edu
"""
january = 2200
february = 2350
march = 2600
april = 2130
may = 2190

expense = []


expense.append(january)
expense.append(february)
expense.append(march)
expense.append(april)
expense.append(may)

question1 = expense[1] - expense[0]
print(f"La respuesta 1 es: {question1}") 

question2 = expense[1] + expense[2] + expense[3]
print(f"La respuesta 2 es: {question2}")

if 2000 in expense:
    print("There are month with 2000 dolars")
else:
    print("There are no month with exactly 2000 dolars")
    
june = 1980
expense.append(june)
print(f"It's added a new month {expense}")

refund = 200
april_actualized = expense[3] + refund
expense[3] = april_actualized
print(f"The April month is actualized {expense}")

#################################################################
heros=['spider man','thor','hulk','iron man','captain america']

#Excersice 1
print(f"The length of the list is: {len(heros)}")
print()
#Excersice 2
heros.append("black panter")
print(f"The list is actualized {heros}")
print()
#Excersice 3
heros.pop()
heros.insert(3, "black panter")
print(f"The list is actualized {heros}")
print()
#Excersice 4
heros[1:3] = ["doctor strange"]
print(f"The list is actualized {heros}")
print()
#Excersice 5
heros.sort()
print(heros)
print()


#################################################################
odds=[]
num = int(input("Put a number: "))
for n in range(num + 1):
    if n % 2 == 0:
      odds.append(n)
      
print(odds)      
      
      
    