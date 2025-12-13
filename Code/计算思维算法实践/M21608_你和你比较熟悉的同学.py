from collections import deque

tree = dict()
set1 = set()
n = int(input())
ma = 1
for _ in range(n):
    a, b = input().split(":")
    p = int(a.strip())
    s = list(map(int, b.split()))
    if s == [-1]:
        continue
    tree[p] = s
    set1.add(p)
    for s1 in s:
        if s1 in set1:
            set1.remove(s1)
for p in set1:
    queue = deque([p])
    set2 = set([p])
    num = 0
    while queue:
        p1 = queue.popleft()
        if p1 in tree:
            s = tree[p1]
            for s1 in s:
                if s1 not in set2:
                    queue.append(s1)
                    set2.add(s1)
        num += 1
    ma = max(ma, num)
print(ma)
