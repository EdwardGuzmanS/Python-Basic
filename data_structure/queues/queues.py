#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 20:39:40 2025

@author: edu
"""
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, data):
        self.queue.appendleft(data)
        
    def dequeue(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def front(self):
        return self.queue[-1]
    

import time
import threading

orders = ['pizza','samosa','pasta','biryani','burger']
food_queue = Queue()

def place_order(orders):
    for order in orders:
        print(f'Placing order for: {order}\n')
        food_queue.enqueue(order)
        time.sleep(0.5)        

def serve_order():
    time.sleep(1)
    while food_queue.size() != 0:
        print(f'Now serving: {food_queue.dequeue()}\n')
        time.sleep(2)

# t1 = threading.Thread(target= place_order, args=(orders,))
# t2 = threading.Thread(target= serve_order)


# t1.start()
# t2.start()

# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
#     1
#     10
#     11
#     100
#     101
#     110
#     111
#     1000
#     1001
#     1010
# Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

# You also need to add front() function in queue class that can return the front element in the queue.


def print_binary(n):
    binary_queue = Queue()
    
    binary_queue.enqueue("1")
    
    for c in range(n):
        print(f'{c+1}.-  {binary_queue.front()}')
        binary_queue.enqueue(binary_queue.front() + "0")
        binary_queue.enqueue(binary_queue.front() + "1")
        binary_queue.dequeue()
        
    

print_binary(10)



