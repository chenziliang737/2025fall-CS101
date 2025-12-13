from math import ceil

X, N = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
while coins[-1] > X:
    coins.pop()
if coins[0] != 1:
    print(-1)
else:
    n = len(coins)
    c = 0
    s = 0
    for i in range(1, n):
        m = ceil((coins[i] - 1 - s) / coins[i - 1])
        c += m
        s += m * coins[i - 1]
    c += ceil((X - s) / coins[-1])
    print(c)
