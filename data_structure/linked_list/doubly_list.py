#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 23:22:01 2025

2)Implement doubly linked list. The only difference with regular linked list 
  is that double linked has prev node reference as well. That way you can 
  iterate in forward and backward direction. Your node class will look this
  
  class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
Add following new methods

    def print_forward(self):
        # This method prints list in forward direction. Use node.next

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
@author: edu
"""

        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None   
        self.tail = None
        
    def __len__(self):
        if self.head is None:
            return 0
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter
        
    def __str__(self):
        if self.head is None:
            return "Empty"
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
            
        return "None <--> " + " <--> ".join(nodes) + "<--> None"
    

    def insert_at_start(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
 

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_start(data)
            return
        
        else:
            last_node = self.tail          
            new_node = Node(data)
            
            last_node.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
   
    def insert_at(self, index, data):        
        
        if index == 0:
            self.insert_at_start(data)
            return
        
        elif 0 > index: 
            raise IndexError("Negative Index")
            
        
        elif index > len(self):
            raise IndexError("The Values are out of bounds")
        
        
        elif index == len(self):
            self.insert_at_end(data)
            return
        
        else:
            counter = 0
            current = self.head
            while current.next:
                if counter == (index - 1):
                    new_node = Node(data)
                    new_node.next = current.next
                    new_node.prev = current
                    current.next.prev = new_node
                    current.next = new_node
                    break

                counter += 1
                current = current.next
            
    def remove_at(self, index):
        if self.head is None:
            raise ValueError("No elements to delete")
            
        
        elif  0 > index: 
            raise IndexError("Negative Index")
            
        
        elif index >= len(self):
            raise IndexError("The value of the index is incorrect")
            return
        
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        
        else:
            counter = 0
            current = self.head
            while current:
                if counter == (index - 1):
                    node_to_remove = current.next
                    current.next = node_to_remove.next
                    if node_to_remove.next:
                        node_to_remove.next.prev = current
                    break
                current = current.next
                counter += 1
    
    def remove_value(self, data):
        if not self.head:
            print("The list is empty")
            return
            
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                node_to_remove = current.next
                current.next = node_to_remove.next
                if node_to_remove.next:
                    node_to_remove.next.prev = current
                break
            current = current.next
    
    def remove_from_end(self):
        if self.head is None:
            print("No elements to remove")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
            
        previous_last_node = self.tail.prev 
        self.tail = previous_last_node
        self.tail.next = None
            
            
    
    def get_last_node(self):
        if self.head is None:
            print("Doesn't exist values in the Linkedlist")
            return

        return self.tail.data
    
    def peek(self):
        '''
        This method is for see the first element on the Linkedlist
        '''
        if self.head is None:     
            return None
        
        return self.head.data
    
    def print_forward(self):
        if self.head is None:
            print("There are no elements in the list")
            return      
        print("None", end = " <--> ")
        current = self.head
        while current:
            print(current.data, end = " <--> ")
            current = current.next
        print("None")
            
    def print_backward(self):
        if self.tail is None:
            print("There are no elements iin the list")
            return
        print("None", end = " <--> ")
        current = self.tail
        while current:
            print(current.data, end = " <--> ")
            current = current.prev
        print("None")

# ==========================
# PRUEBA DEFINITIVA LINKEDLIST
# ==========================

ll = Linkedlist()

print("\n==== 1. __str__ y __len__ en lista vacía ====")
print("Lista vacía (esperado 'Empty' o similar):", str(ll))
print("Largo (esperado 0):", len(ll))

print("\n==== 2. Insertar al inicio y al final ====")
ll.insert_at_start(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
print("Lista después de inserciones (esperado 10 --> 20 --> 30 --> None):", ll)
print("Largo (esperado 3):", len(ll))

print("\n==== 3. Insertar en índice específico ====")
ll.insert_at(1, 15)  # entre 10 y 20
ll.insert_at(0, 5)   # al inicio
ll.insert_at(len(ll), 40)  # al final
print("Lista después de insert_at:", ll)
print("Largo (esperado 6):", len(ll))

print("\n==== 4. Insertar con índices inválidos ====")
try:
    ll.insert_at(-1, 99)
except Exception as e:
    print("Error esperado (índice negativo):", e)
try:
    ll.insert_at(100, 99)
except Exception as e:
    print("Error esperado (fuera de rango):", e)

print("\n==== 5. remove_at en diferentes posiciones ====")
print("Lista antes:", ll)
ll.remove_at(0)   # borra 5
ll.remove_at(2)   # borra 20
ll.remove_at(len(ll)-1)  
print("Lista después de remove_at:", ll)
print("Largo (esperado 3):", len(ll))

print("\n==== 6. remove_at inválidos ====")
try:
    ll.remove_at(-1)
except Exception as e:
    print("Error esperado:", e)
try:
    ll.remove_at(100)
except Exception as e:
    print("Error esperado:", e)

print("\n==== 7. remove_value existente y no existente ====")
print("Lista antes:", ll)
ll.remove_value(15)  # borrar existente
print("Después de borrar 15:", ll)
ll.remove_value(99)  # no existe
print("Después de intentar borrar 99 (sin cambios):", ll)

print("\n==== 8. remove_from_end ====")
print("Lista antes:", ll)
ll.remove_from_end()
print("Después de remove_from_end:", ll)

print("\n==== 9. get_last_node ====")
ll.insert_at_start(30)
print("Último nodo (esperado 30):", ll.get_last_node())

print("\n==== 10. peek ====")
ll.insert_at_start(10)
print("Primer nodo (esperado 10):", ll.peek())
ll2 = Linkedlist()
print("Peek en lista vacía (esperado None):", ll2.peek())

print("\n==== 11. Prueba de borrado hasta vaciar ====")
print("Lista antes:", ll)
while len(ll) > 0:
    print("Peek:", ll.peek())
    ll.remove_from_end()
    print("Lista:", ll)
print("Lista final (esperado vacía):", ll)
