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


def FindNodes(root, l, h):
    if root is None:
        return
    if root.key >= l and root.key <= h:
        print(root.key) 
    right = FindNodes(root.right, l, h)
    left = FindNodes(root.left, l, h)


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
l = int(input("Enter the lowest number: "))
h = int(input("Enter the highest number: "))
FindNodes(root, l, h)