c=0
while True:
    N=int(input())
    if N==0:
        break
    c+=1
    print(f'Test case #{c}')
    S=input()
    pi=[0]*N
    for i in range(1,N):
        j=pi[i-1]
        while j>0 and S[i]!=S[j]:
            j=pi[j-1]
        if S[i]==S[j]:
            j+=1
        pi[i]=j
        if j!=0 and (i+1)%(i+1-j)==0:
            print(f'{i+1} {(i+1)//(i+1-j)}')
    print()