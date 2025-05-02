import pytest
from ..linkedlist import sLinkedList, dLinkedList, cLinkedList

# Common test data
TEST_LIST = [1, 2, 3, 4, 5]

# Fixtures for each linked list type
@pytest.fixture
def empty_singly():
    """Fixture for empty singly linked list"""
    return sLinkedList()

@pytest.fixture
def empty_doubly():
    """Fixture for empty doubly linked list"""
    return dLinkedList()

@pytest.fixture
def empty_circular():
    """Fixture for empty circular linked list"""
    return cLinkedList()

@pytest.fixture
def populated_singly():
    """Fixture for populated singly linked list with values 5->4->3->2->1"""
    ll = sLinkedList()
    for i in range(5):
        ll.insert_beginning(i + 1)
    return ll

@pytest.fixture
def populated_doubly():
    """Fixture for populated doubly linked list with values 5->4->3->2->1"""
    ll = dLinkedList()
    for i in range(5):
        ll.insert_beginning(i + 1)
    return ll

@pytest.fixture
def populated_circular():
    """Fixture for populated circular linked list with values 5->4->3->2->1"""
    ll = cLinkedList()
    for i in range(5):
        ll.insert_beginning(i + 1)
    return ll

# Test classes for each linked list type
class TestSinglyLinkedList:
    @pytest.mark.parametrize("insert_at_end", [True, False])
    def test_initialization_from_list(self, insert_at_end):
        """Test initializing singly linked list from input list"""
        ll = sLinkedList(inp_list=TEST_LIST, insertEnd=insert_at_end)
        assert ll.size() == 5
        if insert_at_end:
            assert ll.head.data == 1
            assert self._get_last_node(ll).data == 5
        else:
            assert ll.head.data == 5
            assert self._get_last_node(ll).data == 1

    def test_insert_beginning(self, populated_singly):
        """Test insertion at beginning"""
        assert populated_singly.size() == 5
        assert populated_singly.head.data == 5

    def test_insert_end(self, empty_singly):
        """Test insertion at end"""
        for i in range(5):
            empty_singly.insert_end(i + 1)
        assert empty_singly.size() == 5
        assert empty_singly.head.data == 1
        assert self._get_last_node(empty_singly).data == 5

    @pytest.mark.parametrize("list_state,expected", [
        ([], True),
        ([1], False),
        ([1, 2], True),
        ([1, 2, 3], False)
    ])
    def test_even_length(self, empty_singly, list_state, expected):
        """Test even length detection"""
        for item in list_state:
            empty_singly.insert_end(item)
        assert empty_singly.is_length_even() == expected

    def test_cyclicity(self, populated_singly):
        """Test cycle detection and length"""
        assert not populated_singly.is_cyclic()
        assert populated_singly.cycle_length() == 0

    @pytest.mark.parametrize("n,expected", [
        (2, 2),
        (1, 1),
        (5, 5),
        (10, False)
    ])
    def test_nth_from_end(self, populated_singly, n, expected):
        """Test finding nth element from end"""
        assert populated_singly.from_the_end(n) == expected

    def test_delete(self, populated_singly):
        """Test node deletion"""
        populated_singly.del_node(3)
        assert populated_singly.size() == 4
        populated_singly.del_node(5)
        assert populated_singly.size() == 3
        # Try deleting non-existent value
        populated_singly.del_node(3)
        assert populated_singly.size() == 3

    def test_reverse_in_place(self, populated_singly):
        """Test in-place reversal"""
        populated_singly.rev_in_place()
        assert populated_singly.head.data == 1
        assert populated_singly.size() == 5
        assert self._get_last_node(populated_singly).data == 5

    def test_swap_pairs(self, populated_singly):
        """Test swapping adjacent pairs"""
        populated_singly.insert_beginning(6)  # Make even length
        assert populated_singly.swap_pairs()
        assert populated_singly.head.data == 5
        assert populated_singly.head.next.data == 6
        # Check last pair
        current = populated_singly.head
        while current.next.next:
            current = current.next
        assert current.data == 1
        assert current.next.data == 2

    @staticmethod
    def _get_last_node(ll):
        """Helper to get last node of a linked list"""
        current = ll.head
        while current.next:
            current = current.next
        return current

