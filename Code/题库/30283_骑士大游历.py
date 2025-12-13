from collections import deque


def solve(x1, y1, x2, y2):
    if (x1, y1) == (x2, y2):
        return 0

    def check(x, y):
        return 0 <= x <= 999 and 0 <= y <= 999

    queue1 = deque([(x1, y1, 0)])
    dict1 = {(x1, y1): 0}
    queue2 = deque([(x2, y2, 0)])
    dict2 = {(x2, y2): 0}
    while queue1 or queue2:
        if len(queue1) < len(queue2):
            x, y, t = queue1.popleft()
            d = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
            for i in range(8):
                x3 = x + d[i][0]
                y3 = y + d[i][1]
                if check(x3, y3) and (x3, y3) not in dict1:
                    queue1.append((x3, y3, t + 1))
                    dict1[(x3, y3)] = t + 1
                    if (x3, y3) in dict2:
                        return dict1[(x3, y3)] + dict2[(x3, y3)]
        else:
            x, y, t = queue2.popleft()
            d = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
            for i in range(8):
                x3 = x + d[i][0]
                y3 = y + d[i][1]
                if check(x3, y3) and (x3, y3) not in dict2:
                    queue2.append((x3, y3, t + 1))
                    dict2[(x3, y3)] = t + 1
                    if (x3, y3) in dict1:
                        return dict1[(x3, y3)] + dict2[(x3, y3)]


for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(solve(x1, y1, x2, y2))
