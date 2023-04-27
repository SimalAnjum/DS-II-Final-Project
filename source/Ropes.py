
# Set the maximum and minimum number of characters in a leaf node of the rope
maxLeafChars = 5
minLeafChars = 1

# Define a Node class to be used in the Rope class
class Node:
    def __init__(self, value):
        self.value = value
        self.size = len(value) # length of the node's value
        self.left = None # left child of the node
        self.right = None # right child of the node

# Define a Rope class
class Rope:

    # Initialize a Rope object
    def __init__(self, input, minLeafChars=1, maxLeafChars=5) -> None:
        self.root = Node(input) # create a root node with the given input
        self.minLeafChars = minLeafChars # set the minimum number of characters in a leaf node
        self.maxLeafChars = maxLeafChars # set the maximum number of characters in a leaf node

    # Define the string representation of a Rope object
    def __repr__(self):
        return self._repr(self.root)

    # Helper function to recursively generate the string representation of a Rope object
    def _repr(self, node):
        if node.left is None and node.right is None:
            return "Rope('{}')".format(node.value)
        else:
            return '({}, {})'.format(self._repr(node.left), self._repr(node.right))

    # Search for a pattern in the Rope object starting at a given position
    def search(self, node, pattern, start=0):
        while node is not None:
            if node.left is None and node.right is None:
                # If the node is a leaf, search for the pattern in its value
                index = node.value.find(pattern, start)
                if index != -1:
                    index += start
                return index
            elif pattern < node.value:
                # If the pattern is less than the node's value, search in the left subtree
                node = node.left
            else:
                # Otherwise, search in the right subtree and update the start position
                start += len(node.left.value) if node.left else 0
                node = node.right
        return -1
    
    
    # Insert a string into the Rope object at a given position
    def insert(self, node, s, i):
        stack = [node]
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                # If the node is a leaf, insert the string into its value
                node.value = node.value[:i] + s + node.value[i:]
                node.size = len(node.value)
                if node.size > self.maxLeafChars:
                    # If the leaf node has exceeded the maximum number of characters, split it
                    self.split(node)
            elif i <= node.left.size:
                # If the insertion position is in the left subtree, search in the left subtree
                if node.right is not None:
                    stack.append(node.right)
                stack.append(node.left)
            else:
                # Otherwise, search in the right subtree and update the insertion position
                i -= node.left.size
                if node.left is not None:
                    stack.append(node.left)
                stack.append(node.right)
                if i > 0:
                    i -= 1

    def delete(self, node, i, j):
        # If the given node is a leaf node with no children
        if node.left is None and node.right is None:
            # Remove the characters from the given index i to index j in the node's value
            node.value = node.value[:i] + node.value[j:]
            # Update the size of the node's value
            node.size = len(node.value)
            # If the size of the node's value is less than the minimum leaf characters allowed, merge the node
            if node.size < self.minLeafChars:
                self.merge(node)
        # If the characters to be deleted are only in the left subtree
        elif i < node.left.size and j <= node.left.size:
            # Recursively delete the characters from the left subtree
            self.delete(node.left, i, j)
            # Update the size of the node after deleting the characters
            node.size -= (j - i)
            # If the right subtree exists and its size is less than the minimum leaf characters allowed, merge it
            if node.right is not None and node.right.size < self.minLeafChars:
                self.merge(node.right)
        # If the characters to be deleted are only in the right subtree
        elif i >= node.left.size and j > node.left.size:
            # Recursively delete the characters from the right subtree
            self.delete(node.right, i - node.left.size, j - node.left.size)
            # Update the size of the node after deleting the characters
            node.size -= (j - i)
            # If the left subtree exists and its size is less than the minimum leaf characters allowed, merge it
            if node.left is not None and node.left.size < self.minLeafChars:
                self.merge(node.left)
        # If the characters to be deleted span both the left and right subtrees
        else:
            # Merge the values of the left and right subtrees while deleting the characters
            left_value = node.left.value[:i] + node.right.value[j - node.left.size:]
            # Compute the size of the new left subtree
            left_size = len(left_value)
            # Create a new node for the right subtree
            right_node = Node(node.right.value[j - node.left.size:], node.right.left, node.right.right)
            # Update the left and right subtrees of the node
            node.left = Node(left_value, node.left.left, node.left.right)
            node.right = right_node
            # Update the value and size of the node
            node.value = node.left.value + node.right.value
            node.size = len(node.value)
            # If the size of the left subtree is less than the minimum leaf characters allowed, merge it
            if node.left.size < self.minLeafChars:
                self.merge(node.left)
            # If the size of the right subtree is less than the minimum leaf characters allowed, merge it
            elif node.right.size < self.minLeafChars:
                self.merge(node.right)


    # Define a method for replacing all occurrences of a given pattern with the given replacement string in the given node's value
    def replace(self, node, pattern, replace_with):
        # Replace all occurrences of the pattern with the replacement string in the node's value
        node.value = node.value.replace(pattern, replace_with)
        # Update the size of the node's value
        node.size = len(node.value)
        # If the size of the node's value is less than the minimum leaf characters allowed, merge the node
        if node.size < self.minLeafChars:
            self.merge(node)

    def split(self, node):
        # Check if the node has any children. If not, return.
        if node.left is None and node.right is None:
            return

        # Split the node's children.
        left_children = []
        right_children = []
        midpoint = len(node.children) // 2

        for i, child in enumerate(node.children):
            if i < midpoint:
                left_children.append(child)
            else:
                right_children.append(child)

        # Create new left and right nodes using the split children.
        node.left = Node(left_children)
        node.right = Node(right_children)

        # Clear the node's children.
        node.children = None


    def merge(self, node):
        # Check if the input node has both left and right children.
        # If not, simply return without doing anything.
        if not node.left and not node.right:
            return
        # Concatenate the values of the left and right child nodes (using empty strings if either child node does not exist),
        # and assign the result to the input node's "value" attribute.
        node.value = (node.left.value if node.left else "") + (node.right.value if node.right else "")

        # Set the input node's "size" attribute to the length of its new "value".
        node.size = len(node.value)

        # Set both the left and right child nodes of the input node to "None", effectively deleting them from the tree.
        node.left, node.right = None, None



# Create a rope
input_string = 'hello_iam_a_rope_data_structure'
rope = Rope(input_string, minLeafChars=2, maxLeafChars=6)

# Test __repr__()
print("Printing the rope:")
print(rope, "\n") # expected output: (Rope('Hello,'), Rope(' world!'))

#size of rope
print("Size of Rope: ", rope.root.size, "\n")

# Test search()
print("Printing the Search Result:")
word = "data"
index = rope.search(rope.root, word , 0)
print("The word", word, "is found at index = ",index, "\n")

print("Printing the Replace Result:")
# Test replace()
rope.replace(rope.root, "hello_iam_a_", "bro_yah_hai_")
print(rope, "\n")

# Test insert()

print("Printing the Insert Result:")
rope.insert(rope.root, '_and_its_working', 41)
print(rope , "\n")
s2 = str(rope)

# Test delete()
print("Printing the Delete Result:")
start = 4
end = 32

print("We are deleting from index = ", start, "to the index = ", end, "which is ",s2[10:37] )
rope.delete(rope.root, start, end)
print(rope, '\n') 
