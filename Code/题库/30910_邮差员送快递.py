import heapq
from collections import defaultdict
n,m=map(int,input().split())
graph1=defaultdict(list)
graph2=defaultdict(list)
for _ in range(m):
    u,v,w=map(int,input().split())
    graph1[u].append((v,w))
    graph2[v].append((u,w))
heap1=[(0,1)]
distance1=[0]+[float('inf')]*n
distance1[1]=0
while heap1:
    x,a=heapq.heappop(heap1)
    for b,w in graph1[a]:
        y=x+w
        if distance1[b]>y:
            heapq.heappush(heap1,(y,b))
            distance1[b]=y
heap2=[(0,1)]
distance2=[0]+[float('inf')]*n
distance2[1]=0
while heap2:
    x,a=heapq.heappop(heap2)
    for b,w in graph2[a]:
        y=x+w
        if distance2[b]>y:
            heapq.heappush(heap2,(y,b))
            distance2[b]=y
print(sum(distance1)+sum(distance2))