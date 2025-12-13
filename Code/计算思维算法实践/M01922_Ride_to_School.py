from math import ceil

while True:
    N = int(input())
    if N == 0:
        break
    list1 = []
    v0 = 0
    t0 = float("inf")
    t0f = float("inf")
    for _ in range(N):
        v, t = map(int, input().split())
        if t >= 0 and v != 0:
            tf = (16200 / v) + t
            list1.append((v, t, tf))
            if t < t0 or (t == t0 and v >= v0):
                v0 = v
                t0 = t
                t0f = tf
    s = {t0f}
    for i in list1:
        v1 = i[0]
        t1 = i[1]
        tf = i[2]
        if v1 != v0:
            S = v0 * v1 * (t0 - t1) / (v0 - v1)
            if 0 <= S <= 16200:
                s.add(tf)
    print(ceil(min(s)))
