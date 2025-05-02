import pytest
from ..tree import BinarySearchTree

@pytest.fixture
def empty_bst():
    """Fixture providing an empty binary search tree"""
    return BinarySearchTree()

@pytest.fixture
def sample_bst():
    """Fixture providing a BST with structure:
                5
                /   \
            4     8
            /     /
            3     7
    """
    bst = BinarySearchTree()
    bst.insert_from_list([5, 4, 3, 8, 7])
    return bst

@pytest.fixture
def complex_bst():
    """Fixture providing a more complex BST with structure:
                5
            /         \
            4             8
        /   \         /   \
        3     4.5     7     9
            /    \\
            4.45   4.75
    """
    bst = BinarySearchTree()
    bst.insert_from_list([5, 4, 3, 8, 7, 4.5, 4.45, 4.75, 9])
    return bst

def verify_bst_structure(bst):
    """Helper function to verify BST structure"""
    assert bst.root.data == 5
    assert bst.root.left.data == 4
    assert bst.root.right.data == 8
    assert bst.root.right.left.data == 7
    assert bst.root.left.left.data == 3

def test_insert_from_list():
    """Test BST creation from list"""
    inp_list = [1, 2, 3]
    bst = BinarySearchTree(inp_list=inp_list)
    assert bst.root.data == 1
    assert bst.root.left is None
    assert bst.root.right.data == 2
    assert bst.root.right.right.data == 3

def test_insert(sample_bst):
    """Test single value insertion"""
    sample_bst.insert(9)
    assert sample_bst.root.right.right.data == 9
    verify_bst_structure(sample_bst)

@pytest.mark.parametrize("traversal_method,expected", [
    ("preorder", [5, 4, 3, 8, 7]),
    ("inorder", [3, 4, 5, 7, 8]),
    ("postorder", [3, 4, 7, 8, 5]),
    ("spiral", [5, 4, 8, 7, 3]),
    (("spiral", True), [5, 8, 4, 3, 7])  # clockwise spiral
])
def test_traversals(sample_bst, traversal_method, expected):
    """Test various tree traversal methods"""
    if isinstance(traversal_method, tuple):
        method, clockwise = traversal_method
        result = getattr(sample_bst, method)(clockwise=clockwise)
    else:
        result = getattr(sample_bst, traversal_method)()
    assert result == expected

def test_empty_tree_traversals(empty_bst):
    """Test traversals on empty tree"""
    assert empty_bst.preorder() == []
    assert empty_bst.inorder() == []
    assert empty_bst.postorder() == []
    assert empty_bst.spiral() == []
    assert empty_bst.spiral(clockwise=True) == []

@pytest.mark.parametrize("is_rhs,expected", [
    (True, [5, 8, 7]),   # RHS view
    (False, [5, 4, 3])   # LHS view
])
def test_tree_views(sample_bst, is_rhs, expected):
    """Test tree views (left-hand side and right-hand side)"""
    view = sample_bst.view(rhs=is_rhs)
    assert len(view) == 3
    assert view == expected

@pytest.mark.parametrize("tree_fixture,expected", [
    ("sample_bst", [5, 4, 3, 7, 8]),
    ("complex_bst", [5, 4, 3, 4.45, 4.75, 7, 9, 8])
])
def test_boundary_nodes(request, tree_fixture, expected):
    """Test boundary node traversal"""
    bst = request.getfixturevalue(tree_fixture)
    boundary = bst.get_boundary()
    assert len(boundary) == len(expected)
    assert boundary == expected

def test_k_distance_from_root(sample_bst):
    """Test finding nodes at distance k from root"""
    k_dist_nodes = sample_bst.k_from_root(2)
    assert k_dist_nodes is not None
    assert len(k_dist_nodes) == 2
    assert k_dist_nodes == [3, 7]

def test_connect_siblings(sample_bst):
    """Test connecting siblings without cyclic connections"""
    sample_bst.connect_siblings()
    verify_bst_structure(sample_bst)
    
    # Verify sibling connections
    assert sample_bst.root.sibling is None
    assert sample_bst.root.left.sibling == sample_bst.root.right
    assert sample_bst.root.right.sibling is None
    assert sample_bst.root.left.left.sibling == sample_bst.root.right.left
    assert sample_bst.root.right.left.sibling is None

def test_connect_siblings_cyclic(sample_bst):
    """Test connecting siblings with cyclic connections"""
    sample_bst.connect_siblings(cyclic=True)
    verify_bst_structure(sample_bst)
    
    # Verify cyclic sibling connections
    assert sample_bst.root.sibling == sample_bst.root
    assert sample_bst.root.left.sibling == sample_bst.root.right
    assert sample_bst.root.right.sibling == sample_bst.root.left
    assert sample_bst.root.left.left.sibling == sample_bst.root.right.left
    assert sample_bst.root.right.left.sibling == sample_bst.root.left.left
