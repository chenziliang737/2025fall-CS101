V, P = map(int, input().split())
village = [0] + list(map(int, input().split()))
prefix = [0]
for a in village[1:]:
    prefix.append(prefix[-1] + a)
cost = {}
for i in range(1, V + 1):
    for j in range(1, i + 1):
        mid = (i + j) // 2
        left = village[mid] * (mid - j + 1) - (prefix[mid] - prefix[j - 1])
        right = (prefix[i] - prefix[mid]) - village[mid] * (i - mid)
        cost[(j, i)] = left + right
if P == 1:
    print(cost[(1, V)])
    exit()
dp = [[0] * (V + 1) for _ in range(P + 1)]
for i in range(1, V + 1):
    dp[1][i] = cost[(1, i)]
for p in range(2, P + 1):
    for i in range(1, V + 1):
        s = float('inf')
        for j in range(i):
            s = min(s, dp[p - 1][j] + cost[(j + 1, i)])
        dp[p][i] = s
print(dp[P][V])
