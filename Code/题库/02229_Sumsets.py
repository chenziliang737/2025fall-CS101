N = int(input())
M = 10**9
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    if i % 2 == 1:
        dp[i] = dp[i - 1] % M
    else:
        dp[i] = (dp[i - 1] + dp[i // 2]) % M
print(dp[N])
