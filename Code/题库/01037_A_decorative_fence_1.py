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
    for i in range(N):
        if (C1 := C - dfs(N, -1, N - i - 1, i)) <= 0:
            p.append(p0.pop(i))
            d0 = -1
            break
        else:
            C = C1
            if (C2 := C1 - dfs(N, 1, N - i - 1, i)) <= 0:
                p.append(p0.pop(i))
                d0 = 1
                break
            else:
                C = C2
                continue
    d = -d0
    n = N - 1
    while p0:
        if d == 1:
            for i in range(n):
                if p0[i] < p[-1]:
                    if (C1 := C - dfs(n, d, n - i - 1, i)) <= 0:
                        p.append(p0.pop(i))
                        d = -d
                        n -= 1
                        break
                    else:
                        C = C1
        elif d == -1:
            for i in range(n):
                if p0[i] > p[-1]:
                    if (C2 := C - dfs(n, d, n - i - 1, i)) <= 0:
                        p.append(p0.pop(i))
                        d = -d
                        n -= 1
                        break
                    else:
                        C = C2
    print(*p)
