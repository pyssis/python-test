x = input()
s1 = x.upper().count('c'.upper())
s2 = x.upper().count('g'.upper())
y = s1 + s2
print(y / len(x) * 100)
