import heapq

N = int(input())
stop = []
for _ in range(N):
    stop.append(tuple(map(int, input().split())))
stop.sort()
L, P = map(int, input().split())
heap = []
s = 0
while L - P > 0:
    while stop and stop[-1][0] >= L - P:
        heapq.heappush(heap, -stop.pop()[1])
    if heap:
        P += -heapq.heappop(heap)
        s += 1
    else:
        print(-1)
        exit()
print(s)
