from collections import defaultdict

N = int(input())
dict1 = defaultdict(set)
for word in range(N):
    list1 = list(map(int, input().split()))
    for article in list1[1:]:
        dict1[article].add(word)


def check(article, word, condition):
    if condition == 1 and word in dict1[article]:
        return True
    elif condition == -1 and word not in dict1[article]:
        return True
    elif condition == 0:
        return True
    else:
        return False


M = int(input())
for _ in range(M):
    list1 = list(map(int, input().split()))
    list2 = []
    for article in dict1.keys():
        if all(check(article, i, list1[i]) for i in range(N)):
            list2.append(article)
    list2.sort()
    if list2:
        print(*list2)
    else:
        print("NOT FOUND")
