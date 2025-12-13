N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input()))


def num(a):
    return bin(a).count('1')


def state(i):
    l = grid[i][:]
    x = 0
    s = 0
    while l:
        if l.pop() == 'H':
            s += 2 ** x
        x += 1
    l1 = []
    for a in range(1 << M):
        if a & (a << 1) or a & (a >> 1) or a & (a << 2) or a & (a >> 2):
            continue
        if not a & s:
            l1.append(a)
    return l1


if N == 1:
    state0 = state(0)
    print(max([num(a) for a in state0]))
    exit()
state2 = state(0)
state1 = state(1)
dp = [[0] * len(state2) for _ in range(len(state1))]
for i in range(len(state1)):
    for j in range(len(state2)):
        b = state1[i]
        c = state2[j]
        if not b & c:
            dp[i][j] = num(b) + num(c)
for n in range(2, N):
    state0 = state(n)
    dp1 = [[0] * len(state1) for _ in range(len(state0))]
    for i in range(len(state0)):
        a = state0[i]
        m = num(a)
        for j in range(len(state1)):
            b = state1[j]
            if a & b:
                continue
            for k in range(len(state2)):
                c = state2[k]
                if not a & c and not b & c:
                    dp1[i][j] = max(dp1[i][j], m + dp[j][k])
    dp = [row[:] for row in dp1]
    state2 = state1[:]
    state1 = state0[:]
print(max([max(row) for row in dp]))
