from decimal import Decimal
from math import floor, ceil

n, M = map(int, input().split())
list1 = []
point = []
for _ in range(n):
    a, b, c = map(lambda x: Decimal(x), input().split())
    if a != 0 and 0 <= -b / a <= M:
        point.append(floor(-b / a))
        point.append(ceil(-b / a))
    list1.append((a, b, c))
point.append(0)
point.append(M)
s_m = float('inf')
s_M = -float('inf')
for x in point:
    s = 0
    for a, b, c in list1:
        s += c * abs(a * x + b)
    s_m = min(s_m, s)
    s_M = max(s_M, s)
print(*[int(s_M), int(s_m)])
