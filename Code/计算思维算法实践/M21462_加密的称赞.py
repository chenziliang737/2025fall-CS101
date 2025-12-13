n = int(input())
list1 = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    list1[i][1 : n + 1] = list(map(int, input().split()))
list2 = [[1] * (n + 2)] + [[1] + [0] * n + [1] for _ in range(n)] + [[1] * (n + 2)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
str = ""
x, y = 1, 1
i = 0
while True:
    if list1[x][y] == 0:
        break
    str += chr(list1[x][y])
    list2[x][y] = 1
    if list2[x + d[i][0]][y + d[i][1]] == 1:
        i = (i + 1) % 4
    x += d[i][0]
    y += d[i][1]
print(str)
