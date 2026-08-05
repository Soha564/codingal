class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def print_tree(node):
    if node:
        print(tree)

print("Binary tree Structure: ")
print(root)

def print_tree(node):
    if node:
        print_tree(node.left)
        print(node.value, end=' ')
        print_tree(node.right)


print_tree(root)