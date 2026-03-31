from collections import deque

m, n = map(int, input().split())
grid = []
for _ in range(m):
    grid.append(list(map(int, input().split())))


def check(x, y):
    return 0 <= x <= m - 1 and 0 <= y <= n - 1


queue = deque([(0, 0, 0)])
queue.append((0, 0, 0))
set1 = set([(0, 0)])
while queue:
    x, y, t = queue.popleft()
    if grid[x][y] == 1:
        print(t)
        break
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(4):
        x1 = x + d[i][0]
        y1 = y + d[i][1]
        if check(x1, y1) and grid[x1][y1] in [0, 1] and (x1, y1) not in set1:
            queue.append((x1, y1, t + 1))
            set1.add((x1, y1))
else:
    print("NO")
