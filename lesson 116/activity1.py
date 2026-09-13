class Node: 
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def FindSecondLargest(root):
    temp = None
    while root.right:
        temp = root
        root = root.right
    return temp.key



root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
second_largest = FindSecondLargest(root)
print("The second largest: ", second_largest)