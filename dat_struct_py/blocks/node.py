class sNode(object):
    """
    Singly Linked List Node
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class dNode:
    """
    Doubly Linked List Node 
    """
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class bNode():
    """
    Binary Tree Node
    """
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 
    