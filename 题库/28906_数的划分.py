N,K=map(int,input().split())
ans=0
def dfs(n,m,k):
    if k==K-1:
        if n>=m:
            global ans
            ans+=1
        return
    for i in range(m,n):
        dfs(n-i,i,k+1)
dfs(N,1,0)
print(ans)