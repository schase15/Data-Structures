"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create new node using the input value
        new_node = ListNode(value)
        # Add a count to the length of the list
        self.length += 1

        # If it is an empty list
        if self.head is None and self.tail is None:
            # Add new node as the head of the list
            self.head = new_node
            # Also define it as the tail of the list
            self.tail = new_node

        # If the list is not empty
        else:
            # Save the old head to assign as new_node's next node
            old_head = self.head
            # Reassign head as the new node
            self.head = new_node
            # Assign old head as next for the new head
            new_node.next = old_head
            # Assign new node as previous for the old head
            old_head.prev = new_node
            
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        # If the list is empty
        if self.head is None and self.tail is None:
            # Do nothing
            return

        # If the list only has one item
        # It has no prev or next reference
        elif self.length == 1:
            # Save value to return later
            value = self.head.value
            # Remove references of head/tail to the single element
            self.head = None
            self.tail = None
            # Adjust the length of the list
            self.length -= 1
            # Return the value removed
            return value

        # If the list is not empty and not only 1 element
        else:
            # Adjust the list length count
            self.length -= 1
            # Save the old head to return the value later
            old_head = self.head
            # Move the head to the next node from the current head
            new_head = old_head.next
            self.head = new_head
            # Remove reference to the old head (previous of the new head)
            self.head.prev = None
            # Return the value of the removed head
            return old_head.value


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create new node out of given value
        new_node = ListNode(value)
        # Adjust the length of the list
        self.length += 1

        # If the list is empty
        if self.head is None and self.tail is None:
            # Assign the new node as both the head and the tail
            self.head = new_node
            self.tail = new_node

        # If the list is not empty
        else:
            # Save old tail to assign as new tail's previous node
            old_tail = self.tail
            new_node.prev = old_tail
            # Assign new node as the tail
            self.tail = new_node
            # Assign new node as the old tail's next
            old_tail.next = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # If the list is empty
        if self.length == 0:
            # Do nothing
            return

        # If the list is one element
        elif self.length ==1:
            # Adjust the length of the list
            self.length -= 1
            # Save the value to return at the end
            value = self.tail.value
            # Remove references of both head and tail
            self.head = None
            self.tail = None
            # Return the removed tail value
            return value

        # Otherwise
        else:
            # Adjust the length of the list
            self.length -= 1
            # Save old tail to use later
            old_tail = self.tail
            # New tail is old tails previous node
            new_tail = old_tail.prev
            # Assign tail to new tail
            self.tail = new_tail
            # Remove reference to old tail
            # Tail node will never have a next node
            self.tail.next = None
            # Return removed tail value
            return old_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        # If the list is empty; do nothing
        # If list is length 1; do nothing, it is already at the front
        # If the selected node is the head; do nothing it is already at the front
        if self.length == 0 or self.length == 1 or node.prev == None:
            return

        # If the selected node is the tail
        # Test to see if it is the tail (no node.next)
        elif node.next == None:
            # Use other methods you already built

            # remove from the tail, save the value
            value = node.value
            self.remove_from_tail()
            # Add node with saved value to the head
            self.add_to_head(value)

        # Otherwise
        else:
            # Given input node,
            # Save the selected node, and the previous and next for easy reference
            selected_node = node
            prev_node = selected_node.prev
            next_node = selected_node.next
            # Assign the previous node's next to the next node
            prev_node.next = next_node
            # Assign the next nodes' previous to the previous node
            next_node.prev = prev_node
            
            # Save old head, assign old head as new head's next
            old_head = self.head
            old_head.prev = selected_node

            # Assign selected node's next as old head
            selected_node.next = old_head

            # Assign selected node as list head
            self.head = selected_node
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # If the list is empty; do nothing
        # If the list is 1 its only element will be listed as a tail. so,
        # If the selected node is the tail; do nothing
        if self.length == 0 or node.next == None:
            return

        # If the selected node is the head
        elif node.prev == None:
            # Save value
            value = node.value
            # Use remove_from_head method
            self.remove_from_head()
            # Add the value to the end of the list
            self.add_to_tail(value)

        # Otherwise:
        else:
            # Connect the two nodes on either side of the selected node
            # Save the selected node, and the previous and next for easy reference
            selected_node = node
            prev_node = selected_node.prev
            next_node = selected_node.next
            # Assign the previous node's next to the next node
            prev_node.next = next_node
            # Assign the next nodes' previous to the previous node
            next_node.prev = prev_node

            # We are removing this node and adding a brand new node using the add_to_tail method
            # So we need to adjust the length of the list
            self.length -= 1

            # Add to tail using add_to_tail method
            value = selected_node.value
            self.add_to_tail(value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # If the list is empty; do nothing
        if self.length == 0:
            return

        # If the list is 1 element; remove the one element
        elif self.length == 1:
            self.head = None
            self.tail = None
            # Adjust length of list
            self.length -= 1

        # If the selected node is the head; use remove_head method
        elif node.prev == None:
            self.remove_from_head()

        # If the selected node is the tail; use remove_tail method
        elif node.next == None:
            self.remove_from_tail()

        # Otherwise
        else:
            # Remove all references to the selected node by connecting the two nodes on either side
            # By-passing the selected node

            # Save the selected node, and the previous and next for easy reference
            selected_node = node
            prev_node = selected_node.prev
            next_node = selected_node.next
            # Assign the previous node's next to the next node
            prev_node.next = next_node
            # Assign the next nodes' previous to the previous node
            next_node.prev = prev_node


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # Start with the max value as the value of the head
        max_value = self.head.value

        # Set next node to move through the list from
        # Start at the front
        next_node = self.head.next

        # While there is a next node
        while next_node != None:

            # Check to see if the value on the next node is greater than the currently saved max_value
            if next_node.value > max_value:
                # If it is, update max_value
                max_value = next_node.value
                # If its not, it will not enter this if statement

            # After checking if it should update the max_value,
            # Update the next_node variable to move to the next node and run the loop again
            next_node = next_node.next

        # When there is no longer a next node, return the max_value
        return max_value
