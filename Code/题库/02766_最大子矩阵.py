import sys
data=iter(sys.stdin.read().strip().split())
N=int(next(data))
list1=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        list1[i][j]=int(next(data))
s=-float('inf')
for j1 in range(N):
    for j2 in range(j1,N):
        list2=[]
        for i in range(N):
            list2.append(sum(list1[i][j1:j2]))
        dp=list2[0]
        m=list2[0]
        for i in range(1,N):
            dp1=max(list2[i],dp+list2[i])
            m=max(m,dp1)
            dp=dp1
        s=max(s,m)
print(s)
