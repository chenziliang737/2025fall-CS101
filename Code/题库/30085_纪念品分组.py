from collections import deque

w = int(input())
n = int(input())
price = []
for _ in range(n):
    price.append(int(input()))
price.sort()
queue = deque(price)
s = 0
while len(queue) > 1:
    while queue and queue[-1] > w - queue[0]:
        queue.pop()
        s += 1
    if len(queue) > 1:
        queue.popleft()
        queue.pop()
        s += 1
if queue:
    s += 1
print(s)
