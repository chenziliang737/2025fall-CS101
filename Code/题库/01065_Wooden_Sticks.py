from collections import deque

for _ in range(int(input())):
    n = int(input())
    iter1 = iter(map(int, input().split()))
    sticks = []
    for _ in range(n):
        sticks.append((next(iter1), next(iter1)))
    sticks.sort()
    queue = deque(sticks)
    s = 0
    while queue:
        m = -float('inf')
        for _ in range(len(queue)):
            a, b = queue.popleft()
            if b >= m:
                m = b
            else:
                queue.append((a, b))
        s += 1
    print(s)
