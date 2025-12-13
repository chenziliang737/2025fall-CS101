from math import ceil

m = int(input())
n = int(input())
nums = list(input().split())


def round(x):
    return x * ceil(20 / len(x))


nums.sort(key=lambda x: (round(x), -len(x)), reverse=True)
dp = [""] * (m + 1)
for x in nums:
    dp1 = dp[:]
    dp1[len(x)] = max(dp[len(x)], x)
    for i in range(len(x) + 1, m + 1):
        if dp[i - len(x)]:
            dp1[i] = max(dp[i], dp[i - len(x)] + x)
        else:
            dp1[i] = dp[i]
    dp = dp1[:]
print(int(dp[-1]))
