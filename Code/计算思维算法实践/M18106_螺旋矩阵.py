n = int(input())
list1 = [[-1] * (n + 2)] + [[-1] + [0] * n + [-1] for _ in range(n)] + [[-1] * (n + 2)]
y = 1
x = 1
ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
for i in range(1, n**2 + 1):
    list1[y][x] = i
    a = y
    b = x
    a += ds[d][0]
    b += ds[d][1]
    if list1[a][b] != 0:
        d = (d + 1) % 4
        y += ds[d][0]
        x += ds[d][1]
    else:
        y = a
        x = b
for i in range(1, n + 1):
    print(*list1[i][1 : n + 1])
