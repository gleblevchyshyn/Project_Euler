first = 0
second = 1
SUM = 0
while second < 4000000:
    tmp = second
    second += first
    first = tmp
    if second % 2 == 0:
        SUM += second

print(SUM)


def calcE():
    x = y = 1
    suma = 0
    while suma < 1000000:
        suma += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y

    return suma
