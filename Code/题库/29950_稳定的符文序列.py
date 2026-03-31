from collections import deque, defaultdict

s = list(input())
queue = deque()
dict1 = defaultdict(int)
ans = 0
for a in s:
    if dict1[a]:
        while queue and queue[0] != a:
            b = queue.popleft()
            dict1[b] = 0
        queue.popleft()
    queue.append(a)
    dict1[a] = 1
    ans = max(ans, len(queue))
print(ans)
