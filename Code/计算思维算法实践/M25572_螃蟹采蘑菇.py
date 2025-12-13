from collections import deque

n = int(input())
list1 = [[1] * (n + 2) for _ in range(n + 2)]
list2 = []
for i in range(1, n + 1):
    list1[i][1 : n + 1] = list(map(int, input().split()))
    for j in range(1, n + 1):
        if list1[i][j] == 5:
            list2.append(i)
            list2.append(j)
set1 = set()


def neighbour(x1, y1, x2, y2):
    list3 = []
    for d in [1, -1]:
        if list1[x1 + d][y1] in [0, 5, 9] and list1[x2 + d][y2] in [0, 5, 9]:
            if (x1 + d, y1, x2 + d, y2) not in set1:
                list3.append((x1 + d, y1, x2 + d, y2))
                set1.add((x1 + d, y1, x2 + d, y2))
        if list1[x1][y1 + d] in [0, 5, 9] and list1[x2][y2 + d] in [0, 5, 9]:
            if (x1, y1 + d, x2, y2 + d) not in set1:
                list3.append((x1, y1 + d, x2, y2 + d))
                set1.add((x1, y1 + d, x2, y2 + d))
    return list3


queue = deque()
queue.append(tuple(list2))
set1.add(tuple(list2))
while queue:
    x1, y1, x2, y2 = queue.popleft()
    if list1[x1][y1] == 9 or list1[x2][y2] == 9:
        print("yes")
        break
    else:
        queue += neighbour(x1, y1, x2, y2)
else:
    print("no")
