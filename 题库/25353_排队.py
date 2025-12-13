from collections import deque

N, D = map(int, input().split())
queue = deque(int(input()) for _ in range(N))
ans = []
while queue:
    list1 = []
    ma = queue[0]
    mi = queue[0]
    for _ in range(len(queue)):
        h = queue.popleft()
        if abs(h - ma) <= D and abs(h - mi) <= D:
            list1.append(h)
        else:
            queue.append(h)
        if h < mi:
            mi = h
        if h > ma:
            ma = h
    ans += sorted(list1)
print(*ans, sep='\n')
