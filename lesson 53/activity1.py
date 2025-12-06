t = ()
print(t)

t = (5, 6, 4)
print(t)

t = (564, "Hello", 7.8)
print(t)

t = ("Hello", [5, 6, 4], (1, 2, 3))
print(t)

t = ('p', 'e', 'r', 'm', 'i', 't')
print(t[0])
print(t[3])
print(t[5])

n_t = ("Hello", [5, 6, 4], (1, 2, 3))

print(n_t[0][2])
print(n_t[1][1])

print(n_t[0:1])
print(n_t[2::-1])

for i in (t):
    print(i)
t = (4, 1, 2, 4, 3, 6, 7, 9, 4, 60, 55, 233, 4, 0.4)
print(max(t))
print(min(t))
print(t.count(4))
t = (4, 1, 2, 4, 3, 6, 7, 9, 4, 60, 55, 233, 4, 0.4, 0.8)
l_t = list(t)
l_t.append(0.6)
t_t = tuple(l_t)
print(t_t)