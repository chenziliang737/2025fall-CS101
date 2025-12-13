nums = list(input().strip())
n = len(nums)
k = int(input())
m = n - k
dp = [['0'] * (m + 1) for _ in range(n)]
dp[0][1] = nums[0]
for i in range(1, n):
    for x in range(1, m + 1):
        if x == i + 1:
            dp[i][x] = ''.join(nums[:i + 1])
            break
        else:
            dp[i][x] = min(dp[i - 1][x], dp[i - 1][x - 1] + nums[i], key=lambda y: int(y))
print(int(dp[-1][-1]))
