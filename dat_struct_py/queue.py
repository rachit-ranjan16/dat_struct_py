from .blocks.node import sNode

class lQueue(object):
    """Circular Queue using a Linked List
            Operations Covered
                1. Create a queue by enquing elements one by one or through an input sequence
                2. Check whether the queue is Empty
                3. Enqueue an element
                4. Dequeue an element
                5. Length
                6. Print
                7. Flush"""

    def __init__(self, inp=[]):
        """Initialize Queue
        Supports enqueue through passed input sequence"""
        self.front = None
        self.rear = None
        if len(inp) != 0:
            for i in inp:
                self.enQ(i)

    def isEmpty(self):
        """Returns True if Queue is empty, False otherwise"""
        if self.front is None:
            return True
        else:
            return False

    def enQ(self,data):
        """Enqueue an element to the rear of the Q"""
        if self.isEmpty():
            self.front = sNode(data)
            self.rear = self.front
            return
        self.rear.next = sNode(data)
        self.rear = self.rear.next

    def deQ(self):
        """Dequeue an element from the front of the Q"""
        if self.isEmpty():
            print("Underflow")
            return
        popped_element = self.front.data
        self.front = self.front.next
        return popped_element

    def size(self):
        """Returns size of the Q"""
        if not self.front and not self.rear:
            return 0
        elif self.front == self.rear:
            return 1
        cur = self.front
        l = 0
        while cur != self.rear.next:
            l += 1
            cur = cur.next
        return l

    def print_elements(self):
        """Print Elements of the Q"""
        if self.isEmpty():
            print("Underflow")
            return None
        cur = self.front
        while cur != self.rear.next:
            print ("%r" % cur.data)
            cur = cur.get_next

    def flush(self):
        """Flushes the Q"""
        while self.isEmpty() is False:
            self.deQ()
        self.front = None
        self.rear = None
