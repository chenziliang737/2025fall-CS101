from collections import deque

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input()))
condition = [[False] * M for _ in range(N)]
island = []


def check(x, y):
    return 0 <= x <= N - 1 and 0 <= y <= M - 1


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for x0 in range(N):
    for y0 in range(M):
        if grid[x0][y0] == "X" and not condition[x0][y0]:
            island.append(set())
            queue = deque([(x0, y0)])
            condition[x0][y0] = True
            while queue:
                x, y = queue.popleft()
                if x in [0, M - 1] or y in [0, N - 1]:
                    island[-1].add((x, y))
                for dx, dy in d:
                    x1 = x + dx
                    y1 = y + dy
                    if check(x1, y1):
                        if grid[x1][y1] == "X" and not condition[x1][y1]:
                            queue.append((x1, y1))
                            condition[x1][y1] = True
                        if grid[x1][y1] == ".":
                            island[-1].add((x, y))
for i in range(3):
    island[i] = sorted(list(island[i]))
res = [float("inf")] * 3
for i in range(3):
    for t1 in island[i]:
        for t2 in island[(i + 1) % 3]:
            res[i] = min(res[i], abs(t1[0] - t2[0]) + abs(t1[1] - t2[1]) - 1)
s1 = sum(res) - max(res)
s2 = float("inf")
for x0 in range(N):
    for y0 in range(M):
        if grid[x0][y0] == ".":
            ans = [float("inf")] * 3
            for i in range(3):
                ans[i] = min([abs(x0 - t[0]) + abs(y0 - t[1]) - 1 for t in island[i]])
            s2 = min(s2, sum(ans) + 1)
print(min(s1, s2))
