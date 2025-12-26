nums = list(map(int, input().split()))
n = len(nums)
stack = []
set1 = set()
S = 0


def dfs(x):
    for y in range(x, n):
        if not stack or nums[y] >= stack[-1]:
            stack.append(nums[y])
            dfs(y + 1)
            stack.pop()
    if len(stack) >= 2:
        set1.add(tuple(stack))


dfs(0)
print(len(set1))
