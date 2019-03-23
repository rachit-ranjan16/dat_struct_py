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
        """
            Returns Clockwise/Counter Clockwise Spirally Traversed Tree
        """
        if not self.root: 
            return [] 
        if not clockwise:
            return self._spiral_anticlock_helper()
        else: 
            return self._spiral_clock_helper()
    
    def _rhs_view(self):
        """
            Returns the RHS View/Projection of the tree
        """
        q, out  = [], [] 
        q.append(self.root)
        while q:
            c = len(q)
            while c!=0:
                if c == 1:
                    out.append(q[0].data)
                n = q.pop(0)
                if n.left: 
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                c -= 1 
        return out

    def _lhs_view(self):
        """
            Returns the LHS View/Projection of the tree
        """
        q, out = [], []
        q.append(self.root)
        while q:
            c = len(q)
            while c != 0:
                if c == 1:
                    out.append(q[0].data)
                n = q.pop(0)
                if n.right:
                    q.append(n.right)
                if n.left:
                    q.append(n.left)
                c -= 1
        return out

    def view(self, rhs=True):
        """
            Returns the Right/Left Hand View/Projection of the tree
        """
        if not self.root: 
            return []
        if not rhs: 
            return self._lhs_view()
        else: 
            return self._rhs_view()

    def get_leaves(self, out=[]):
        """
            Returns leaves of the tree
        """
        pass 

    def _get_leaves(self, root, visited_set, out):
        if not root:
            return 
        if not root.left and not root.right: 
            if root not in visited_set:
                visited_set.add(root)
                out.append(root.data)
        if root.left:
            self._get_leaves(root.left, visited_set, out)
        if root.right:
            self._get_leaves(root.right, visited_set, out)


    def get_boundary(self):
        """
            Returns the boundary nodes of the tree
        """
        if not self.root: 
            return []
        out = []
        visited_set = set()
        visited_set.add(self.root)
        out.append(self.root.data)
        l = self.root.left

        # Traverse Left to Bottom
        while l:
            visited_set.add(l)
            out.append(l.data)
            l = l.left
        
        # Get all the leaves
        self._get_leaves(self.root, visited_set, out)
        #TODO Remove this 
        # return out
        
        # Get al the nodes from right bottom to the root
        stack = []
        r = self.root.right 
        while r:
            if r not in visited_set:
                visited_set.add(r)
                stack.append(r)
            r = r.right
        for node in stack[::-1]:
            out.append(node.data)
        
        return out 