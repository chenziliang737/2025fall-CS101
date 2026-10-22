import heapq
from collections import defaultdict
N,M=map(int,input().split())
graph=defaultdict(list)
for _ in range(M):
    a,b,x=map(int,input().split())
    graph[a].append((b,x))
heap=[(0,1)]
dict1={1:0}
while heap:
    x,a=heapq.heappop(heap)
    if dict1.get(a,float('inf'))<x:
        continue
    if a==N:
        ans=x
        break
    for b,y in graph[a]:
        if dict1.get(b,float('inf'))>x+y:
            heapq.heappush(heap,(x+y,b))
            dict1[b]=x+y
print(ans)