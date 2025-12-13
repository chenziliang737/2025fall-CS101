from collections import deque


def find(i, j, list1, list2):
    list3 = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if list1[i + x][j + y] == "W" and list2[i + x][j + y] == 0:
                list3.append((i + x, j + y))
    return list3


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    list1 = [["."] * (M + 2) for _ in range(N + 2)]
    list2 = [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        list1[i][1 : M + 1] = list(input())
    s = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if list1[i][j] == "W" and list2[i][j] == 0:
                list2[i][j] = 1
                queue = deque()
                queue += find(i, j, list1, list2)
                while queue:
                    t = queue.popleft()
                    list2[t[0]][t[1]] = 1
                    queue += find(t[0], t[1], list1, list2)
                s += 1
    print(s)
