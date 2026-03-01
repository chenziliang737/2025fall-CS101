import sys

sys.setrecursionlimit(1 << 20)
n = int(input())
pre = list(map(int, input().split()))


def dfs(pre):
    if len(pre) <= 1:
        return pre
    root = pre[0]
    left = [x for x in pre if x < root]
    right = [x for x in pre if x > root]
    return dfs(left) + dfs(right) + [root]


print(" ".join(map(str, dfs(pre))))
