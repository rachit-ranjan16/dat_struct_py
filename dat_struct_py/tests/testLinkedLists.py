import unittest
from ..linkedlist import sLinkedList, dLinkedList, cLinkedList


class testLinkedLists(unittest.TestCase):

    def setUp(self):
        self.sLL = sLinkedList()
        self.dLL = dLinkedList()
        self.cLL = cLinkedList()
        for i in range(5):
            self.sLL.insert_beginning(i+1)
            self.dLL.insert_beginning(i+1)
            self.cLL.insert_beginning(i+1)

    def testSinglyLLInsertFromBeginning(self):
        self.assertEqual(self.sLL.size(),5)
        self.assertEqual(self.sLL.head.get_data(), 5)

    def testSinglyLLInsertFromEnd(self):
        l = sLinkedList()
        for i in range(5):
            l.insert_end(i+1)
        self.assertEqual(l.size(),5)
        self.assertEqual(l.head.get_data(), 1)

    def testSinglyLLEvenLength(self):
        self.assertEqual(self.sLL.is_length_even(), False)

    def testSinglyLLCyclicity(self):
        self.assertEqual(self.sLL.is_cyclic(), False)
        self.assertEqual(self.sLL.cycle_length(), 0)

    def testSinglyLLNthElementFromEnd(self):
        self.assertEqual(self.sLL.from_the_end(2), 2)

    def testSinglyLLDelete(self):
        self.sLL.del_node(3)
        self.assertEqual(self.sLL.size(), 4)
        self.sLL.del_node(5)
        self.assertEqual(self.sLL.size(), 3)
        self.sLL.del_node(3)
        self.assertEqual(self.sLL.size(), 3)

    def testDoublyLLInsertFromBeginning(self):
        self.assertEqual(self.dLL.head.get_data(),5)
        self.assertEqual(self.dLL.size(), 5)

    def testDoublyLLInsertFromEnd(self):
        l = dLinkedList()
        for i in range(5):
            l.insert_end(i+1)
        self.assertEqual(l.size(),5)
        self.assertEqual(l.head.get_data(), 1)

    def testDoublyLLEvenLength(self):
        self.assertEqual(self.dLL.is_length_even(), False)

    def testDoublyLLCyclicity(self):
        self.assertEqual(self.dLL.is_cyclic(), False)
        self.assertEqual(self.dLL.cycle_length(), 0)

    def testDoublyLLNthElementFromEnd(self):
        self.assertEqual(self.dLL.from_the_end(2), 2)

    def testDoublyLLDelete(self):
        self.dLL.del_node(3)
        self.assertEqual(self.dLL.size(), 4)
        self.dLL.del_node(5)
        self.assertEqual(self.dLL.size(), 3)
        self.dLL.del_node(3)
        self.assertEqual(self.dLL.size(), 3)

    def testCicularlyLLInsertFromBeginning(self):
        self.assertEqual(self.cLL.head.get_data(),5)
        self.assertEqual(self.cLL.size(), 5)

    def testCicularlyLLInsertFromEnd(self):
        l = cLinkedList()
        for i in range(5):
            l.insert_end(i+1)
        self.assertEqual(l.size(),5)
        self.assertEqual(l.head.get_data(), 1)

    def testCicularlyLLEvenLength(self):
        self.assertEqual(self.cLL.is_length_even(), False)

    def testCicularlyLLCyclicity(self):
        self.assertEqual(self.cLL.is_cyclic(), True)
        self.assertEqual(self.cLL.cycle_length(), 5)

    def testCicularlyLLNthElementFromEnd(self):
        self.assertEqual(self.cLL.from_the_end(2), 2)

    def testCicularlyLLDelete(self):
        self.cLL.del_node(3)
        self.assertEqual(self.cLL.size(), 4)
        self.cLL.del_node(5)
        self.assertEqual(self.cLL.size(), 3)
        self.cLL.del_node(3)
        self.assertEqual(self.cLL.size(), 3)


if __name__ == "__main__":
    unittest.main()
