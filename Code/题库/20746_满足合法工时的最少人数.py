from math import ceil
time=list(map(int,input().split(',')))
t=int(input())
l=0
r=sum(time)
while r-l>1:
    m=(l+r+1)//2
    s=sum(ceil(x/m) for x in time)
    if s<=t:
        r=m
    else:
        l=m
print(r)