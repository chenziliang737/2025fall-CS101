from collections import defaultdict

dict1 = defaultdict(set)
dict2 = defaultdict(int)
M = int(input())
for _ in range(M):
    a, b, c = input().split(",")
    if c == "yes":
        dict1[a].add(b)
    dict2[a] += 1
list1 = sorted(dict2.keys(), key=lambda x: (-len(dict1[x]), dict2[x], x))
for i in range(min(12, len(list1))):
    print(f"{i+1} {list1[i]} {len(dict1[list1[i]])} {dict2[list1[i]]}")
