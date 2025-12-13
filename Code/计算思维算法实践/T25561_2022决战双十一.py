import re

n, m = map(int, input().split())
l1 = [{}] * (n + 1)
for i in range(1, n + 1):
    str1 = input()
    si = map(int, re.findall(r"(\d):", str1))
    pi = map(int, re.findall(r":(\d+)", str1))
    l1[i] = {t[0]: t[1] for t in zip(si, pi)}
l2 = [{}] * (m + 1)
for j in range(1, m + 1):
    str2 = input()
    qi = map(int, re.findall(r"(\d+)-", str2))
    xi = map(int, re.findall(r"-(\d+)", str2))
    l2[j] = {t[0]: t[1] for t in zip(qi, xi)}
p = [0] * (m + 1)
S = float("inf")


def dfs(a):
    if a == n + 1:
        s = p[0]
        s -= 50 * (p[0] // 300)
        for si in range(1, m + 1):
            xi = 0
            for q, x in l2[si].items():
                if p[si] >= q:
                    xi = max(xi, x)
            s -= xi
        global S
        S = min(S, s)
    else:
        for si, pi in list(l1[a].items()):
            p[0] += pi
            p[si] += pi
            dfs(a + 1)
            p[0] -= pi
            p[si] -= pi


dfs(1)
print(S)
