import sys
import bisect
data=iter(sys.stdin.read().split())
def solve():
    x=int(next(data))
    h=[float('inf')]+[int(next(data)) for _ in range(x)]
    stack=[]
    ans=0
    left=[-1]*(x+1)
    for i in range(x,-1,-1):
        while stack and h[stack[-1]]<=h[i]:
            top=stack.pop()
            left[top]=i
        stack.append(i)
    stack=[]
    for j in range(1,x+1):
        while stack and h[stack[-1]]>h[j]:
            stack.pop()
        stack.append(j)
        i=stack[bisect.bisect_right(stack,left[j])]
        ans=max(ans,j-i+1)
    print(ans)
solve()