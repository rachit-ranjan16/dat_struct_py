import pytest
from ..heap import MinHeap, MaxHeap

# Test data fixtures
@pytest.fixture
def test_data():
    """Fixture providing sample data for heap testing"""
    return [4, 2, 8, 1, 6, 3]

@pytest.fixture
def empty_min_heap():
    """Fixture providing empty min heap"""
    return MinHeap()

@pytest.fixture
def empty_max_heap():
    """Fixture providing empty max heap"""
    return MaxHeap()

@pytest.fixture
def populated_min_heap(test_data):
    """Fixture providing min heap populated with test data"""
    return MinHeap(test_data)

@pytest.fixture
def populated_max_heap(test_data):
    """Fixture providing max heap populated with test data"""
    return MaxHeap(test_data)

class TestEmptyHeaps:
    """Tests for empty heap behavior"""
    
    @pytest.mark.parametrize("heap_fixture", ["empty_min_heap", "empty_max_heap"])
    def test_empty_heap_properties(self, request, heap_fixture):
        """Test properties of empty heaps"""
        heap = request.getfixturevalue(heap_fixture)
        assert heap.is_empty()
        assert heap.get_top() is None
        assert heap.size() == 0
        assert heap.extract_top() is None

class TestHeapCreation:
    """Tests for heap initialization"""
    
    def test_min_heap_creation(self, test_data):
        """Test min heap creation with input list"""
        heap = MinHeap(test_data)
        assert heap.size() == 6
        assert heap.get_top() == 1  # Should have minimum element at top

    def test_max_heap_creation(self, test_data):
        """Test max heap creation with input list"""
        heap = MaxHeap(test_data)
        assert heap.size() == 6
        assert heap.get_top() == 8  # Should have maximum element at top

class TestHeapOperations:
    """Tests for heap operations"""

    @pytest.mark.parametrize("values,expected_order", [
        ([4, 2, 8, 1, 6, 3], [1, 2, 3, 4, 6, 8]),  # Min heap extraction order
    ])
    def test_min_heap_operations(self, empty_min_heap, values, expected_order):
        """Test min heap insert and extract operations"""
        # Test insertions
        for x in values:
            empty_min_heap.insert(x)
        
        assert empty_min_heap.size() == len(values)
        assert empty_min_heap.get_top() == min(values)
        
        # Test extractions - should come out in ascending order
        extracted = []
        while not empty_min_heap.is_empty():
            extracted.append(empty_min_heap.extract_top())
        
        assert extracted == expected_order

    @pytest.mark.parametrize("values,expected_order", [
        ([4, 2, 8, 1, 6, 3], [8, 6, 4, 3, 2, 1]),  # Max heap extraction order
    ])
    def test_max_heap_operations(self, empty_max_heap, values, expected_order):
        """Test max heap insert and extract operations"""
        # Test insertions
        for x in values:
            empty_max_heap.insert(x)
        
        assert empty_max_heap.size() == len(values)
        assert empty_max_heap.get_top() == max(values)
        
        # Test extractions - should come out in descending order
        extracted = []
        while not empty_max_heap.is_empty():
            extracted.append(empty_max_heap.extract_top())
        
        assert extracted == expected_order

class TestHeapProperty:
    """Tests for heap property maintenance"""

    def test_min_heap_property(self, populated_min_heap):
        """Test that min heap property is maintained"""
        size = populated_min_heap.size()
        
        for parent_idx in range(size // 2):
            left = 2 * parent_idx + 1
            right = 2 * parent_idx + 2
            
            if left < size:
                assert populated_min_heap.heap[parent_idx] <= populated_min_heap.heap[left]
            if right < size:
                assert populated_min_heap.heap[parent_idx] <= populated_min_heap.heap[right]

    def test_max_heap_property(self, populated_max_heap):
        """Test that max heap property is maintained"""
        size = populated_max_heap.size()
        
        for parent_idx in range(size // 2):
            left = 2 * parent_idx + 1
            right = 2 * parent_idx + 2
            
            if left < size:
                assert populated_max_heap.heap[parent_idx] >= populated_max_heap.heap[left]
            if right < size:
                assert populated_max_heap.heap[parent_idx] >= populated_max_heap.heap[right]

    @pytest.mark.parametrize("heap_type,test_data,expected_top", [
        (MinHeap, [5, 3, 8, 1, 2], 1),
        (MaxHeap, [5, 3, 8, 1, 2], 8),
    ])
    def test_heapify_after_creation(self, heap_type, test_data, expected_top):
        """Test that heapify works correctly during heap creation"""
        heap = heap_type(test_data)
        assert heap.get_top() == expected_top