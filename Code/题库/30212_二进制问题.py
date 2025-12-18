f = [1]
for i in range(1, 31):
    f.append(i * f[-1])
N, K = map(int, input().split())
if K == 0:
    print(0)
    exit()


def dfs(n, k):
    if n == 0:
        return 0
    m = len(bin(n)) - 2
    if k == 1:
        return m
    if m < k:
        return 0
    elif m > k:
        a = f[m - 1] // (f[k] * f[m - 1 - k])
        a += dfs(n & (2 ** (m - 1) - 1), k - 1)
        return a
    else:
        return dfs(n & (2 ** (m - 1) - 1), k - 1)


print(dfs(N, K))
