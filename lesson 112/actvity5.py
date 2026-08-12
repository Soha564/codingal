class Node: 
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                print(f"Inserted {data} to the left of {self.data}")
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                print(f"Inserted {data} to the right of {self.data}")
            else:
                self.right.insert(data)
        else:
            print(f"Value {data} already exists in the tree.")
val = []
def inorder(root):
    if root:
        inorder(root.left)
        val.append(root.data)
        inorder(root.right)
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(13)
root.insert(7)
inorder(root)
print("The second smallest number:", val[1]) 