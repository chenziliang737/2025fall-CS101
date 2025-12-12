n=int(input())
list1=list(map(int,input().split()))
a=0
list2=[]
for i in list1:
    a+=i
    list2.append(a)
b=min(list2)
if b<=0:
    print(-b+1)
else:
    print(1)