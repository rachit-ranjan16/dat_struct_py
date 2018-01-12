from .blocks.node import SNode

class lStack(object):
    """Stack using a Singly Linked List
            Operations Covered
                1. Create a stack by pushing elements one by one or through an input sequence
                2. Check whether the stack is empty
                3. Check whether the stack is full
                4. Push an element
                5. Pop an element
                6. Peek the top element
                7. Check balanced paranthesis"""
    def __init__(self, limit=10, inp_list=[]):
        """Initialize Stack.
            Supports Optional
                1. Stack limit
                2. Pushes thorugh passed input sequence"""
        self.head = None
        self.limit = limit
        if len(inp_list) != 0:
            for i in inp_list:
                self.push(i)

    def __size(self):
        """Returns Size of the Linked List used for Stack Creation"""
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
        """Return True if stack is full, False otherwise"""
        if self.head is None:
            return False
        else:
            return self.__size() == self.limit

    def isEmpty(self):
        """Returns True if Stack is empty, False otherwise"""
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        """Push an element into the stack if not Full"""
        if self.isFull():
            print ('OverFlow')
        else:
            t = SNode()
            t.set_data(data)
            t.set_next(self.head)
            self.head = t

    def pop(self):
        """Pop the topmost element from the stack"""
        if self.isEmpty():
            print ('UnderFlow')
            return None
        else:
            popped_element = self.head.get_data()
            self.head = self.head.get_next()
            return popped_element

    def peek(self):
        """Return the top element of the stack"""
        if self.isEmpty():
            print ('UnderFlow')
            return None
        else:
            return self.head.get_data()

    def __sym_match(self, s1, s2):
        """Returns True if the input symbols are symmetric, False otherwise """
        if (s1 == '[' and s2 ==']') or (s2 == '[' and s1 =='['):
            return True
        elif (s1 == '{' and s2 == '}') or (s2 == '{' and s1 == '}'):
            return True
        elif (s1 == '(' and s2 ==')') or (s2 == '(' and s1 == ')'):
            return True
        else:
            return False

    def symbols_balanced(self, expr):
        """Returns True if the passed symbols(brackets) are sequentially balanced, False otherwise"""
        balanced = False
        for symbol in expr:
            if symbol in ('[', '{', '('):
                self.push(symbol)
            else:
                if self.isEmpty():
                    return False
                else:
                    st_top_sym = self.pop()
                if not self.__sym_match(st_top_sym, symbol):
                    return False
                else:
                    balanced = True
        return balanced
