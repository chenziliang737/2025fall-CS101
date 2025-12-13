for _ in range(int(input())):
    w = int(input())
    l = []
    r = []
    for n in range(19, -1, -1):
        if (3 ** n - 1) // 2 < abs(w) <= (3 ** (n + 1) - 1) // 2:
            if w > 0:
                r.append(n)
                w -= 3 ** n
            elif w < 0:
                l.append(n)
                w += 3 ** n
    s = []
    if l:
        while l:
            s.append(f'{3 ** l.pop()}')
            s.append(',')
        s.pop()
    else:
        s.append('empty')
    s.append(' ')
    if r:
        while r:
            s.append(f'{3 ** r.pop()}')
            s.append(',')
        s.pop()
    else:
        s.append('empty')
    print(''.join(s))
