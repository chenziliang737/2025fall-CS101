N = int(input())
list1 = []
for _ in range(N):
    l, n = map(int, input().split())
    list2 = list(map(int, input().split()))
    list2.sort()
    mi = 0
    for i in list2:
        if i <= l / 2:
            mi = max(mi, i)
        else:
            mi = max(mi, l - i)
    ma = max(l - list2[0], list2[-1])
    list1.append((mi, ma))
for t in list1:
    print(*t)
