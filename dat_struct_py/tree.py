from .blocks.node import bNode

class BinarySearchTree: 
    """
    Binary Tree 
    Operations Covered 
        1. Create a binary search tree by
            a. Inserting values one by one
            b. Passing in an input list
        2. Traversals 
            a. Preorder 
            b. Inorder
            c. Postorder 
            d. Spiral
                i. Clockwise
                ii. Anticlockwise
            e. Boundary
                i. Left to Right 
                ii. Right to Left 
        3. Print Leaves 
        4. Node K nodes away from the root 
        5. Max Width of the Tree
        6. Right Hand Side View 
    """
    def __init__(self, inp_list=[]):
        """
            Initializes BST with empty root/passed input data list
        """
        self.root = None
        if inp_list:
            self.insert_from_list(inp_list)
            pass
    
    def _insert(self, node, data):
        """
            Recursively inserts data into the BST
        """
        if data <= node.data: 
            if not node.left: 
                node.left = bNode(data)
            else: 
                self._insert(node.left, data)
        else:
            if not node.right: 
                node.right = bNode(data)
            else: 
                self._insert(node.right, data)

    def insert(self, data):
        """
            Wrapper for recursively inserting into BST
        """
        if not self.root: 
            self.root = bNode(data)
        else: 
            self._insert(self.root, data)
    
    def insert_from_list(self, inp_list):
        """
            Creates a BST from the passed input list
        """
        for data in inp_list:
            self.insert(data)
        