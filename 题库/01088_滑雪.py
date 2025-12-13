R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(map(int, input().split())))


def check(x, y):
    return 0 <= x <= R - 1 and 0 <= y <= C - 1


dp = [[1] * C for _ in range(R)]
condition = [[False] * C for _ in range(R)]


def dfs(x, y):
    if condition[x][y]:
        return dp[x][y]
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in range(4):
        x1 = x + d[i][0]
        y1 = y + d[i][1]
        if check(x1, y1) and grid[x1][y1] < grid[x][y]:
            dp[x][y] = max(dp[x][y], dfs(x1, y1) + 1)
    condition[x][y] = True
    return dp[x][y]


s = 1
for x in range(R):
    for y in range(C):
        s = max(s, dfs(x, y))
print(s)
