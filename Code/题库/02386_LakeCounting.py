import sys

sys.setrecursionlimit(20000)
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input()))


def check(x, y):
    return 0 <= x <= N - 1 and 0 <= y <= M - 1


def dfs(x, y):
    grid[x][y] = "."
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if check(x + dx, y + dy) and grid[x + dx][y + dy] == "W":
                dfs(x + dx, y + dy)


S = 0
for x in range(N):
    for y in range(M):
        if grid[x][y] == "W":
            dfs(x, y)
            S += 1
print(S)
