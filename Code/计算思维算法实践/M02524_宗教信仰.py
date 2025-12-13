c = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    list1 = [n, m]
    for _ in range(m):
        a, b = map(int, input().split())
        list1.append((a, b))
    dict1 = {x: {x} for x in range(1, n + 1)}
    s = n
    if m == 0:
        pass
    else:
        for t in list1[2:]:
            a = t[0]
            b = t[1]
            s -= 1
            set1 = dict1[a]
            set2 = dict1[b]
            if set1 == set2:
                s += 1
                continue
            set3 = set1 | set2
            for i in set3:
                dict1[i] = set3
    c += 1
    print(f"Case {c}: {s}")
