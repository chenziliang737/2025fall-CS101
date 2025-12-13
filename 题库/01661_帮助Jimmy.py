from functools import lru_cache

t = int(input())
for _ in range(t):
    N, X, Y, MAX = map(int, input().split())
    stage = []
    for i in range(N):
        stage.append(list(map(int, input().split())))
    stage.sort(key=lambda x: -x[2])
    stage.append([-1 << 15, 1 << 15, 0])


    @lru_cache(maxsize=None)
    def dfs(x, y):
        for c in range(N + 1):
            x1, x2, h = stage[c]
            if y - MAX <= h < y and x1 <= x <= x2:
                if h == 0:
                    return 0
                return min(x - x1 + dfs(x1, h), x2 - x + dfs(x2, h))
        else:
            return float('inf')


    print(Y + dfs(X, Y))
