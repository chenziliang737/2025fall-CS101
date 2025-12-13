N, M = map(int, input().split())
music = list(map(int, input().split()))
set1 = set()
m = 1
for i in music:
    set1.add(i)
    if len(set1) == M:
        set1 = set()
        m += 1
print(m)
