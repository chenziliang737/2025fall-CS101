import sys
from collections import deque,defaultdict
def solve():
    data=iter(map(int,sys.stdin.read().split()))
    n,m=next(data),next(data)
    graph=defaultdict(set)
    for _ in range(m):
        a,b=next(data),next(data)
        graph[a].add(b)
        graph[b].add(a)
    unvisited=set(range(1,n+1))
    ans=0
    while unvisited:
        i=next(iter(unvisited))
        unvisited.remove(i)
        queue=deque([i])
        while queue:
            a=queue.popleft()
            l=[]
            for b in unvisited:
                if b not in graph[a]:
                    l.append(b)
            for b in l:
                unvisited.remove(b)
                queue.append(b)
        ans+=1
    print(ans-1)
solve()