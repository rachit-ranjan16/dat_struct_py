from .blocks.node import SNode, DNode

class sLinkedList(object):
    """	Singly Linked List
			Without Dedicated Header Node
		Operations Covered
			1. Creating a LinkedList by inserting elements (one by one or through input list)
				a. At the beginning
				b. At the end
				c. Any Position
			2. Delete a node carrying some value
			3. Length
			4. Print
            5. Quick check whether the list has even length
            6. Return element nth element from the end
            7. Quick check whether a cycle exists
            8. Return cycle length(if one exsits)
            9. Reverse in Place
            10. Swap Pairs - Works only for Even length linkedlist"""
    def __init__(self, head=None, inp_list=[], insertEnd=True):
        """Initializes LinkedList.
        Supports inserts through passed optional input list from both beginning and end"""
        self.head = head
        if len(inp_list) != 0:
            if insertEnd:
                for ele in inp_list: self.insert_end(ele)
            else:
                for ele in inp_list: self.insert_beginning(ele)

    def insert_beginning(self, data):
        """Insert a Node into start of Linked List"""
        n = SNode(data)
        n.set_next(self.head)
        self.head = n # head moves as each new node is added

    def insert_end(self, data):
        """Insert a Node at the end of the Linked List"""
        if self.head is None:
            self.head = SNode(data)
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

    def size(self):
        """Return Number of elements in the Linked List"""
        cur = self.head
        c = 0
        while cur is not None:
            cur = cur.get_next()
            c += 1
        return c

    def print_elements(self):
        """Print Elements of the Linked List"""
        cur = self.head
        while cur is not None:
            print ("%r" % cur.get_data())
            cur = cur.get_next()

    def is_length_even(self):
        """Return True if the Linked List has even number of elements"""
        if self.head is None:
            return True
        cur = self.head
        while cur is not None and cur.get_next() is not None:
            cur = cur.get_next().get_next()
            if cur is None:
                return True
        return False

    def from_the_end(self,n):
        """Returns Node no n from the end of the LinkedList"""
        l = self.size();
        if n > l :
            print ('Nth position exceeds length of the list')
            return False
        cur = self.head
        fast = cur
        i = 0
        while i < n:
            fast = fast.get_next()
            i += 1
        while fast is not None:
            cur = cur.get_next()
            fast = fast.get_next()
        return cur.get_data()

    def is_cyclic(self):
        """Returns True if a Cycle is still present"""
        slow_ptr = self.head
        fast_ptr = self.head
        while (slow_ptr and fast_ptr):
            fast_ptr = fast_ptr.get_next()
            if fast_ptr == slow_ptr:
                return True
            if fast_ptr is None:
                return False
            fast_ptr = fast_ptr.get_next()
            if fast_ptr == slow_ptr:
                return True
            slow_ptr = slow_ptr.get_next()

    def cycle_length(self):
        """Returns length of cycle(if one exists) using the fast pointer technique"""
        if self.head is None or self.head.get_next() is None:
            return 0
        if not self.is_cyclic(): return 0
        slow = self.head
        fast = self.head.get_next()
        len1 = 1
        while slow != fast:
            len1 += 1
            slow = slow.get_next()
            if fast.get_next().get_next() is None:
                return 0
            fast = fast.get_next().get_next()
        return len1

    def rev_in_place(self):
        """Reverses linkedlist in place"""
        last = None
        cur = self.head
        while cur is not None:
            nxt = cur.get_next()
            cur.set_next(last)
            last = cur
            cur = nxt
        self.head = last

    def swap_pairs(self):
        """Swaps liked list nodes in pairs in place
            Works only for even length LinkedLists
            Returns True if swap pairs is successful and False Otherwise """
        if self.head is None:
            print ('Empty List')
            return False
        if not self.is_length_even():
            print ('Need an Even Length Linked List for this')
            return False
        cur = self.head
        while cur is not None and cur.get_next() is not None:
            t = cur.get_data()
            cur.set_data(cur.get_next().get_data())
            cur.get_next().set_data(t)
            cur = cur.get_next().get_next()
        return True


