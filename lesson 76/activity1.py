def hanoi(n, source, destination, helper):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    hanoi(n-1, source, helper, destination)
    print("Move disk", n, "from", source, "to", destination)
    hanoi(n-1, helper, destination, source)

hanoi(3, "A", "C", "B")