nc = int(input())
list1 = []
for _ in range(nc):
    n, m, b = map(int, input().split())
    dict1 = {}
    for i in range(n):
        ti, xi = map(int, input().split())
        if dict1.get(ti, -1) == -1:
            dict1[ti] = [xi]
        else:
            dict1[ti].append(xi)
    list1.append([n, m, b, dict1])
for list2 in list1:
    n = list2[0]
    m = list2[1]
    b = list2[2]
    dict1 = list2[3]
    for ti in sorted(dict1.keys()):
        if len(dict1[ti]) >= m:
            b -= sum(sorted(dict1[ti], reverse=True)[0:m])
        else:
            b -= sum(dict1[ti])
        if b <= 0:
            print(ti)
            break
    if b > 0:
        print("alive")
