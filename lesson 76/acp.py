def paths(r, c, path):
    if r == 0 and c == 0:
        print(path)
        return

    if c > 0:
        paths(r, c - 1, path + "r")
    if r > 0:
        paths(r - 1, c, path + "d")



rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

paths(rows - 1, cols - 1, "")
