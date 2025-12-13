from collections import deque
from math import floor

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    queue = deque()
    queue.append(1)
    set1 = set()
    set1.add(n)

    def position(s):
        x = n
        for i in bin(s)[3:]:
            if i == "1":
                x *= 3
            else:
                x = floor(x / 2)
        return x

    while queue:
        s = queue.popleft()
        x = position(s)
        if x == m:
            break
        if x == 0:
            continue
        s1 = s << 1 | 1
        x1 = position(s1)
        if x1 not in set1:
            queue.append(s1)
            set1.add(x1)
        s2 = s << 1 | 0
        x2 = position(s2)
        if x2 not in set1:
            queue.append(s2)
            set1.add(x2)
    print(len(bin(s)[3:]))
    dict1 = {"1": "H", "0": "O"}
    print("".join(list(map(lambda x: dict1[x], list(bin(s)[3:])))))
