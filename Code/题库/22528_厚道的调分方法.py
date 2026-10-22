from math import ceil
score=list(map(float,input().split()))
score.sort()
N=len(score)
x0=score[N-ceil(0.6*N)]
def f(b):
    a=b/10**9
    return a*x0+1.1**(a*x0)
l=0
r=10**9
while r-l>1:
    m=(l+r+1)//2
    if f(m)>=85:
        r=m
    else:
        l=m
print(r)