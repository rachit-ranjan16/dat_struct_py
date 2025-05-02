class TrieNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}
        self.sentence = ""
        self.end_word = False

    def __str__(self):
        return f"val={self.val} children={self.children} sentence={self.sentence} end_word={self.end_word}"


class Trie:
    def __init__(self):
        self.root = TrieNode("*")
        self._word_count = 0

    def insert(self, inp: str):
        if not inp:
            return
        curr = self.root
        exists = True  # Track if word already exists
        for ch in inp:
            if not curr.children.get(ch):
                curr.children[ch] = TrieNode(ch)
                exists = False
            curr = curr.children[ch]
        if not curr.end_word:  # Only increment if this is a new word
            self._word_count += 1
        curr.end_word = True
        curr.sentence = inp

    def lookup(self, inp: str) -> bool:
        if not inp:
            return False
        curr: TrieNode = self.root
        for ch in inp:
            if curr.children.get(ch):
                curr = curr.children[ch]
            else:
                return False
        return curr.end_word

    def delete(self, word: str) -> bool:
        """Delete a word from the trie. Returns True if word was found and deleted."""
        if not word:
            return False

        def _delete_helper(node: TrieNode, word: str, depth: int) -> tuple[bool, bool]:
            """Recursively delete a word from the trie.
            
            Args:
                node: Current trie node being processed
                word: Word to delete
                depth: Current character position in the word

            Returns:
                tuple(bool, bool): A tuple containing:
                    - is_empty_branch: True if this node can be deleted (no children and not end of other words)
                    - word_deleted: True if the target word was found and deleted
            """
            if depth == len(word):
                if node.end_word:
                    node.end_word = False
                    node.sentence = ""
                    self._word_count -= 1
                    # Return (True, True) if node has no children and can be deleted,
                    # (False, True) if node has children or marks end of another word
                    return len(node.children) == 0, True
                return False, False

            ch = word[depth]
            if ch not in node.children:
                return False, False

            is_empty_branch, word_deleted = _delete_helper(node.children[ch], word, depth + 1)

            # Clean up empty branches
            if is_empty_branch:
                del node.children[ch]
                # Current node can be deleted if it has no other children and isn't end of a word
                return len(node.children) == 0 and not node.end_word, word_deleted

            return False, word_deleted

        _, word_deleted = _delete_helper(self.root, word, 0)
        return word_deleted

    def get_word_count(self) -> int:
        """Return the number of unique words in the trie."""
        return self._word_count

    def find_words_with_prefix(self, prefix: str) -> list[str]:
        """Find all words that start with the given prefix."""
        result = []
        if not prefix:
            return result

        # Find the node corresponding to the prefix
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return result
            curr = curr.children[ch]

        # Collect all words under this node
        def _collect_words(node: TrieNode):
            if node.end_word:
                result.append(node.sentence)
            for child in node.children.values():
                _collect_words(child)

        _collect_words(curr)
        return result

    def autocomplete(self, prefix: str, limit: int) -> list[str]:
        """Return up to 'limit' number of autocomplete suggestions for the given prefix."""
        if not prefix or limit <= 0:
            return []
            
        # Get all matching words and sort them by length (shorter words first)
        matches = self.find_words_with_prefix(prefix)
        matches.sort(key=len)
        
        # Return up to limit suggestions
        return matches[:limit]
