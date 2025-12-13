n, m = map(int, input().split())
list1 = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    list1[i][1 : m + 1] = list(map(int, input().split()))
list2 = [list1[i][:] for i in range(len(list1))]


def mycount(list1, i, j):
    dx = [0, -1, 1]
    dy = [0, -1, 1]
    a = 0
    for x in dx:
        for y in dy:
            a += list1[i + x][j + y]
    a -= list1[i][j]
    return a


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if list1[i][j] == 1 and mycount(list1, i, j) < 2:
            list2[i][j] = 0
        if list1[i][j] == 1 and mycount(list1, i, j) > 3:
            list2[i][j] = 0
        if list1[i][j] == 0 and mycount(list1, i, j) == 3:
            list2[i][j] = 1
for row in list2[1 : n + 1]:
    print(" ".join(map(str, row[1 : m + 1])))
