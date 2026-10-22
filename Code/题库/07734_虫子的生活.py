import sys
sys.setrecursionlimit(1<<20)
c=1
for _ in range(int(input())):
    n,m=map(int,input().split())
    flag=False
    p=[i for i in range(2*n+1)]
    def find(x):
        if p[x]!=x:
            p[x]=find(p[x])
        return p[x]
    for _ in range(m):
        x,y=map(int,input().split())
        if flag:
            continue
        if find(x)==find(y) or find(x+n)==find(y+n):
            flag=True
        else:
            p[find(x+n)]=find(y)
            p[find(y+n)]=find(x)
    print(f'Scenario #{c}:')
    if flag:
        print('Suspicious bugs found!')
    else:
        print('No suspicious bugs found!')
    print()
    c+=1