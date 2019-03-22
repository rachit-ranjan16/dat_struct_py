import unittest
from ..tree import BinarySearchTree

class TestBinarySearchTrees(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree() 
        self.bst.insert_from_list([5, 4, 3, 8, 7])
        #       5 
        #     /   \ 
        #    4      8
        #  /      /
        # 3      7
    
    def check_integrity(self):
        self.assertEqual(self.bst.root.data, 5)
        self.assertEqual(self.bst.root.left.data, 4)
        self.assertEqual(self.bst.root.right.data, 8)
        self.assertEqual(self.bst.root.right.left.data, 7)
        self.assertEqual(self.bst.root.left.data, 4)
        self.assertEqual(self.bst.root.left.left.data, 3)

    def testInsertFromList(self):
        inp_list = [i + 1 for i in range(3)]
        bst = BinarySearchTree(inp_list=inp_list)
        self.assertEqual(bst.root.data, 1)
        self.assertIsNone(bst.root.left)
        self.assertEqual(bst.root.right.data, 2)
        self.assertIsNone(bst.root.right.left)
        self.assertEqual(bst.root.right.right.data, 3)
        self.assertIsNone(bst.root.right.right.left)
        self.assertIsNone(bst.root.right.right.right)

    def testInsert(self):
        self.bst.insert(9)
        self.assertEqual(self.bst.root.right.right.data, 9)
        self.check_integrity()
    
    def testEmptyTreeTraversals(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder(), [])
        self.assertEqual(bst.inorder(), [])
        self.assertEqual(bst.postorder(), [])
        self.assertEqual(bst.spiral(), [])
        self.assertEqual(bst.spiral(clockwise=True), [])

    def testPreorderTraversal(self):
        preorder = self.bst.preorder()
        print(preorder)
        self.assertEqual(len(preorder), 5)
        self.assertEqual(preorder, [5, 4, 3, 8, 7])
    
    def testInorderTraversal(self):
        inorder = self.bst.inorder() 
        self.assertEqual(len(inorder), 5)
        self.assertEqual(inorder, [3, 4, 5, 7, 8])

    def testPostorderTraversal(self):
        postorder = self.bst.postorder()
        self.assertEqual(len(postorder), 5)
        self.assertEqual(postorder, [3, 4, 7, 8, 5])

    def testSpiralAntiClockwise(self):
        spiral_anticlock = self.bst.spiral()
        self.assertEqual(len(spiral_anticlock), 5)
        self.assertEqual(spiral_anticlock, [5, 4, 8, 7, 3])

    def testSpiralClockwise(self):
        spiral_clock = self.bst.spiral(clockwise=True)
        self.assertEqual(len(spiral_clock), 5)
        self.assertEqual(spiral_clock, [5, 8, 4, 3, 7])

    def testRhsView(self):
        rhs_view = self.bst.view(rhs=True)
        self.assertEqual(len(rhs_view), 3)
        self.assertEqual(rhs_view, [5, 8, 7])

    def testLhsView(self):
        lhs_view = self.bst.view(rhs=False)
        self.assertEqual(len(lhs_view), 3)
        self.assertEqual(lhs_view, [5, 4, 3])
