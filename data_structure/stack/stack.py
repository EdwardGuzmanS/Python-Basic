#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 22:12:21 2025

Implement the stack data type from zero (remaining)
Implement reverse_string("") (success)
Implement matching brackets (success)
Implement Tower of Hanoi (remaining)


@author: edu
"""
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, data):
        self.container.append(data) 
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
        
    def isEmpty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
#Implement Reverse String    
def reverse_str(text: str) -> str:
    stack = Stack()
    reverse_stack = ""
    
    for c in text:
        stack.push(c)
        
    for _ in range(len(text)):# Se puede cambiar por:
    #while stack.size() != 0
       reverse_stack += stack.pop()
    print(reverse_stack)
    
reverse_str("Valery")
#91-DIVOC ereuqnoc lliw eW

#Implement Mathcing brackets
def matching_brackets(brackets_string: str) -> bool:
    bracket_stack = Stack()
    dict_reverse_brackets = {"]" : "[",
                             "}" : "{",
                             ")" : "("
                             }
    
    rigth_bracket = dict_reverse_brackets.keys()
    left_bracket = dict_reverse_brackets.values()
    
    for bracket in brackets_string:
        if bracket in left_bracket:
            bracket_stack.push(bracket)
            
        elif bracket in rigth_bracket:
            if bracket_stack.isEmpty():
                return False
            
            elif bracket_stack.pop() != dict_reverse_brackets[bracket]:
                return False   
        else:
            continue
        
    return bracket_stack.isEmpty()
        
# print("[()] ->", matching_brackets("[()]") )
# print()
# print("[() ->", matching_brackets("[()") )
# print()
# print("[()) ->", matching_brackets("[())") )
# print()
# print("[(a) + (b)] ->", matching_brackets("[()]") )
# print()
# print("({a+b}) ->", matching_brackets("({a+b})"))
# print()
# print("))((a+b}{ ->", matching_brackets("))((a+b}{"))
# print()
# print("((a+b)) ->", matching_brackets("((a+b))"))
# print()
# print(")) ->", matching_brackets("))"))
# print()
# print("[a+b]*(x+2y)*{gg+kk} ->", matching_brackets("[a+b]*(x+2y)*{gg+kk}"))


#Implement Tower of Hanoi














