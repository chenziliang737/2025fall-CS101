import sys
from collections import deque
data=iter(sys.stdin.read().strip().split())
m=int(next(data))
n=int(next(data))
list1=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        list1[i][j]=int(next(data))
list2=[[0]*n for _ in range(m)]
N=0
S=0
for i in range(m):
    for j in range(n):
        if list2[i][j]==0:
            N+=1
            queue=deque()
            queue.append((i,j))
            s=1
            list2[i][j]=1
            while queue:
                p,q=queue.popleft()
                b=bin(list1[p][q]+16)
                if b[3]=='0' and list2[p+1][q]==0:
                    queue.append((p+1,q))
                    list2[p+1][q]=1
                    s+=1
                if b[4]=='0' and list2[p][q+1]==0:
                    queue.append((p,q+1))
                    list2[p][q+1]=1
                    s+=1
                if b[5]=='0' and list2[p-1][q]==0:
                    queue.append((p-1,q))
                    list2[p-1][q]=1
                    s+=1
                if b[6]=='0' and list2[p][q-1]==0:
                    queue.append((p,q-1))
                    list2[p][q-1]=1
                    s+=1
            S=max(S,s)
print(N)
print(S)