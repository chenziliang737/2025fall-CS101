key=input()
matrix=[[0]*5 for _ in range(5)]
dict1={}
x=0
for a in key:
    if a=='j':
        a='i'
    if a not in dict1:
        matrix[x//5][x%5]=a
        dict1[a]=(x//5,x%5)
        x+=1
for i in range(97,123):
    b=chr(i)
    if b=='j':
        b='i'
    if b not in dict1:
        matrix[x//5][x%5]=b
        dict1[b]=(x//5,x%5)
        x+=1
n=int(input())
for _ in range(n):
    word=input()
    stack=[]
    for a in word:
        if a=='j':
            a='i'
        if not stack:
            stack.append(a)
            continue
        if len(stack[-1])==2:
            stack.append(a)
            continue
        if stack[-1]!=a:
            b=stack.pop()
            stack.append(b+a)
        else:
            if stack[-1]=='x':
                stack.pop()
                stack.append('xq')
                stack.append(a)
            else:
                b=stack.pop()
                stack.append(b+'x')
                stack.append(a)
    if len(stack[-1])==1:
        if stack[-1]=='x':
            stack.pop()
            stack.append('xq')
        else:
            b=stack.pop()
            stack.append(b+'x')
    s=''
    for t in stack:
        a,b=t[0],t[1]
        x1,y1=dict1[a]
        x2,y2=dict1[b]
        if x1==x2:
            s+=matrix[x1][(y1+1)%5]
            s+=matrix[x2][(y2+1)%5]
            continue
        elif y1==y2:
            s+=matrix[(x1+1)%5][y1]
            s+=matrix[(x2+1)%5][y2]
            continue
        else:
            s+=matrix[x1][y2]
            s+=matrix[x2][y1]
            continue
    print(s)