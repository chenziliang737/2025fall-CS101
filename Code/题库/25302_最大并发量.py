for _ in range(int(input())):
    n=int(input())
    event=[]
    for _ in range(n):
        x,y=map(int,input().split())
        event.append((x,1))
        event.append((y,-1))
    event.sort()
    s=0
    ans=0
    for t in event:
        s+=t[1]
        if s>ans:
            ans=s
    print(ans)