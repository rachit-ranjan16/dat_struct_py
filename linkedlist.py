from blocks.node import SNode, DNode

class sLinkedList(object):
    """	Singly Linked List
			Without Dedicated Header Node
		Operations Covered
			1. Creating a LinkedList by inserting elements
				a. At the beginning
				b. At the end
				c. Any Position
			2. Length
			3. Print
			4. Delete a node carrying some value
            5. Quick check whether the list has even length"""

    def __init__(self, head=None):
        self.head = head

    def insert_beginning(self, data):
        """Insert a Node into start of Linked List"""
        n = SNode(data)
        n.set_next(self.head)
        self.head = n # head moves as each new node is added

    def insert_end(self, data):
        """Insert a Node at the end of the Linked List"""
        if self.head is None:
            head = SNode(data)
            return
        cur = self.head
        while cur.get_next() is not None:
            cur = cur.get_next()
        cur.set_next(SNode(data))

    def insert_pos(self, data, pos):
        """Insert a node at given position in the Linked List """
        n = SNode(data)
        cur = self.head

        if pos > self.size() or pos < 0:
            return None
        elif pos == self.size():
            self.insert_end(data)
        elif pos == 0:
            self.insert_beginning(data)
        else:
            i = 0
            while i < pos - 1:
                print (i)
                cur = cur.get_next()
                i += 1

            n.set_next(cur.get_next())
            cur.set_next(n)

    def print_elements(self):
        """Print Elements of the Linked List"""
        cur = self.head
        i = 1
        while cur is not None:
            print ("%r" % cur.get_data())
            cur = cur.get_next()
            i += 1

    def size(self):
        """Return Length of the Linked List"""
        i = 0
        cur = self.head
        while cur.get_next() is not None:
            cur = cur.get_next()
            i += 1
        return i

    def del_node(self, data):
        """Delete a node with given data"""
        if self.head.get_data() == data:
            t = self.head
            self.head = self.head.get_next()
            # Python Garbage collection works on a Reference Map.
            # As soon as all references to a member die,it is automatically garbage collected
        cur = self.head.get_next()
        t = self.head
        while cur is not None:
            if cur.get_data() == data:
                t.set_next(cur.get_next())
            t = cur
            cur = cur.get_next()

    def is_length_even(self):
        """Return True if the Linked List has even length"""
        if self.head is None:
            return True
        cur = self.head
        while cur is not None and cur.get_next() is not None:
            cur = cur.get_next().get_next()
            if cur is None:
                return True
        return False


class dLinkedList:
    """	Doubly Linked List
			Without Dedicated Header Node
		Operations Covered
			1. Creating a LinkedList by inserting elements
				a. At the beginning
				b. At the end
				c. Any Position
			2. Length
			3. Print
			4. Delete a node carrying some value
            5. Quick check whether the list has even length"""
    def __init__(self, head=None):
        self.head = head

    def size(self):
        cur = self.head
        c = 0
        while cur is not None:
            cur = cur.get_next()
            c += 1
        return c

    def insert_beginning(self, data):
        n = DNode(data)
        n.set_next(self.head)
        if self.head is not None:
            self.head.set_prev(n)
        self.head = n

    def insert_end(self, data):
        n = DNode(data)
        cur = self.head
        while cur.get_next() is not None:
            cur = cur.get_next()
        cur.set_next(n)
        n.set_prev(cur)

    def insert_pos(self, data, pos):
        if pos > self.sizeDL() or pos < 0:
            return 0
        elif pos == 0:
            self.insert_beg(data)
        elif pos == self.sizeDL():
            self.insert_end(data)
        else:
            n = DNode(data)
            cur = self.head
            c = 0
            while c < pos - 1:
                cur = cur.get_next()
                c += 1
            n.set_next(cur.get_next)
            n.set_prev(cur)
            cur.get_next().set_prev(n)
            cur.set_next(n)

    def del_node(self, value):
        if self.head.get_data() == value:
            self.head.get_next().set_prev(None)
            self.head = self.head.get_next()
        cur = self.head.get_next()
        t = self.head
        while cur is not None:
            if cur.get_data() == value:
                t.set_next(cur.get_next())
                if cur.get_next() is not None:
                    cur.get_next().set_prev(t)
            t = cur
            cur = cur.get_next()

    def print_elements(self,forward=True):
        cur = self.head
        if forward:
            while cur is not None:
                tail = cur
                print ('%r' % cur.get_data())
                cur = cur.get_next()
        else:
            while tail is not None:
                print('%r' % tail.get_data())
                tail = tail.get_prev()

    def is_length_even(self):
        """Return True if the Linked List has even length"""
        if self.head is None:
            return True
        cur = self.head
        while cur is not None and cur.get_next() is not None:
            cur = cur.get_next().get_next()
            if cur is None:
                return True
        return False


