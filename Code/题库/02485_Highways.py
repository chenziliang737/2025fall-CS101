import sys, heapq

data = iter(map(int, sys.stdin.read().split()))
for _ in range(next(data)):
    N = next(data)
    grid = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(next(data))
        grid.append(row)
    condition = [False] * N
    cost = [float("inf")] * N
    cost[0] = 0
    heap = [(0, 0)]
    while heap:
        t, x = heapq.heappop(heap)
        if condition[x]:
            continue
        condition[x] = True
        for y in range(N):
            t1 = grid[x][y]
            if not condition[y] and cost[y] > t1:
                heapq.heappush(heap, (t1, y))
                cost[y] = t1
    print(max(cost))
