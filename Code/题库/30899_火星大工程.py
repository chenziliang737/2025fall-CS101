from collections import deque,defaultdict
n,m=map(int,input().split())
graph1=defaultdict(list)
graph2=defaultdict(list)
indegree=defaultdict(int)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph1[a].append((b,c))
    graph2[b].append((a,c))
    indegree[b]+=1
topo_order=[]
queue=deque([i for i in range(1,n+1) if indegree[i]==0])
while queue:
    a=queue.popleft()
    topo_order.append(a)
    for b,c in graph1[a]:
        indegree[b]-=1
        if indegree[b]==0:
            queue.append(b)
idx={a:i for i,a in enumerate(topo_order)}
EST=[0]*n
for i in range(n):
    u=topo_order[i]
    for v,c in graph1[u]:
        j=idx[v]
        EST[j]=max(EST[j],EST[i]+c)
time=max(EST)
LST=[time]*n
for j in range(n-1,-1,-1):
    v=topo_order[j]
    for u,c in graph2[v]:
        i=idx[u]
        LST[i]=min(LST[i],LST[j]-c)
res=[]
for u in sorted(graph1.keys()):
    for v,c in sorted(graph1[u]):
        i,j=idx[u],idx[v]
        if EST[i]+c==LST[j]:
            res.append([u,v])
print(time)
for t in res:
    print(*t)