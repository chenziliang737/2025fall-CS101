from collections import deque, defaultdict

T = int(input())
for _ in range(T):
    R, C, K = map(int, input().split())

    def emptylist():
        return [float("inf")] * K

    queue = deque()
    dict1 = defaultdict(emptylist)
    list1 = [["!"] * (C + 2) for _ in range(R + 2)]
    for i in range(1, R + 1):
        list2 = list(input())
        for j in range(C):
            if list2[j] == "S":
                x0, y0 = i, j + 1
            if list2[j] == "E":
                xm, ym = i, j + 1
        list1[i][1 : C + 1] = list2
    queue.append((x0, y0, 0))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ans = 0
    while queue:
        x, y, t = queue.popleft()
        if x == xm and y == ym:
            print(t)
            break
        for k in range(4):
            x1 = x + dx[k]
            y1 = y + dy[k]
            if list1[x1][y1] in [".", "S", "E"] and dict1[(x1, y1)][t % K] > t + 1:
                dict1[(x1, y1)][t % K] = t + 1
                queue.append((x1, y1, t + 1))
            elif (
                list1[x1][y1] == "#" and (t + 1) % K == 0 and dict1[(x1, y1)][0] > t + 1
            ):
                dict1[(x1, y1)][0] = t + 1
                queue.append((x1, y1, t + 1))
    else:
        print("Oop!")