class TestDoublyLinkedList:
    @pytest.mark.parametrize("insert_at_end", [True, False])
    def test_initialization_from_list(self, insert_at_end):
        """Test initializing doubly linked list from input list"""
        ll = dLinkedList(inp_list=TEST_LIST, insertEnd=insert_at_end)
        assert ll.size() == 5
        if insert_at_end:
            assert ll.head.data == 1
            assert self._get_last_node(ll).data == 5
        else:
            assert ll.head.data == 5
            assert self._get_last_node(ll).data == 1

    def test_insert_beginning(self, populated_doubly):
        """Test insertion at beginning"""
        assert populated_doubly.size() == 5
        assert populated_doubly.head.data == 5

    def test_insert_end(self, empty_doubly):
        """Test insertion at end"""
        for i in range(5):
            empty_doubly.insert_end(i + 1)
        assert empty_doubly.size() == 5
        assert empty_doubly.head.data == 1
        assert self._get_last_node(empty_doubly).data == 5

    @pytest.mark.parametrize("list_state,expected", [
        ([], True),
        ([1], False),
        ([1, 2], True),
        ([1, 2, 3], False)
    ])
    def test_even_length(self, empty_doubly, list_state, expected):
        """Test even length detection"""
        for item in list_state:
            empty_doubly.insert_end(item)
        assert empty_doubly.is_length_even() == expected

    def test_cyclicity(self, populated_doubly):
        """Test cycle detection and length"""
        assert not populated_doubly.is_cyclic()
        assert populated_doubly.cycle_length() == 0

    @pytest.mark.parametrize("n,expected", [
        (2, 2),
        (1, 1),
        (5, 5),
        (12, False)
    ])
    def test_nth_from_end(self, populated_doubly, n, expected):
        """Test finding nth element from end"""
        assert populated_doubly.from_the_end(n) == expected

    def test_delete(self, populated_doubly):
        """Test node deletion"""
        populated_doubly.del_node(3)
        assert populated_doubly.size() == 4
        populated_doubly.del_node(5)
        assert populated_doubly.size() == 3
        populated_doubly.del_node(3)  # Try deleting non-existent value
        assert populated_doubly.size() == 3

    def test_reverse_in_place(self, populated_doubly):
        """Test in-place reversal"""
        populated_doubly.rev_in_place()
        assert populated_doubly.head.data == 1
        assert populated_doubly.size() == 5
        assert self._get_last_node(populated_doubly).data == 5

    def test_swap_pairs(self, populated_doubly):
        """Test swapping adjacent pairs"""
        populated_doubly.insert_beginning(6)  # Make even length
        assert populated_doubly.swap_pairs()
        assert populated_doubly.head.data == 5
        assert populated_doubly.head.next.data == 6
        # Check last pair
        current = populated_doubly.head
        while current.next.next:
            current = current.next
        assert current.data == 1
        assert current.next.data == 2

    @staticmethod
    def _get_last_node(ll):
        """Helper to get last node of a linked list"""
        current = ll.head
        while current.next:
            current = current.next
        return current

class TestCircularLinkedList:
    @pytest.mark.parametrize("insert_at_end", [True, False])
    def test_initialization_from_list(self, insert_at_end):
        """Test initializing circular linked list from input list"""
        ll = cLinkedList(inp_list=TEST_LIST, insertEnd=insert_at_end)
        assert ll.size() == 5
        if insert_at_end:
            assert ll.head.data == 1
            assert self._get_last_node(ll).data == 5
        else:
            assert ll.head.data == 5
            assert self._get_last_node(ll).data == 1

    def test_insert_beginning(self, populated_circular):
        """Test insertion at beginning"""
        assert populated_circular.size() == 5
        assert populated_circular.head.data == 5

    def test_insert_end(self, empty_circular):
        """Test insertion at end"""
        for i in range(5):
            empty_circular.insert_end(i + 1)
        assert empty_circular.size() == 5
        assert empty_circular.head.data == 1
        assert self._get_last_node(empty_circular).data == 5

    @pytest.mark.parametrize("list_state,expected", [
        ([], True),
        ([1], False),
        ([1, 2], True),
        ([1, 2, 3], False)
    ])
    def test_even_length(self, empty_circular, list_state, expected):
        """Test even length detection"""
        for item in list_state:
            empty_circular.insert_end(item)
        assert empty_circular.is_length_even() == expected

    def test_cyclicity(self, populated_circular, empty_circular):
        """Test cycle detection and length"""
        assert populated_circular.is_cyclic()
        assert populated_circular.cycle_length() == 5
        assert empty_circular.cycle_length() == 0

    @pytest.mark.parametrize("n,expected", [
        (2, 2),
        (1, 1),
        (5, 5),
        (10, False)
    ])
    def test_nth_from_end(self, populated_circular, n, expected):
        """Test finding nth element from end"""
        assert populated_circular.from_the_end(n) == expected

    def test_delete(self, populated_circular):
        """Test node deletion"""
        populated_circular.del_node(3)
        assert populated_circular.size() == 4
        populated_circular.del_node(5)
        assert populated_circular.size() == 3
        populated_circular.del_node(3)  # Try deleting non-existent value
        assert populated_circular.size() == 3

    def test_reverse_in_place(self, populated_circular):
        """Test in-place reversal"""
        populated_circular.rev_in_place()
        assert populated_circular.head.data == 1
        assert populated_circular.size() == 5
        assert self._get_last_node(populated_circular).data == 5

    def test_swap_pairs(self, populated_circular):
        """Test swapping adjacent pairs"""
        populated_circular.insert_beginning(6)  # Make even length
        assert populated_circular.swap_pairs()
        assert populated_circular.head.data == 5
        assert populated_circular.head.next.data == 6
        # Check last pair
        current = populated_circular.head
        while current.next.next != populated_circular.head:
            current = current.next
        assert current.data == 1
        assert current.next.data == 2

    @staticmethod
    def _get_last_node(ll):
        """Helper to get last node of a circular linked list"""
        if not ll.head:
            return None
        current = ll.head
        while current.next != ll.head:
            current = current.next
        return current
