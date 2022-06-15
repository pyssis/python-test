a = int(input())
b = int(input())
c = 0
d = 0
for j in range (a,b+1):
    if j%3 == 0:
        c = c+j
        d = d+1
    j+=1
print(c/d)
