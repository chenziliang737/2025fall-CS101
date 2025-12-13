d = int(input())
n = int(input())
dict1 = {}
for _ in range(n):
    x, y, i = map(int, input().split())
    for p in range(-d, d + 1):
        for q in range(-d, d + 1):
            if 0 <= x + p <= 1024 and 0 <= y + q <= 1024:
                dict1[(x + p, y + q)] = dict1.get((x + p, y + q), 0) + i
s = 0
place = set()
for a in dict1.keys():
    if dict1[a] > s:
        s = dict1[a]
        place = set()
        place.add(a)
    elif dict1[a] == s:
        place.add(a)
print(f"{len(place)} {s}")
