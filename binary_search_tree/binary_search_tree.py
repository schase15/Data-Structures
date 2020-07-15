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

        if self.value == target:
            return True
        # If the input value is greater than the node value, move to the right -> re-run method
        elif self.value < target:
            # Check if there is a next node to move to to continue the comparison
            # If there is not then it is the end of the tree and there is no match, return False
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        # If the input value is less than the node value, move to the left -> re-run method
        else:
            # Check to see if there is a node to the left to move to
            # If not then it is the end of the tree, return False
            if self.left is None:
                return False
            else:   
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
    def for_each(self, fn):

        # Each time the function is called do self.value.fn
        fn(self.value)

        # Then, if there is a left -> move to the left and repeat
        if self.left:
            print('Moved left')
            self.left.for_each(fn)

        # If there is a right -> move to the right and repeat
        if self.right:
            print('Moved right')
            self.right.for_each(fn)

        # # If there is not a right, or not a left, do nothing



    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
