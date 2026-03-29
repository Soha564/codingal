# reversing in groups of n
def reverse(a, a_size, n):
    temp = 0
    while(temp<a_size):
        start = temp
        end = min(temp + n- 1, a_size - 1)

        while (start < end):
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
        temp += n
a = [5,23,2,564567,1,32,4,34,3245,6,43,31]
n = int(input("Enter a number: "))
a_size = len(a)
reverse(a, a_size, n)
for i in range(0, a_size):
    print(a[i], end = " ")