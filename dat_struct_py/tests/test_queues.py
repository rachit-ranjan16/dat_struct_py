import pytest
from ..queue import lQueue

@pytest.fixture
def empty_queue():
    """Fixture providing an empty queue"""
    return lQueue()

@pytest.fixture
def populated_queue():
    """Fixture providing a queue populated with values 1-5"""
    return lQueue(inp=[x + 1 for x in range(5)])

def test_queue_creation_with_input_list(populated_queue):
    """Test queue initialization with input list"""
    assert populated_queue.front.data == 1
    assert populated_queue.rear.data == 5
    assert populated_queue.size() == 5

def test_empty_queue_operations(empty_queue):
    """Test operations on empty queue"""
    assert empty_queue.isEmpty()
    assert empty_queue.deQ() is None
    assert empty_queue.print_elements() is None
    assert empty_queue.size() == 0

@pytest.mark.parametrize("values,expected_size", [
    ([1, 2, 3], 3),
    ([], 0),
    ([1], 1),
    ([1, 2, 3, 4, 5], 5)
])
def test_enqueue_size(empty_queue, values, expected_size):
    """Test enqueue operation and size tracking"""
    for val in values:
        empty_queue.enQ(val)
    assert empty_queue.size() == expected_size
    if values:
        assert empty_queue.front.data == values[0]
        assert empty_queue.rear.data == values[-1]

def test_enqueue_dequeue_sequence(empty_queue):
    """Test sequence of enqueue and dequeue operations"""
    # Test enqueue operations
    for i in range(5):
        empty_queue.enQ(i + 1)
    assert empty_queue.front.data == 1
    assert empty_queue.rear.data == 5
    
    # Test dequeue operations
    for i in range(5):
        assert empty_queue.deQ() == i + 1
    
    # Test enqueueing after emptying
    empty_queue.enQ(3)
    assert empty_queue.size() == 1
    assert empty_queue.deQ() == 3
    assert empty_queue.isEmpty()

def test_flush(populated_queue):
    """Test flushing the queue"""
    assert populated_queue.size() == 5
    populated_queue.flush()
    assert populated_queue.size() == 0
    assert populated_queue.front is None
    assert populated_queue.rear is None
    assert populated_queue.isEmpty()

def test_sequence_after_flush(populated_queue):
    """Test queue operations after flushing"""
    populated_queue.flush()
    # Try operations after flush
    populated_queue.enQ(1)
    assert populated_queue.size() == 1
    assert populated_queue.front.data == 1
    assert populated_queue.rear.data == 1
    assert populated_queue.deQ() == 1
    assert populated_queue.isEmpty()
