class Node:
    def __init__(self, data):
        self.left_child = None
        self.data = data
        self.right_child = None
def find_height(root):
    if root is None:
        return 0
    left_height = find_height(root.left_child)
    right_height = find_height(root.right_child)
    if left_height != right_height:
        return 1+max(left_height, right_height)
    else:
        return left_height + 1



root = Node(1)
root.left_child = Node(2)
root.right_child = Node(3)
root.left_child.left_child = Node(4)
root.left_child.right_child = Node(5)
root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)
root.right_child.left_child.left_child = Node(8)
root.right_child.left_child.right_child = Node(9)
root.left_child.left_child.left_child = Node(10)
root.left_child.left_child.right_child = Node(11)
root.right_child.right_child.left_child = Node(12)
root.right_child.right_child.right_child = Node(13)
root.left_child.right_child.left_child = Node(14)

height_recursive = find_height(root)
print(f"The height of the binary tree(recursive) is: {height_recursive}")