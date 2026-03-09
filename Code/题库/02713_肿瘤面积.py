n = int(input())
l = []
for i in range(n):
    roll = list(map(int, input().split()))
    for j in range(n):
        if roll[j] == 0:
            l.append((i, j))
x1, y1 = l[0]
x2, y2 = l[-1]
print((x2 - x1 - 1) * (y2 - y1 - 1))
