N = int(input())
l = list(map(int, input().split()))
dp1 = [1] * N
for i in range(1, N):
    for j in range(i):
        if l[i] > l[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
dp2 = [1] * N
for j in range(N - 2, -1, -1):
    for i in range(j, N):
        if l[j] > l[i]:
            dp2[j] = max(dp2[j], dp2[i] + 1)
print(N - max([dp1[x] + dp2[x] - 1 for x in range(N)]))
