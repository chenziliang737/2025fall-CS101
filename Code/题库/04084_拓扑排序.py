from collections import defaultdict
import heapq

v, a = map(int, input().split())
dict1 = defaultdict(int)
connection = [[0] * (v + 1) for _ in range(v + 1)]
for _ in range(a):
    x, y = map(int, input().split())
    dict1[y] += 1
    connection[x][y] += 1
heap = []
for x in range(1, v + 1):
    if dict1[x] == 0:
        heapq.heappush(heap, x)
ans = []
while heap:
    x = heapq.heappop(heap)
    ans.append(x)
    for y in range(1, v + 1):
        if connection[x][y] > 0:
            dict1[y] -= connection[x][y]
            if dict1[y] == 0:
                heapq.heappush(heap, y)
print(*[f"v{i}" for i in ans])
