class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLL:
    def _init_(self):
        self.head = None

    def Search_Node(self, data):
        t = 0
        temp = self.head
        while temp:
            if temp.data == data:
                t = 1;
                break;
            temp  = temp.next
        if t == 1:
            print("Data found")
        else: print("Data not found")

    def display(self):
        if self.head == None:
            print("The list is empty")
        else:

            temp = self.head
            while temp:
                print(temp.data, "--->", end=" ")
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
l.Search_Node(100)
l.Search_Node(20)