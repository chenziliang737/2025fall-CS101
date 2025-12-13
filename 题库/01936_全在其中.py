while True:
    try:
        s, t = input().split()
    except EOFError:
        break
    m = len(s)
    n = len(t)
    dp = [[0] * n for _ in range(m)]
    if s[0] == t[0]:
        dp[0][0] = 1
    for i in range(1, m):
        if s[i] == t[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i - 1][0]
    for j in range(1, n):
        if s[0] == t[j]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m):
        for j in range(1, n):
            if s[i] == t[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    if dp[-1][-1] == m:
        print('Yes')
    else:
        print('No')
