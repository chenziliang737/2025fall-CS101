def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
    return p[x]


n, k = map(int, input().split())
p = [0] * (3 * n + 1)
for i in range(3 * n + 1):
    p[i] = i
ans = 0
for _ in range(k):
    a, x, y = map(int, input().split())
    if x > n or y > n:
        ans += 1
        continue
    if a == 1:
        if find(x + n) == find(y) or find(y + n) == find(x):
            ans += 1
            continue
        p[find(x)] = find(y)
        p[find(x + n)] = find(y + n)
        p[find(x + 2 * n)] = find(y + 2 * n)
    else:
        if find(x) == find(y) or find(y + n) == find(x):
            ans += 1
            continue
        p[find(x + n)] = find(y)
        p[find(y + 2 * n)] = find(x)
        p[find(x + 2 * n)] = find(y + n)
print(ans)
