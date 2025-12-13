import math

N, L = map(int, input().split())
points = []
for _ in range(N):
    points.append(tuple(map(int, input().split())))


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


points.sort()
lower = []
for p in points:
    while len(lower) > 1 and cross(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)
upper = []
for p in reversed(points):
    while len(upper) > 1 and cross(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)
hull = lower[:-1] + upper[:-1]
n = len(hull)
l = 0
for i in range(n):
    j = (i + 1) % n
    l += distance(hull[i], hull[j])
l += 2 * math.pi * L
print(f'{l:.0f}')
