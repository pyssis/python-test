import math

x = str(input())
if x == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(S)
elif x == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
    print(S)
elif x == 'круг':
    r = int(input())
    S = 3.14 * r ** 2
    print(S)
