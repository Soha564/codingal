arr = [2, 1, 5, 3, 4]

tree = [0] * (4 * len(arr))

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2

    build(node * 2, start, mid)
    build(node * 2+1, mid + 1, end)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]
def query(node, start, end, l, r):
    if end < 1 or start > r:
        return 0
    if 1 <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2

    left = query(node * 2, start, mid, l, r)
    right = query(node * 2 +1, mid +1, end, l, r)

    return left + right

build(1, 0, len(arr) - 1)

answer = query(1, 0, len(arr) - 1, 0, 4)

print(answer)