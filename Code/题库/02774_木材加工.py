N,K=map(int,input().split())
wood=[]
for _ in range(N):
    wood.append(int(input()))
def check(d):
    s=0
    for a in wood:
        s+=a//d
    return s>=K
l=0
r=sum(wood)//K+1
while r-l>1:
    d=(l+r)//2
    if check(d):
        l=d
    else:
        r=d
print(l)