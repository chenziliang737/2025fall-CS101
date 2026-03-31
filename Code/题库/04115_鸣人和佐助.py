from collections import deque

M, N, K = map(int, input().split())
grid = []
for i in range(M):
    roll = list(input())
    for j in range(N):
        if roll[j] == "@":
            x0, y0 = i, j
        if roll[j] == "+":
            x2, y2 = i, j
    grid.append(roll)
visited = [[[False] * (K + 1) for _ in range(N)] for _ in range(M)]
queue = deque([(0, x0, y0, K)])
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
check = lambda x, y: 0 <= x <= M - 1 and 0 <= y <= N - 1
while queue:
    t, x, y, k = queue.popleft()
    if (x, y) == (x2, y2):
        print(t)
        break
    for dx, dy in d:
        x1, y1 = x + dx, y + dy
        if check(x1, y1):
            if grid[x1][y1] in ["*", "@", "+"] and not visited[x1][y1][k]:
                queue.append((t + 1, x1, y1, k))
                visited[x1][y1][k] = True
            elif grid[x1][y1] == "#" and k > 0 and not visited[x1][y1][k - 1]:
                queue.append((t + 1, x1, y1, k - 1))
                visited[x1][y1][k - 1] = True
else:
    print(-1)
