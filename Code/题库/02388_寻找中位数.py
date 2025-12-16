import heapq

N = int(input())
mheap = []
Mheap = []
for n in range(1, N + 1):
    a = int(input())
    if n % 2 == 0:
        if not Mheap or a >= Mheap[0]:
            heapq.heappush(Mheap, a)
        else:
            heapq.heappush(mheap, -a)
            b = -heapq.heappop(mheap)
            heapq.heappush(Mheap, b)
    else:
        if not mheap or a <= -mheap[0]:
            heapq.heappush(mheap, -a)
        else:
            heapq.heappush(Mheap, a)
            b = heapq.heappop(Mheap)
            heapq.heappush(mheap, -b)
print(-mheap[0])
