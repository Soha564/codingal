class Node:
    def __init__(self, data):
        self.left_child = None
        self.data = data
        self.right_child = None
def find_sum_recursive(root):
    if root is None:
        return 0
    return find_sum_recursive(root.left_child) + find_sum_recursive(root.right_child) + root.data

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
root.left_child.right_child.right_child = Node(15)

sum_recursive = find_sum_recursive(root)
print(f"The sum of the binary tree(recursive) is: {sum_recursive}")