class Node: 
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def collect_values(root, values):
    if root is None:
        return
    collect_values(root.left, values)
    values.append(root.key)
    collect_values(root.right, values)
def FindTwo(root, sum):
    values = []
    collect_values(root, values)
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            ii = values[i]
            jj = values[j]
            if ii+jj == sum:
                return ii, jj
    return None
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
sum = int(input("Enter a number: "))
print(FindTwo(root, sum))