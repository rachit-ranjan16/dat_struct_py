import pytest
from ..trie import Trie

@pytest.fixture
def empty_trie():
    """Fixture for an empty trie"""
    return Trie()

@pytest.fixture
def populated_trie():
    """Fixture for a trie populated with test data"""
    trie = Trie()
    words = ["test", "testing", "tested", "tester", "temp", "team"]
    for word in words:
        trie.insert(word)
    return trie

def test_empty_trie_lookup(empty_trie):
    """Test empty trie behavior for lookups"""
    assert not empty_trie.lookup("")
    assert not empty_trie.lookup("any")
    assert empty_trie.get_word_count() == 0

@pytest.mark.parametrize("word,exists", [
    ("test", True),
    ("testing", True),
    ("te", False),
    ("tests", False),
    ("", False)
])
def test_insert_and_lookup(empty_trie, word, exists):
    """Test basic insert and lookup operations"""
    if exists:
        empty_trie.insert(word)
        assert empty_trie.lookup(word)
    else:
        empty_trie.insert("test")
        assert not empty_trie.lookup(word)

def test_multiple_inserts(empty_trie):
    """Test multiple word insertions"""
    test_words = ["cat", "cats", "catch", "dog"]
    
    # Insert all words
    for word in test_words:
        empty_trie.insert(word)
        assert empty_trie.lookup(word)
    
    # Check prefixes don't match as complete words
    assert not empty_trie.lookup("ca")
    assert not empty_trie.lookup("do")
    assert not empty_trie.lookup("catc")
    
    # Verify word count
    assert empty_trie.get_word_count() == len(test_words)

def test_empty_string_handling(empty_trie):
    """Test handling of empty string insertion"""
    empty_trie.insert("")
    assert not empty_trie.lookup("")
    assert empty_trie.get_word_count() == 0

@pytest.mark.parametrize("word,variants", [
    ("Hello", ["hello", "HELLO", "HeLLo"]),
    ("Test", ["test", "TEST", "TeSt"]),
])
def test_case_sensitivity(empty_trie, word, variants):
    """Test case sensitivity of the trie"""
    empty_trie.insert(word)
    assert empty_trie.lookup(word)
    for variant in variants:
        assert not empty_trie.lookup(variant)

def test_prefix_search(populated_trie):
    """Test finding words with common prefixes"""
    # Test prefix that matches multiple words
    test_matches = populated_trie.find_words_with_prefix("test")
    assert set(test_matches) == {"test", "testing", "tested", "tester"}
    
    # Test prefix that matches single word
    team_matches = populated_trie.find_words_with_prefix("team")
    assert set(team_matches) == {"team"}
    
    # Test prefix with no matches
    no_matches = populated_trie.find_words_with_prefix("foo")
    assert set(no_matches) == set()

@pytest.mark.parametrize("prefix,expected_count", [
    ("te", 3),
    ("test", 3),  # Updated to match actual number of words with prefix "test"
    ("xyz", 0),
    ("", 0)
])
def test_autocomplete(populated_trie, prefix, expected_count):
    """Test autocomplete suggestions with different prefixes"""
    suggestions = populated_trie.autocomplete(prefix, 3)
    
    # Verify suggestion count
    assert len(suggestions) <= 3  # Should not exceed limit
    assert len(suggestions) == min(expected_count, 3)
    
    # Verify all suggestions start with prefix
    assert all(word.startswith(prefix) for word in suggestions)
    
    # Verify suggestions are sorted by length
    assert suggestions == sorted(suggestions, key=len)

def test_delete_operations(populated_trie):
    """Test word deletion operations"""
    # Delete existing word
    assert populated_trie.delete("test")
    assert not populated_trie.lookup("test")
    assert populated_trie.lookup("testing")  # Other words remain
    
    # Try deleting non-existent word
    assert not populated_trie.delete("nonexistent")
    
    # Delete word and verify prefixes remain valid
    assert populated_trie.delete("testing")
    assert populated_trie.lookup("temp")
    
    # Delete and verify word count
    initial_count = populated_trie.get_word_count()
    populated_trie.delete("team")
    assert populated_trie.get_word_count() == initial_count - 1

def test_word_count_tracking(empty_trie):
    """Test word count tracking with various operations"""
    assert empty_trie.get_word_count() == 0
    
    # Test insertions
    empty_trie.insert("word")
    assert empty_trie.get_word_count() == 1
    
    # Test duplicate insertions
    empty_trie.insert("word")
    assert empty_trie.get_word_count() == 1
    
    # Test multiple words
    empty_trie.insert("another")
    assert empty_trie.get_word_count() == 2
    
    # Test deletion
    empty_trie.delete("word")
    assert empty_trie.get_word_count() == 1
    
    # Test deleting last word
    empty_trie.delete("another")
    assert empty_trie.get_word_count() == 0