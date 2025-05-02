class Heap:
    """Base Heap class that can work as either MinHeap or MaxHeap
    Operations Covered
        1. Create a heap by
            a. Adding elements one by one
            b. Passing an input list (heapifies the list)
        2. Insert an element
        3. Get top element (min for MinHeap, max for MaxHeap)
        4. Extract top element
        5. Size
        6. isEmpty
        7. Heapify a list
    """
    def __init__(self, inp_list=[], is_min_heap=True):
        """Initialize heap with optional input list
        Args:
            inp_list: Optional list to heapify
            is_min_heap: If True creates MinHeap, else MaxHeap
        """
        self.heap = []
        self.is_min_heap = is_min_heap
        if inp_list:
            self.heap = inp_list[:]
            self._heapify()
    
    def _should_swap(self, parent_val, child_val):
        """Determines if parent and child should be swapped based on heap type"""
        if self.is_min_heap:
            return parent_val > child_val
        return parent_val < child_val

    def _heapify(self):
        """Convert the input list into a heap"""
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, index):
        """Move a node up the heap until heap property is satisfied"""
        parent = (index - 1) // 2
        while index > 0 and self._should_swap(self.heap[parent], self.heap[index]):
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        """Move a node down the heap until heap property is satisfied"""
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self._should_swap(self.heap[smallest], self.heap[left]):
                smallest = left
            if right < size and self._should_swap(self.heap[smallest], self.heap[right]):
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def insert(self, value):
        """Insert a new value into the heap"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def get_top(self):
        """Return the top element without removing it"""
        if not self.heap:
            return None
        return self.heap[0]

    def extract_top(self):
        """Remove and return the top element"""
        if not self.heap:
            return None
            
        if len(self.heap) == 1:
            return self.heap.pop()

        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return top

    def size(self):
        """Return number of elements in the heap"""
        return len(self.heap)

    def is_empty(self):
        """Return True if heap is empty, False otherwise"""
        return len(self.heap) == 0


class MinHeap(Heap):
    """MinHeap implementation where the root is the minimum element"""
    def __init__(self, inp_list=[]):
        super().__init__(inp_list, is_min_heap=True)


class MaxHeap(Heap):
    """MaxHeap implementation where the root is the maximum element"""
    def __init__(self, inp_list=[]):
        super().__init__(inp_list, is_min_heap=False)