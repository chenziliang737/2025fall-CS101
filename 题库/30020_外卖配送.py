from math import ceil

a, b, c, d, e = map(int, input().split())
s = ceil(b / 2)
x = 6 * (ceil(b / 2)) - 2 * b
if c > x:
    s += ceil((c - x) / 6)
y = 5 * a + 18 * s - 6 * b - 3 * c
if d > y:
    s += ceil((d - y) / 18)
z = 11 * a + 36 * s - 12 * b - 6 * c - 2 * d
if e > z:
    s += ceil((e - z) / 36)
s += a
print(s)
