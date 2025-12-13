import heapq

N = int(input())
list1 = list(map(int, input().split()))
heapq.heapify(list1)
s = 0
while len(list1) > 1:
    a = heapq.heappop(list1)
    b = heapq.heappop(list1)
    s += a + b
    heapq.heappush(list1, a + b)
print(s)
