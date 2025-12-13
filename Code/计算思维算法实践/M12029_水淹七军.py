import sys

data = iter(sys.stdin.read().strip().split())
from collections import deque


def water(i, j, list1, list2):
    h = list2[i][j][1]
    list3 = []
    for x in [1, -1]:
        if list2[i + x][j][0] == 0 and list1[i + x][j] < h:
            list2[i + x][j] = (1, h)
            list3.append((i + x, j))
        elif list2[i + x][j][0] == 1 and list2[i + x][j][1] < h:
            list2[i + x][j] = (1, h)
            list3.append((i + x, j))
        if list2[i][j + x][0] == 0 and list1[i][j + x] < h:
            list2[i][j + x] = (1, h)
            list3.append((i, j + x))
        elif list2[i][j + x][0] == 1 and list2[i][j + x][1] < h:
            list2[i][j + x] = (1, h)
            list3.append((i, j + x))
    return list3


K = int(next(data))
result = []
for _ in range(K):
    M = int(next(data))
    N = int(next(data))
    list1 = [[float("inf")] * (N + 2) for _ in range(M + 2)]
    list2 = [[(0, float("inf"))] * (N + 2) for _ in range(M + 2)]
    for i in range(1, M + 1):
        list3 = [int(next(data)) for _ in range(N)]
        list1[i][1 : N + 1] = list3
        list2[i][1 : N + 1] = [(0, j) for j in list3]
    I = int(next(data))
    J = int(next(data))
    P = int(next(data))
    for _ in range(P):
        X = int(next(data))
        Y = int(next(data))
        if list2[X][Y][0] == 1 and list1[X][Y] < list2[X][Y][1]:
            continue
        queue = deque()
        queue.append((X, Y))
        list2[X][Y] = (1, list1[X][Y])
        while queue:
            t = queue.popleft()
            list3 = water(t[0], t[1], list1, list2)
            queue += list3
    if list2[I][J][0] == 1 and list2[I][J][1] > list1[I][J]:
        result.append("Yes")
    else:
        result.append("No")
sys.stdout.write("\n".join(result) + "\n")
