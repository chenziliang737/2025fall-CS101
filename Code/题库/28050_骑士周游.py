n = int(input())
x0, y0 = map(int, input().split())
d = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


def check(x, y):
    return 0 <= x <= n - 1 and 0 <= y <= n - 1


condition = [[0] * n for _ in range(n)]
condition[x0][y0] = 1


def dfs(m, x, y):
    if m == n**2:
        return True
    dict1 = {}
    for dx, dy in d:
        x1 = x + dx
        y1 = y + dy
        if check(x1, y1) and condition[x1][y1] == 0:
            dict1[(x1, y1)] = 0
            for t in d:
                x2 = x1 + t[0]
                y2 = y1 + t[1]
                if check(x2, y2) and condition[x2][y2] == 0:
                    dict1[(x1, y1)] += 1
    for x1, y1 in sorted(dict1.keys(), key=lambda x: dict1[x]):
        condition[x1][y1] = 1
        if dfs(m + 1, x1, y1):
            return True
        condition[x1][y1] = 0
    return False


if dfs(1, x0, y0):
    print("success")
else:
    print("fail")
