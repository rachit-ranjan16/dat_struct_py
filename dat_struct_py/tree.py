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
    
    def _preorder_helper(self, node, out=[]):
        """
            Recursive helper for preorder traversal
        """
        if not node:
            return
        out.append(node.data)
        if node.left:
            self._preorder_helper(node.left, out)
        if node.right: 
            self._preorder_helper(node.right, out)
        return out

    def preorder(self):
        """
            Returns Preorder Traversal List 
        """
        if not self.root:
            return []
        return self._preorder_helper(self.root)

    def _inorder_helper(self, node, out=[]):
        """
            Recursive helper for inorder traversal
        """
        if not node: 
            return 
        if node.left:
            self._inorder_helper(node.left, out)
        out.append(node.data)
        if node.right: 
            self._inorder_helper(node.right, out)
        return out 
    
    def inorder(self):
        """
            Returns Preorder Traversal List 
        """
        if not self.root:
            return []
        if not self.root:
            return []
        return self._inorder_helper(self.root)

    def _postorder_helper(self, node, out=[]):
        """
            Recursive helper for inorder traversal
        """
        if not node:
            return
        if node.left:
            self._inorder_helper(node.left, out)
        if node.right:
            self._inorder_helper(node.right, out)
        out.append(node.data)
        return out

    def postorder(self):
        """
            Returns Postorder Traversal List 
        """
        if not self.root:
            return []
        return self._postorder_helper(self.root)

    def _spiral_anticlock_helper(self):
        """
            Returns Clockwise Spirally Traversed Tree
        """
        s1 = [self.root]
        s2 = []
        out = []
        while s1 or s2:
            while s1:
                n = s1.pop()
                out.append(n.data)
                if n.right:
                    s2.append(n.right)
                if n.left:
                    s2.append(n.left)
            while s2:
                n = s2.pop()
                out.append(n.data)
                if n.left:
                    s1.append(n.left)
                if n.right:
                    s1.append(n.right)
        return out

    def _spiral_clock_helper(self):
        """
            Returns Anti Clockwise Spirally Traversed Tree
        """
        s1 = [self.root]
        s2 = []
        out = []
        while s1 or s2:
            while s1:
                n = s1.pop()
                out.append(n.data)
                if n.left:
                    s2.append(n.left)
                if n.right:
                    s2.append(n.right)
            while s2:
                n = s2.pop()
                out.append(n.data)
                if n.right:
                    s1.append(n.right)
                if n.left:
                    s1.append(n.left)
        return out
    
    def spiral(self, clockwise=False):
        if not self.root: 
            return [] 
        if not clockwise:
            return self._spiral_anticlock_helper()
        else: 
            return self._spiral_clock_helper()
