from collections import deque

p = list(input().split())


def board(p):
    b = [['0'] * 3 for _ in range(3)]
    for i in range(9):
        b[i // 3][i % 3] = p[i]
    return b


def position(p):
    for i in range(9):
        if p[i] == 'x':
            return (i // 3, i % 3)


def check(x, y):
    return 0 <= x <= 2 and 0 <= y <= 2


queue = deque([[p, '']])
set1 = set([tuple(p)])
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
m = ['u', 'd', 'l', 'r']
while queue:
    p, s = queue.popleft()
    if p == ['1', '2', '3', '4', '5', '6', '7', '8', 'x']:
        print(s)
        break
    b = board(p)
    x, y = position(p)
    for i in range(4):
        x1, y1 = x + d[i][0], y + d[i][1]
        if check(x1, y1):
            b[x][y], b[x1][y1] = b[x1][y1], b[x][y]
            p1 = b[0] + b[1] + b[2]
            if tuple(p1) not in set1:
                queue.append([p1, s + m[i]])
                set1.add(tuple(p1))
            b[x][y], b[x1][y1] = b[x1][y1], b[x][y]
else:
    print('unsolvable')
