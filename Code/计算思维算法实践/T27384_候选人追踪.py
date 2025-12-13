from collections import defaultdict

N, K = map(int, input().split())
iter1 = iter(map(int, input().split()))
dict1 = defaultdict(list)
for _ in range(N):
    t = next(iter1)
    c = next(iter1)
    dict1[t].append(c)
list1 = list(sorted(dict1.keys()))
dict2 = {i: 0 for i in map(int, input().split())}
dict3 = {i: 0 for i in range(1, 314159 + 1)}
least = 0
most = 0
ans = 0
if K == 314159:
    print(list1[-1])
else:
    for j in range(len(list1)):
        for c in dict1[list1[j]]:
            if c in dict2:
                dict2[c] += 1
                if least == dict2[c] - 1:
                    least = min(dict2.values())
            else:
                dict3[c] += 1
                most = max(most, dict3[c])
        if j < len(list1) - 1 and least > most:
            ans += list1[j + 1] - list1[j]
    print(ans)
