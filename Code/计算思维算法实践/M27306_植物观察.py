def find(x):
    if x == p[x]:
        return x
    else:
        return find(p[x])


n, m = map(int, input().split())
p = [i for i in range(2 * n)]
flag = True
for _ in range(m):
    a, b, c = map(int, input().split())
    if c == 0:
        if find(a + n) == find(b) or find(a) == find(b + n):
            flag = False
            continue
        p[find(a)] = find(b)
        p[find(a + n)] = find(b + n)
    else:
        if find(a) == find(b):
            flag = False
            continue
        p[find(a + n)] = find(b)
        p[find(b + n)] = find(a)
if flag:
    print("YES")
else:
    print("NO")
