from collections import deque

s = input()
i = 0
queue = deque()
while 2**i <= len(s):
    queue.append(s[2**i - 1])
    i += 1
s1 = ""
while queue:
    s1 += queue.popleft()
    if queue:
        s1 += queue.pop()
print(s1)
