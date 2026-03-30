# from Milestone import Student, Courses, University

"""
    Linked list created by Johnny
"""

class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next  = next
    
    def __repr__(self):
        return f"Node({self.item})"
    
class LinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None
        
    def enqueue(self,item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
    
    def dequeue(self):
        if self.head is None:
            raise AttributeError
        item = self.head.item
        
        if self.head.next is None:
            self.head = None
            self.tail = None
            return item
        self.head = self.head.next
        return item

    def peek(self):
        return self.head.item
    
    def is_empty(self):
        if self.head.item == None:
            return True

l1 = LinkedList()
l1.enqueue(3)
l1.enqueue(4)
print(l1.dequeue())
print(l1.tail)
