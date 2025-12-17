def mycount(a,s):
    c=0
    for i in range(s,int(a**0.5+1)):
        if a%i==0 and i<=a//i:
            c+=mycount(a//i,i)
    c+=1
    return c
n=int(input())
list1=[]
for _ in range(n):
    a=int(input())
    list1.append(mycount(a,2))
for a in list1:
    print(a)