for _ in range(int(input())):
    M, N = map(int, input().split())
    s = 0


    def dfs(m, n, i):
        if n == N:
            if m <= i:
                global s
                s += 1
            return
        for x in range(min(m, i) + 1):
            dfs(m - x, n + 1, x)


    dfs(M, 1, float('inf'))
    print(s)
