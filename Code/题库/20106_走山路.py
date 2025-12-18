import heapq

m, n, p = map(int, input().split())
grid = []
for _ in range(m):
    row = list(input().split())
    for i in range(n):
        if row[i].isdigit():
            row[i] = int(row[i])
    grid.append(row)


def check(x, y):
    return 0 <= x <= m - 1 and 0 <= y <= n - 1


for _ in range(p):
    x0, y0, x1, y1 = map(int, input().split())
    if grid[x0][y0] == "#" or grid[x1][y1] == "#":
        print("NO")
        continue
    heap = [(0, x0, y0)]
    dict1 = {(x0, y0): 0}
    while heap:
        t, x, y = heapq.heappop(heap)
        if (x, y) == (x1, y1):
            print(t)
            break
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in d:
            x2 = x + dx
            y2 = y + dy
            if check(x2, y2) and grid[x2][y2] != "#":
                t1 = t + abs(grid[x2][y2] - grid[x][y])
                if dict1.get((x2, y2), float("inf")) > t1:
                    heapq.heappush(heap, (t1, x2, y2))
                    dict1[(x2, y2)] = t1
    else:
        print("NO")
