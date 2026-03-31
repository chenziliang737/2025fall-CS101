import heapq

for _ in range(int(input())):
    N, M = map(int, input().split())
    grid = []
    for i in range(N):
        roll = list(input())
        for j in range(M):
            if roll[j] == "r":
                x0, y0 = i, j
            if roll[j] == "a":
                x2, y2 = i, j
        grid.append(roll)
    heap = [(0, x0, y0)]
    condition = [[False] * M for _ in range(N)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    check = lambda x, y: 0 <= x <= N - 1 and 0 <= y <= M - 1
    while heap:
        t, x, y = heapq.heappop(heap)
        if (x, y) == (x2, y2):
            print(t)
            break
        for dx, dy in d:
            x1, y1 = x + dx, y + dy
            if check(x1, y1) and grid[x1][y1] != "#" and not condition[x1][y1]:
                if grid[x1][y1] == "x":
                    heapq.heappush(heap, (t + 2, x1, y1))
                    condition[x1][y1] = True
                elif grid[x1][y1] in ["a", "@"]:
                    heapq.heappush(heap, (t + 1, x1, y1))
                    condition[x1][y1] = True
    else:
        print("Impossible")
