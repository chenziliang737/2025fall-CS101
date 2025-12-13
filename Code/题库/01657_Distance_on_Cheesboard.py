for _ in range(int(input())):
    a, b = input().split()
    x = abs(ord(a[0]) - ord(b[0]))
    y = abs(int(a[1]) - int(b[1]))
    l = [0, 0, 0, 0]
    if x == 0 and y == 0:
        print(*l)
        continue
    l[0] = max(x, y)
    if x == 0 or y == 0 or x == y:
        l[1] = 1
    else:
        l[1] = 2
    if x == 0 or y == 0:
        l[2] = 1
    else:
        l[2] = 2
    if x == y:
        l[3] = 1
    elif abs(x - y) % 2 == 0:
        l[3] = 2
    else:
        l[3] = 'Inf'
    print(*l)
