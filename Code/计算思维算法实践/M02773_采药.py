T, M = map(int, input().split())
dp1 = [0] * (T + 1)
dp2 = [0] * (T + 1)
for i in range(M):
    t, v = map(int, input().split())
    for j in range(1, T + 1):
        if j >= t:
            a = dp1[j]
            b = v + dp1[j - t]
            dp2[j] = max(a, b)
    dp1 = dp2[:]
print(dp2[-1])
