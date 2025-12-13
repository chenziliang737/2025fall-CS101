n, m = map(int, input().split())
list1 = [[0] * m for _ in range(n)]
for i in range(n):
    list1[i] = list(map(int, input().split()))
list2 = list(map(list, zip(*list1)))
a = 0
for i in range(n):
    a += list1[i].count(1)
b = 0
for i in range(n):
    for j in range(m - 1):
        if list1[i][j] == 1 and list1[i][j + 1] == 1:
            b += 1
for j in range(m):
    for i in range(n - 1):
        if list2[j][i] == 1 and list2[j][i + 1] == 1:
            b += 1
print(4 * a - 2 * b)
