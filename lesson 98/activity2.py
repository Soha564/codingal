class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLL:
    def _init_(self):
        self.head = None

    def Counting_Node(self):
        t = 0
        temp = self.head
        while temp:
            t += 1
            temp  = temp.next
        return t

    def display(self):
            temp = self.head
            while temp:
                print(temp.next, end=" ")
                temp = temp.next

l = DoublyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n2.prev = n1
l.display()
print(end = '\n')
print(l.Counting_Node())