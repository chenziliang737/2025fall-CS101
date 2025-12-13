N = int(input())
list1 = list(map(int, input().split()))
dp1 = [1] * N
dp2 = [1] * N
for i in range(1, N):
    for j in range(i):
        if list1[j] < list1[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if list1[j] < list1[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
s = 0
for i in range(N):
    s = max(s, dp1[i] + dp2[i] - 1)
print(s)
