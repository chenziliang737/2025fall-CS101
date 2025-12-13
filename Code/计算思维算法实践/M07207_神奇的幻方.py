N = int(input())
list1 = [[0] * (2 * N - 1) for _ in range(2 * N - 1)]
i = 0
j = N - 1
a = 1
for _ in range((2 * N - 1) ** 2):
    list1[i][j] = a
    a += 1
    i1 = (i - 1) % (2 * N - 1)
    j1 = (j + 1) % (2 * N - 1)
    if (i, j) == (0, 2 * N - 2) or list1[i1][j1] != 0:
        i1 = (i + 1) % (2 * N - 1)
        j1 = j
    i = i1
    j = j1
for row in list1:
    print(*row)
