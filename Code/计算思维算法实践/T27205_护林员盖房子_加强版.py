m, n = map(int, input().split())
area = []
for _ in range(m):
    area.append(list(map(int, input().split())))
height = [[0] * n]
for i in range(m):
    row = []
    for j in range(n):
        if area[i][j] == 0:
            row.append(height[-1][j] + 1)
        else:
            row.append(0)
    height.append(row)
del height[0]
S = 0
for i in range(m):
    row = height[i]
    width = [[0, 0] for _ in range(n)]
    stack1 = []
    for j in range(n):
        h = row[j]
        while stack1 and row[stack1[-1]] > h:
            width[stack1.pop()][0] = j
        stack1.append(j)
    while stack1:
        width[stack1.pop()][0] = n
    stack2 = []
    for k in range(n - 1, -1, -1):
        h = row[k]
        while stack2 and row[stack2[-1]] > h:
            width[stack2.pop()][1] = k
        stack2.append(k)
    while stack2:
        width[stack2.pop()][1] = -1
    for i in range(n):
        S = max(S, row[i] * (width[i][0] - width[i][1] - 1))
print(S)
