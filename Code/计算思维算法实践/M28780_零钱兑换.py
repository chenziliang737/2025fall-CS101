from math import inf

n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [0] + [inf for _ in range(m)]
for i in range(n):
    for j in range(coins[i], m + 1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)
print(dp[m] if dp[m] != inf else -1)
