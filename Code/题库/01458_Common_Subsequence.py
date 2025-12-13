import sys

data = iter(sys.stdin.read().split())
while True:
    try:
        X = next(data)
        Y = next(data)
    except StopIteration:
        break
    m = len(X)
    n = len(Y)
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if X[0] == Y[0] else 0
    for j in range(n):
        if dp[0][j - 1] == 1 or X[0] == Y[j]:
            dp[0][j] = 1
    for i in range(m):
        if dp[i - 1][0] == 1 or X[i] == Y[0]:
            dp[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp[-1][-1])
