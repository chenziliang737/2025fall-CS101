n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()
dict1 = {}
for _ in range(m):
    f = input()
    dict1[f] = dict1.get(f, 0) + 1
list2 = sorted(dict1.values(), reverse=True)
a = 0
b = 0
for i in range(len(list2)):
    a += list1[i] * list2[i]
    b += list1[-1 - i] * list2[i]
print(*[a, b])
