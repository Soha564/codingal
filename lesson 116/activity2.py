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


def FindSecondSmallest(root):
    temp = None
    while root.left:
        temp = root
        root = root.left
    return temp.key



root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
second_smallest = FindSecondSmallest(root)
print("The second smallest: ", second_smallest)