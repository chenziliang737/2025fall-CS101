from collections import defaultdict

m, n, k = map(int, input().split(','))
dict1 = defaultdict(list)
for i in range(m + 1, n):
    s = sum(map(int, list(str(i))))
    if s % k == 0:
        dict1[s // k].append(i)
for key in sorted(dict1.keys()):
    print(','.join(map(str, dict1[key])))
