while True:
    n=int(input())
    if n==0:
        break
    point=[]
    pointset=set()
    for _ in range(n):
        x,y=map(int,input().split())
        point.append((x,y))
        pointset.add((x,y))
    point.sort()
    s=0
    for i in range(1,n):
        for j in range(i):
            x1,y1=point[j]
            x2,y2=point[i]
            a=[-(y2-y1),(x2-x1)]
            if (x1+a[0],y1+a[1]) in pointset and (x2+a[0],y2+a[1]) in pointset:
                s+=1
            b=[(y2-y1),-(x2-x1)]
            if (x1+b[0],y1+b[1]) in pointset and (x2+b[0],y2+b[1]) in pointset:
                s+=1
    print(s//4)