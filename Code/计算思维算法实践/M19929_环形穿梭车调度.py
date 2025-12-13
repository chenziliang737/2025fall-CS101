from collections import defaultdict

m, n = map(int, input().split())
list1 = [-1] + list(map(int, input().split()))
list2 = [-1] + list(map(int, input().split()))
dict1 = defaultdict(list)
dict2 = dict()
for i in range(1, m + 1):
    dict1[list1[i]].append((i, list2[i]))
    dict2[(i, list2[i])] = list2[i]
for i in range(n, 0, -1):
    for ti in sorted(dict1[i], key=lambda t: -t[0]):
        ni = ti[0]
        wi = ti[1]
        for j in range(i, n + 1):
            for tj in dict1[j]:
                if tj[0] > ni:
                    dict2[ti] = max(dict2[ti], dict2[tj] + wi)
s = 0
for v in dict2.values():
    s = max(s, v)
print(s)
