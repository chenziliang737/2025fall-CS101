from collections import defaultdict
n=int(input())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().split())))
dp=defaultdict(dict)
def dfs(a,m,j):
    if j in dp[a]:
        return dp[a][j]
    if m==2:
        dp[a][j]=grid[0][j]
        return grid[0][j]
    s=float('inf')
    for k in range(n):
        if a&(1<<k) and k not in [0,j]:
            s=min(s,dfs(a&(~(1<<j)),m-1,k)+grid[k][j])
    dp[a][j]=s
    return s
S=float('inf')
for j in range(1,n):
    S=min(S,dfs((1<<n)-1,n,j)+grid[0][j])
print(S)