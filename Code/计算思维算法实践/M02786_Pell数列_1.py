from collections import deque

n = int(input())
list1 = []
for _ in range(n):
    list1.append(int(input()))
list2 = sorted(list1, reverse=True)
list3 = [0] * n
queue = deque()
queue.append(1)
queue.append(0)
c = 0
while list2:
    p = (2 * queue[-1] + queue[-2]) % 32767
    queue.append(p)
    queue.popleft()
    c += 1
    if c == list2[-1]:
        j = list1.index(list2[-1])
        list3[j] = p
        list2.pop()
for i in list3:
    print(i)
