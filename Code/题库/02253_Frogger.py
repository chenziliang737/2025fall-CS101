import math, heapq

c = 1
while True:
    n = int(input())
    if n == 0:
        break
    point = []
    distance = [[0] * n for _ in range(n)]
    for i in range(n):
        x, y = map(int, input().split())
        point.append((x, y))
        for j in range(i):
            x1, y1 = point[j]
            d = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
            distance[i][j] = d
            distance[j][i] = d
    heap = [(0, 0)]
    dict1 = {0: 0}
    while heap:
        d, i = heapq.heappop(heap)
        if i == 1:
            print(f"Scenario #{c}")
            print(f"Frog Distance = {d:.3f}")
            print()
            break
        dict1[i] = d
        for j in range(n):
            if j not in dict1:
                d1 = max(d, distance[i][j])
                heapq.heappush(heap, (d1, j))
    c += 1
    input()
