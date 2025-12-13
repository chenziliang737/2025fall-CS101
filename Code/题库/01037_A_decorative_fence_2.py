from functools import lru_cache

for _ in range(int(input())):
    N, C = map(int, input().split())


    @lru_cache(maxsize=None)
    def dfs(n, d, b, s):
        if n == 1:
            return 1
        if d == 1:
            return sum([dfs(n - 1, -d, b - i, s + i - 1) for i in range(1, b + 1)])
        elif d == -1:
            return sum([dfs(n - 1, -d, b + i - 1, s - i) for i in range(1, s + 1)])


    p = []
    p0 = list(range(1, N + 1))
    C1 = 0
    for i in range(N):
        if C1 + dfs(N, -1, N - i - 1, i) >= C:
            p.append(p0.pop(i))
            d0 = -1
            C -= C1
            break
        C1 += dfs(N, -1, N - i - 1, i)
        if C1 + dfs(N, 1, N - i - 1, i) >= C:
            p.append(p0.pop(i))
            d0 = 1
            C -= C1
            break
        C1 += dfs(N, 1, N - i - 1, i)
    d = -d0
    n = N - 1
    while p0:
        C1 = 0
        for i in range(n):
            if d * p0[i] < d * p[-1]:
                if C1 + dfs(n, d, n - i - 1, i) >= C:
                    p.append(p0.pop(i))
                    d = -d
                    n -= 1
                    C -= C1
                    break
                C1 += dfs(n, d, n - i - 1, i)
    print(*p)
