from .blocks.node import sNode

class lStack(object):
    """Stack using a Singly Linked List
            Operations Covered
                1. Create a stack by pushing elements one by one or through an input sequence
                2. Check whether the stack is empty
                3. Check whether the stack is full
                4. Push an element
                5. Pop an element
                6. Peek the top element
                7. Check balanced paranthesis
                8. Flush
                9. Remove adjacent recurring elements from input"""
    def __init__(self, limit=25, inp=[]):
        """Initialize Stack.
            Supports Optional
                1. Stack limit
                2. Pushes thorugh passed input sequence"""
        self.head = None
        self.limit = limit
        if len(inp) != 0:
            for i in inp:
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
                cur = cur.next
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
            t = sNode(data)
            t.next= self.head
            self.head = t

    def pop(self):
        """Pop the topmost element from the stack"""
        if self.isEmpty():
            print ('UnderFlow')
            return None
        else:
            popped_element = self.head.data
            self.head = self.head.next
            return popped_element

    def peek(self):
        """Return the top element of the stack"""
        if self.isEmpty():
            print ('UnderFlow')
            return None
        else:
            return self.head.data

    def __sym_match(self, s1, s2):
        """Returns True if the input symbols are symmetric, False otherwise """
        if s1 == '[' and s2 == ']':
            return True
        elif s1 == '{' and s2 == '}':
            return True
        elif s1 == '(' and s2 == ')':
            return True
        return False

    def symbols_balanced(self, expr):
        """Returns True if the passed symbols(brackets) are sequentially balanced, False otherwise"""
        if not expr:  # Handle empty string case
            return False
            
        for symbol in expr:
            if symbol in ('[', '{', '('):
                self.push(symbol)
            else:
                if symbol not in (']', '}', ')'):
                    return False  # Non-bracket character
                if self.isEmpty():
                    return False
                st_top_sym = self.pop()
                if not self.__sym_match(st_top_sym, symbol):
                    self.flush()
                    return False
        
        # Check if any unclosed brackets remain
        result = self.isEmpty()
        self.flush()
        return result

    def flush(self):
        """Empties the stack"""
        while self.isEmpty() is False:
            self.pop()

    def filter_adj_rec_ele(self, inp):
        """Filters out all the adjacent duplicate elements from the input"""
        if not inp:
            return ""
            
        # Empty the stack first (in case it was used before)
        self.flush()
        result = []
        # Process the input string
        for char in inp:
            # If stack is not empty and top element equals current char
            if not self.isEmpty() and self.peek() == char:
                # Pop the matching element (remove the pair)
                self.pop()
            else:
                # Push the current character to the stack
                self.push(char)
        
        # Build the result string by popping all elements from the stack
        # The elements will be in reverse order
        while not self.isEmpty():
            result.append(self.pop())
        
        # Reverse the result to get the correct order
        return ''.join(reversed(result))
