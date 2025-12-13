from collections import deque

m, n = map(int, input().split())
map1 = [[-1] * (n + 2) for _ in range(m + 2)]
for i in range(1, m + 1):
    map1[i][1 : n + 1] = list(map(int, input().split()))
set1 = set()
queue = deque()
queue.append((1, 1, 0))
while queue:
    x, y, t = queue.popleft()
    if map1[x][y] == 1:
        print(t)
        break
    set1.add((x, y))
    for d in [1, -1]:
        if map1[x + d][y] in [0, 1] and (x + d, y) not in set1:
            queue.append((x + d, y, t + 1))
        if map1[x][y + d] in [0, 1] and (x, y + d) not in set1:
            queue.append((x, y + d, t + 1))
else:
    print("NO")
