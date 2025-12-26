import bisect

N, C = map(int, input().split())
position = [-float("inf")]
for _ in range(N):
    position.append(int(input()))
position.sort()


def check(d):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        j = bisect.bisect(position, position[i] - d) - 1
        dp[i] = dp[j] + 1
    return dp[N] >= C


l = 1
r = position[-1] - position[1] + 1
while r - l > 1:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid
print(l)
