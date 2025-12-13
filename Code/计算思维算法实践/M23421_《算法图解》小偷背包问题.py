N, B = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = [[0] * B for _ in range(N)]
for i in range(N):
    for j in range(B):
        w = list2[i]
        if j + 1 > w:
            a = list1[i] + list3[i - 1][j - w]
            b = list3[i - 1][j]
            list3[i][j] = max(a, b)
        elif j + 1 == w:
            a = list1[i]
            b = list3[i - 1][j]
            list3[i][j] = max(a, b)
        else:
            list3[i][j] = list3[i - 1][j]
print(list3[N - 1][B - 1])
