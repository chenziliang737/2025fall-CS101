x0,y0=map(int,input().split())
x1,y1=map(int,input().split())
d=list(map(int,input().split()))
E=int(input())
flag=False
x,y=x0,y0
for _ in range(E):
    x+=d[0]
    y+=d[1]
    if (x,y) in [(0,0),(8,0),(16,0),(0,5),(8,5),(16,5)]:
        if flag:
            print(1)
        else:
            print(-1)
        break
    if not flag:
        if (x,y)==(x1,y1):
            x0,y0=x1,y1
            flag=True
    else:
        if (x,y)==(x0,y0):
            x1,y1=x0,y0
            flag=False
    if x in [0,16]:
        d[0]*=-1
    if y in [0,5]:
        d[1]*=-1
else:
    print(0)