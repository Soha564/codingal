class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None
def traverse(root, tilt):
    if (not root):
        return 0
    left = traverse(root.left, tilt)
    right = traverse(root.right, tilt)

    tilt[0] += abs(left - right)

    return left + right + root.data

def Tilt(root):
    tilt = [0]
    traverse(root, tilt)
    return tilt[0]
if __name__  == '__main__':
    root = None
    root = newNode(4)
    root.left = newNode(2)
    root.right = newNode(9)
    root.left.left = newNode(3)
    root.left.right = newNode(8)
    root.right.right = newNode(7)
    print("The Tilt of the whole tree is", Tilt(root))