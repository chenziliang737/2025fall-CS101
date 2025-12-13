x0, y0 = map(int, input().split())
xm, ym = map(int, input().split())
M = int(input())
set1 = set()
for _ in range(M):
    set1.add(tuple(map(int, input().split())))
dict1 = {}  # 记录当下最小步数
dict2 = {}  # 记录当下父节点
dict3 = {}  # 记录到达该点的路径数
set2 = set()


def check(x, y):
    if 0 <= x <= 10 and 0 <= y <= 10 and (x, y) not in set1 and (x, y) not in set2:
        return True


def neighbour(x, y):
    move = [
        [1, 2, 0, 1],
        [-1, 2, 0, 1],
        [2, 1, 1, 0],
        [2, -1, 1, 0],
        [1, -2, 0, -1],
        [-1, -2, 0, -1],
        [-2, 1, -1, 0],
        [-2, -1, -1, 0],
    ]
    neighbor = []
    for t in move:
        x1 = x + t[0]
        y1 = y + t[1]
        if check(x1, y1) and (x + t[2], y + t[3]) not in set1:
            neighbor.append((x1, y1))
    return neighbor


dict1[(x0, y0)] = 0
dict3[(x0, y0)] = 1
flag = True
while dict1:
    t = min(dict1.keys(), key=lambda x: dict1[x])
    if t == (xm, ym):
        if flag:
            str1 = f"({xm},{ym})"
            t1 = (t[0], t[1])
            while t1 != (x0, y0):
                t1 = dict2[t1]
                str1 = f"({t1[0]},{t1[1]})-" + str1
            flag = False
    c = dict1.pop(t)
    set2.add(t)
    for t1 in neighbour(t[0], t[1]):
        if (c1 := dict1.get(t1, float("inf"))) > c + 1:
            dict1[t1] = c + 1
            dict2[t1] = t
            dict3[t1] = dict3[t]
        elif c1 == c + 1:
            dict3[t1] += dict3[t]
if dict3[(xm, ym)] > 1:
    print(dict3[(xm, ym)])
else:
    print(str1)
