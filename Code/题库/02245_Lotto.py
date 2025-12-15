import sys

data = list(sys.stdin.read().split("\n"))
output = []
for line in data[:-1]:
    line = list(map(int, line.split()))
    k = line[0]
    nums = line[1:]
    condition = [False] * k
    ans = []
    res = []

    def dfs(x):
        if x == 6:
            res.append(" ".join(map(str, ans)))
            return
        for i in range(k):
            if not condition[i] and (not ans or nums[i] > ans[-1]):
                ans.append(nums[i])
                condition[i] = True
                dfs(x + 1)
                ans.pop()
                condition[i] = False

    dfs(0)
    output.append("\n".join(res) + "\n")
print("\n".join(output).rstrip())
