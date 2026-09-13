class Node: 
    def __init__(self, leaf = True):
        self.leaf = leaf
        self.children = []
        self.keys = []
class BTree:
    def __init__(self):
        self.root = Node()
    def insert(self, key):
        root = self.root

        if len(root.keys) == 3:
            new_root = Node(False)
            new_root.children.append(root)   
            self.split_child(new_root, 0)
            self.root = new_root 
        self.insert_key(self.root, key)
    def split(self, parent, index):
        old = parent.children[index]
        new = Node(old.leaf)
        
        middle = old.keys[1]
        new.keys = old.keys[2:]
        old.keys = old.keys[:1]

        if not old.leaf:
            new.children = old.children[2:]
            old.children = old.children[:2]
        parent.keys.insert(index, middle)
        parent.children.insert(index+1, new)

    def insert_key(self, node, key):
        if node.leaf:
            node.keys.append(key)
            node.key.sort()
        else:
            i = len(node.keys) - 1
            while i>= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            if len(node.children[i].keys) == 3:
                self.split(node, i)

                if key > node.keys[i]:
                    i += 1
            self.insert_key(node.children[i], key)
    def display(self, node = None, level = 0):
        if node is None:
            node = self.root
        print(" " * level + str(node.keys))
        for child in node.children:
            self.display(child, level + 1)

tree = BTree()
values = [10, 20, 5, 6, 12, 30, 7, 17]
for value in values:
    tree.insert(value)

tree.display()        
