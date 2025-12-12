from collections import deque
n,k,s=map(int,input().split())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().split())))
if k==s:
    print(0)
    exit()
queue1=deque([(k,0)])
dict1={k:0}
queue2=deque([(s,0)])
dict2={s:0}
while queue1:
    k1,t1=queue1.popleft()
    for k3 in range(n):
        if grid[k1][k3]==1 and k3 not in dict1:
            queue1.append((k3,t1+1))
            dict1[k3]=t1+1
while queue2:
    k2,t2=queue2.popleft()
    for k3 in range(n):
        if grid[k2][k3]==1 and k3 not in dict2:
            queue2.append((k3,t2+1))
            dict2[k3]=t2+1
S=float('inf')
flag=False
for i in range(n):
    if i in dict1 and i in dict2 and dict1[i]==dict2[i]:
        flag=True
        S=min(S,dict1[i])
if flag:
    print(S)
else:
    print(-1)