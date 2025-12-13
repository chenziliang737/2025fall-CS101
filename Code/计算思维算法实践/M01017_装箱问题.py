list1 = []
while True:
    list2 = list(map(int, input().split()))
    if list2 == [0, 0, 0, 0, 0, 0]:
        break
    list1.append(list2)
list3 = []
for list2 in list1:
    a, b, c, d, e, f = list2[0], list2[1], list2[2], list2[3], list2[4], list2[5]
    s = f + e + d
    if c % 4 == 0:
        s += c // 4
    else:
        s += c // 4 + 1
    bmax = 5 * d
    if c % 4 == 1:
        bmax += 5
    elif c % 4 == 2:
        bmax += 3
    elif c % 4 == 3:
        bmax += 1
    if b > bmax:
        if (b - bmax) % 9 == 0:
            s += (b - bmax) // 9
        else:
            s += (b - bmax) // 9 + 1
    amax = (s - f) * 36 - e * 25 - d * 16 - c * 9 - b * 4
    if a > amax:
        if (a - amax) % 36 == 0:
            s += (a - amax) // 36
        else:
            s += (a - amax) // 36 + 1
    list3.append(s)
for i in list3:
    print(i)
