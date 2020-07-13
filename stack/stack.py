"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# # Stack class using an array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # storage is an array
#         self.storage = []

#     # Return the size of the storage
#     def __len__(self):
#         return self.size

#     # Add on a value to the end of the array
#     # Modify self.size to be the length of the array
#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     # Remove the last value from the array
#     # Update the length of the array
#     def pop(self):
#         # If empty do nothing
#         if self.size == 0:
#             return None
#         else:
#             popped = self.storage.pop()
#             self.size = len(self.storage)
#             return popped



# Stack class using linked list

# Import linked list
import sys
sys.path.append('../singly_linked_list')

from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        # Starts as a blank linked list
        self.size = 0
        # storage is a linked list
        self.storage = LinkedList()

    def __len__(self):
        # Return the size of the storage
        return self.size

    # Add on a value to the end of the array using the LinkedList methods
    def push(self, value):
        # Add 1 to the length of the storage
        self.size += 1
        # Use add to tail method to add value to the end of the linked list
        return self.storage.add_to_tail(value)

    # Remove the last value from the array - Last in first out 
    def pop(self):
        # If there is only one element left, it is the head
        # use remove head method
        if self.size == 1:
            # Decrease the size of the storage by 1
            self.size -= 1
            return self.storage.remove_head()

        elif self.size > 1:
            # Decrease the size of the storage by 1
            self.size -= 1
            return self.storage.remove_tail()

        else:
            return


'''
3. The biggest differences between implementing the stack class with an array vs with a linked list
is that you need to be much more specific with the linked list. The linked list has a specified head and
tail. The remove tail function only works with the tail of the linked list. When there is one element left,
if it is listed as a head and not a tail, than it will not be removed by the remove_tail method. With an array,
the pop() method will return the last element in the array even if it is the last one. 
'''
