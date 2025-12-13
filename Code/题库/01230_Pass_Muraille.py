for _ in range(int(input())):
    n, k = map(int, input().split())
    wall = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        wall.append((x1, x2))
    wall.sort(key=lambda x: (x[1], x[0]))
    condition = [0] * 101
    s = 0
    for t in wall:
        x1, x2 = t[0], t[1]
        if all(condition[x] < k for x in range(x1, x2 + 1)):
            for x in range(x1, x2 + 1):
                condition[x] += 1
        else:
            s += 1
    print(s)