class dLinkedList:
    """	Doubly Linked List
			Without Dedicated Header Node
		Operations Covered
			1. Creating a LinkedList by inserting elements (one by one or through input list)
				a. At the beginning
				b. At the end
				c. Any Position
			2. Delete a node carrying some value
			3. Size
			4. Print
            5. Quick check whether the list has even length
            6. Return nth element from the end
            7. Quick check whether a cycle exists
            8. Return cycle length(if one exsits)
            9. Reverse in Place
            10. Swap Pairs - Works only for Even length linkedlist"""
    def __init__(self, head=None, inp_list=[], insertEnd=True):
        """Initializes  Doubly LinkedList
        Supports inserts through passed optional input list from both beginning and end"""
        self.head = head
        if len(inp_list) != 0:
            if insertEnd:
                for ele in inp_list: self.insert_end(ele)
            else:
                for ele in inp_list: self.insert_beginning(ele)

    def insert_beginning(self, data):
        """Insert a Node into start of Doubly Linked List"""
        n = DNode(data)
        n.set_next(self.head)
        if self.head is not None:
            self.head.set_prev(n)
        self.head = n

    def insert_end(self, data):
        """Insert a Node into end of Doubly Linked List"""
        if not self.head:
            self.head = DNode(data)
            return
        n = DNode(data)
        cur = self.head
        while cur.get_next() is not None:
            cur = cur.get_next()
        cur.set_next(n)
        n.set_prev(cur)

    def insert_pos(self, data, pos):
        """Insert a node at given position in the Doubly Linked List"""
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
        """Delete a node with given data"""
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

    def size(self):
        """Return the number of elements in Doubly LinkedList"""
        cur = self.head
        c = 0
        while cur is not None:
            cur = cur.get_next()
            c += 1
        return c

    def print_elements(self,forward=True):
        """Print Elements of the Doubly Linked List Backward and forward"""
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
        """Return True if the Doubly Linked List has even number of elements"""
        if self.head is None:
            return True
        cur = self.head
        while cur is not None and cur.get_next() is not None:
            cur = cur.get_next().get_next()
            if cur is None:
                return True
        return False

    def from_the_end(self,n):
        """Returns node number n from the end of the Doubly LinkedList"""
        l = self.size();
        if n > l :
            print ('Nth position exceeds length of the list')
            return False
        cur = self.head
        fast = cur
        i = 0
        while i < n:
            fast = fast.get_next()
            i += 1
        while fast is not None:
            cur = cur.get_next()
            fast = fast.get_next()
        return cur.get_data()

    def is_cyclic(self):
        """Returns True if a Cycle is still present"""
        slow_ptr = self.head
        fast_ptr = self.head
        while (slow_ptr and fast_ptr):
            fast_ptr = fast_ptr.get_next()
            if fast_ptr == slow_ptr:
                return True
            if fast_ptr is None:
                return False
            fast_ptr = fast_ptr.get_next()
            if fast_ptr == slow_ptr:
                return True
            slow_ptr = slow_ptr.get_next()

    def cycle_length(self):
        """Returns length of cycle(if one exists) using the fast pointer technique"""
        if self.head is None or self.head.get_next() is None:
            return 0
        if not self.is_cyclic(): return 0
        slow = self.head
        fast = self.head.get_next()
        len1 = 1
        while slow != fast:
            len1 += 1
            slow = slow.get_next()
            if fast.get_next().get_next() is None:
                return 0
            fast = fast.get_next().get_next()
        return len1

    def rev_in_place(self):
        """Reverses linkedlist in place"""
        last = None
        cur = self.head
        while cur is not None:
            nxt = cur.get_next()
            cur.set_next(last)
            last = cur
            cur = nxt
        self.head = last

    def swap_pairs(self):
        """Swaps liked list nodes in pairs in place
            Works only for even length LinkedLists
            Returns True if swap pairs is successful and False Otherwise """
        if self.head is None:
            print ('Empty List')
            return False
        if not self.is_length_even():
            print ('Need an Even Length Linked List for this')
            return False
        cur = self.head
        while cur is not None and cur.get_next() is not None:
            t = cur.get_data()
            cur.set_data(cur.get_next().get_data())
            cur.get_next().set_data(t)
            cur = cur.get_next().get_next()
        return True


class cLinkedList(object):
    """	Circular Singly Linked List
			Without Dedicated Header Node
		Operations Covered
			1. Creating a LinkedList by inserting elements (one by one or through input list)
				a. At the beginning
				b. At the end
				c. Any Position
			2. Delete a node carrying some value
			3. Size
			4. Print
            5. Quick check whether the list has even length
            6. Return nth element from the end
            7. Quick check whether a cycle exists
            8. Return cycle length(if one exists)"""
    def __init__(self, head=None, inp_list=[], insertEnd=True):
        """Initializes Singly Circularly LinkedList
        Supports inserts through passed optional input list from both beginning and end"""
        self.head = head
        if len(inp_list) != 0:
            if insertEnd:
                for ele in inp_list: self.insert_end(ele)
            else:
                for ele in inp_list: self.insert_beginning(ele)

    def insert_beginning(self, data):
        """Insert a Node into start of Circular Linked List"""
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
        """Insert a Node into end of Circular LinkedList"""
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
        """Insert a node at given position in the Circular LinkedList """
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

    def del_node(self, data):
        """Delete a node with given data"""
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

    def size(self):
        """Return the Number of elements in the Circular LinkedList"""
        i = 1
        if self.head is None:
            return 0
        cur = self.head
        while cur.get_next() is not self.head:
            i += 1
            cur = cur.get_next()
        return i

    def print_elements(self):
        """Print Elements of the Doubly Linked List"""
        cur = self.head.get_next()
        print ('%d' % self.head.get_data())
        while cur is not self.head:
            print ("%d" % cur.get_data())
            cur = cur.get_next()

    def is_length_even(self):
        """Return True if the Doubly Linked List has even number of elements"""
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

    def from_the_end(self,n):
        """Returns Node no n from the end of the LinkedList"""
        l = self.size();
        if n > l :
            print ('Nth position exceeds length of the list')
            return False
        cur = self.head
        fast = cur
        i = 0
        while i < n:
            fast = fast.get_next()
            i += 1
        while fast != self.head:
            cur = cur.get_next()
            fast = fast.get_next()
        return cur.get_data()

    def is_cyclic(self):
        """Returns True if a Cycle is still present"""
        slow_ptr = self.head
        fast_ptr = self.head
        while (slow_ptr and fast_ptr):
            fast_ptr = fast_ptr.get_next()
            if fast_ptr == slow_ptr:
                return True
            if fast_ptr is None:
                return False
            fast_ptr = fast_ptr.get_next()
            if fast_ptr == slow_ptr:
                return True
            slow_ptr = slow_ptr.get_next()

    def cycle_length(self):
        """Returns length of cycle(if one exists) using the fast pointer technique"""
        if self.head is None or self.head.get_next() is None:
            return 0
        if not self.is_cyclic(): return 0
        slow = self.head
        fast = self.head.get_next()
        len1 = 1
        while slow != fast:
            len1 += 1
            slow = slow.get_next()
            if fast.get_next().get_next() is None:
                return 0
            fast = fast.get_next().get_next()
        return len1
