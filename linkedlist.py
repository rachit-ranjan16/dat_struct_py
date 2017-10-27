from node import Node
class linkedList(object):
    """	Singly Linked List
			Without Dedicated Header Node
		Operations Covered
			1. Creating a LinkedList by inserting elements
				a. At the beginning
				b. At the end
				c. Any Position
			2. Length
			3. Print
			4. Deleting a node carrying some value """

    def __init__(self, head=None):
        self.head = head

    def insert_beginning(self, data):
        n = Node(data)
        n.set_next(self.head)
        self.head = n # head moves as each new node is added

    def insert_end(self, data):
        if self.head is None:
            head = Node(data)
            return
        cur = self.head
        while cur.get_next() is not None:
            cur = cur.get_next()
        cur.set_next(Node(data))


    def insert_pos(self, data, pos):
        n = Node(data)
        cur = self.head

        if pos > self.list_length() or pos < 0:
            return None
        elif pos == self.list_length():
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
        cur = self.head
        i = 1
        while cur is not None:
            print ("%d -> %r" % (i, cur.get_data()))
            cur = cur.get_next()
            i += 1

    def list_length(self):
        i = 0
        cur = self.head
        while cur.get_next() is not None:
            cur = cur.get_next()
            i += 1
        return i

    def del_node(self, data):
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
        if self.head is None:
            return True
        cur = self.head
        while cur is not None and cur.get_next() is not None:
            cur = cur.get_next().get_next()
            if cur is None:
                return True
        return False

if __name__ == "__main__":
    l = linkedList()
    for i in range(5):
        l.insert_beginning(i)
    l.print_elements()
    print(l.is_length_even())
