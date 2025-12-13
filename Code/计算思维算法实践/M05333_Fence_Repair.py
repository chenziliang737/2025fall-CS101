import heapq

heap = []
heapq.heapify(heap)
N = int(input())
for _ in range(N):
    L = int(input())
    heapq.heappush(heap, L)
s = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    s += a + b
    heapq.heappush(heap, a + b)
print(s)
