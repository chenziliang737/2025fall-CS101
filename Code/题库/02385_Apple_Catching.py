T, W = map(int, input().split())
trees = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W + 1) for _ in range(T + 1)]
for i in range(1, T + 1):
    for j in range(min(i, W) + 1):
        if j % 2 + 1 == trees[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
print(max(dp[T]))
