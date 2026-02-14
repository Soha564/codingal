def tree(n):
    if(n != 0):
        print(n)
        tree(n - 1)
        tree(n - 1)
tree(2)