import unittest
from ..queue import lQueue

class testQ(unittest.TestCase):

    def setUp(self):
        self.Q = lQueue()

    def testQueueCreationWithInputList(self):
        someQ = lQueue(inp=[x+1 for x in range(5)])
        self.assertEqual(someQ.front.data, 1)
        self.assertEqual(someQ.rear.data, 5)
        self.assertEqual(someQ.size(), 5)

    def testEnQAndDeQ(self):
        for i in range(5):
            self.Q.enQ(i+1)
        self.assertEqual(self.Q.front.data, 1)
        self.assertEqual(self.Q.rear.data, 5)
        self.assertEqual(self.Q.deQ(), 1)
        self.assertEqual(self.Q.deQ(), 2)
        self.assertEqual(self.Q.deQ(), 3)
        self.assertEqual(self.Q.deQ(), 4)
        self.assertEqual(self.Q.deQ(), 5)
        self.Q.enQ(3)
        self.assertEqual(self.Q.size(), 1)
        self.assertEqual(self.Q.deQ(), 3)
        self.assertEqual(self.Q.isEmpty(), True)
        self.assertIsNone(self.Q.deQ())
        self.assertIsNone(self.Q.print_elements())

    def testFlush(self):
        self.Q = lQueue(inp=[x+1 for x in range(5)])
        self.assertEqual(self.Q.size(), 5)
        self.Q.flush()
        self.assertEqual(self.Q.size(),0)
        self.assertIsNone(self.Q.front)
        self.assertIsNone(self.Q.rear)
