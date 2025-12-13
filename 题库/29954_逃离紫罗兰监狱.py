from collections import deque

R, C, K = map(int, input().split())
list1 = []
for i in range(R):
    list2 = list(input())
    for j in range(C):
        if list2[j] == 'S':
            x0, y0 = i, j
        if list2[j] == 'E':
            x1, y1 = i, j
    list1.append(list2)


def check(x, y):
    return 0 <= x <= R - 1 and 0 <= y <= C - 1


visited = [[[False] * (K + 1) for _ in range(C)] for _ in range(R)]
queue = deque([])
queue.append((x0, y0, 0, 0))
visited[x0][y0][0] = True
while queue:
    x, y, t, k = queue.popleft()
    if x == x1 and y == y1:
        print(t)
        break
    for d in [1, -1]:
        if check(x + d, y) and list1[x + d][y] in ['.', 'S', 'E'] and not visited[x + d][y][k]:
            queue.append((x + d, y, t + 1, k))
            visited[x + d][y][k] = True
        if check(x, y + d) and list1[x][y + d] in ['.', 'S', 'E'] and not visited[x][y + d][k]:
            queue.append((x, y + d, t + 1, k))
            visited[x][y + d][k] = True
        if check(x + d, y) and list1[x + d][y] == '#' and k < K and not visited[x + d][y][k + 1]:
            queue.append((x + d, y, t + 1, k + 1))
            visited[x + d][y][k + 1] = True
        if check(x, y + d) and list1[x][y + d] == '#' and k < K and not visited[x][y + d][k + 1]:
            queue.append((x, y + d, t + 1, k + 1))
            visited[x][y + d][k + 1] = True
else:
    print(-1)
