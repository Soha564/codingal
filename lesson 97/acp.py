class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next


l = DoublyLL()

n = Node(10)
l.head = n

n1 = Node(20)
n.next = n1
n1.prev = n

n2 = Node(30)
n1.next = n2
n2.prev = n1

l.display()

