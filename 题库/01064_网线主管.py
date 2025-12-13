from decimal import Decimal

N, K = map(int, input().split())
lines = []
s = 0
for _ in range(N):
    a = int(100 * Decimal(input()))
    s += a
    lines.append(a)
l = 0
r = s // K + 1
while r - l > 1:
    mid = (l + r) // 2
    if sum(map(lambda x: x // mid, lines)) < K:
        r = mid
    else:
        l = mid
print(f'{l / 100:.2f}')
