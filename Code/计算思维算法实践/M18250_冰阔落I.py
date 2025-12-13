def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x


while True:
    try:
        n, m = map(int, input().split())
        parent = list(range(n + 1))
        for _ in range(m):
            a, b = map(int, input().split())
            if find(a) == find(b):
                print("Yes")
            else:
                print("No")
                union(a, b)
        unique_parents = set(find(x) for x in range(1, n + 1))
        ans = sorted(unique_parents)
        print(len(ans))
        print(*ans)
    except EOFError:
        break
