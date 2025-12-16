while True:
    l = list(map(int, input().split()))
    if l == [0]:
        break
    n, m, x1, y1, x2, y2 = l
    lines = [(x1, y1, x1, y2)]
    for _ in range(n):
        u, l = map(int, input().split())
        lines.append((u, y1, l, y2))
    lines.append((x2, y1, x2, y2))
    toys = [0] * (n + 1)

    def cross(a, b):
        return a[0] * b[1] - a[1] * b[0]

    for _ in range(m):
        x, y = map(int, input().split())
        l = -1
        r = n
        while r - l > 1:
            mid = (l + r + 1) // 2
            x1, y1, x2, y2 = lines[mid + 1]
            if cross([x1 - x, y1 - y], [x2 - x, y2 - y]) > 0:
                l = mid
            else:
                r = mid
        toys[r] += 1
    for i in range(n + 1):
        print(f"{i}: {toys[i]}")
    print()
