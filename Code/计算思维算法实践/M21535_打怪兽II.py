n, w = map(int, input().split())
P = sum(map(int, input().split()))
dp = [0] * (w + 1)
dp1 = [0] * (w + 1)
for _ in range(n):
    xi, yi = map(int, input().split())
    if xi > P:
        continue
    if yi <= w:
        for i in range(yi, w + 1):
            dp1[i] = max(dp[i], dp[i - yi] + 1)
    dp = dp1[:]
print(dp[-1])
