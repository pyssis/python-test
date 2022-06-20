a = str(input())
b = len(a) - 1
c = 1
d = ''
if len(a) == 1:
    d = d + a + str(c)
else:
    for i in range(0, b):
        if a[i] == a[i + 1]:
            c += 1
        elif a[i] != a[i + 1]:
            d = d + a[i] + str(c)
            c = 1
    for j in range(b, b + 1):
        if a[-1] == a[-2]:
            d = d + a[j] + str(c)
        elif a[-1] != a[-2]:
            d = d + a[j] + str(c)
            c = 1
print(d)
