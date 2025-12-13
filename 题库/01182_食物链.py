n, k = map(int, input().split())
p = [0] + [i for i in range(1, 3 * n + 1)]


def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
    return p[x]


s = 0
for _ in range(k):
    d, x, y = map(int, input().split())
    if x > n or y > n:
        s += 1
        continue
    if d == 1:
        if find(x) == find(y + n) or find(x + n) == find(y):
            s += 1
            continue
        p[find(x)] = find(y)
        p[find(x + n)] = find(y + n)
        p[find(x + 2 * n)] = find(y + 2 * n)
    else:
        if find(x) == find(y) or find(x) == find(y + n):
            s += 1
            continue
        p[find(x + n)] = find(y)
        p[find(x + 2 * n)] = find(y + n)
        p[find(x)] = find(y + 2 * n)
print(s)
