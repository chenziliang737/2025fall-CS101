import math

N = int(input())
M = int(input())
if M == 1:
    S = float('inf')
    R = 1
    while R ** 2 <= N:
        if N % (R ** 2) == 0:
            S = min(S, R ** 2 + 2 * R * (N // (R ** 2)))
        R += 1
    print(S)
    exit()
S = float('inf')
flag = False
Rstack = []
hstack = []


def minV(i):
    return (i * (i + 1) // 2) ** 2


def maxV(R, h, i):
    return R ** 2 * h * i - (R ** 2 + 2 * R * h) * i * (i + 1) // 2 + (2 * R + h) * i * (i + 1) * (2 * i + 1) // 6 - (
                i * (i + 1) // 2) ** 2


def check(R, h, i, n):
    return N - n - maxV(R, h, i) <= R ** 2 * h <= N - n - minV(i)


def dfs(i, n, s):
    global S
    if s >= S:
        return
    if i == M - 1:
        if N < minV(i):
            return
        Rmin = i + 1
        Rmax = int(math.sqrt((N - minV(i)) / (i + 1)))
        for R in range(Rmax, Rmin - 1, -1):
            hmin = i + 1
            hmax = int((N - minV(i)) / R ** 2)
            for h in range(hmax, hmin - 1, -1):
                if check(R, h, i, n):
                    Rstack.append(R)
                    hstack.append(h)
                    dfs(i - 1, R ** 2 * h, R ** 2 + 2 * R * h)
                    Rstack.pop()
                    hstack.pop()
        return
    if i == 0:
        Rmin = math.ceil(math.sqrt((N - n) / (hstack[-1] - 1)))
        Rmax = Rstack[-1] - 1
        for R in range(Rmax, Rmin - 1, -1):
            if (N - n) % (R ** 2) == 0:
                h = (N - n) // (R ** 2)
                global flag
                flag = True
                S = min(S, s + 2 * R * h)
        return
    Rmax = min(Rstack[-1] - 1, int(math.sqrt((N - n - minV(i)) / (i + 1))))
    Rmin = i + 1
    for R in range(Rmax, Rmin - 1, -1):
        hmax = min(hstack[-1] - 1, int((N - n - minV(i)) / (R ** 2)))
        hmin = i + 1
        for h in range(hmax, hmin - 1, -1):
            if check(R, h, i, n):
                Rstack.append(R)
                hstack.append(h)
                dfs(i - 1, n + R ** 2 * h, s + 2 * R * h)
                Rstack.pop()
                hstack.pop()


dfs(M - 1, 0, 0)
print(S) if flag else print(0)
