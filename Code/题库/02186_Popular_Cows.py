import sys
sys.setrecursionlimit(1<<20)
from collections import defaultdict
N,M=map(int,input().split())
graph=defaultdict(list)
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
scc_id=[-1]*(N+1)
scc_num=[]
dfn=[-1]*(N+1)
low=[-1]*(N+1)
stack=[]
condition=[False]*(N+1)
t=0
def dfs(u):
    global t
    dfn[u]=low[u]=t
    t+=1
    stack.append(u)
    condition[u]=True
    for v in graph[u]:
        if dfn[v]==-1:
            dfs(v)
            low[u]=min(low[u],low[v])
        elif condition[v]:
            low[u]=min(low[u],dfn[v])
    if low[u]==dfn[u]:
        c=0
        while True:
            x=stack.pop()
            scc_id[x]=len(scc_num)
            condition[x]=False
            c+=1
            if x==u:
                break
        scc_num.append(c)
for u in range(1,N+1):
    if dfn[u]==-1:
        dfs(u)
out_degree=[0]*len(scc_num)
for i in range(1,N+1):
    for j in graph[i]:
        if scc_id[i]!=scc_id[j]:
            out_degree[scc_id[i]]+=1
ans=0
for i in range(len(scc_num)):
    if out_degree[i]==0:
        if ans:
            ans=0
            break
        else:
            ans=scc_num[i]
print(ans)