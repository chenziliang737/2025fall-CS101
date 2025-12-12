import sys
data=iter(sys.stdin.read().split('\n'))
list1=[]
for _ in range(int(next(data))):
    list1.append(list(map(int,next(data).split())))
list1.sort()
stack=[]
for t in list1:
    if stack and stack[-1][1]>=t[0]:
        stack[-1][1]=max(stack[-1][1],t[1])
    else:
        stack.append(t)
for t in stack:
    print(*t)