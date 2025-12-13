x, y, m, n, L = map(int, input().split())
a, b = m - n, y - x
if a == 0:
    print('Impossible')
    exit()
elif a < 0:
    a, b = -a, -b
if b < 0:
    b += L
if L % a == 0:
    if b % a == 0:
        print(b // a)
        exit()
    else:
        print('Impossible')
        exit()
for i in range(1, L):
    c = (a * i) % L
    if b % c == 0:
        print(i * (b // c))
        exit()
