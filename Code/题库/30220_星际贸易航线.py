import sys
from functools import lru_cache

sys.setrecursionlimit(2000000000)
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))


@lru_cache(maxsize=None)
def dfs(x, y, d):
    if (x, y) == (N - 1, M - 1):
        if grid[x][y] < 0 and d == 1:
            return -grid[x][y]
        else:
            return grid[x][y]
    if d == 1:
        a = -float("inf")
        if x < N - 1:
            a = max(a, dfs(x + 1, y, 1) + grid[x][y])
        if y < M - 1:
            a = max(a, dfs(x, y + 1, 1) + grid[x][y])
        if grid[x][y] < 0:
            if x < N - 1:
                a = max(a, dfs(x + 1, y, 0) - grid[x][y])
            if y < M - 1:
                a = max(a, dfs(x, y + 1, 0) - grid[x][y])
        return a
    else:
        a = -float("inf")
        if x < N - 1:
            a = max(a, dfs(x + 1, y, 0) + grid[x][y])
        if y < M - 1:
            a = max(a, dfs(x, y + 1, 0) + grid[x][y])
        return a


print(dfs(0, 0, 1))
