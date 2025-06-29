class Rope:
    def __init__(self, data=''):
        self.left = None
        self.right = None
        self.data = data
        self.weight = len(data)

    def __str__(self):
        if self.left is None and self.right is None:
            return self.data
        return str(self.left) + str(self.right)

    def concatenate(self, other):
        new_root = Rope()
        new_root.left = self
        new_root.right = other
        # Weight should be the total weight of the left subtree (self)
        new_root.weight = self._get_total_weight()
        return new_root

    def _get_total_weight(self):
        """Get the total weight of this rope subtree"""
        if self.left is None and self.right is None:
            return len(self.data)
        total = 0
        if self.left:
            total += self.left._get_total_weight()
        if self.right:
            total += self.right._get_total_weight()
        return total

    def index(self, i):
        if self.weight <= i and self.right is not None:
            return self.right.index(i - self.weight)
        if self.left is not None:
            return self.left.index(i)
        return self.data[i]

    def split(self, i):
        if self.left is None and self.right is None:
            return Rope(self.data[:i]), Rope(self.data[i:])
        if i < self.weight:
            l, r = self.left.split(i)
            return l, r.concatenate(self.right)
        if i > self.weight:
            l, r = self.right.split(i - self.weight)
            return self.left.concatenate(l), r
        return self.left, self.right

    def insert(self, i, s):
        l, r = self.split(i)
        return l.concatenate(Rope(s)).concatenate(r)

    def rebalance(self):
        # Helper to collect all leaf strings
        def collect_leaves(node):
            if node.left is None and node.right is None:
                return [node.data]
            leaves = []
            if node.left:
                leaves.extend(collect_leaves(node.left))
            if node.right:
                leaves.extend(collect_leaves(node.right))
            return leaves

        # Helper to build a balanced rope from list of strings
        def build_balanced(leaves):
            if not leaves:
                return None
            if len(leaves) == 1:
                return Rope(leaves[0])
            mid = len(leaves) // 2
            left = build_balanced(leaves[:mid])
            right = build_balanced(leaves[mid:])
            return left.concatenate(right)

        leaves = collect_leaves(self)
        balanced = build_balanced(leaves)
        # Copy balanced tree into self
        self.left = balanced.left
        self.right = balanced.right
        self.data = balanced.data
        self.weight = balanced.weight

    def report(self):
        return str(self)
