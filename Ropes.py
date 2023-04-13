class RopeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.weight = len(value)

    def __len__(self):
        return self.weight

class Rope:
    def __init__(self, s):
        self.root = self._build_rope(s)

    def _build_rope(self, s):
        if len(s) <= 1:
            return RopeNode(s)
        mid = len(s) // 2
        node = RopeNode(s)
        node.left = self._build_rope(s[:mid])
        node.right = self._build_rope(s[mid:])
        return node

    def _search(self, node, i):
        if node is None:
            return None
        if i < node.weight:
            if node.left is None:
                return node.value[i]
            return self._search(node.left, i)
        else:
            if node.right is None:
                return node.value[i - node.weight]
            return self._search(node.right, i - node.weight)

    def search(self, i):
        return self._search(self.root, i)
