from collections import deque

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    grid = [[[0] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            row = list(input())
            grid[i][j] = row
            for k in range(C):
                if row[k] == "S":
                    x0, y0, z0 = i, j, k
        input()

    def check(x, y, z):
        return 0 <= x <= L - 1 and 0 <= y <= R - 1 and 0 <= z <= C - 1

    queue = deque([(x0, y0, z0, 0)])
    set1 = set([(x0, y0, z0)])
    d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while queue:
        x, y, z, t = queue.popleft()
        if grid[x][y][z] == "E":
            print(f"Escaped in {t} minute(s).")
            break
        for dx, dy, dz in d:
            x1 = x + dx
            y1 = y + dy
            z1 = z + dz
            if (
                check(x1, y1, z1)
                and grid[x1][y1][z1] != "#"
                and (x1, y1, z1) not in set1
            ):
                queue.append((x1, y1, z1, t + 1))
                set1.add((x1, y1, z1))
    else:
        print("Trapped!")
