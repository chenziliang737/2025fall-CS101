n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp = [[], [1], [2, 2]]
    for m in range(3, n + 1):
        dp.append([0] * m)
        dp[m][m - 1] = m
        for a in range(m - 2, 0, -1):
            dp[m][a] = dp[m][a + 1] + dp[m - 1][a - 1]
        dp[m][0] = dp[m][1]
    print(dp[n][0])
