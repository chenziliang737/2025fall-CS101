m, n, p = map(int, input().split())
heigh = []
for _ in range(m):
    list1 = list(input().split())
    for i in range(n):
        if list1[i].isdigit():
            list1[i] = int(list1[i])
        else:
            list1[i] = -1
    heigh.append(list1)


def check(x, y):
    if 0 <= x <= m - 1 and 0 <= y <= n - 1 and heigh[x][y] >= 0:
        return True
    else:
        return False


def neighbour(t):
    x = t[0]
    y = t[1]
    list2 = []
    for d in [1, -1]:
        if check(x + d, y):
            list2.append((x + d, y))
        if check(x, y + d):
            list2.append((x, y + d))
    return list2


def find(dict1):
    cmin = float("inf")
    for t, c in dict1.items():
        if c < cmin:
            cmin = c
            tmin = t
    return tmin


for _ in range(p):
    x0, y0, xm, ym = map(int, input().split())
    if heigh[x0][y0] == -1 or heigh[xm][ym] == -1:
        print("NO")
        continue
    dict1 = {}
    set1 = set()
    dict1[(x0, y0)] = 0
    while dict1:
        t = find(dict1)
        if t == (xm, ym):
            print(dict1[t])
            break
        set1.add(t)
        c = dict1.pop(t)
        list2 = neighbour(t)
        for t1 in list2:
            if t1 not in set1:
                c1 = c + abs(heigh[t1[0]][t1[1]] - heigh[t[0]][t[1]])
                dict1[t1] = min(dict1.get(t1, float("inf")), c1)
    else:
        print("NO")
