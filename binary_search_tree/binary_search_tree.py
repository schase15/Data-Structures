"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

""" Define the root by simply setting it as a variable for the first node
root = BSTNode(26)
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Compare the input value against the node's value
    # Check if the direction we need to go in has a node
        #  If not, wrap the value in a node and park it
        #  Otherwise, go back to step 1, but with the node in that spot

    # This doesn't work if there is no root

    def insert(self, value):
        # Compare the input value with the value of the Node
        if value < self.value:
            # We need to go left
            # If there is no child node to the left
            if self.left is None:
                # Create and park the new node
                self.left = BSTNode(value)

            # Otherwise there is already a child
            else:
                # Call the insert method to do this loop again, until we reach no child node
                self.left.insert(value)
        
        # If the input value is greater than or equal to we move to the right
        else:
            # See if there is no right child
            if self.right is None:
                # Wrap the value in BSTNode and park it
                self.right = BSTNode(value)

            # Otherwise there is a child node
            else:
                # Call the insert method to continue the loop until we find a node without a child
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If the input value is equal to the node value, return true
        # Base Case
        if self.value == target:
            return True

    # Recursive cases: How do we move closer to the base case
        
        # If the input value is greater than the node value, move to the right -> re-run method on right child node
        elif self.value < target:
            # Check if there is a next node to move to to continue the comparison
            # If there is not then it is the end of the tree and there is no match, return False
            if self.right is None:
                return False
            else:
                # Call contains method on right child
                # Eventually we will need to return a value
                return self.right.contains(target)

        # If the input value is less than the node value, move to the left -> re-run method on left child node
        else:
            # Check to see if there is a node to the left to move to
            # If not then it is the end of the tree, return False
            if self.left is None:
                return False
            else: 
                # Call contains method on left child
                # Eventually we will need to return a value  
                return self.left.contains(target)

    # Return the maximum value found in the tree
    # Max value will be stored all the way to the far right of the tree
    def get_max(self):
        # if there is a node on the right move to that node
        # When you can no longer move to the right, return the value
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    # This is using depth first traversal
    def for_each(self, fn):

        # Each time the function is called do self.value.fn
        fn(self.value)

        # Then, if there is a left -> move to the left and repeat
        if self.left:
            self.left.for_each(fn)

        # If there is a right -> move to the right and repeat
        if self.right:
            self.right.for_each(fn)

        # # If there is not a right, or not a left, do nothing

### This part was done in class to explore in depth and breadth traversal methods ###

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO 
        # we'll use a stack 
        stack = []
        stack.append(self)

        # so long as our stack has nodes in it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack 
            current = stack.pop()

            # add the current node's right child first 
            if current.right:
                stack.append(current.right)

            # add the current node's left child 
            if current.left:
                stack.append(current.left)

            # call the anonymous function 
            fn(current.value)

    def iterative_breadth_first_for_each(self, fn):
        from collections import deque
        # BFT: FIFO 
        # we'll use a queue to facilitate the ordering 
        queue = deque()
        queue.append(self)

        # continue to traverse so long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):     
        # Move down to the bottom left. That is the lowest value.
        # If there is a left child, move there and re-run method
        if node.left:
            # Will not need to return a value, just move there
            node.in_order_print(node.left) 

        # Once there is no longer a left node to go to
        # i.e, it is the lowest value remaining
        # Print the node value
        print(node.value)

        # After going down the left side, check if there is a right node to move to
        # If there is, move to the right and re-run the method
            # Moving down the left side of this new node
        # Only printing the values of nodes that have no left node, 
        # or no left nodes that have not been traversed already
        if node.right:
            node.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Use a queue to store the node values for printing
        # Queue is first in first out
        # Use Deque class
            # popleft() will remove an element from the left side of the deque and return its value
        
        from collections import deque

        # Use the deque class to facilitate the ordering
        queue = deque()

        # Add first node to queue
        queue.append(node)

        # Continue to traverse as long as there are nodes in the queue
        while len(queue) > 0:
            # Look at the left most node in the queue
            current = queue.popleft()

            # If there is a node on the left of the current node, add that to the queue
            if current.left:
                queue.append(current.left)

            # If there is a node on the right of the current node, add that to the queue
            if current.right:
                queue.append(current.right)

            # After adding the left and right nodes to the queue, print the current node's value
            print(current.value)

            # Add the end of this function the 'current' node will be permanetly removed from the queue
            # and it will move to the next node in the queue, until it reaches an empty queue


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        # Use a stack to hold the nodes in order, last in first out method
        stack = []

        # Add in the passed in first node
        stack.append(node)

        # Continue to traverse the stack (last in first out method), until the stack is empty
        while len(stack) >0:

            # Look at (pop off) the last node (top) in the stack
            current = stack.pop()

            # If there is a node on the left of the current node, add that to the stack
            if current.left:
                stack.append(current.left)

            # If there is a node on the right of the current node, add that to the stack
            if current.right:
                stack.append(current.right)

            # After adding the left and right nodes to the queue, print the current node's value
            print(current.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
