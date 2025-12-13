res = [[], [' /\\ ', '/__\\']]
for _ in range(9):
    m = len(res[-1])
    triangle = []
    for i in range(m):
        triangle.append(' ' * m + res[-1][i] + ' ' * m)
    for i in range(m):
        triangle.append(res[-1][i] * 2)
    res.append(triangle)
while True:
    n = int(input())
    if n == 0:
        break
    for s in res[n]:
        print(s.rstrip())
    print()
