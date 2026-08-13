class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
count = 0
def printSingleChildNodes(root):
    global count
    if root is None:
        return count
    if (root.right_child and  root.left_child):
        count +=1
    printSingleChildNodes(root.left_child)
    printSingleChildNodes(root.right_child)
    return count

root = Node(1)
root.left_child = Node(2)
root.right_child = Node(3)
root.left_child.left_child = Node(4)
root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)
root.right_child.left_child.right_child = Node(9)
root.left_child.left_child.left_child = Node(10)
root.left_child.left_child.right_child = Node(11)
root.left_child.left_child.right_child.left_child = Node(12)
result = printSingleChildNodes(root)

print("Number of Single Child Nodes: ", result)