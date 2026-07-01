class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            nxt = curr.next      
            curr.next = prev    
            prev = curr         
            curr = nxt           

        self.head = prev         

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print()


l = SinglyLL()

n = Node(10)
l.head = n

n1 = Node(20)
n.next = n1

n2 = Node(30)
n1.next = n2

print("Original list:")
l.display()

print("Reversed list:")
l.reverse()
l.display()
