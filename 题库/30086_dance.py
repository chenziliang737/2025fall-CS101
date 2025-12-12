N,D=map(int,input().split())
list1=list(map(int,input().split()))
list1.sort()
for i in range(N):
    if list1[2*i+1]-list1[2*i]>D:
        print('No')
        break
else:
    print('Yes')