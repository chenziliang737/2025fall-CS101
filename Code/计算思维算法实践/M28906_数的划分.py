n, k = map(int, input().split())
s = 0


def dfs(n1, k1, a1):
    if k1 == k - 1:
        if n - n1 >= a1:
            global s
            s += 1
        return
    if n1 + a1 * (k - k1) > n:
        return
    for i in range(a1, int((n - n1) / (k - k1)) + 1):
        dfs(n1 + i, k1 + 1, i)


dfs(0, 0, 1)
print(s)
