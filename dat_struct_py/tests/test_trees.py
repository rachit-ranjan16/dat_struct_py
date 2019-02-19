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