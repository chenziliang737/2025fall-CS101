import sys
sys.setrecursionlimit(1<<20)
from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    words=[]
    for _ in range(n):
        words.append(input())
    words.sort()
    graph=defaultdict(list)
    indegree=defaultdict(int)
    outdegree=defaultdict(int)
    for i in range(n):
        word=words[i]
        a,b=word[0],word[-1]
        graph[a].append((b,word,i))
        indegree[b]+=1
        outdegree[a]+=1
    flag=False
    start=''
    end=''
    for a in graph.keys():
        if outdegree[a]-indegree[a]==1:
            if not start:
                start=a
            else:
                flag=True
                break
        elif indegree[a]-outdegree[a]==1:
            if not end:
                end=a
            else:
                flag=True
                break
        elif indegree[a]!=outdegree[a]:
            flag=True
            break
    if flag:
        print('***')
        continue
    if not start:
        start=min(graph.keys())
    ans=[]
    condition=[False]*n
    def dfs(a):
        for b,word,i in graph[a]:
            if not condition[i]:
                condition[i]=True
                dfs(b)
                ans.append(word)
    dfs(start)
    if len(ans)!=n:
        print('***')
    else:
        print('.'.join(reversed(ans)))