from collections import deque

for _ in range(int(input())):
    R, C, K = map(int, input().split())
    grid = []
    for i in range(R):
        row = list(input())
        grid.append(row)
        for j in range(C):
            if row[j] == "S":
                x0, y0 = i, j

    def check(x, y):
        return 0 <= x <= R - 1 and 0 <= y <= C - 1

    queue = deque([(x0, y0, 0)])
    condition = [[[False] * K for _ in range(C)] for _ in range(R)]
    while queue:
        x, y, t = queue.popleft()
        if grid[x][y] == "E":
            print(t)
            break
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(4):
            x1 = x + d[i][0]
            y1 = y + d[i][1]
            if check(x1, y1):
                if (
                    grid[x1][y1] in [".", "S", "E"]
                    and not condition[x1][y1][(t + 1) % K]
                ):
                    queue.append((x1, y1, t + 1))
                    condition[x1][y1][(t + 1) % K] = True
                if (
                    grid[x1][y1] == "#"
                    and (t + 1) % K == 0
                    and not condition[x1][y1][(t + 1) % K]
                ):
                    queue.append((x1, y1, t + 1))
                    condition[x1][y1][(t + 1) % K] = True
    else:
        print("Oop!")
