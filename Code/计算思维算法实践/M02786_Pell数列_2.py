from collections import deque

queue = deque()
queue.append(1)
queue.append(0)
pell = [0]
for _ in range(1000000):
    p = (2 * queue[-1] + queue[-2]) % 32767
    pell.append(p)
    queue.append(p)
    queue.popleft()
for _ in range(int(input())):
    print(pell[int(input())])
