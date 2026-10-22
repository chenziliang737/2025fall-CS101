from collections import defaultdict
P=int(input())
place=[]
mark={}
for _ in range(P):
    s=input()
    mark[s]=len(place)
    place.append(s)
Q=int(input())
path=path=[[(float('inf'),'')]*P for _ in range(P)]
for i in range(P):
    path[i][i]=(0,'')
for _ in range(Q):
    a,b,x=input().split()
    x=int(x)
    u,v=mark[a],mark[b]
    path[u][v]=(x,f'->({x})->')
    path[v][u]=(x,f'->({x})->')
for u in range(P):
    for v in range(P):
        for w in range(P):
            if path[u][w][0]+path[w][v][0]<path[u][v][0]:
                x=path[u][w][0]+path[w][v][0]
                s=path[u][w][1]+place[w]+path[w][v][1]
                path[u][v]=(x,s)
R=int(input())
for _ in range(R):
    a,b=input().split()
    u,v=mark[a],mark[b]
    if u==v:
        print(a)
    else:
        print(a+path[u][v][1]+b)