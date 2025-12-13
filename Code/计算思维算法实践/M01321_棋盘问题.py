while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        break
    set1 = set()
    for i in range(n):
        list1 = list(input())
        for j in range(n):
            if list1[j] == "#":
                set1.add((i, j))
    s = 0

    def dfs(a, b):
        if len(a) == k:
            global s
            s += 1
            return
        for t in set1:
            if t[0] not in a and t[1] not in b and t[0] > max(a):
                dfs(a + [t[0]], b + [t[1]])

    for t in set1:
        if t[0] <= n - k:
            dfs([t[0]], [t[1]])
    print(s)
