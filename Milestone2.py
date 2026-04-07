# from Milestone import Student, Courses, University

"""
Enrollment record created by Ryan
"""
class EnrollmentRecord:
    def __init__(self, student, enroll_date):
        self.student = student
        self.enroll_date = enroll_date
    def __repr__(self):
        return f"Enrollment Record: {self.student.student_id}, {self.enroll_date}"
    
"""
    Linked list created by Johnny
"""

class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next
    
    def __repr__(self):
        return f"Node({self.item})"
    
class LinkedQueue:
    def __init__(self): 
        self.head = None
        self.tail = None
        self._size = 0
        
    def enqueue(self,item):
        if self.is_empty():
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        self._size += 1
    
    def dequeue(self):
        if self.head is None:
            raise AttributeError
        item = self.head.item
        
        if self.head.next is None:
            self.head = None
            self.tail = None
            return item
        self.head = self.head.next
        self._size -= 1
        return item
    
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self._size

l1 = LinkedQueue()
l1.enqueue(3)
l1.enqueue(4)
print(l1.dequeue())
print(l1.tail)
