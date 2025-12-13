from collections import deque

while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break
    queue = deque()
    for i in range(p - 1, p - 1 + n):
        a = i % n + 1
        queue.append(a)
    list1 = []
    c = 0
    while queue:
        c += 1
        a = queue.popleft()
        if c == m:
            c = 0
            list1.append(str(a))
            continue
        queue.append(a)
    print(",".join(list1))
