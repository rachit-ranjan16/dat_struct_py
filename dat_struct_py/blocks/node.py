class sNode(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class dNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        

class bNode():
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 
    