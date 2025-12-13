R, C = map(int, input().split())
list1 = [[-1] * (C + 2) for _ in range(R + 2)]
list11 = []
for i in range(1, R + 1):
    list1[i][1 : C + 1] = list(map(int, input().split()))
    for j in range(1, C + 1):
        list11.append((list1[i][j], i, j))
list2 = [[0] * (C + 2)] + [[0] + [1] * C + [0] for _ in range(R)] + [[0] * (C + 2)]


def mycount(i, j):
    global list1
    global list2
    c = 1
    list3 = []
    for x in [1, -1]:
        if list1[i + x][j] < list1[i][j]:
            list3.append(list2[i + x][j])
        if list1[i][j + x] < list1[i][j]:
            list3.append(list2[i][j + x])
    if list3:
        c = max(list3) + 1
    return c


set1 = set()
for t in sorted(list11):
    n = t[0]
    i = t[1]
    j = t[2]
    c = mycount(i, j)
    list2[i][j] = c
    set1.add(c)
print(max(set1))
