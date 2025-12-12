res=[0,1]
def Hanoi(n):
    s=float('inf')
    for k in range(1,n):
        s=min(s,res[k]+2**(n-k)-1+res[k])
    return s
for n in range(2,13):
    res.append(Hanoi(n))
for ans in res[1:]:
    print(ans)