import sys

data = iter(sys.stdin.read().strip().split())
N = int(next(data))
list1 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        list1[i][j] = int(next(data))
list2 = [[0] * N for _ in range(N)]
list2[0] = list1[0]
for i in range(1, N):
    for j in range(N):
        list2[i][j] = list2[i - 1][j] + list1[i][j]
s = -float('inf')
for i in range(N):
    for j in range(i):
        row = [list2[i][x] - list2[j][x] for x in range(N)]
        dp = [row[0]] + [-float('inf')] * (N - 1)
        for k in range(1, N):
            dp[k] = max(row[k], row[k] + dp[k - 1])
        s = max(s, max(dp))
print(s)
