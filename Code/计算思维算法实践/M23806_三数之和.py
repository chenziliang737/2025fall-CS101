list1 = list(map(int, input().split()))
list1.sort()
n = len(list1)
dict1 = {}
for i in list1:
    dict1[i] = dict1.get(i, 0) + 1
s1 = set()
for i in range(n - 1):
    for j in range(i + 1, n):
        a = list1[i]
        b = list1[j]
        if -(a + b) in dict1:
            if -(a + b) in [a, b] and dict1[-(a + b)] == 1:
                continue
            if a == 0 and b == 0 and dict1[0] <= 2:
                continue
            list2 = [a, b, -(a + b)]
            list2.sort()
            s1.add(tuple(list2))
print(len(s1))
