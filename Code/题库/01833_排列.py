f = [1]
for i in range(1, 2000):
    f.append(f[-1] * i)
for _ in range(int(input())):
    N, k = map(int, input().split())
    p1 = list(map(int, input().split()))
    p0 = list(range(1, N + 1))
    n = N - 1
    m = 0
    for x in p1:
        i = p0.index(x)
        m += i * f[n]
        p0.pop(i)
        n -= 1
    m = (m + k) % (f[N])
    p2 = []
    p0 = list(range(1, N + 1))
    n = N - 1
    while p0:
        i = m // f[n]
        p2.append(p0.pop(i))
        m = m % f[n]
        n -= 1
    print(*p2)
