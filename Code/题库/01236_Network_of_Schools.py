from collections import defaultdict
N=int(input())
graph=defaultdict(list)
for i in range(1,N+1):
    l=list(map(int,input().split()))
    for j in l[:-1]:
        graph[i].append(j)
time=[[0,0] for _ in range(N+1)]
t=1
for i in range(1,N+1):
    if time[i][0]==0:
        def dfs1(x):
            global t
            time[x][0]=t
            for y in graph[x]:
                if time[y][0]==0:
                    t+=1
                    dfs1(y)
            t+=1
            time[x][1]=t
        dfs1(i)
transgraph=defaultdict(list)
for i in graph.keys():
    for j in graph[i]:
        transgraph[j].append(i)
condition=[False for _ in range(N+1)]
sccs=[]
sccs_id=[-1]*(N+1)
for x in sorted(list(range(1,N+1)),key=lambda y:-time[y][1]):
    if condition[x]==False:
        l=[]
        def dfs2(x):
            l.append(x)
            condition[x]=True
            sccs_id[x]=len(sccs)
            for y in transgraph[x]:
                if not condition[y]:
                    dfs2(y)
        dfs2(x)
        sccs.append(l)
degree=[[0,0] for _ in range(len(sccs))]
for i in range(1,N+1):
    for j in graph[i]:
        x=sccs_id[i]
        y=sccs_id[j]
        if x!=y:
            degree[x][1]+=1
            degree[y][0]+=1
a=sum([1 if t[0]==0 else 0 for t in degree])
b=sum([1 if t[1]==0 else 0 for t in degree])
print(a)
print(0) if len(sccs)==1 else print(max(a,b))