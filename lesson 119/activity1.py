ar = [" " for _ in range(5)]
n = 5

front = -1
rear = -1

def enqueue(customer_name):
    global n, front, rear
    if rear == n-1:
        print("Queue overflow! No more customers")
        return
    if front == -1 and rear == -1:
        front = 0
        rear = 0
    else:
        rear += 1
    ar[rear] = customer_name
    print(customer_name, "added.")
def dequeue(customer_name):
    global n, rear, front
    if front == -1:
        print("No customers in Queue to remove.")
        return
    index = -1
    for i in range(front, rear +1):
        if ar[i] == customer_name:
            index = i
            ar.pop(i)
            print("Remaining customers: ", end = ' ')
            i = front
            while i <= rear:
                print(ar[i], end = ' ')
                i += 1
            print("\n", end = ' ')
            break
    if index == -1:
        print("Customer not found within queue")
def display():
    global n, rear, front
    if front == -1:
        print("Queue is empty.")
    else:
        print("Customers in queue: ", end = ' ')
        i = front
        while i <= rear:
            print(ar[i], end = ' ')
            i += 1
        print("\n", end = ' ')
            
print("1. Add a customer.")
print("2. Remove a customer.")
print("3. Display all customers.")
print("4. Exit.")

loop = True
while loop:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        customer_name = input("Enter the customer's name: ")
        enqueue(customer_name)
    elif ch == 2:
        customer_name = input("Enter the customer's name: ")
        dequeue(customer_name)
    elif ch == 3:
        display()
    elif ch == 4:
        print("Exitting..")
        break
    else:
        print("Invalid choice")
    


