n=int(input())
list1=[]
for _ in range(n):
    list1.append(list(map(int,input().split())))
s=0
while list1:
    if len(list1)==1:
        s=max(s,list1[0][0])
        break
    c=sum(list1[0])
    for i in range(1,len(list1)-1):
        c+=list1[i][0]+list1[i][-1]
        del list1[i][0]
        del list1[i][-1]
    c+=sum(list1[-1])
    s=max(s,c)
    del list1[0]
    del list1[-1]
print(s)