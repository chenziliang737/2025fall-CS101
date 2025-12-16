import sys

data = iter(sys.stdin.read().split("\n"))
while True:
    s = next(data)
    if s == ".":
        break
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[j] != s[i]:
            j = pi[j - 1]
        if s[j] == s[i]:
            j += 1
        pi[i] = j
    if n % (n - pi[n - 1]) == 0:
        print(n // (n - pi[n - 1]))
    else:
        print(1)
