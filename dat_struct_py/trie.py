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
        self.root = TrieNode('*')

    def insert(self, inp: str):
        if not inp:
            return
        curr = self.root
        for ch in inp:
            if not curr.children.get(ch):
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]
        curr.end_word = True
        curr.sentence = inp

    def lookup(self, inp: str) -> bool:
        if not inp:
            return False
        curr:TrieNode = self.root
        for ch in inp:
            if curr.children.get(ch):
                curr = curr.children[ch]
            else:
                return False
        return curr.end_word
