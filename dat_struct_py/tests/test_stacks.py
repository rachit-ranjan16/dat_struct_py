import pytest
from ..stack import lStack

@pytest.fixture
def empty_stack():
    """Fixture providing an empty stack with default limit of 10"""
    return lStack(10)

@pytest.fixture
def filled_stack():
    """Fixture providing a stack filled with values 1-5"""
    stack = lStack(10)
    for i in range(5):
        stack.push(i + 1)
    return stack

def test_stack_creation_with_input():
    """Test stack creation with input list and limit"""
    inp_list = [x + 1 for x in range(5)]
    stack = lStack(limit=6, inp=inp_list)
    assert not stack.isFull()
    assert not stack.isEmpty()
    assert stack.peek() == 5

@pytest.mark.parametrize("values,limit,expected_full", [
    ([1, 2, 3], 5, False),
    ([1, 2, 3, 4, 5], 5, True),
    ([], 1, False),
    ([1], 1, True)
])
def test_stack_capacity(values, limit, expected_full):
    """Test stack capacity handling"""
    stack = lStack(limit)
    for val in values:
        stack.push(val)
    assert stack.isFull() == expected_full

def test_push_and_peek(empty_stack):
    """Test push operation and peek functionality"""
    assert empty_stack.isEmpty()
    
    for i in range(5):
        empty_stack.push(i + 1)
        assert empty_stack.peek() == i + 1
    
    assert not empty_stack.isFull()
    assert not empty_stack.isEmpty()

def test_stack_overflow(empty_stack):
    """Test stack overflow behavior"""
    # Fill stack to limit
    for i in range(10):
        empty_stack.push(i + 1)
    
    assert empty_stack.isFull()
    assert empty_stack.peek() == 10
    
    # Try pushing when full
    empty_stack.push(45)
    assert empty_stack.peek() == 10  # Should not change
    assert empty_stack.isFull()

def test_pop_and_underflow(empty_stack):
    """Test pop operation and underflow handling"""
    # Push some items
    for i in range(3):
        empty_stack.push(i + 1)
    
    # Pop all items
    assert empty_stack.pop() == 3
    assert empty_stack.pop() == 2
    assert empty_stack.pop() == 1
    
    # Test underflow
    assert empty_stack.pop() is None
    assert empty_stack.peek() is None
    assert empty_stack.isEmpty()

@pytest.mark.parametrize("expression,expected", [
    ('[]', True),
    ('[({{()}})]', True),
    ('[{)]]]]}]', False),
    ('[({{()}}]', False),
    ('{}]', False),
    ('abc', False),
    ('', False),
    ('{{[]}}()', True),
    ('([)]', False)
])
def test_balanced_symbols(expression, expected):
    """Test balanced symbol checking"""
    stack = lStack()
    assert stack.symbols_balanced(expression) == expected

def test_flush_operations():
    """Test flush operation in different stack states"""
    # Test flush on stack with input
    stack_with_input = lStack(inp="something")
    assert stack_with_input.flush() is None
    assert stack_with_input.isEmpty()
    
    # Test flush on empty stack
    empty = lStack()
    assert empty.flush() is None
    assert empty.isEmpty()
    
    # Test flush on stack with elements
    stack = lStack(5)
    stack.push(5)
    stack.push(6)
    assert not stack.isEmpty()
    assert stack.flush() is None
    assert stack.isEmpty()
    
    # Test operations after flush
    stack.push(4)
    assert not stack.isEmpty()
    assert stack.peek() == 4

@pytest.mark.parametrize("input_str,expected", [
    ('mississippi', 'm'),
    ('Rachitt', 'Rachi'),
    ('Rachittt', 'Rachit'),
    ('aaa', 'a'),
    ('abba', ''),
    ('', ''),
    ('abcdef', 'abcdef')
])
def test_filter_adjacent_recurring_elements(empty_stack, input_str, expected):
    """Test filtering of adjacent recurring elements"""
    assert empty_stack.filter_adj_rec_ele(input_str) == expected
