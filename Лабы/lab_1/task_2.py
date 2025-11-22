def sum_array(arr, n):
    s = 0
    for i in range(n):
        s += arr[i]
    return s


def read_int(prompt):
    return int(input(prompt))


n = 10
a = [1, 3, -5, 0, 4, 6, -1, 9, 3, 2]

m = a[0]
for i in range(1, n):
    if m < a[i]:
        m = a[i]
print(m)

s = sum_array(a, n)
print(s)

z = s // m
k = 0

for i in range(n):
    if a[i] > z:
        k += a[i]
    else:
        k -= a[i]

print(k)

x = read_int("Enter x: ")
y = read_int("Enter y: ")
s = 0

while x != 0 and y != 0:
    x -= 1
    y -= 1
    s += x + y

print(s)
