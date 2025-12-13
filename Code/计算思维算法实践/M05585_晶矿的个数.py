from collections import deque


def find(i, j, list1, list2):
    list3 = []
    for x in [1, -1]:
        if list1[i + x][j] == list1[i][j] and list2[i + x][j] == 0:
            list3.append((i + x, j))
        if list1[i][j + x] == list1[i][j] and list2[i][j + x] == 0:
            list3.append((i, j + x))
    return list3


k = int(input())
for _ in range(k):
    n = int(input())
    list1 = [["#"] * (n + 2)]
    for _ in range(n):
        list1.append(["#"] + list(input()) + ["#"])
    list1.append(["#"] * (n + 2))
    list2 = [[0] * (n + 2) for _ in range(n + 2)]
    a = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if list1[i][j] == "r" and list2[i][j] == 0:
                queue = deque()
                queue += find(i, j, list1, list2)
                list2[i][j] = 1
                while queue:
                    t = queue.popleft()
                    queue += find(t[0], t[1], list1, list2)
                    list2[t[0]][t[1]] = 1
                a += 1
    b = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if list1[i][j] == "b" and list2[i][j] == 0:
                queue = deque()
                queue += find(i, j, list1, list2)
                list2[i][j] = 2
                while queue:
                    t = queue.popleft()
                    queue += find(t[0], t[1], list1, list2)
                    list2[t[0]][t[1]] = 2
                b += 1
    print(f"{a} {b}")
