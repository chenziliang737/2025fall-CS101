while True:
    R, n = map(int, input().split())
    if R == -1 and n == -1:
        break
    list1 = list(map(int, input().split()))
    list1.sort()
    list2 = [0] * n
    m = -float("inf")
    s = 0
    for i in range(n):
        if list2[i] == 0:
            for j in range(i, n):
                if list1[j] > list1[i] + R:
                    break
                m = list1[j]
                list2[j] = 1
            s += 1
            for k in range(j, n):
                if list1[k] <= m + R:
                    list2[k] = 1
                if list1[k] > m + R:
                    break
    print(s)
