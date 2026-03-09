from collections import defaultdict

n = int(input())
dict1 = defaultdict(list)
for _ in range(n):
    s, m, d = input().split()
    m = int(m)
    d = int(d)
    dict1[(m, d)].append(s)
for t in sorted(dict1.keys()):
    if len(dict1[t]) > 1:
        l = list(t) + dict1[t]
        print(*l)
