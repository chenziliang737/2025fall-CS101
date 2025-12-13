T, M = map(int, input().split())
dp = [[0, 0] for _ in range(T + 1)]
for i in range(1, T + 1):
    a, b = map(int, input().split())
    dp[i][0] = max(dp[i - 1][0] + a, dp[i - 1][1] + b - M)
    dp[i][1] = max(dp[i - 1][0] + a - M, dp[i - 1][1] + b)
print(max(dp[-1]))
