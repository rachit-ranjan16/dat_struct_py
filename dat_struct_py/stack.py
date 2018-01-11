from .blocks.node import SNode

class lStack(object):

    def __init__(self, limit=10):
        self.head = None
        self.limit = limit

    def size(self):
        if self.head is None:
            return 0
        else:
            cur = self.head
            l = 0
            while cur is not None:
                l += 1
                cur = cur.get_next()
            return l

    def isFull(self):
        if self.head is None:
            return False
        else:
            return self.size() == self.limit

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print ('OverFlow')
        else:
            t = SNode()
            t.set_data(data)
            t.set_next(self.head)
            self.head = t

    def pop(self):
        if self.isEmpty():
            print ('UnderFlow')
            return None
        else:
            popped_element = self.head.get_data()
            self.head = self.head.get_next()
            return popped_element

    def peek(self):
        if self.isEmpty():
            print ('UnderFlow')
            return None
        else:
            return self.head.get_data()
