import unittest
from ..stack import lStack

class testStacks(unittest.TestCase):

    def setUp(self):
        self.stack = lStack(10)

    def testStackCreationWithInputListAndLimit(self):
        inp_list = [x+1 for x in range(5)]
        another_stack = lStack(limit=6,inp=inp_list)
        self.assertEqual(another_stack.isFull(), False)
        self.assertEqual(another_stack.isEmpty(), False)
        self.assertEqual(another_stack.peek(), 5)

    def testPushAndPeek(self):
        self.assertEqual(self.stack.isEmpty(), True)
        for i in range(5):
            self.stack.push(i+1)
        self.assertEqual(self.stack.peek(), 5)
        self.assertEqual(self.stack.isFull(), False)
        self.assertEqual(self.stack.isEmpty(), False)

    def testPushOnStackAndOverFlow(self):
        for i in range(10):
            self.stack.push(i+1)
        self.assertEqual(self.stack.isFull(), True)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(45)
        self.assertEqual(self.stack.isFull(), True)
        self.assertEqual(self.stack.peek(), 10)

    def testPopStackAndUnderFlow(self):
        for i in range(3):
            self.stack.push(i+1)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertIsNone(self.stack.pop())
        self.assertIsNone(self.stack.peek())

    def testBalancedWithStack(self):
        sym_stack = lStack()
        self.assertEqual(sym_stack.symbols_balanced('[]'), True)
        sym_stack.flush()
        self.assertEqual(sym_stack.symbols_balanced('[({{()}})]'), True)
        sym_stack.flush()
        self.assertEqual(sym_stack.symbols_balanced('[{)]]]]}]'), False)
        sym_stack.flush()
        self.assertEqual(sym_stack.symbols_balanced('[({{()}}]'), False)
        sym_stack.flush()
        self.assertEqual(sym_stack.symbols_balanced('{}]'), False)
        sym_stack.flush()
        self.assertEqual(sym_stack.symbols_balanced('abc'), False)

    def testFlush(self):
        self.assertIsNone(lStack(inp="something").flush())
        self.assertIsNone(lStack().flush())
        self.stack.push(5)
        self.stack.push(5)
        self.assertEqual(self.stack.isEmpty(), False)
        self.assertIsNone(self.stack.flush())
        self.assertEqual(self.stack.isEmpty(), True)
        self.stack.push(4)
        self.assertEqual(self.stack.isEmpty(), False)

    def testFilterAdjRecurringElements(self):
        self.assertEqual(self.stack.filter_adj_rec_ele('mississippi'), 'm')
        self.assertEqual(self.stack.filter_adj_rec_ele('Rachitt'), 'Rachi')
        self.assertEqual(self.stack.filter_adj_rec_ele('Rachittt'), 'Rachit')
