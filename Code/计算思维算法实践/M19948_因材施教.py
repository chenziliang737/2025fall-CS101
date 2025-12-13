import heapq

n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list1.sort()
heap = []
heapq.heapify(heap)
for i in range(n - 1):
    heapq.heappush(heap, -(list1[i + 1] - list1[i]))
s = list1[-1] - list1[0] + sum(heapq.nsmallest(m - 1, heap))
print(s)
