import sys

data = sys.stdin.read().split()
n = int(data[0])
word_list = data[1:]
word_list.sort()
dp = [1] * (n)
for i in range(1, n):
    for j in range(i):
        if not word_list[i].startswith(word_list[j]):
            dp[i] += dp[j]
print(sum(dp) + 1)
