import math

n = int(input())
grid = [[0] * 9]
for _ in range(8):
    grid.append([0] + list(map(int, input().split())))
prefix = [[0] * 9 for _ in range(9)]
for i in range(1, 9):
    for j in range(1, 9):
        prefix[i][j] = grid[i][j] + prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1]


def square(x1, y1, x2, y2):
    a = prefix[x2][y2] - prefix[x2][y1 - 1] - prefix[x1 - 1][y2] + prefix[x1 - 1][y1 - 1]
    return (a - mu) ** 2


mu = prefix[-1][-1] / n
S = float('inf')
stack = []


def dfs(x1, y1, x2, y2, m):
    global S
    if sum(stack) >= S:
        return
    if m == n:
        stack.append(square(x1, y1, x2, y2))
        S = min(S, sum(stack))
        stack.pop()
        return
    if x2 > x1:
        for x3 in range(x1, x2):
            stack.append(square(x1, y1, x3, y2))
            dfs(x3 + 1, y1, x2, y2, m + 1)
            stack.pop()
        for x3 in range(x1 + 1, x2 + 1):
            stack.append(square(x3, y1, x2, y2))
            dfs(x1, y1, x3 - 1, y2, m + 1)
            stack.pop()
    if y2 > y1:
        for y3 in range(y1, y2):
            stack.append(square(x1, y1, x2, y3))
            dfs(x1, y3 + 1, x2, y2, m + 1)
            stack.pop()
        for y3 in range(y1 + 1, y2 + 1):
            stack.append(square(x1, y3, x2, y2))
            dfs(x1, y1, x2, y3 - 1, m + 1)
            stack.pop()


dfs(1, 1, 8, 8, 1)
o = math.sqrt(S / n)
print(f'{o:.3f}')
