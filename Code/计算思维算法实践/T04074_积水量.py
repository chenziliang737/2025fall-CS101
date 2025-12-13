m = int(input())
for _ in range(m):
    n = int(input())
    heigh = list(map(int, input().split()))
    list1 = [0] * n
    a = -1
    for i in range(n):
        if heigh[i] > a:
            a = heigh[i]
        list1[i] = a
    list2 = [0] * n
    b = -1
    for j in range(n - 1, -1, -1):
        if heigh[j] > b:
            b = heigh[j]
        list2[j] = b
    s = sum(map(lambda x: min(list1[x], list2[x]) - heigh[x], range(n)))
    print(s)
