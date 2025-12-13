import heapq

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))


def check(x, y):
    return 0 <= x <= n - 1 and 0 <= y <= m - 1


res = [[float('inf')] * m for _ in range(n)]
res[0][0] = 0
heap = [(0, 0, 0)]
heapq.heapify(heap)
while heap:
    t, x, y = heapq.heappop(heap)
    if (x, y) == (n - 1, m - 1):
        print(t)
        break
    for d in [1, -1]:
        if check(x + d, y):
            c = max(t, abs(grid[x + d][y] - grid[x][y]))
            if res[x + d][y] > c:
                res[x + d][y] = c
                heapq.heappush(heap, (c, x + d, y))
        if check(x, y + d):
            c = max(t, abs(grid[x][y + d] - grid[x][y]))
            if res[x][y + d] > c:
                res[x][y + d] = c
                heapq.heappush(heap, (c, x, y + d))
