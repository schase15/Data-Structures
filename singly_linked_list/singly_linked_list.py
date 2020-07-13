# Single Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

## Clunky, inefficient way to build linked lists
## Have to start from the head and traverse all the way to the end of the list to add a new element
## Runtime was O(n)

# ll = Node(1)
# ll.set_next = Node(2)
# ll.next.set_next = Node(3)
# ll.next.next.set_next = Node(4)
# ll.next.next.next.set_next = Node(5)

## Create a tail variable
## Runtime is now O(1)
## Create new node, set the old tail to point to the new node, reassign the new node as the tail


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):

        # 1. create the Node from the value
        new_node = Node(value)

        # What do we do if tail is None?
        # We should also look at the head to see if it is an empty linked list
        if self.head is None and self.tail is None:

            # If it is an empty linked list, add a single node which is both the head and the tail
            self.head = new_node

            # Set the new node to be the tail
            self.tail = new_node

        # These three steps assume that the tail is already reffering to a Node
        else:
            # 2. Set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)

            # 3. Reassign the self.tail to refer to the new Node 
            self.tail = new_node

    def remove_head(self):
        # If we have an empty linked list
        if self.head is None and self.tail is None:
             return
        
        # What if we only have a single elem in the linked list?
        # Both head and tail are pointing to the same Node

        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None

            # Also delete the linked list's tail reference
            self.tail = None

            return head.get_value()

        val = self.head.get_value()

        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val
    
    def remove_tail(self):
        # If we have an empty linked list
        if self.head is None:
             return 
       
        # If we have a non-empty linked list
        # We have to start at the head and move down the linked list
        # until we get to the node right before the tail
        current = self.head

        # Iterate through until you reach the last node before the tail
        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()

        # At this point, 'current' is the node right before the tail
        value = self.tail.get_value()

        # Move self.tail to the Node right before
        self.tail = current
        self.tail.set_next(None)
        return value

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head

        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True

            # update our current node to the current node's next node
            current = current.get_next()

        # if we've gotten here, then the target node isn't in our list
        return False

        
    def get_max(self):
        if not self.head:
            return None

        # reference to the largest value we've seen so far
        max_value = self.head.get_value()

        # reference to our current node as we traverse the list
        current = self.head.get_next()

        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:

                # if so, update our max_value variable
                max_value = current.get_value()

            # update the current node to the next node in the list
            current = current.get_next()

        return max_value
