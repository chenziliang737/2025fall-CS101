N=int(input())
dp=[[0]*(N+1) for _ in range(N+1)]
for n in range(1,N+1):
    dp[n][n]=1
    for m in range(n-1,-1,-1):
        dp[n][m]=dp[n][m+1]+dp[n-1][m-1]
print(dp[N][0])