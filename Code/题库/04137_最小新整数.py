for _ in range(int(input())):
    n,k=input().split()
    l=list(map(int,list(n)))
    k=int(k)
    m=len(l)
    t=0
    stack=[]
    for i in range(m):
        a=l[i]
        while stack and stack[-1]>a and t-1+m-i>=m-k:
            stack.pop()
            t-=1
        if t<m-k:
            stack.append(a)
            t+=1
    print(int(''.join(list(map(str,stack)))))