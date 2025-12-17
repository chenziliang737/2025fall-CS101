from collections import deque
list1=[]
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    list1.append([n,m])
for list2 in list1:
    n=list2[0]
    m=list2[1]
    queue=deque()
    for i in range(1,n+1):
        queue.append(i)
    s=0
    while len(queue)>1:
        a=queue.popleft()
        s+=1
        if s==m:
            s=0
            continue
        queue.append(a)
    print(queue[0])
