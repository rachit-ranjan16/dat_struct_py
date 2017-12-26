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

    def testSinglyLLInputFromListBeginning(self):
        inp_list = [1,2,3,4,5]
        l = sLinkedList(inp_list=inp_list, insertEnd=False)
        self.assertEqual(l.size(), 5)
        self.assertEqual(l.head.get_data(), 5)
        cur = l.head
        while cur.get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 1)

    def testSinglyLLInputFromListEnd(self):
        inp_list = [1,2,3,4,5]
        l = sLinkedList(inp_list=inp_list)
        self.assertEqual(l.size(), 5)
        self.assertEqual(l.head.get_data(), 1)
        cur = l.head
        while cur.get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 5)

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
        self.assertEqual(sLinkedList().is_length_even(), True)

    def testSinglyLLCyclicity(self):
        self.assertEqual(self.sLL.is_cyclic(), False)
        self.assertEqual(self.sLL.cycle_length(), 0)
        self.assertEqual(sLinkedList().cycle_length(), 0)

    def testSinglyLLNthElementFromEnd(self):
        self.assertEqual(self.sLL.from_the_end(2), 2)
        self.assertEqual(self.sLL.from_the_end(10), False)

    def testSinglyLLDelete(self):
        self.sLL.del_node(3)
        self.assertEqual(self.sLL.size(), 4)
        self.sLL.del_node(5)
        self.assertEqual(self.sLL.size(), 3)
        self.sLL.del_node(3)
        self.assertEqual(self.sLL.size(), 3)

    def testSinglyLLRevInPlace(self):
        self.sLL.rev_in_place()
        self.assertEqual(self.sLL.head.get_data(), 1)
        cur = self.sLL.head
        self.assertEqual(self.sLL.size(), 5)
        while cur.get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 5)

    def testSinglyLLSwapPairs(self):
        self.assertEqual(sLinkedList().swap_pairs(), False)
        self.sLL.insert_beginning(6)
        self.assertEqual(self.sLL.swap_pairs(), True)
        self.assertEqual(self.sLL.head.get_data(), 5)
        self.assertEqual(self.sLL.head.get_next().get_data(), 6)
        cur = self.sLL.head
        while cur.get_next().get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 1)
        self.assertEqual(cur.get_next().get_data(), 2)
        self.assertEqual(self.sLL.head.get_data(), 5)

    def testDoublyLLInputFromListBeginning(self):
        inp_list = [1,2,3,4,5]
        l = dLinkedList(inp_list=inp_list, insertEnd=False)
        self.assertEqual(l.size(), 5)
        self.assertEqual(l.head.get_data(), 5)
        cur = l.head
        while cur.get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 1)

    def testDoublyLLInputFromListEnd(self):
        inp_list = [1,2,3,4,5]
        l = dLinkedList(inp_list=inp_list)
        self.assertEqual(l.size(), 5)
        self.assertEqual(l.head.get_data(), 1)
        cur = l.head
        while cur.get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 5)

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
        self.assertEqual(dLinkedList().is_length_even(), True)

    def testDoublyLLCyclicity(self):
        self.assertEqual(self.dLL.is_cyclic(), False)
        self.assertEqual(self.dLL.cycle_length(), 0)
        self.assertEqual(dLinkedList().cycle_length(), 0)

    def testDoublyLLNthElementFromEnd(self):
        self.assertEqual(self.dLL.from_the_end(2), 2)
        self.assertEqual(self.dLL.from_the_end(12), False)

    def testDoublyLLDelete(self):
        self.dLL.del_node(3)
        self.assertEqual(self.dLL.size(), 4)
        self.dLL.del_node(5)
        self.assertEqual(self.dLL.size(), 3)
        self.dLL.del_node(3)
        self.assertEqual(self.dLL.size(), 3)

    def testDoublyLLRevInPlace(self):
        self.dLL.rev_in_place()
        self.assertEqual(self.dLL.head.get_data(), 1)
        cur = self.dLL.head
        self.assertEqual(self.dLL.size(), 5)
        while cur.get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 5)

    def testDoublyLLSwapPairs(self):
        self.assertEqual(sLinkedList().swap_pairs(), False)
        self.dLL.insert_beginning(6)
        self.assertEqual(self.dLL.swap_pairs(), True)
        self.assertEqual(self.dLL.head.get_data(), 5)
        self.assertEqual(self.dLL.head.get_next().get_data(), 6)
        cur = self.dLL.head
        while cur.get_next().get_next() is not None:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 1)
        self.assertEqual(cur.get_next().get_data(), 2)
        self.assertEqual(self.dLL.head.get_data(), 5)

    def testCircularlyLLInputFromListBeginning(self):
        inp_list = [1,2,3,4,5]
        l = cLinkedList(inp_list=inp_list, insertEnd=False)
        self.assertEqual(l.size(), 5)
        self.assertEqual(l.head.get_data(), 5)
        cur = l.head
        while cur.get_next() != l.head:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 1)

    def testCircularlyLLInputFromListEnd(self):
        inp_list = [1,2,3,4,5]
        l = cLinkedList(inp_list=inp_list)
        self.assertEqual(l.size(), 5)
        self.assertEqual(l.head.get_data(), 1)
        cur = l.head
        while cur.get_next() != l.head:
                cur = cur.get_next()
        self.assertEqual(cur.get_data(), 5)

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
        self.assertEqual(cLinkedList().is_length_even(), True)

    def testCicularlyLLCyclicity(self):
        self.assertEqual(self.cLL.is_cyclic(), True)
        self.assertEqual(self.cLL.cycle_length(), 5)
        self.assertEqual(cLinkedList().cycle_length(), 0)

    def testCicularlyLLNthElementFromEnd(self):
        self.assertEqual(self.cLL.from_the_end(2), 2)
        self.assertEqual(self.cLL.from_the_end(10), False)

    def testCicularlyLLDelete(self):
        self.cLL.del_node(3)
        self.assertEqual(self.cLL.size(), 4)
        self.cLL.del_node(5)
        self.assertEqual(self.cLL.size(), 3)
        self.cLL.del_node(3)
        self.assertEqual(self.cLL.size(), 3)

if __name__ == "__main__":
    unittest.main()
