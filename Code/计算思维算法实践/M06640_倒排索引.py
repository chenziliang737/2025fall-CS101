from collections import defaultdict

dict1 = defaultdict(list)
N = int(input())
for i in range(1, N + 1):
    list1 = list(input().split())
    for word in list1[1:]:
        dict1[word].append(i)
        if len(dict1[word]) >= 2 and dict1[word][-2] == dict1[word][-1]:
            dict1[word].pop()
M = int(input())
for _ in range(M):
    word = input()
    if word in dict1:
        print(*dict1[word])
    else:
        print("NOT FOUND")
