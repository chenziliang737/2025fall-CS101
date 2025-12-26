import sys

sys.setrecursionlimit(2 << 10)
n = int(input())
matrix = [[1] * (2**n) for _ in range(2**n)]


def dfs(x1, y1, x2, y2):
    x3 = (x1 + x2) // 2
    y3 = (y1 + y2) // 2
    for x in range(x1, x3 + 1):
        for y in range(y1, y3 + 1):
            matrix[x][y] = 0
    if x2 - x1 == 1 and y2 - y1 == 1:
        return
    dfs(x1, y3 + 1, x3, y2)
    dfs(x3 + 1, y1, x2, y3)
    dfs(x3 + 1, y3 + 1, x2, y2)


dfs(0, 0, 2**n - 1, 2**n - 1)
for row in matrix:
    print(*row)
