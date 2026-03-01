import heapq

n = int(input())
heap = []
for _ in range(n):
    l = list(map(int, input().split()))
    if l[0] == 1:
        heapq.heappush(heap, l[1])
    else:
        print(heapq.heappop(heap))
