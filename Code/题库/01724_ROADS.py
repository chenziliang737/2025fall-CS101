import heapq
from collections import defaultdict
K=int(input())
N=int(input())
R=int(input())
road=[[[] for _ in range(N+1)] for _ in range(N+1)]
graph=defaultdict(list)
for _ in range(R):
    S,D,L,T=map(int,input().split())
    road[S][D].append((L,T))
    graph[S].append(D)
heap=[(0,-K,1)]
dist=[[float('inf') for _ in range(K+1)] for _ in range(N+1)]
dist[1][K]=0
while heap:
    L,T,a=heapq.heappop(heap)
    T=-T
    if dist[a][T]<L:
        continue
    if a==N:
        print(L)
        break
    for b in graph[a]:
        for l,t in road[a][b]:
            L1=L+l
            T1=T-t
            if T1>=0 and dist[b][T1]>L1:
                heapq.heappush(heap,(L1,-T1,b))
                dist[b][T1]=L1
else:
    print(-1)