class FingerTree:
    def __init__(self, node=None, left=None, right=None, size=0):
        self.node = node
        self.left = left
        self.right = right
        self.size = size

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < len(self.left):
            return self.left[index]
        if index == len(self.left):
            return self.node.value
        return self.right[index - len(self.left) - 1]

    def push_left(self, value):
        if not self.node:
            self.node = Leaf(value)
            self.size = 1
        elif len(self.left) < len(self.right):
            self.left = self.left.push_left(value)
            self.size += 1
        else:
            new_node, self.left = self.node.split(self.left.push_left(value), self.right)
            self.node = new_node
            self.size += 1

    def push_right(self, value):
        if not self.node:
            self.node = Leaf(value)
            self.size = 1
        elif len(self.right) < len(self.left):
            self.right = self.right.push_right(value)
            self.size += 1
        else:
            self.right, new_node = self.node.split(self.left, self.right.push_right(value))
            self.node = new_node
            self.size += 1

    def __str__(self):
        return str(self.node) + " " + str(self.left) + " " + str(self.right)

class Node:
    def __init__(self, value, left=None, right=None, size=0):
        self.value = value
        self.left = left
        self.right = right
        self.size = size

    def __len__(self):
        return self.size

    def split(self, left, right):
        if len(left) <= len(right):
            new_left = Node(left.value, left.left, left.right + self.left, len(left) + len(self.left) + 1)
            return new_left, Node(right.value, new_left.right, right.right, len(right) + len(self.right) + 1)
        else:
            new_right = Node(right.value, self.right + right.left, right.right, len(right) + len(self.right) + 1)
            return Node(left.value, left.left, self.left + new_right.left, len(left) + len(self.left) + 1), new_right

    def __str__(self):
        return str(self.left) + " " + str(self.value) + " " + str(self.right)

class Leaf:
    def __init__(self, value):
        self.value = value
        self.size = 1

    def __len__(self):
        return self.size

    def split(self, left, right):
        return Leaf(left.value), Leaf(right.value)

    def __str__(self):
        return str(self.value)
