import heapq

N = int(input())
list1 = []
for _ in range(N):
    s, f = map(int, input().split())
    list1.append((s, f))
list1.sort()
L, P = map(int, input().split())
c = 0
heap = []
heapq.heapify(heap)
while L - P > 0:
    while list1 and list1[-1][0] >= L - P:
        t = list1.pop()
        s = t[0]
        f = t[1]
        heapq.heappush(heap, (-f, s))
    if heap:
        t = heapq.heappop(heap)
        P += -t[0]
        c += 1
    else:
        c = -1
        break
print(c)
