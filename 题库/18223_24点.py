m = int(input())
list1 = []
for i in range(m):
    list1.append(list(map(int, input().split())))
for i in range(m):
    list2 = list1[i]
    T = False
    for a in [-1, 1]:
        for b in [-1, 1]:
            for c in [-1, 1]:
                for d in [-1, 1]:
                    s = a * list2[0] + b * list2[1] + c * list2[2] + d * list2[3]
                    if s == 24:
                        T = True
    if T:
        print('YES')
    else:
        print('NO')
