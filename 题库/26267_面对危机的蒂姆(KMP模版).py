S=input()
T=input()
s=T+'!'+S
n=len(s)
m=len(T)
pi=[0]*n
for i in range(1,n):
    j=pi[i-1]
    while j>0 and s[j]!=s[i]:
        j=pi[j-1]
    if s[j]==s[i]:
        j+=1
    pi[i]=j
    if j==m and i!=m:
        print('YES')
        exit()
else:
    print('NO')