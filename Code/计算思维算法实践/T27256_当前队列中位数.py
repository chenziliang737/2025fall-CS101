import heapq, re

minheap = []
maxheap = []
l = 0
dl = -1
c = [0, 0]
dict1 = {}
n = int(input())


def rejust():
    while minheap and minheap[0][1] <= dl:
        t = heapq.heappop(minheap)
        del dict1[t[1]]
        c[0] -= 1
    while maxheap and maxheap[0][1] <= dl:
        t = heapq.heappop(maxheap)
        del dict1[t[1]]
        c[1] -= 1
    while len(maxheap) - c[1] + 1 < len(minheap) - c[0]:
        t = heapq.heappop(minheap)
        dict1[t[1]] = 1
        heapq.heappush(maxheap, (-t[0], t[1]))
    while len(maxheap) - c[1] > len(minheap) - c[0]:
        t = heapq.heappop(maxheap)
        dict1[t[1]] = 0
        heapq.heappush(minheap, (-t[0], t[1]))


for _ in range(n):
    command = input()
    if re.match("add", command):
        num = int(command[4:])
        if not minheap or num <= -minheap[0][0]:
            heapq.heappush(minheap, (-num, l))
            dict1[l] = 0
            l += 1
            if len(maxheap) - c[1] + 1 < len(minheap) - c[0]:
                t = heapq.heappop(minheap)
                dict1[t[1]] = 1
                heapq.heappush(maxheap, (-t[0], t[1]))
        else:
            heapq.heappush(maxheap, (num, l))
            dict1[l] = 1
            l += 1
            if len(maxheap) - c[1] > len(minheap) - c[0]:
                t = heapq.heappop(maxheap)
                dict1[t[1]] = 0
                heapq.heappush(minheap, (-t[0], t[1]))
        rejust()
    elif re.match("del", command):
        dl += 1
        c[dict1[dl]] += 1
        rejust()
    elif re.match("query", command):
        if len(minheap) - c[0] > len(maxheap) - c[1]:
            print(-minheap[0][0])
        else:
            a = (-minheap[0][0] + maxheap[0][0]) / 2
            if a == int(a):
                print(int(a))
            else:
                print(f"{a:.1f}")
