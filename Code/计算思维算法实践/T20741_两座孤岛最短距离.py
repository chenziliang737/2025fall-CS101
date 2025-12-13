import heapq
from collections import deque

n = int(input())
area = []
for _ in range(n):
    area.append(list(map(int, list(input()))))
m = len(area[0])


def check(x, y):
    return 0 <= x <= n - 1 and 0 <= y <= m - 1


step = [[float("inf")] * m for _ in range(n)]
heap = []
heapq.heapify(heap)
set2 = set()
flag1 = True
for i in range(n):
    for j in range(m):
        if area[i][j] == 1 and flag1:
            queue = deque()
            set1 = set()
            queue.append((i, j))
            set1.add((i, j))
            step[i][j] = 0
            while queue:
                x, y = queue.popleft()
                for d in [1, -1]:
                    if (
                        check(x + d, y)
                        and area[x + d][y] == 1
                        and (x + d, y) not in set1
                    ):
                        queue.append((x + d, y))
                        set1.add((x + d, y))
                        step[x + d][y] = 0
                    if (
                        check(x, y + d)
                        and area[x][y + d] == 1
                        and (x, y + d) not in set1
                    ):
                        queue.append((x, y + d))
                        set1.add((x, y + d))
                        step[x][y + d] = 0
                p = q = 0
                for d in [1, -1]:
                    if check(x + d, y):
                        p += 1
                        if area[x + d][y] == 1:
                            q += 1
                    if check(x, y + d):
                        p += 1
                        if area[x][y + d] == 1:
                            q += 1
                if p != q:
                    heapq.heappush(heap, (0, x, y))
                    set2.add((x, y))
            flag1 = False
flag2 = True
while flag2:
    s, x, y = heapq.heappop(heap)
    for d in [1, -1]:
        if check(x + d, y) and area[x + d][y] == 1 and step[x + d][y] == float("inf"):
            print(s)
            flag2 = False
            break
        if check(x, y + d) and area[x][y + d] == 1 and step[x][y + d] == float("inf"):
            print(s)
            flag2 = False
            break
        if check(x + d, y) and (x + d, y) not in set2:
            step[x + d][y] = min(step[x + d][y], s + 1)
            heapq.heappush(heap, (step[x + d][y], x + d, y))
            set2.add((x + d, y))
        if check(x, y + d) and (x, y + d) not in set2:
            step[x][y + d] = min(step[x][y + d], s + 1)
            heapq.heappush(heap, (step[x][y + d], x, y + d))
            set2.add((x, y + d))
