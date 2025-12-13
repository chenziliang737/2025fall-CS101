from collections import deque

n, d = map(int, input().split())
queue = deque(int(input()) for _ in range(n))
ans = []
while queue:
    inlist = []
    ma = queue[0]
    mi = queue[0]
    for _ in range(len(queue)):
        h = queue.popleft()
        if abs(h - ma) <= d and abs(h - mi) <= d:
            inlist.append(h)
        else:
            queue.append(h)
        if h < mi:
            mi = h
        if h > ma:
            ma = h
    ans += sorted(inlist)
print(*ans, sep="\n")
