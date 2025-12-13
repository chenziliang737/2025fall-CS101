import heapq
import sys

data = iter(map(int, sys.stdin.read().split()))
while True:
    try:
        N = next(data)
    except StopIteration:
        break
    grid = []
    for _ in range(N):
        grid.append([next(data) for _ in range(N)])
    cost = [float('inf')] * N
    condition = [False] * N
    cost[0] = 0
    heap = [(0, 0)]
    heapq.heapify(heap)
    while heap:
        t, x = heapq.heappop(heap)
        if condition[x] == True:
            continue
        condition[x] = True
        if sum(condition) == N:
            print(sum(cost))
            break
        for j in range(N):
            if condition[j] == False and grid[x][j] < cost[j]:
                heapq.heappush(heap, (grid[x][j], j))
                cost[j] = grid[x][j]
