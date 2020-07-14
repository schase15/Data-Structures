"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# # Queue class with an array as storage
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         # Add value to the end of the storage
#         self.storage.append(value) # O(1)
#         # Add 1 to the size of the Queue
#         self.size += 1

#     # Remove the first value - Queue's function first in first out
#     def dequeue(self):
#         # If the Queue is empty
#         if self.size == 0:
#             return
#         else:
#             # Subtract 1 from the size of the storage
#             self.size -= 1
#             # Remove the first element 
#             return self.storage.pop(0) # O(n)


import sys
sys.path.append('../singly_linked_list')

from singly_linked_list import LinkedList

# Queue class with an array as LinkedList
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        # Add value to the end of the storage
        self.storage.add_to_tail(value) # O(1)
        # Add 1 to the size of the Queue
        self.size += 1

    # Remove the first value - Queue's function first in first out
    def dequeue(self):
        # If the Queue is empty
        if self.size == 0:
            return
       
        else:
            # Subtract 1 from the size of the storage
            self.size -= 1
            # Remove the first element 
            return self.storage.remove_head() # O(1)


'''
Runtimes are quicker with linked list
'''

'''
Using a linked list vs using an array is very similar when implementing a Queue class.
Values are added to the end using the add_to_tail method of the LinkedList or the append method
in the array. Then values are removed from the front by using the remove head method for the LinkedList
or the pop(0) method for the array. The remove_head method sets tail equal to none if there is only
1 element in storage. 
'''

