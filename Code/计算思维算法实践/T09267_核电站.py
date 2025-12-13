N, M = map(int, input().split())
list1 = [[0] * M for _ in range(N + 1)]
list1[1][0], list1[1][1] = 1, 1
for n in range(2, N + 1):
    list1[n][0] = sum(list1[n - 1])
    for m in range(1, M):
        list1[n][m] = list1[n - 1][m - 1]
print(sum(list1[N]))
