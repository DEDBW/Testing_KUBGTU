def sqr(num):
    return num ** 2


n = 10
a = [5, 2, 7, -9, 4, 8, -1, 0, 3, 6]
s = 0
for i in a:
    if i > 0:
        s += sqr(i)
print(f"Сумма квадратов равна: {s}")