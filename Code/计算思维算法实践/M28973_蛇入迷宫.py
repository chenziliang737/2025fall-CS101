from collections import deque

n = int(input())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))


def check(x, y, d):
    x1, y1 = x + d, y + 1 - d
    if all(0 <= i <= n - 1 for i in [x, y, x1, y1]):
        return True
    else:
        return False


queue = deque()
set1 = set()
queue.append((0, 0, 0, 0))
set1.add((0, 0, 0))
while queue:
    x, y, d, t = queue.popleft()
    if x == n - 1 and y == n - 2 and d == 0:
        print(t)
        break
    x1, y1 = x + d, y + 1 - d
    if (
        check(x + 1, y, d)
        and p[x + 1][y] == 0
        and p[x1 + 1][y1] == 0
        and (x + 1, y, d) not in set1
    ):
        queue.append((x + 1, y, d, t + 1))
        set1.add((x + 1, y, d))
    if (
        check(x, y + 1, d)
        and p[x][y + 1] == 0
        and p[x1][y1 + 1] == 0
        and (x, y + 1, d) not in set1
    ):
        queue.append((x, y + 1, d, t + 1))
        set1.add((x, y + 1, d))
    if (
        check(x, y, 1 - d)
        and p[x + 1 - d][y + d] == 0
        and p[x1 + 1 - d][y1 + d] == 0
        and (x, y, 1 - d) not in set1
    ):
        queue.append((x, y, 1 - d, t + 1))
        set1.add((x, y, 1 - d))
else:
    print(-1)
