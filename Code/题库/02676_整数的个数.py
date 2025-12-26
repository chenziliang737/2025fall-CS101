from collections import defaultdict

k = int(input())
l = list(map(int, input().split()))
dict1 = defaultdict(int)
for x in l:
    if x in [1, 5, 10]:
        dict1[x] += 1
print(dict1[1])
print(dict1[5])
print(dict1[10])
