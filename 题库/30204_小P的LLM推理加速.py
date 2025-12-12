import sys
data=iter(sys.stdin.read().split('\n'))
n,m=map(int,next(data).split())
x0=float('inf')
y0=float('inf')
l=[]
for _ in range(n):
    x,y=map(int,next(data).split())
    if (x+y,x)<=(x0+y0,x0):
        x0=x
        y0=y
    l.append(x)
l.sort()
stack=[]
res=[0]
for x in l:
    if stack and x+stack[-1]>=x0+y0:
        break
    stack.append(x)
    res.append(res[-1]+x)
while res[-1]<=m:
    res.append(res[-2]+x0+y0)
print(len(res)-2)