import unittest
from dat_struct_py.rope import Rope

class TestRope(unittest.TestCase):

    def test_create_rope(self):
        rope = Rope("hello world")
        self.assertEqual(str(rope), "hello world")

    def test_concatenate(self):
        r1 = Rope("hello ")
        r2 = Rope("world")
        r3 = r1.concatenate(r2)
        self.assertEqual(str(r3), "hello world")

    def test_index(self):
        rope = Rope("hello world")
        self.assertEqual(rope.index(4), 'o')

    def test_split(self):
        rope = Rope("hello world")
        l, r = rope.split(5)
        self.assertEqual(str(l), "hello")
        self.assertEqual(str(r), " world")

    def test_insert(self):
        rope = Rope("hello world")
        rope = rope.insert(5, " beautiful")
        self.assertEqual(str(rope), "hello beautiful world")

    def test_rebalance(self):
        # Create an unbalanced rope by repeated concatenation
        rope = Rope("a")
        for c in "bcdefghijklmnopqrstuvwxyz":
            rope = rope.concatenate(Rope(c))
        unbalanced_str = str(rope)
        # Rope should still represent the correct string
        self.assertEqual(unbalanced_str, "abcdefghijklmnopqrstuvwxyz")
        # Rebalance and check structure and content
        rope.rebalance()
        rebalanced_str = str(rope)
        self.assertEqual(rebalanced_str, "abcdefghijklmnopqrstuvwxyz")
        # Insert and rebalance again
        rope = rope.insert(13, "-")
        rope.rebalance()
        self.assertEqual(str(rope), "abcdefghijklm-nopqrstuvwxyz")

if __name__ == '__main__':
    unittest.main()
