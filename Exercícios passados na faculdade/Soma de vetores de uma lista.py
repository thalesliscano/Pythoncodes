a = list(map(int,input().split()))
# a = [20, 17, 23, 24, 15, 18, 22, 21, 24, 19, 21, 15, 24, 24, 16]
b = list(map(int,input().split()))
# b = [18,17, 21, 22, 25, 22, 14, 17, 28, 21, 33, 27, 16, 17, 22]

tam = len(a)

c = [0]*tam

d = []
for i in range(0,tam):
    c[i] = a[i] + b[i]
    # c.append(d)
