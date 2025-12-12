for _ in range(int(input())):
    N,M=map(int,input().split())
    p=[i for i in range(2*N+1)]
    condition=[False for _ in range(N+1)]
    def find(x):
        if p[x]!=x:
            p[x]=find(p[x])
        return p[x]
    for _ in range(M):
        message=input().split()
        if message[0]=='D':
            x=int(message[1])
            y=int(message[2])
            p[find(x+N)]=find(y)
            p[find(y+N)]=find(x)
            condition[x]=True
            condition[y]=True
        else:
            x=int(message[1])
            y=int(message[2])
            if not condition[x] or not condition[y]:
                print('Not sure yet.')
                continue
            if find(x)==find(y):
                print('In the same gang.')
            elif find(x)==find(y+N):
                print('In different gangs.')
            else:
                print('Not sure yet.')