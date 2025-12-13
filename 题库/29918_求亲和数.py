from collections import defaultdict


def qhs(x):
    s = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s += i + x // i
    return s


n = int(input())
dict1 = defaultdict(list)
res = []
for x in range(220, n + 1):
    y = qhs(x)
    if x < y <= n:
        dict1[y].append(x)
    elif y < x <= n:
        if x in dict1 and y in dict1[x]:
            res.append([y, x])
for x, y in sorted(res):
    print(f'{x} {y}')
