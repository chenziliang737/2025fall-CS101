T, n = map(int, input().split())
dp = [0] * (T + 1)
dp1 = [0] * (T + 1)
for _ in range(n):
    ti, wi = map(int, input().split())
    dp1[ti] = max(dp[ti], wi)
    for t in range(ti + 1, T + 1):
        if dp[t - ti] != 0:
            dp1[t] = max(dp[t], dp[t - ti] + wi)
    dp = dp1[:]
s = dp1[-1]
if s:
    print(s)
else:
    print(-1)
