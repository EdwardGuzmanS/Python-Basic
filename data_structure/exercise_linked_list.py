#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 21:36:10 2025
This is a exercise to improve in LinkedList so 

1) implement the following methods.

    def remove_by_value(self, data):
        # Remove first node that contains data
        
    
    @author: edu
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_start(data)
            return
        
        new_node = Node(data)
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
        
    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_start()
            
        if index == -1:
            self.insert_at_end(data)
        
        if index > self.get_length_list():
            raise Exception("Insert valid index")
        
        count = 0
        current_node = self.head
        
        while current_node:
            if count == (index - 1):
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                break
            current_node = current_node.next
            count += 1
            
    def remove_at(self, index):
        if index < 0 or (self.get_length_list() -1) < index:
            raise Exception("Insert a valid index")
        if index == 0:
            self.head = self.head.next
        
        count = 0
        current_node = self.head
        while current_node:
            if count == (index - 1):
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            count += 1
    
    def get_length_list(self):
        if self.head is None:
            return 0
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
            
    def display(self):
        if self.head is None:
            print("List is empty")
        current = self.head
        while current:
            print(current.data, end = ' --> ')
            current = current.next
        print('None')

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("There are no elements to remove")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:     
                current.next = current.next.next
                break
            current = current.next
            
ll = Linked_list()
ll.insert_at_end("banana")
ll.insert_at_end("mango")
ll.insert_at_end("grapes")
ll.insert_at_end("orange")
ll.display()
ll.remove_by_value("mango")

ll.display()
