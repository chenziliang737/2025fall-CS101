c = 1
while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    p = [i for i in range(n + 1)]

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    for _ in range(m):
        x, y = map(int, input().split())
        p[find(y)] = find(x)
    set1 = set()
    for x in range(1, n + 1):
        set1.add(find(x))
    print(f"Case {c}: {len(set1)}")
    c += 1
