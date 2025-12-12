N,L,M=map(int,input().split())
dp=[0]*M
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
for num in l1:
    dp[num%M]+=1
matrix=[[0]*M for _ in range(M)]
for num in l2:
    for i in range(M):
        matrix[i][(i-num)%M]+=1
def square(matrix):
    matrix1=[[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            matrix1[i][j]=sum([matrix[i][k]*matrix[k][j] for k in range(M)])%(10**9+7)
    return matrix1
def plus(dp,matrix):
    dp1=[0]*M
    for i in range(M):
        dp1[i]=sum([matrix[i][j]*dp[j] for j in range(M)])%(10**9+7)
    return dp1
L-=2
while L>1:
    if L%2==1:
        dp=plus(dp,matrix)
    matrix=square(matrix)
    L=L//2
if L:
    dp=plus(dp,matrix)
s=0
for i in range(N):
    s+=dp[(-l2[i]-l3[i])%M]
print(s%(10**9+7))