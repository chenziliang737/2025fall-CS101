N,M=map(int,input().split())
grid=[]
for _ in range(N):
    grid.append(list(map(int,input().split())))
if N==1:
    print(N)
    exit()
dp=[1]*M
for n in range(1,N):
    dp1=[0]*M
    i=0
    for j in range(M):
        s=0 if j==0 else dp1[j-1]
        while i<M and grid[n][j]>=grid[n-1][i]:
            s+=dp[i]
            i+=1
        dp1[j]=s
    dp=dp1[:]
print(sum(dp))