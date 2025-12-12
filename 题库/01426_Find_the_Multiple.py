while True:
    n=int(input())
    if n==0:
        break
    dict1={}
    x=0
    while True:
        a=10**x%n
        l=[]
        for i in range(n):
            if i in dict1 and (i+a)%n not in dict1:
                l.append(i)
        for i in l:
            dict1[(i+a)%n]=dict1[i]+[x]
        if a not in dict1:
            dict1[a]=[x]
        if 0 in dict1:
            print(sum([10**x for x in dict1[0]]))
            break
        x+=1