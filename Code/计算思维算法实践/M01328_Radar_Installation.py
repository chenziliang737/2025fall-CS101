from math import sqrt

c = 1
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    list1 = []
    T = True
    for _ in range(n):
        x, y = map(int, input().split())
        if y > d:
            T = False
            continue
        l = x - sqrt(d**2 - y**2)
        r = x + sqrt(d**2 - y**2)
        list1.append((l, r))
    if T:
        list1.sort()
        s = 1
        set1 = set(list1[0])
        m = list1[0][1]
        for i in range(1, len(list1)):
            if list1[i][0] <= m:
                set1.add(list1[i])
                m = min(m, list1[i][1])
            else:
                s += 1
                set1 = set(list1[i])
                m = list1[i][1]
    else:
        s = -1
    print(f"Case {c}: {s}")
    c += 1
    input()