class cLinkedList(object):
    """	Circular Singly Linked List
			Without Dedicated Header Node
		Operations Covered
			1. Creating a LinkedList by inserting elements
				a. At the beginning
				b. At the end
				c. Any Position
			2. Length
			3. Print
			4. Delete a node carrying some value
            5. Quick check whether the list has even length"""
    def __init__(self, head=None):
        self.head = head

    def insert_beginning(self, data):
        n = SNode(data)
        n.set_next(n)
        if self.head is not None:
            cur = self.head
            while cur.get_next() != self.head:
                cur = cur.get_next()
            n.set_next(self.head)
            cur.set_next(n)
        self.head = n # head moves as each new node is added


    def insert_end(self, data):
        n = SNode(data)
        n.set_next(n)
        if self.head is not None:
            cur = self.head
            while cur.get_next() != self.head:
                cur = cur.get_next()
            cur.set_next(n)
            n.set_next(self.head)
        else:
            self.head = n

    def insert_pos(self, data, pos):
        """Insert a node at given position in the Linked List """
        n = SNode(data)
        cur = self.head
        if pos > self.size() or pos < 0:
            return None
        elif pos == self.size():
            self.insert_end(data)
        elif pos == 0:
            self.insert_beginning(data)
        else:
            i = 0
            while i < pos - 1:
                print (i)
                cur = cur.get_next()
                i += 1

            n.set_next(cur.get_next())
            cur.set_next(n)

    def print_elements(self):
        cur = self.head.get_next()
        i = 1
        print ('%d' % self.head.get_data())
        while cur is not self.head:
            i += 1
            print ("%d" % cur.get_data())
            cur = cur.get_next()

    def size(self):
        i = 1
        if self.head is None:
            return 0
        cur = self.head
        while cur.get_next() is not self.head:
            i += 1
            cur = cur.get_next()
        return i

    def del_node(self, data):
        if self.head.get_data() == data:
            cur = self.head.get_next()
            while cur.get_next() is not self.head:
                cur = cur.get_next()
            cur.set_next(self.head.get_next())
            self.head = self.head.get_next()
        else:
            cur = self.head.get_next()
            t = self.head
            while cur.get_next() is not self.head:
                if cur.get_data() == data:
                    t.set_next(cur.get_next())
                    cur.set_next(None)
                    cur = t.get_next()
                else:
                    t = cur
                    cur = cur.get_next()

    def is_length_even(self):
        if self.head is None:
            return True
        cur = self.head
        i = -1
        while cur.get_next() != self.head:
            cur = cur.get_next()
            i += 1
        if i%2 == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    print("Singly Linked List")
    l = sLinkedList()
    for i in range(5):
        l.insert_beginning(i)
    l.print_elements()
    print(l.is_length_even())
    print("Doubly Linked List")
    l = dLinkedList()
    for i in range(5):
        l.insert_beginning(i)
    l.print_elements()
    print(l.is_length_even())
    print("Circular Singly Linked List")
    l = cLinkedList()
    for i in range(4):
        l.insert_beginning(i)
    l.print_elements()
    print(l.is_length_even())
